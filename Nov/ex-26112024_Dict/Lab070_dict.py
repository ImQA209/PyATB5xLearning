my_dict = {
    "name": "iyappan",
    "age": 34,
    "company": "zeesoft",
    "Role": "QA Engineer",
    "experience": 6
}
print(my_dict)
my_dict["Role"] = "Test Engineer"
print(my_dict)
del my_dict["experience"]
print(my_dict)

for key, value in my_dict.items():
    print(key, " >>", value)
print("age" in my_dict)
print("Name" in my_dict)
