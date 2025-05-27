astronaut_experience = {'Rakesh': 3, 'Sunita': 7, 'Kalpana': 2, 'Ravish': 5}
mission_crew = ['Sunita', 'Kalpana']

#for astronaut in astronaut_experience:
for astronaut, experience in astronaut_experience.items():
    if astronaut in mission_crew and experience > 5:
        print(f"{astronaut} is an experienced crew member for this mission.")
    elif astronaut in mission_crew:
        print(f"{astronaut} is a crew member for this mission.")
    else:
        print(f"{astronaut} is not assigned to this mission.")