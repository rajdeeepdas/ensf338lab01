import re
def count_vowels(word):
    vowels = "aeiouy"
    return sum(1 for char in word.lower() if char in vowels)

def calculate_average_vowels(filename, start_line):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # start line
    start_index = next((i for i, line in enumerate(lines) if start_line in line), None)
    if start_index is None:
        raise ValueError(f"Start line '{start_line}' not found in the file.")

    # Loading relevant lines into an array
    relevant_lines = lines[start_index:]

    #  counters
    total_vowels = 0
    total_words = 0

   
    for line in relevant_lines:
        # Splitting into words using regex to handle punctuation
        words = re.findall(r'\b\w+\b', line)
        total_vowels += sum(count_vowels(word) for word in words)
        total_words += len(words)

    
    average_vowels = total_vowels / total_words if total_words > 0 else 0
    return average_vowels

filename = 'pg2701.txt'
start_line = 'CHAPTER 1. Loomings.'


try:
    average_vowels = calculate_average_vowels(filename, start_line)
    print(f"The average number of vowels per word is: {average_vowels:.2f}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except ValueError as e:
    print(e)

