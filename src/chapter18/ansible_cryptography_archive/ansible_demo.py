from secure_ansible import AnsibleCommunicator, load_private_key, load_public_key, is_key_expired, check_and_rotate_keys, is_key_revoked, revoke_key

# Load keys
alice_private_key = load_private_key("keys/aditi_private_key.pem", "strong password")
alice_public_key = load_public_key("keys/aditi_public_key.pem")
bob_private_key = load_private_key("keys/benyamin_private_key.pem", "strong password")
bob_public_key = load_public_key("keys/benyamin_public_key.pem")

#check_and_rotate_keys("aditi")

if is_key_expired("aditi"):
    print("Warning: Alice's public key has expired.")
if is_key_expired("benyamin"):
    print("Warning: Bob's public key has expired.")

revoke_key("benyamin")

if is_key_revoked("benyamin"):
    print("Warning: Benyamin's key is revoked.")

# Create Ansible Communicators
alice_ansible = AnsibleCommunicator("Alice", alice_private_key, alice_public_key)
bob_ansible = AnsibleCommunicator("Bob", bob_private_key, bob_public_key)

# Alice sends a message to Bob
message = "Hello Bob! How's the weather on Mars?"
print(f"Alice's original message: {message}")

encrypted_data = alice_ansible.send_message(message, bob_public_key)

if encrypted_data:
    # Bob receives and decrypts the message
    decrypted_message, decrypted_signature = bob_ansible.receive_message(encrypted_data)
    print(f"Bob's decrypted message: {decrypted_message}")
    
    # Bob verifies the signature
    if bob_ansible.verify_message(decrypted_message, decrypted_signature, alice_public_key):
        print("Signature verified. The message is authentic and intact.")
    else:
        print("Warning: The signature is invalid. The message may have been tampered with.")
else:
    print("Message was lost in transmission.")

# Simulate a tampered message
tampered_message = "Hello Bob! Please send 1000 space credits to my account."
if encrypted_data:
    _, original_signature = bob_ansible.receive_message(encrypted_data)
    if bob_ansible.verify_message(tampered_message, original_signature, alice_public_key):
        print("Oh no! The tampered message was verified.")
    else:
        print("The tampered message failed verification, as expected.")