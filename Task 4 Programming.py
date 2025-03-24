#Cameron Buttery
#2305196

#For random number generation
import random 
#For graph plotting
import matplotlib.pyplot as plt 
import numpy as np

#1 My student ID
myID = "2305196"

#2
while True:
    varCount = int(input("Enter an integer (>=50): "))
    #Check if the input is greater than or equal to 50
    if varCount >= 50: 
        print("Valid input", varCount)
        break
    else:
        #If the input is less than 50, print an error message and ask for another input
        print("Invalid input", varCount) 
        
#3
#int(d) for d in myID creates an iterable of integers by converting each element in myID to an integer.
#The sum function then takes this iterable and calculates the total sum of these integers.
s_d = sum(int(d) for d in myID)
# random.seed(ssd) ssd is not defined so corrected to the correct variable s_d
random.seed(s_d) 

#4
#Random list of integers between 1 and 200
data = [random.randint(1, 200) for _ in range(varCount)] 

#computes the sum of data
data_sum = sum(data) 
#computes the mean of data
data_mean = data_sum / varCount 
#computes the minimum value of data
data_min = min(data) 
#computes the maximum value of data
data_max = max(data) 

# prints the results
print(f"Sum: {data_sum}, Mean: {data_mean:.2f}, Min: {data_min}, Max: {data_max}")

#Plot a histogram of the data
plt.hist(data, bins=10, edgecolor='black') 
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
#Display the histogram
plt.show() 

#Things i have changed
#1. I have added in my name and student ID.
#2. I corrected my loop to ask for another input as originally it would just print an error message and then break the loop.
#3. I corrected the random.seed function to use the correct variable s_d.
#4. I have added in the calculation of the sum of the data, the mean of the data, the minimum value of the data and the maximum value of the data.
#5. I have added in a histogram of the data.
