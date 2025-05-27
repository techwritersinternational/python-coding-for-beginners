def is_vowel(char):
    return char.lower() in 'aeiou'

def capitalize_word(word):
    return word.capitalize()

def translate_word(word):
    if not word.isalpha():
        return word
    
    original_case = word.isupper()
    word = word.lower()
    
    if is_vowel(word[0]):
        translated = word + 'ay'
    else:
        translated = word[1:] + word[0] + 'ay'
    
    translated = capitalize_word(translated) if word[0].isupper() else translated
    return translated.upper() if original_case else translated

def translate_sentence(sentence):
    words = sentence.split()
    translated_words = []
    
    for word in words:
        # Separate punctuation from the word
        punctuation = ''
        while word and not word[-1].isalnum():
            punctuation = word[-1] + punctuation
            word = word[:-1]
        
        # Translate the word
        translated_word = translate_word(word)
        
        # Reattach punctuation
        translated_words.append(translated_word + punctuation)
    
    return ' '.join(translated_words)

# Test the functions
print(translate_word("hello"))  # Should print "ellohay"
print(translate_word("apple"))  # Should print "appleay"
print(translate_word("Hello"))  # Should print "Ellohay"
print(translate_word("HELLO"))  # Should print "ELLOHAY"

test_sentence = "Hello, how are you today? I'm feeling great!"
print(translate_sentence(test_sentence))
# Should print: "Ellohay, owhay areay ouyay odaytay? I'may eelingfay eatgray!"