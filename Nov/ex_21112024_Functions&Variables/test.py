rows = 5  # Number of rows

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for numbers
        print("*" * j)  # Print the same number in each row
    print()  # Move to the next line
