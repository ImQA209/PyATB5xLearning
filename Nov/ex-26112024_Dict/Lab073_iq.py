# Frequency of character in string

string = input("Enter the character")

char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
