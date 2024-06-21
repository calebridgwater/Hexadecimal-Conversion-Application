# Binary, Decimal, and Hexadecimal numberical conversion interface project!
# this script is for a a 3 way conversion tool to return the binary, decimal, and hexadecimal alpha-numerical representations of a user's inputed value, in a graphical user interface.
# CB 2024 06 21

import tkinter as tk
from tkinter import messagebox

# define conversion functions for decimal values to binary and hexadecimal values. 
def decimal_to_binary(decimal_number):
     return bin(decimal_number)[2:]
def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:].upper()

# Conversion function
def convert_number (event=None):  #added 'event=None' parameter to handle keybinding to the return key for this function. 
    input_str = entry.get()
    try:
# will determine the input type and convert the field's value to all three alpha-numerical formats.
        if input_str.startswith('0x') or input_str.startswith('0X'):
# hexadecimal input
            decimal_number = int(input_str, 16)
        elif input_str.startswith('0b') or input_str.startswith('0B'):
# binary input
            decimal_number = int(input_str, 2)
        else: 
# decimal input
            decimal_number = int(input_str)           
# Convert a decimal to binary and hexadecimal
            binary_number = decimal_to_binary(decimal_number)
            hexadecimal_number = decimal_to_hexadecimal(decimal_number)
# Display the conversion results
            result_label.config(text=f"Decimal:{decimal_number}\nBinary: {binary_number}\nHexadecimal: {hexadecimal_number}")
    except ValueError: 
        messagebox.showerror("Invalid Input", "Please enter a valid number (decimal, hexadecimal, or binary).")
        
# define an application exit window, incase one is not displayed on the application header, to close the window.
def exit_application():
    root.destroy()
    
# creates the main window
root = tk.Tk()
root.title("Three-way converter")

# creates and places the GUI window widgets
instructions_label = tk.Label(root, text="Enter a number (decimal, binary with '0b', or hexadecimal with '0x'):")
instructions_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0))

entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_number)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.grid(row=4, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# add the Return/Enter keybind as an event for the convert_number function 
root.bind('<Return>', convert_number)

# run the converter application
root.mainloop()

#_________________________________________________________________________________________
#Code below this is left over from previous converter versions and not used in the above applicaiton.

# Defines the main conversion function with three interchangable options between decimals, binary, and hexadecimal numbers.
#def main():
#    while True:
#        print("Decimal Converter")
#        print("1. Convert to Binary")
#        print("2. Convert to Hexadecimal")
#        print("3. Exit")
#        
#        choice = input("Choose your option (1, 2, or 3): ")
#        
#        if choice == '1':
#            decimal_number = get_valid_decimal_input() 
#            binary_number = decimal_to_binary(decimal_number)
#            print(f"The binary representation of {decimal_number} is {binary_number}\n")
#        elif choice == '2':
#            decimal_number = int(input("Enter a decimal number: "))
#            hexadecimal_number = decimal_to_hexadecimal(decimal_number)
#            print(f"The hexadecimal representation of {decimal_number} is {hexadecimal_number}\n")
#        elif choice == '3':
#            print("Exiting the program. Have a nice day!")
#            break
#        else: 
#            print("Invalid choice. Please select an available option (1, 2, or 3)\n")
#
#def get_valid_decimal_input():
#    while True:
#        try:
#            decimal_number = int(float(input("Enter a decimal number: ")))
#            return decimal_number 
#        except ValueError:
#            print("invalid input. please enter a valid decimal number.")
#         
#def decimal_to_binary(decimal_number):
#    if decimal_number == 0:
#        return "0" 
#    binary_number = ""
#    while decimal_number > 0:
#        reminder = decimal_number % 2 
#        binary_number = str(reminder) + binary_number
#        decimal_number = decimal_number // 2
#    return binary_number
#    
#def decimal_to_hexadecimal(decimal_number):
#    if decimal_number == 0:
#        return "0"
#    hex_digits = "0123456789ABCDEF"
#    hexadecimal_number = ""
#    while decimal_number > 0:
#        remainder = decimal_number % 16
#        hexadecimal_number  = hex_digits[remainder] + hexadecimal_number
#        decimal_number = decimal_number // 16
#    return hexadecimal_number 
#
#if __name__ == "__main__":
#    main()
#        