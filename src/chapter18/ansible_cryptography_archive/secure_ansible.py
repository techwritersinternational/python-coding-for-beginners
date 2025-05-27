from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptography.exceptions import InvalidKey

import os

import time
import random

import base64



import json
from datetime import datetime, timedelta

from generate_keys import generate_and_save_key_pair, get_key_fingerprint

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
    # Check if the message is already bytes
    if isinstance(message, bytes):
        message_bytes = message
    else:
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
    # Check if the message is already bytes
    if isinstance(message, bytes):
        message_bytes = message
    else:
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
    try:
        if len(message) > 190:  # Approximate max length for 2048-bit RSA with OAEP
            return encrypt_large_message(message, public_key)
        else:
            return encrypt_message(message, public_key)
    except InvalidKey:
        print("Error: Invalid public key")
        return None
    

def decrypt_message(encrypted_message, private_key):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted

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
        return self._simulate_transmission((encrypted_message, encrypted_signature))

    # Update the receive_message method in AnsibleCommunicator
    def receive_message(self, encrypted_data):
        try:
            encrypted_message, encrypted_signature = encrypted_data
            if is_message_corrupted(encrypted_message) or is_message_corrupted(encrypted_signature):
                raise ValueError("Received corrupted message")
            
            decrypted_message = decrypt_for_ansible(encrypted_message, self.private_key)
            decrypted_signature = decrypt_for_ansible(encrypted_signature, self.private_key)
            return decrypted_message, decrypted_signature
        except ValueError as e:
            print(f"Error: {str(e)}")
            return None, None


    def verify_message(self, message, signature, sender_public_key):
        return verify_signature(message, signature, sender_public_key)


    def _simulate_transmission(self, data):
        print(f"{self.name} is transmitting a message...")
        time.sleep(2)  # Simulate transmission delay
        if random.random() < 0.05:  # 5% chance of transmission failure
            print("Transmission failed due to solar flare interference!")
            return None
        print("Message transmitted successfully.")
        return data


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
    except Exception as e:
        print(f"Verification error: {str(e)}")
        return False


def is_key_expired(name):
    """Check if a key is expired"""
    try:       
        expiration_date = get_expiry_date(name)
        return datetime.now() > expiration_date
    except:
        # If we can't determine, consider it expired for safety
        return True

def get_expiry_date(name):
    """Get the expiration date of a key"""
    try:
        with open(f"keys/{name}_metadata.json", "r") as f:
            metadata = json.load(f)
        
        return datetime.fromisoformat(metadata["expires_at"])
    except:
        return None

def check_and_rotate_keys(name):
    expiry_date = get_expiry_date(name)

    if datetime.now() > expiry_date - timedelta(days=30):  # 30 days before expiry
        print(f"Rotating keys for {name}")
        new_expiry_date = generate_and_save_key_pair(name, "strong password")
        return new_expiry_date

    return expiry_date



# File to store revoked keys
REVOKED_KEYS_FILE = "revoked_keys.json"

def load_revoked_keys():
    """Load the list of revoked keys from JSON file"""
    if not os.path.exists(REVOKED_KEYS_FILE):
        # Create empty revocation list if file doesn't exist
        with open(REVOKED_KEYS_FILE, "w") as f:
            json.dump([], f)
        return []
    
    try:
        with open(REVOKED_KEYS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading revoked keys: {e}")
        return []  # Return empty list on error

def save_revoked_keys(revoked_keys_list):
    """Save the list of revoked keys to JSON file"""
    try:
        with open(REVOKED_KEYS_FILE, "w") as f:
            json.dump(revoked_keys_list, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving revoked keys: {e}")
        return False

def revoke_key(name):
    """Add a key's fingerprint to the revocation list"""
    public_key = load_public_key(f"keys/{name}_public_key.pem")
    fingerprint = get_key_fingerprint(public_key)
    
    # Load current revocation list
    revoked_keys = load_revoked_keys()
    
    # Add the fingerprint if not already present
    if fingerprint not in revoked_keys:
        revoked_keys.append(fingerprint)
        
        # Save updated list
        if save_revoked_keys(revoked_keys):
            print(f"Key with fingerprint {fingerprint} has been revoked")
            return True
        else:
            print(f"Failed to revoke key with fingerprint {fingerprint}")
            return False
    else:
        print(f"Key with fingerprint {fingerprint} was already revoked")
        return True

def is_key_revoked(name):
    """Check if a key has been revoked"""
    public_key = load_public_key(f"keys/{name}_public_key.pem")
    fingerprint = get_key_fingerprint(public_key)
    revoked_keys = load_revoked_keys()
    return fingerprint in revoked_keys

def is_message_corrupted(encrypted_message):
    try:
        # Attempt to decode the base64 message
        base64.b64decode(encrypted_message, validate=True)
        return False
    except base64.binascii.Error:
        return True

# Usage
