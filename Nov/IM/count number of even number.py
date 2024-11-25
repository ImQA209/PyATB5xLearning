e_count = 0

for i in range(1, 11):
    if i % 2 == 0 :
        e_count=e_count+1


count = 0

for i in range(1, 11):
    if i % 2 == 1 :
        count=count+1

print("The total number of even number is:",e_count)
print("The total number of odd number is:",count)