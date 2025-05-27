astronaut_1 = {'first_name': 'Elena', 'last_name': 'Vega', 'age': 32, 'experience': 8}
astronaut_2 = {'first_name': 'Kai', 'last_name': 'Chang', 'age': 38, 'experience': 12}
astronaut_3 = {'first_name': 'Aisha', 'last_name': 'Okafor', 'age': 29, 'experience': 1}

astronauts = [astronaut_1, astronaut_2, astronaut_3]

for astronaut in astronauts:
   year_word = 'year' if astronaut['experience'] == 1 else 'years'
   print(f"{astronaut['first_name']} {astronaut['last_name']}, age {astronaut['age']}, {astronaut['experience']} {year_word} of experience")

astronaut_1['number_of_missions'] = 3
astronaut_2['number_of_missions'] = 5
astronaut_3['number_of_missions'] = 2

print("\nUpdated astronaut information:")
for astronaut in astronauts:
   print(astronaut)