# Task 1: Basic Mathematical Operations  
# output are in readme file, as an image 
def basic_operations():  
    # Taking input from the user  
    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))  
    
    
    addition = num1 + num2  
    subtraction = num1 - num2  
    multiplication = num1 * num2  
    division = num1 / num2 if num2 != 0 else "Cannot divide by zero"  

     
    print(f"\nResults of operations on {num1} and {num2}:")  
    print(f"Addition: {addition}")  
    print(f"Subtraction: {subtraction}")  
    print(f"Multiplication: {multiplication}")  
    print(f"Division: {division}")  

 
basic_operations()  

# Task 2: Create a Personalized Greeting  

def personalized_greeting():  
   
    first_name = input("Enter your first name: ")  
    last_name = input("Enter your last name: ")  
    
    full_name = f"{first_name} {last_name}"  
    
    print(f"\nHello, {full_name}! Welcome!")  

personalized_greeting()  
