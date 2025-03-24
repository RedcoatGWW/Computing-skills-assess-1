import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scipy

# Mean and standard deviation
mu, sigma = 0, 1  
data = np.random.normal(mu, sigma, 1000)

# Plotting the histogram
plt.figure(figsize=(8, 5))
count, bins, _ = plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Calculate the mean, median, standard deviation, minimum and maximum values
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
min_val = np.min(data)
max_val = np.max(data)

# Prints all of the calculated values
print(f"Mean: {mean:.2f}, Median: {median:.2f}, Standard Deviation: {std_dev:.2f}, Min: {min_val}, Max: {max_val}")

# Fit a normal distribution curve
x = np.linspace(min_val, max_val, 500)
# Computes the value of the probability density function
pdf = scipy.norm.pdf(x, mean, std_dev)
plt.plot(x, pdf, 'r', linewidth=2, label='Distribution Curve')

# Labels and titles
plt.title("Histogram with Normal Distribution Curve")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()


