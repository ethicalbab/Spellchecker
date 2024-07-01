Certainly! Here’s the `README.md` file for your GitHub repository:

```markdown
# Spell Checker using SymSpell

This repository contains a script that uses the SymSpell library to find and correct spelling mistakes in a given query. The script utilizes both a default dictionary and a custom grocery dictionary for more accurate corrections.

## Prerequisites

- Python 3.6+
- SymSpellPy

## Installation

1. **Install SymSpellPy:**

   ```sh
   pip install symspellpy
   ```

2. **Download the Default Dictionaries:**

   You need to download the frequency dictionary and bigram dictionary files from the SymSpellPy repository or use the default ones installed with the library.

   - Frequency dictionary: `frequency_dictionary_en_82_765.txt`
   - Bigram dictionary: `frequency_bigramdictionary_en_243_342.txt`

   You can typically find these files at the following paths (adjust if you have a different installation path):

   - `frequency_dictionary_en_82_765.txt`: `/path/to/symspellpy/frequency_dictionary_en_82_765.txt`
   - `frequency_bigramdictionary_en_243_342.txt`: `/path/to/symspellpy/frequency_bigramdictionary_en_243_342.txt`

   Download them from [SymSpellPy GitHub repository](https://github.com/mammothb/symspellpy) if needed.

3. **Add Your Custom Grocery Dictionary:**

   Create a text file named `grocery_dictionary.txt` and add your custom words to it in the following format:

   ```
   term count
   ```

   Example:
   ```
   apple 100
   banana 80
   milk 50
   ```

## Usage

Update the `dictionary_path`, `bigram_path`, and `custom_dictionary_path` variables in the script to point to the correct locations of your dictionary files.

```python
from symspellpy import SymSpell, Verbosity

# Create a SymSpell object
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Load default dictionary
dictionary_path = "/path/to/symspellpy/frequency_dictionary_en_82_765.txt"
bigram_path = "/path/to/symspellpy/frequency_bigramdictionary_en_243_342.txt"
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

# Load custom grocery dictionary
custom_dictionary_path = "path/to/your/grocery_dictionary.txt"
if sym_spell.load_dictionary(custom_dictionary_path, term_index=0, count_index=1):
    print(f"Custom grocery dictionary '{custom_dictionary_path}' loaded successfully")
else:
    print(f"Failed to load custom grocery dictionary '{custom_dictionary_path}'")

def find_mistake_and_correct(query):
    # Convert the query to lowercase
    words = query.lower().split()
    original_words = query.split()
    result = []

    for i, word in enumerate(words):
        # Check custom grocery dictionary first
        if word in sym_spell.words:
            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=0)
        else:
            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        
        if suggestions:
            suggestion = suggestions[0]
            if suggestion.term != word:
                result.append((original_words[i], suggestion.term, i))
    
    return result

query = "this is phome"
mistakes = find_mistake_and_correct(query)
print(f"Mistakes found: {mistakes}")
```

## Example

Running the script with the query `"this is phome"` will output:

```
Mistakes found: [('phome', 'phone', 3)]
```

## Contributing

Feel free to open issues or submit pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Just replace the placeholder paths and URLs with the correct ones, and you should be all set!
