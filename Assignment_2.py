# Task 1: Check if a Number is Even or Odd  

def check_even_odd():  
    
    number = int(input("Enter an integer: "))
    if number % 2 == 0:  
        print(f"{number} is even.")  
    else:  
        print(f"{number} is odd.")  
check_even_odd()  

# Task 2: Sum of Integers from 1 to 50 Using a Loop  

def sum_integers():  
    total_sum = 0  
    
    for number in range(1, 51):  
        total_sum += number  

    print(f"The sum of integers from 1 to 50 is: {total_sum}")  

sum_integers()  
