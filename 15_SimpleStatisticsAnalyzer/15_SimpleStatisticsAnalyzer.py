# Goal
# Input multiple numbers and store them in a list
# Calculate mean, median, mode, variance, and standard deviation


import statistics

print("📊 Simple Statistics Analyzer")

# Input numbers
data = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("\n📌 Results")
print(f"Data: {data}")
print(f"Mean: {statistics.mean(data):.2f}")
print(f"Median: {statistics.median(data)}")
print(f"Mode: {statistics.mode(data)}")
print(f"Variance: {statistics.pvariance(data):.2f}")
print(f"Standard Deviation: {statistics.pstdev(data):.2f}")
