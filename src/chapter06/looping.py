# filename: looping.py
celestial_voyager = {
   'name': 'Celestial Voyager',
   'model': 'CV-9800',
   'manufacturer': 'Galactic Frontier Industries',
   'length': 523.7,
   'crew': 180
}

for key, value in celestial_voyager.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")