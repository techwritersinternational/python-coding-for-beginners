cosmic_radiation = 15  # millisieverts

if cosmic_radiation < 5:
    print("Radiation level is safe.")
elif cosmic_radiation < 20:
    print("Radiation level is elevated. Consider additional shielding.")
else:
    print("Warning: Dangerous radiation levels! Immediate action required.")