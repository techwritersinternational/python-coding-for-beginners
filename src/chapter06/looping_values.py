# filename: looping_values.py
person = {
    'ada': 'byron',
    'alan': 'turing',
    'annabella': 'byron',
    'charles': 'babbage'
}

for lastname in set(person.values()):
    print(f"Hello, {lastname.title()}.")