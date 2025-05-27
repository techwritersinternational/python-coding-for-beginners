spacecraft = ['Soyuz', 'Chandrayaan', 'Apollo', 'Shenzhou']

for name in spacecraft:
    if name == "Apollo":
        launch_continent = "North America"
    else:
        launch_continent = "Asia"
    print(f"{name} was launched from {launch_continent}.")