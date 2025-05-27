cosmic_threats = ['black hole', 'asteroid', 'supernova']
print(cosmic_threats)
cosmic_threats[0] = 'dark matter'
print(cosmic_threats)

cosmic_threats = ['black hole', 'asteroid', 'supernova']
cosmic_threats.append('gamma-ray burst')
print(cosmic_threats)

cosmic_threats = ['black hole', 'asteroid', 'supernova']
cosmic_threats.insert(1, 'neutron star')
print(cosmic_threats)

cosmic_threats = ['black hole', 'asteroid', 'supernova']
del cosmic_threats[1]
print(cosmic_threats)

cosmic_threats = ['black hole', 'asteroid', 'supernova']
popped_threat = cosmic_threats.pop()
print(cosmic_threats)
print(popped_threat)

cosmic_threats = ['black hole', 'asteroid', 'supernova', 'dark matter']
cosmic_threats.remove('dark matter')
print(cosmic_threats)