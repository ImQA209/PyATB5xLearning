# pgm for age>18 vote
User_age=int(input("Enter your age\n"))
"""
if User_age >18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
"""
print("You are eligible to vote to put" if User_age >18 else "You are not eligible to vote to put")