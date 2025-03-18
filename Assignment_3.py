# Task 1: Calculate Factorial Using a Function  

def factorial(n):  
    """Calculate the factorial of a number n using a loop."""  
    if n < 0:  
        return "Factorial is not defined for negative numbers."  
    result = 1  
    for i in range(1, n + 1):  
        result *= i  
    return result  

# Calling the function with a sample number  
number = 5  
calculated_factorial = factorial(number)  
print(f"The factorial of {number} is: {calculated_factorial}")  

