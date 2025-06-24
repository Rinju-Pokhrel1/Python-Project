# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def sub(x, y):
    return x - y

# Function to multiply two numbers
def mul(x, y):
    return x * y

# Function to divide two numbers
def div(x, y):
    if y == 0:  # Check if divisor is 0 to prevent error
        return "Error! Cannot divide by zero."
    return x / y

# Show the options to the user
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

while True:
    choice = input("Enter your choice (1/2/3/4): ")

    # Check if choice is valid
    if choice in ('1', '2', '3', '4'):
        # Take input numbers from user
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        # Perform the chosen operation
        if choice == '1':
            print(f"{x} + {y} = {add(x, y)}")
        elif choice == '2':
            print(f"{x} - {y} = {sub(x, y)}")
        elif choice == '3':
            print(f"{x} * {y} = {mul(x, y)}")
        elif choice == '4':
            result = div(x, y)
            print(f"{x} / {y} = {result}")

        # Ask if user wants another calculation
    
        next_calc = input("Do you want to do another calculation? (yes/no): ").lower()
        if next_calc != 'yes':
            print("Thank you!")
            break  # Exit the while loop

    else:
        print("Please enter 1, 2, 3, or 4:")
