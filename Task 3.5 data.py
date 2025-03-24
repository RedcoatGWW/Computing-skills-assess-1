import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scipy

# Mean and standard deviation
mu, sigma = 0, 1  
data = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

# Plotting the histogram
plt.figure(figsize=(12, 8))
count, bins, _ = plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Calculate the mean, median, standard deviation, Q1, Q3, minimum and maximum values
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
min_val = np.min(data)
max_val = np.max(data)
Q1 = np.quantile(data, 0.25)
Q3 = np.quantile(data, 0.75)

# Prints all of the calculated values
print(f"Mean: {mean:.2f}, Median: {median:.2f}, Standard Deviation: {std_dev:.2f}, Min: {min_val}, Max: {max_val}, Q1: {Q1}, Q3: {Q3}")

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


