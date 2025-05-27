# filename: looping_matching_key.py
person = {
    'ada': 'lovelace',
    'alan': 'turing',
    'annabella': 'byron',
    'charles': 'babbage'
}

first_programmer = 'ada'
difference_engineers = ['ada', 'charles']

for firstname in person.keys():
    if firstname == first_programmer:
       print(f"Hello, {firstname.title()}. You are the first ever programmer.")

    if firstname in difference_engineers:
        print(f"Hello, {firstname.title()}. You worked on the difference engine.")