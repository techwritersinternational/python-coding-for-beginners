import json
import os

from ai_api_wrapper import LLMAPIWrapper

TRANSLATIONS_FILE = 'translations.json'

SYSTEM_PROMPT = """You are an expert linguist specializing in extraterrestrial languages. Your task is to translate between an unknown alien language and English. 

When given a phrase in the alien language, translate it to English. If given an English phrase, translate it to the alien language. 

Follow these guidelines:
1. Maintain consistent translations for specific words or phrases.
2. The alien language uses made-up words that sound alien but follow a consistent internal logic.
3. If you encounter a word you haven't seen before, invent a plausible translation based on the context and previous translations.

Remember, you are translating an actual language, not just making random sounds. Strive for consistency and logic in your translations. Return only the translation. Do not return an explanation of the translation choices."""

API = "anthropic"

def read_alien_phrases(filename):
    try:
        with open(filename, 'r') as file:
            phrases = file.read().splitlines()
        return phrases
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")
        return []



def translate_phrase(phrase, to_english=True):
    # Load existing translations
    translations = load_translations()
    
    phrase = clean_text(phrase)

    # Check if we already have this translation
    if to_english:
        translation = find_english_for_alien(phrase, translations)
    else:
        translation = find_alien_for_english(phrase, translations)

    if translation:
        return translation

    api_wrapper = LLMAPIWrapper()

    stateful_system_prompt = build_stateful_system_prompt()
    response = api_wrapper.call_api(API, phrase, stateful_system_prompt)

    response = clean_text(response)

    if response:
        # Store the new translation
        if to_english:
            translations["translations"].append({
                "Alien": phrase,
                "English": response
            })
        else:
            translations["translations"].append({
                "Alien": response,
                "English": phrase
            })
        
        save_translations(translations) 

        return response
    else:
        return "Failed to translate"

def clean_text(phrase):
    # Remove any unwanted characters
    phrase = phrase.replace(".", "")
    phrase = phrase.replace("\"", "")
    phrase = phrase.strip()
    phrase = phrase.capitalize()
    return phrase

def find_english_for_alien(alien_phrase, data):
    for translation in data['translations']:
        if translation['Alien'] == alien_phrase:
            return translation['English']
    return None

def find_alien_for_english(english_phrase, data):
    for translation in data['translations']:
        if translation['English'] == english_phrase:
            return translation['Alien']
    return None


def load_translations():
    if os.path.exists(TRANSLATIONS_FILE):
        with open(TRANSLATIONS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_translations(translations):
    with open(TRANSLATIONS_FILE, 'w') as f:
        json.dump(translations, f, indent=2)


def build_stateful_system_prompt():
    base_prompt = SYSTEM_PROMPT
    
    previous_translations = load_translations()

    if previous_translations and len(previous_translations) > 0:
        # Add known translations to the prompt
        translation_examples = "\n\nHere are some known translations to maintain consistency:\n"
        for original, translated in previous_translations.items():
            translation_examples += f"{original} <-> {translated}\n"
        
        base_prompt += translation_examples
    return base_prompt


def main():
    print("Welcome to the Alien Language Translator!")
    print("Enter 'quit' to exit the program.")
    print("Enter 'switch' to toggle between alien-to-English and English-to-alien translation.")

    to_english = True  # Start with alien-to-English translation

    while True:
        if to_english:
            print("\nEnter an alien phrase to translate to English:")
        else:
            print("\nEnter an English phrase to translate to alien language:")

        user_input = input("> ").strip()

        if user_input.lower() == 'quit':
            print("Thank you for using the Alien Language Translator. Goodbye!")
            break
        elif user_input.lower() == 'switch':
            to_english = not to_english
            print(f"Switched to {'alien-to-English' if to_english else 'English-to-alien'} translation.")
            continue
        elif not user_input:
            print("Please enter a phrase to translate.")
            continue

        translation = translate_phrase(user_input, to_english)

        print(f"Translation: {translation}")

if __name__ == "__main__":
    main()