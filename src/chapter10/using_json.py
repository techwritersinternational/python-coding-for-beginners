import json

space_mission = {
    "name": "Mars Expedition Alpha",
    "launch_date": "2045-07-01",
    "crew": ["John Doe", "Patience Adebayo", "Alyx Johnson"],
    "objectives": ["Establish base", "Conduct experiments", "Search for water"]
}

with open('mission_data.json', 'w') as data_file:
    json.dump(space_mission, data_file, indent=4)