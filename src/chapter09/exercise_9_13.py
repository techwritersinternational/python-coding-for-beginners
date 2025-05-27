import hashlib

class Ansible:
   def __init__(self, id):
       self.id = id
       print(f"Ansible unit {self.id} initialized.")
   
   def send_message(self, message):
       """Create a hash of the message and return the hash."""
       message_hash = hashlib.sha256(message.encode()).hexdigest()
       print(f"\n{self.id} sending message...")
       print(f"Message: {message}")
       print(f"Hash: {message_hash}")
       return message_hash
   
   def receive_message(self, message, original_hash):
       """Verify received message by comparing hashes."""
       received_hash = hashlib.sha256(message.encode()).hexdigest()
       print(f"\n{self.id} receiving message...")
       print(f"Message: {message}")
       print(f"Original hash: {original_hash}")
       print(f"Computed hash: {received_hash}")
       
       if received_hash == original_hash:
           print("Status: Message integrity verified.")
           return True
       else:
           print("WARNING: Message may have been tampered with!")
           return False


# Create ansible units
sender = Ansible("Alpha")
receiver = Ansible("Beta")

# Test 1: Normal transmission
print("\n=== Test 1: Normal Transmission ===")
message = "Send supplies to Mars Base Alpha"
message_hash = sender.send_message(message)
receiver.receive_message(message, message_hash)

# Test 2: Tampered message
print("\n=== Test 2: Tampered Message ===")
message = "Send supplies to Mars Base Alpha"
message_hash = sender.send_message(message)

# Infiltrator tampering with message
tampered_message = "Send supplies to Rebel Base Delta"
print("\nINFILTRATOR: Intercepting and modifying message...")
print(f"Original: {message}")
print(f"Modified: {tampered_message}")

receiver.receive_message(tampered_message, message_hash)

# Test 3: Subtle tampering
print("\n=== Test 3: Subtle Tampering ===")
message = "Transfer 1000 credits to Account #12345"
message_hash = sender.send_message(message)

# Infiltrator making subtle change
tampered_message = "Transfer 1000 credits to Account #12346"
print("\nINFILTRATOR: Making subtle modification...")
print(f"Original: {message}")
print(f"Modified: {tampered_message}")

receiver.receive_message(tampered_message, message_hash)
