# Task 1: Create a Dictionary of Student Marks  

def student_marks():  
    # Creating a dictionary with student names and their marks  
    marks_dict = {  
        "Alice": 85,  
        "Bob": 92,  
        "Charlie": 78,  
        "David": 90,  
        "Eve": 88  
    }  

    # Asking the user to input a student's name  
    student_name = input("Enter the student's name: ")  

    if student_name in marks_dict:  
        print(f"{student_name}'s marks: {marks_dict[student_name]}")  
    else:  
        print(f"Error: {student_name} does not exist in the records.")  

student_marks()  

# Task 2: Demonstrate List Slicing  

def demonstrate_list_slicing():  
    numbers = list(range(1, 11))  
    first_five = numbers[:5]  
    reversed_five = first_five[::-1]  

    print(f"Extracted list: {first_five}")  
    print(f"Reversed list: {reversed_five}")  

demonstrate_list_slicing()  
