File_name = "Test.txt"
content = "Welcome to python automation"
with open(File_name, "w") as file:
    file.write(content)
with open(File_name, "r") as file:
    content2 = file.read()
    print(content2)
