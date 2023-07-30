from spellchecker import SpellChecker

def auto_correct_tool(word):
    spell = SpellChecker()
    corrected_word = spell.correction(word)
    suggestions = spell.candidates(word)
    
    if corrected_word == word:
        print(f"The word '{word}' is spelled correctly.")
    else:
        print(f"The word '{word}' is misspelled. Did you mean '{corrected_word}'?")
        
    if suggestions:
        print("Other suggestions:")
        for suggestion in suggestions:
            print(suggestion)

# Example usage
word_to_correct = "sleping"
auto_correct_tool(word_to_correct)
