from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import serialization

import os

from getpass import getpass 

import hashlib

from secure_ansible import load_public_key

from datetime import datetime, timedelta

import time

import json



def generate_key_pair(expiry_days=365):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    expiry_date = datetime.now() + timedelta(days=expiry_days)
    
    return private_key, public_key, expiry_date

def generate_and_save_key_pair(name, password):
    private_key, public_key, expiry_date = generate_key_pair()
    
    # Ensure the keys directory exists
    os.makedirs('keys', exist_ok=True)
    
    # Save the private key
    with open(f"keys/{name}_private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
        ))
    
    # Save the public key
    with open(f"keys/{name}_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    
    # Save metadata including expiration
    metadata = {
        "name": name,
        "created_at": datetime.now().isoformat(),
        "expires_at": expiry_date.isoformat(),
        "fingerprint": get_key_fingerprint(public_key)
    }
    
    with open(f"keys/{name}_metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"Key pair for {name} generated and saved in the 'keys' directory.")

def get_key_fingerprint(public_key):
    key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return hashlib.sha256(key_bytes).hexdigest()


def check_and_rotate_keys(name, password):
    expiry_date = get_expiry_date(name)
    if datetime.now() > expiry_date - timedelta(days=30):  # 30 days before expiry
        print(f"Rotating keys for {name}")
        generate_and_save_key_pair(name, password)

def get_expiry_date(name):
    """Get the expiration date of a key"""
    try:
        with open(f"keys/{name}_metadata.json", "r") as f:
            metadata = json.load(f)
        
        return datetime.fromisoformat(metadata["expires_at"])
    except:
        return None

def is_key_expired(name):
    """Check if a key is expired"""
    try:       
        expiration_date = get_expiry_date(name)
        return datetime.now() > expiration_date
    except:
        # If we can't determine, consider it expired for safety
        return True
    

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

def benchmark_key_generation(key_sizes):
    for size in key_sizes:
        start_time = time.time()
        private_key, public_key, _ = generate_key_pair(size)
        end_time = time.time()
        print(f"{size}-bit key generation time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    benchmark_key_generation([1024, 2048, 4096])

#    fingerprint = get_key_fingerprint(load_public_key("keys/aditi_public_key.pem"))
 #   print(f"Key fingerprint: {fingerprint}")

  #  aditi_password = getpass("Enter a password for Aditi: ")
   # bram_password = getpass("Enter a password for Bram: ")

#    generate_and_save_key_pair("aditi", aditi_password)
 #   generate_and_save_key_pair("bram", bram_password)

