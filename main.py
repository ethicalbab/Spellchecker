from symspellpy import SymSpell, Verbosity

# Create a SymSpell object
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Load default dictionary
dictionary_path = "/Users/bab/anaconda3/lib/python3.11/site-packages/symspellpy/frequency_dictionary_en_82_765.txt"
bigram_path = "/Users/bab/anaconda3/lib/python3.11/site-packages/symspellpy/frequency_bigramdictionary_en_243_342.txt"
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

# Load custom grocery dictionary
custom_dictionary_path = "grocery_dictionary.txt"
if sym_spell.load_dictionary(custom_dictionary_path, term_index=0, count_index=1):
    print(f"Custom grocery dictionary '{custom_dictionary_path}' loaded successfully")
else:
    print(f"Failed to load custom grocery dictionary '{custom_dictionary_path}'")

def find_mistake_and_correct(query):
    # Convert the query to lowercase
    words = query.lower().split()
    original_words = query.split()
    result = []
    current_pos = 0  # Track the current character position

    for i, word in enumerate(words):
        # Check custom grocery dictionary first
        if word in sym_spell.words:
            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=0)
        else:
            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        
        if suggestions:
            suggestion = suggestions[0]
            if suggestion.term != word:
                start_index = query.lower().index(word, current_pos)
                end_index = start_index + len(word) - 1
                result.append((original_words[i], suggestion.term, start_index, end_index))
        current_pos += len(word) + 1  # +1 for the space
    formatted_result = []
    for original, corrected, start_index, end_index in result:
        formatted_result.append(f"Characters {start_index}-{end_index}: '{original}' -> '{corrected}'")
    
    return formatted_result

query = "this is phome"
mistakes = find_mistake_and_correct(query)
print(f"Mistakes found: {mistakes}")
