import json
import timeit
import matplotlib.pyplot as plt
import numpy as np


with open('large-file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# Define the processing function

def modify_data(records):
    for record in records:
        record['size'] = 42


# Specify record counts and number of repetitions

record_counts = [1000, 2000, 5000, 10000]
num_repeats = 100
average_times = []


# Measure processing time for each record count

for n in record_counts:
    timer = timeit.Timer(lambda: modify_data(data[:n]))
    total_time = timer.timeit(number=num_repeats)
    avg_time = total_time / num_repeats
    average_times.append(avg_time)
    print(f"Average time for processing {n} records: {avg_time:.6f} seconds")


# Using numpy.polyfit to compute a linear fit (slope and intercept)
slope, intercept = np.polyfit(record_counts, average_times, 1)
print(f"\nLinear Regression: processing_time = {slope:.6e} * n + {intercept:.6e}")

# Generate regression line data for plotting
x_fit = np.linspace(min(record_counts), max(record_counts), 100)
y_fit = slope * x_fit + intercept


# Plotting 

plt.figure(figsize=(8, 6))
plt.plot(record_counts, average_times, 'bo', markersize=8, label='Measured Average Time')
plt.plot(x_fit, y_fit, 'r-', linewidth=2,
         label=f'Linear Fit:\nTime = {slope:.2e} * records + {intercept:.2e}')
plt.xlabel('Number of Records Processed')
plt.ylabel('Average Processing Time (seconds)')
plt.title('Processing Time vs. Number of Records')
plt.legend()
plt.grid(True)
plt.savefig('output.3.2.png')
plt.show()
