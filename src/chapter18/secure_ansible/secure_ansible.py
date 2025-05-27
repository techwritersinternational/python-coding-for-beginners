from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
import os

from cryptography.exceptions import InvalidKey

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

import base64

import random


# error-handling here
def load_private_key(filename, password):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=string_to_bytes(password),
        )
    return private_key

def load_public_key(filename):
    with open(filename, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    return public_key

def string_to_bytes(message):
    if isinstance(message, bytes):
        return message
    return message.encode('utf-8')

def encrypt_message(message, public_key):
    message_bytes = string_to_bytes(message)
    encrypted = public_key.encrypt(
        message_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted


def encrypt_large_message(message, public_key):
    message_bytes = string_to_bytes(message)
    
    # Generate a random AES key
    aes_key = os.urandom(32)  # 256-bit key
    
    # Encrypt the message with AES
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message_bytes) + encryptor.finalize()
    
    # Encrypt the AES key with RSA
    encrypted_aes_key = encrypt_message(aes_key.hex(), public_key)
    
    # Combine the encrypted AES key, IV, and encrypted message
    return encrypted_aes_key + iv + encrypted_message

def encrypt_for_ansible(message, public_key):
    if len(message) > 190:  # Approximate max length for 2048-bit RSA with OAEP
        return encrypt_large_message(message, public_key)
    else:
        return encrypt_message(message, public_key)


def decrypt_message(encrypted_message, private_key):
    try:
        decrypted = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted
    except Exception as e:
        print(f"Decryption error: {str(e)}")
        return None
    
def bytes_to_string(byte_message):
    if isinstance(byte_message, str):
        return byte_message
    return byte_message.decode('utf-8')


def decrypt_large_message(encrypted_data, private_key):
    # Extract the encrypted AES key (first 256 bytes for 2048-bit RSA)
    encrypted_aes_key = encrypted_data[:256]
    # Extract the IV (next 16 bytes)
    iv = encrypted_data[256:272]
    # The rest is the encrypted message
    encrypted_message = encrypted_data[272:]
    
    # Decrypt the AES key
    aes_key_hex = bytes_to_string(decrypt_message(encrypted_aes_key, private_key))
    aes_key = bytes.fromhex(aes_key_hex)
    
    # Decrypt the message with AES
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
    
    return decrypted_message


def decrypt_for_ansible(encrypted_data, private_key):
    try:
        if len(encrypted_data) > 256:  # Likely a large message
            decrypted_bytes = decrypt_large_message(encrypted_data, private_key)
        else:
            decrypted_bytes = decrypt_message(encrypted_data, private_key)
        return bytes_to_string(decrypted_bytes)
    except InvalidKey:
        return "Error: Invalid key. Could not decrypt the message."
    except Exception as e:
        return f"Error: An unexpected error occurred during decryption: {str(e)}"



class AnsibleCommunicator:
    def __init__(self, name, private_key, public_key):
        self.name = name
        self.private_key = private_key
        self.public_key = public_key

    def send_message(self, message, recipient_public_key):
        signature = sign_message(message, self.private_key)
        encrypted_message = encrypt_for_ansible(message, recipient_public_key)
        encrypted_signature = encrypt_for_ansible(signature, recipient_public_key)
        return self.simulate_transmission((encrypted_message, encrypted_signature))

    def receive_message(self, encrypted_data):
        encrypted_message, encrypted_signature = encrypted_data
        decrypted_message = decrypt_for_ansible(encrypted_message, self.private_key)
        decrypted_signature = decrypt_for_ansible(encrypted_signature, self.private_key)
        return decrypted_message, decrypted_signature

    def verify_message(self, message, signature, sender_public_key):
        return verify_signature(message, signature, sender_public_key)

    def simulate_transmission(self, message):
        print(f"{self.name} is transmitting a message...")
        if random.random() < 0.05:  # 5% chance of transmission failure
            print("Transmission failed due to solar flare interference!")
            return None
        print("Message transmitted successfully.")
        return message


def sign_message(message, private_key):
    message_bytes = string_to_bytes(message)
    signature = private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    # Return base64 encoded signature for easier handling
    return base64.b64encode(signature).decode('utf-8')



def verify_signature(message, signature, public_key):
    try:
        message_bytes = string_to_bytes(message)
        # Convert base64 signature back to bytes
        signature_bytes = base64.b64decode(signature)
        
        public_key.verify(
            signature_bytes,
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        print(f"Verification error: invalid signature")
        return False
    







