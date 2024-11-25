
def print_left_triangle(rows):
    for i in range(1,rows):
        print(" " * (rows - i) + "*" * i)

# Get the number of rows from the user

print_left_triangle(5)
