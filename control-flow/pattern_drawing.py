# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Outer loop controls the number of rows
while row < size:
    # Inner loop prints asterisks in the same line
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after finishing a row
    print()
    
    # Increase the row counter
    row += 1
