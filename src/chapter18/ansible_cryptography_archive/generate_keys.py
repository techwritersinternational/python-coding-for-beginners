from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import serialization
import os

from datetime import datetime, timedelta

import json

import hashlib

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
            encryption_algorithm=
            serialization.BestAvailableEncryption(password.encode())
            #encryption_algorithm=serialization.NoEncryption()
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

