from secure_ansible import load_public_key, encrypt_for_ansible
import base64

# Load Bram's public key
bram_public_key = load_public_key("keys/bram_public_key.pem")

# Encrypt a message for Bram
message = "Hello, Bram! This is a secure message from Aditi. How's the weather on Mars? The weather here has been fine. We have been working on a new project and I wanted to share some details with you. I have encrypted this message using your public key. Please decrypt it using your private key. Thanks!"
#message = "Hello, Bram! This is a secure message from Aditi. How's the weather on Mars?" 

encrypted_message = encrypt_for_ansible(message, bram_public_key)

# Convert to base64 for easy transmission
encrypted_base64 = base64.b64encode(encrypted_message)

encrypted_text_for_output = encrypted_base64.decode('utf-8')

print("Encrypted message:")
print(encrypted_text_for_output)