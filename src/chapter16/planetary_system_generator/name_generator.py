import random

SYLLABLES = [
    "al", "an", "ar", "as", "at", "ea", "ed", "en", "er", "es", "ha", "he", "hi", "in", "is", "it",
    "le", "ma", "ne", "ng", "nt", "on", "or", "ou", "re", "se", "st", "te", "th", "ti", "to", "ve",
    "wa", "ze", "be", "ce", "de", "fe", "ge", "ke", "me", "pe", "que", "ra", "sa", "ta", "xa", "ya"
]

STAR_SUFFIXES = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
PLANET_SUFFIXES = ["Prime", "Secundus", "Tertius", "Quartus", "Quintus", "Sextus", "Septimus", "Octavus", "Nonus", "Decimus"]
MOON_SUFFIXES = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]

def generate_name(seed, syllable_count=2):
    """Generate a name using the given seed and syllable count."""
    random.seed(seed)
    name = ''.join(random.choice(SYLLABLES).capitalize() for _ in range(syllable_count))
    return name

def generate_star_name(seed):
    """Generate a star name."""
    name = generate_name(seed)
    suffix = random.choice(STAR_SUFFIXES)
    return f"{name} {suffix}"

def generate_planet_name(star_name, index, seed):
    """Generate a planet name."""
    name = generate_name(seed)
    suffix = PLANET_SUFFIXES[index] if index < len(PLANET_SUFFIXES) else str(index + 1)
    return f"{star_name} {name} {suffix}"

def generate_moon_name(planet_name, index, seed):
    """Generate a moon name."""
    name = generate_name(seed, syllable_count=1)
    suffix = MOON_SUFFIXES[index] if index < len(MOON_SUFFIXES) else str(index + 1)
    return f"{planet_name} {name} {suffix}"