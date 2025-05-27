crew_members = [
    "Captain Jane Doe\n",
    "First Officer John Smith\n",
    "Engineer Alice Johnson\n"
]

with open('crew_manifest.txt', 'w') as manifest:
    manifest.writelines(crew_members)