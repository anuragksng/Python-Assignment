# Task 1: Read a File and Handle Errors  
# result is storing at Readme file
def read_file():  
    try:  
        # Opening and reading the file  
        with open('sample.txt', 'r') as file:  
            content = file.readlines()  
            # Printing each line of the file  
            for line in content:  
                print(line.strip())  # .strip() removes any leading/trailing whitespace  
    except FileNotFoundError:  
        print("Error: The file 'sample.txt' does not exist.")  

# Calling the function  
read_file()  

# Task 2: Write and Append Data to a File  

def write_and_append_to_file():  
    user_input = input("Enter some data to write to the file: ")  
    
    # Writing user input to the file  
    with open('output.txt', 'w') as file:  
        file.write(user_input + "\n")  # Writing user input followed by a newline  
    
    # Appending additional data to the file  
    additional_data = "This is some additional data."  
    with open('output.txt', 'a') as file:  
        file.write(additional_data + "\n")  # Append additional data followed by a newline  
    
    # Reading and displaying the final content of the file  
    with open('output.txt', 'r') as file:  
        print("\nFinal content of the file:")  
        print(file.read())  # Read and print the entire content of the file  

write_and_append_to_file()  
