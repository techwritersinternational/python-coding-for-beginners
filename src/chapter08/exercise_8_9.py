def send_ansible_messages(messages):
   if not messages:
       print("No messages in queue for ansible transmission.")
       return
   
   print("Beginning ansible transmission sequence...")
   
   for message in messages:
       print(f"\nTransmitting message:")
       print(f">>> {message}")
       print("Message transmitted successfully.")
   
   print("\nAll messages have been transmitted.")

# Test the function with different message lists
messages1 = [
   "Colony on Kepler-186f requests additional supplies",
   "Deep space probe has detected unusual radiation signature",
   "Mining operation on Europa reports successful extraction"
]

messages2 = []

# Test with non-empty list
print("Test 1: Multiple messages")
send_ansible_messages(messages1)

# Test with empty list
print("\nTest 2: Empty message queue")
send_ansible_messages(messages2)