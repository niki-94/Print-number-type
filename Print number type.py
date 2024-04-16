# Auto detect text files and perform LF normalization
* text=auto
# Get input from the user
user_input = input("Enter a number: ")

# Try to convert the input to a number
try:
    user_number = float(user_input)
    # Check if the input is an integer or a float
    if user_number.is_integer():
        print("Number type: Integer")
    else:
        print("Number type: Float")
except ValueError:
    print("Input is not a valid number")