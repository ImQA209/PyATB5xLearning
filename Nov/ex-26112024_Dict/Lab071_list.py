student_info1 = {
    "name": "iyappan",
    "department": "cse",
    "city": {
        "home": "chennai",
        "office": "Madurai"}
}
student_info2 = {
    "name": "iyappanManivannan",
    "department": "ece",
    "city": {
        "home": "karaikal",
        "office": "pondy"}
}
student_info3 = {
    "name": "Ganesh",
    "department": "eee",
    "city": {
        "home": "Theni",
        "office": "Namakkal"}
}

student_lit = [student_info1, student_info2, student_info3]
print(student_lit)
print(student_lit[0]["city"]["office"])
print(student_lit[2]["city"]["office"])
print(student_info3["city"]["home"])
