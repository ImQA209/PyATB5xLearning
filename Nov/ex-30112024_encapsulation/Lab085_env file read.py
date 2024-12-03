import os

from dotenv import load_dotenv


class login():
    def __init__(self, email, password):
        self.Email = email
        self.Password = password

    def display(self):
        if self.Email == "Iyappan@gmail.com" and self.Password == "Iyappan":
            print("Login sucessful")
        else:
            print("login failed")


load_dotenv()

email = os.getenv("Email")
password = os.getenv("Password")
print(email, password)

user_details = login(email, password)
user_details.display()
