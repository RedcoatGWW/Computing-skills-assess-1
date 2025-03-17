import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#1 
mu, sigma = 0, 1  # Mean and standard deviation
data = np.random.normal(mu, sigma, 1000)

# Step 2: Plot a histogram
plt.figure(figsize=(8, 5))
count, bins, _ = plt.hist(data)

# Step 3: Calculate descriptive statistics
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
min_val = np.min(data)
max_val = np.max(data)

print(f"Mean: {mean:.4f}")
print(f"Median: {median:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")
print(f"Min: {min_val:.4f}, Max: {max_val:.4f}")

# Step 4: Fit a normal distribution curve
x = np.linspace(min_val, max_val, 100)
pdf = stats.norm.pdf(x, mean, std_dev)
plt.plot(x, pdf, 'r', linewidth=2)

# Labels and title
plt.title("Histogram and Normal Distribution Fit")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
