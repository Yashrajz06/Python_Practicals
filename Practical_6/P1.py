correct_password = "Yashraj@2206209"

while True:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Access Granted!")
        break
    print("Incorrect password. Try again.")
