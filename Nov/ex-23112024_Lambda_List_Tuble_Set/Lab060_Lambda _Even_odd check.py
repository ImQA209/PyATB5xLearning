# Write program to calculate the given number is even or odd

# def check_even(num):
#     if num % 2==0:
#         print("even")
#     else:
#         print("Odd")
# check_even(3)
#

check_even_odd= lambda num: "even" if num %2 == 0  else "odd"
print(check_even_odd(5))
print(check_even_odd(10))