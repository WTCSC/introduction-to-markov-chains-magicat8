import random
import re

# Open the file with UTF-8 encoding
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Preprocessing text to handle punctuation and capitalization
text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
text = text.lower()  # Convert all words to lowercase

words = text.split()
transitions = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

def generate_text(start_word, num_words):
    current_word = start_word.lower()  # Start word in lowercase to match dictionary
    result = [current_word]
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    generated_text = " ".join(result)
    return generated_text.capitalize() + '.'

# Get user input for starting word and number of words
start_word = input("Enter a starting word: ")
num_words = int(input("Enter the number of words to generate: "))
print(generate_text(start_word, num_words))
