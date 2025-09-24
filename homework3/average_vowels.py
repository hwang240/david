# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(s: str):
    letter_vowels = set("aeiouAEIOU") # takes all the vowels
    vowels = consonants = 0
    for characters in s:
        if characters.isalpha():
            if characters in letter_vowels:
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph: str):
    normalized = paragraph.replace('!', '.').replace('?', '.') # this changes sentences ending in ! and ? into .
    
    raw_parts = normalized.split('.') # split on '.' and strip spaces, which only keeps the non-empty sentences
    sentences = [s.strip() for s in raw_parts if s.strip()]

    n = len(sentences)
    if n == 0:
        return 0, 0.0, 0.0

    total_vowels = 0
    total_consonants = 0
    for s in sentences:
        vowels, consonants = counting_vowels_and_consonants(s)
        total_vowels += vowels
        total_consonants += consonants

    avg_vowels = total_vowels / n
    avg_consonants = total_consonants / n
    return n, avg_vowels, avg_consonants

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
import average_vowels as av
print(av.average_vowels_and_consonants(av.paragraph))