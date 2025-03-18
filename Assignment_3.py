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


# Task 2: Using the Math Module for Calculations  
import math  

def perform_calculations():  
    # Asking the user for a number  
    number = float(input("Enter a number: "))  
    
    # Calculating results using the math module  
    square_root = math.sqrt(number)  
    natural_log = math.log(number) if number > 0 else "Undefined for non-positive numbers"  
    sine_value = math.sin(number)  # sine function takes radians  

    print(f"The square root of {number} is: {square_root}")  
    print(f"The natural logarithm (log base e) of {number} is: {natural_log}")  
    print(f"The sine of {number} (radians) is: {sine_value}")  

perform_calculations()  
