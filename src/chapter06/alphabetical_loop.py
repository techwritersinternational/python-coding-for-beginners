# filename: looping_alphabetical.py
person = {
    'ada': 'lovelace',
    'alan': 'turing',
    'annabella': 'byron',
    'charles': 'babbage'
}

for firstname in sorted(person.keys()):
    print(f"Hello, {firstname.title()}.")