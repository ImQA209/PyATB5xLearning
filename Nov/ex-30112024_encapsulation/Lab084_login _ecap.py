class login():
    def __init__(self, email, password):
        self.Email = email
        self.Password = password

    def display(self):
        if self.Email == "Iyappan@gmail.com" and self.Password == "Iyappan":
            print("Login sucessful")
        else:
            print("login failed")


user_details = login("Iyappan@gmail.com", "Iyappan")
user_details.display()
