# Find the howmany vowels in this input string
my_dict = "a,c,d,e,o"
vowels = "aeiou"
vowels_count = 0
for char in my_dict:
    if char in vowels:
        vowels_count = vowels_count + 1
print(vowels_count)
