# Program Name: Assignment1.py
# Course: IT3883/Section 01/W02
# Student Name: Bayden Blackwell 
# Assignment Number: Lab#1
# Due Date: 01/25/2025
# Purpose: This program implements a text-based menu to manipulate and display an input buffer. 
# Resources: Python documentation and personal knowledge.

def main():
    # init an empty input buffer
    input_buffer = ""
    
    while True:
        # menu options
        print("\nMenu:")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the program")
        
        # user choice
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            data = input("Enter the string to append: ")
            input_buffer += data  # append the input string to the buffer
            print("Data appended.")
        elif choice == "2":
            input_buffer = ""  # reset the buffer to empty
            print("Input buffer cleared.")
        elif choice == "3":
            if input_buffer:
                print(f"Current input buffer: {input_buffer}")
            else:
                print("The input buffer is empty.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")

# run the program
if __name__ == "__main__":
    main()
