#Cameron Buttery
#2305196

import random
import matplotlib.pyplot as plt
import numpy as np
#1
myID = "2305196"

#2
while True:
    varCount = int(input("Enter an integer (>=50): "))
    if varCount >= 50:
        print("Valid input", varCount)
        break
    else:
        print("Invalid input", varCount)
        
#3
s_d = sum(int(d) for d in myID)
# random.seed(ssd) ssd is not defined so corrected to the correct variable s_d
#int(d) for d in myID creates an iterable of integers by converting each element in myID to an integer.
#The sum function then takes this iterable and calculates the total sum of these integers.
random.seed(s_d)

#4
data = [random.randint(1, 200) for _ in range(varCount)]

data_sum = sum(data)
data_mean = data_sum / varCount
data_min = min(data)
data_max = max(data)

# print(f"Sum: {data_sum}, Mean: {data_mean:.2d}, Min: {data_min}, Max: {data_max}")
#The .2d is incorrect as it is reading the sum as an int instead of the target float
print(f"Sum: {data_sum}, Mean: {data_mean:.2f}, Min: {data_min}, Max: {data_max}")

x = np.random.normal(data_mean, data_min, varCount)

plt.hist(x)
plt.show() 