# filename: looping_names_keys.py
person = {
    'ada': 'lovelace',
    'alan': 'turing',
    'annabella': 'byron',
    'charles': 'babbage'
}

for firstname in person:
    print(f"Hello, {firstname.title()}.")  