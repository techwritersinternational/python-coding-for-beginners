# filename: looping_names.py
person = {
    'ada': 'lovelace',
    'alan': 'turing',
    'annabella': 'byron',
    'charles': 'babbage'
}

for firstname, lastname in person.items():
    print(f"{firstname.title()}'s lastname is {lastname.title()}.")  