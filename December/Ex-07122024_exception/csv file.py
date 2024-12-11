import csv

with open("TestData.csv") as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        if len(col) < 2:
            continue
        print("The user details:", col[0], col[1], sep=" | ")
# import csv
#
# with open("TestData.csv") as csvfile:
#     reader = csv.reader(csvfile, delimiter='\t')  # Use '\t' for tab or specify ' ' for space
#     for col in reader:
#         # Skip empty or malformed rows
#         if len(col) < 2:
#             continue
#         # Strip whitespace if needed
#         print(col[0].strip(), col[1].strip(), sep="|")
