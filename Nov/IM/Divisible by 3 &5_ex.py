# count = 0
count = 0
for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print(i)
        count=count+1
print("Count:" ,count)

