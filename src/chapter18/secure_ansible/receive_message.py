from secure_ansible import load_private_key, decrypt_for_ansible
import base64

# Load Bram's private key
bram_private_key = load_private_key("keys/bram_private_key.pem")

# The encrypted message (paste the encryped message from the previous section)
encrypted_base64 = input("Enter the encrypted message: ")

# Convert from base64 and decrypt
encrypted_message = base64.b64decode(encrypted_base64)
decrypted_message = decrypt_for_ansible(encrypted_message, bram_private_key)

print("Decrypted message:")
print(decrypted_message)