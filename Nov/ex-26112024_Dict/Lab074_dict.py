dict1 = {"a": 2, "b": 3, "c": 4}
dict2 = {"a": 2, "b": 3}
missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)
