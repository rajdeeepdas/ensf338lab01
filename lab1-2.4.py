import timeit

def count_vowels(word):
    vowels = "aeiouy"
    return sum(1 for char in word.lower() if char in vowels)

def calculate_average_vowels(filename, start_line):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

  
    for i, line in enumerate(lines):
        if start_line in line:
            lines = lines[i:]
            break
    else:
        raise ValueError(f"Start line '{start_line}' not found in the file.")

    total_vowels = 0
    total_words = 0

    for line in lines:
        words = line.split()
        total_vowels += sum(count_vowels(word) for word in words)
        total_words += len(words)


    return total_vowels / total_words if total_words > 0 else 0

def timed_calculate_average_vowels():
    filename = 'pg2701.txt'
    start_line = 'CHAPTER 1. Loomings.'
    return calculate_average_vowels(filename, start_line)

#  timeit 
execution_time = timeit.timeit(timed_calculate_average_vowels, number=100)

#  average time for 100 repetitions
average_time = execution_time / 100
print(f"Average time for 100 repetitions: {average_time:.6f} seconds")
