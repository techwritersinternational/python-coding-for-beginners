available_modules = ['Habitation', 'Laboratory', 'Power']
required_modules = ['Habitation', 'Laboratory', 'Power', 'Propulsion']

for module in required_modules:
    if module in available_modules:
        print(f"{module} module is available.")
    else:
        print(f"{module} module is not available. Mission cannot proceed.")