import json
import timeit
import matplotlib.pyplot as plt


with open('large-file.json', 'r', encoding='utf-8') as f:
        data = json.load(f)




def modify_data():
    # Process only the first 1000 records
    for record in data[:1000]:
        record['size'] = 42



# Set repeat to 1000; each repetition runs modify_data() exactly once.
num_repeats = 1000
times = timeit.repeat(modify_data, number=1, repeat=num_repeats)

# Optional: print a few timing samples to the console
print("Sample measured times (seconds):")
print(times[:10])  # print the first 10 measured times


# Plot the histogram of the measured times using matplotlib

plt.figure(figsize=(8, 6))
plt.hist(times, bins=30, edgecolor='black')
plt.title("Distribution of Processing Times for 1000 Records")
plt.xlabel("Processing Time (seconds)")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("output.3.3.png")
plt.show()
