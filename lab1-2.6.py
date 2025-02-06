import timeit

# Function to compute 2^n
def pow2(n):
    return 2 ** n

# Timing the execution of 10000 instances of pow2(10000)
time_pow2 = timeit.timeit(lambda: pow2(10000), number=10000)
print(f"Time taken for 10000 instances of pow2(10000): {time_pow2} seconds")

# Function using a for loop to compute pow2(n) for n up to 1000
def pow2_loop(n):
    results = []
    for i in range(n + 1):
        results.append(pow2(i))
    return results

# Function using list comprehension to compute pow2(n) for n up to 1000
def pow2_list_comprehension(n):
    return [pow2(i) for i in range(n + 1)]

# Timing the execution of 1000 instances of each approach
time_loop = timeit.timeit(lambda: pow2_loop(1000), number=1000)
time_list_comprehension = timeit.timeit(lambda: pow2_list_comprehension(1000), number=1000)

print(f"Time taken for 1000 instances using for loop: {time_loop} seconds")
print(f"Time taken for 1000 instances using list comprehension: {time_list_comprehension} seconds")
