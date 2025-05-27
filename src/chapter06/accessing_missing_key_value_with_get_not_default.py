# filename: accessing_missing_key_value_with_get_not_default.py
lunar_buggy = {'color': 'black chrome', 'wheels': 4, 'radio': 'sub-ether'}
print(lunar_buggy)  # Outputs: {'color': 'black chrome', 'wheels': 4, 'radio': 'sub-ether'}

del lunar_buggy['radio']
print(lunar_buggy)  # Outputs: {'color': 'black chrome', 'wheels': 4}

print(f"This lunar buggy has a {lunar_buggy.get('radio', 'basic')} radio.")