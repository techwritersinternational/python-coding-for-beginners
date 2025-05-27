from secure_ansible import load_private_key, decrypt_for_ansible
import base64

# Load Benyamin's private key
benyamin_private_key = load_private_key("keys/benyamin_private_key.pem")

# The encrypted message (you would normally receive this from somewhere)
encrypted_base64 = input("Enter the encrypted message: ")

# Convert from base64 and decrypt
encrypted_message = base64.b64decode(encrypted_base64)
decrypted_message = decrypt_for_ansible(encrypted_message, benyamin_private_key)

print("Decrypted message:")
print(decrypted_message)
