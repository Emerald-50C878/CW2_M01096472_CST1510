print("Today we are making a login prompt.")
#first initialise input
username = input("Enter your username: ")
password = input("Enter your password: ")
act_user = ["superstevan", "Vaiiorex", "neicowo", "ttruths"]
act_password = ["CrystalGems100%"]
loop_var = True
while loop_var == True:
    if username in act_user:
        print(f"Username found! Welcome {username}")
    else:
        print("Username is not registered... Please create an account using the home page.")
        loop_var = False
    if password in password:
        print(f"Password correct!")
    else:
        print("Password incorrect, try again.")
        loop_var = False

    print(f"Login Successful!")