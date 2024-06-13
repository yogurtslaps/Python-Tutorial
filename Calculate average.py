# Write a function to calculate the average of the numbers in a list of items using the built-in sum function 

def Average(num1): 
    return sum(num1) / len(num1) 

num1 = [23, 4, 16, 26, 9, 2] 
average = Average(num1) 

print("Average of the list =", average)