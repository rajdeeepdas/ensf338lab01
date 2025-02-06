import json
import timeit

# Load the JSON file
with open('large-file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def modify_data():
    for record in data:
        record['size'] = 42

# Measure execution time over 10 runs
num_runs = 10
avg_time = timeit.timeit(modify_data, number=num_runs) / num_runs

print(f"Average time to modify size field: {avg_time:.6f} seconds")

# Write back the modified data in reverse order
with open('output.2.5.json', 'w', encoding='utf-8') as f:
    json.dump(data[::-1], f, indent=4)