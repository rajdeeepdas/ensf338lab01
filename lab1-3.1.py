import json
import matplotlib.pyplot as plt

# Load the JSON data from file
with open("internetdata.json", "r") as f:
    data = json.load(f)

# Prepare lists for the two groups:
#   group1: countries with income per person < 10,000
#   group2: countries with income per person >= 10,000
group1_internet = []
group2_internet = []

for record in data:
    income = record.get("incomeperperson")
    internet_rate = record.get("internetuserate")
    
    # Skip records with missing income or internet data
    if income is None or internet_rate is None:
        continue

    if income < 10000:
        group1_internet.append(internet_rate)
    else:
        group2_internet.append(internet_rate)

# Create histogram for group 1 (income < 10,000)
plt.figure()
plt.hist(group1_internet, bins=10, edgecolor='black')
plt.title("Internet Usage (Income < 10,000)")
plt.xlabel("Internet Usage (%)")
plt.ylabel("Frequency")
plt.savefig("hist1.png")
plt.close()  # close the figure

# Create histogram for group 2 (income >= 10,000)
plt.figure()
plt.hist(group2_internet, bins=10, edgecolor='black')
plt.title("Internet Usage (Income >= 10,000)")
plt.xlabel("Internet Usage (%)")
plt.ylabel("Frequency")
plt.savefig("hist2.png")
plt.close()  # close the figure

print("Histograms saved as hist1.png and hist2.png")
