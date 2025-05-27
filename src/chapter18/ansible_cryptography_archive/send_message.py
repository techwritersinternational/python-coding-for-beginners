from secure_ansible import load_public_key, encrypt_for_ansible
import base64

# Load Benyamin's public key
bob_public_key = load_public_key("keys/benyamin_public_key.pem")

# Encrypt a message for Benyamin
message = "Hello, Benyamin! This is a secure message from Aditi. How's the weather on Mars?"
encrypted_message = encrypt_for_ansible(message, bob_public_key)

# Convert to base64 for easy transmission
encrypted_base64 = base64.b64encode(encrypted_message).decode('utf-8')

print("Encrypted message:")
print(encrypted_base64)