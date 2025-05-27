from secure_ansible import AnsibleCommunicator, load_private_key, load_public_key

from generate_keys import check_and_rotate_keys, revoke_key, is_key_revoked

from getpass import getpass


aditi_password = getpass("What is Aditi's password? ")
bram_password = getpass("What is Bram's password? ")

check_and_rotate_keys("aditi", aditi_password)
check_and_rotate_keys("bram", bram_password)

revoke_key("bram")

if is_key_revoked("bram"):
    print("Warning: Bram's key is revoked.")
    exit()

# Load keys
aditi_private_key = load_private_key("keys/aditi_private_key.pem", aditi_password)
aditi_public_key = load_public_key("keys/aditi_public_key.pem")
bram_private_key = load_private_key("keys/bram_private_key.pem",  bram_password)
bram_public_key = load_public_key("keys/bram_public_key.pem")

# Create Ansible Communicators
aditi_ansible = AnsibleCommunicator("Aditi", aditi_private_key, aditi_public_key)
bram_ansible = AnsibleCommunicator("Bram", bram_private_key, bram_public_key)

# Aditi sends a message to Bram
message = "Hello Bram! How's the weather on Mars?"
print(f"Aditi's original message: {message}")

encrypted_data = aditi_ansible.send_message(message, bram_public_key)

if encrypted_data:
    # Bram receives and decrypts the message
    decrypted_message, decrypted_signature = bram_ansible.receive_message(encrypted_data)
    print(f"Bram's decrypted message: {decrypted_message}")
    
    # Bram verifies the signature
    if bram_ansible.verify_message(decrypted_message, decrypted_signature, aditi_public_key):
        print("Signature verified. The message is authentic and intact.")
    else:
        print("Warning: The signature is invalid. The message may have been tampered with.")
else:
    print("Message was lost in transmission.")

# Simulate a tampered message
tampered_message = "Hello Bram! Please send 1000 space credits to my account."
if encrypted_data:
    _, original_signature = bram_ansible.receive_message(encrypted_data)
    if bram_ansible.verify_message(tampered_message, original_signature, aditi_public_key):
        print("Oh no! The tampered message was verified.")
    else:
        print("The tampered message failed verification, as expected.")