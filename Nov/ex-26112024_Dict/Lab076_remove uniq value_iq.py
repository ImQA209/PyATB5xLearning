# remove duplicate value from dictionary

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}

uniq_value = set()
result = {}

for key, value in my_dict.items():
    if value not in uniq_value:
        result[key] = value
        uniq_value.add(value)
print(result)
