def backup_ansible(messages, backup):
   print("Beginning ansible transmission and backup sequence...")
   
   while messages:
       message = messages.pop(0)  # Remove and return the first message
       print(f"\nTransmitting: {message}")
       backup.append(message)
       print("Message backed up successfully.")
   
   print("\nAll messages transmitted and backed up.")

def restore_ansible(messages, backup):
   print("Beginning ansible backup restoration...")
   
   while backup:
       message = backup.pop()  # Remove and return the last message
       messages.append(message)
       print(f"\nRestored: {message}")
   
   print("\nAll messages restored from backup.")

# Test the functions
messages = [
   "Mining colony needs immediate resupply",
   "Unusual stellar phenomenon detected",
   "Research station reports successful experiment"
]
backup_storage = []

print("Original messages:", messages)
print("Original backup:", backup_storage)

print("\n=== BACKUP OPERATION ===")
backup_ansible(messages, backup_storage)

print("Messages after backup:", messages)
print("Backup after backup:", backup_storage)

print("\n=== RESTORE OPERATION ===")
restore_ansible(messages, backup_storage)

print("Messages after restore:", messages)
print("Backup after restore:", backup_storage)
