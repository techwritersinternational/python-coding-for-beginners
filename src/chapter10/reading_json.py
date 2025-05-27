import json

with open('mission_data.json', 'r') as data_file:
    loaded_mission = json.load(data_file)

print(loaded_mission['name'])  # Output: Mars Expedition Alpha