# Function to print full pyramid pattern

row = int(input("Enter number of rows: "))

for i in range(row):

# Print leading spaces

    for j in range(row - i - 1):

        print(" ", end="")

    # Print stars

    for k in range(2 * i + 1):

        print("*", end="")

    # Move to the next line after each row

    print()