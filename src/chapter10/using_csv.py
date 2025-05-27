import csv

crew_data = [
    ['Name', 'Role', 'Age'],
    ['John Doe', 'Commander', 45],
    ['Patience Adebayo', 'Pilot', 38],
    ['Alyx Johnson', 'Engineer', 41]
]

with open('crew.csv', 'w', newline='') as data_file:
    writer = csv.writer(data_file)
    writer.writerows(crew_data)