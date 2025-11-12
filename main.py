import bcrypt
from login import login_user, register_user

def menu():
    print(" ---! Choose an option: !---")
    print("*=-[1] Register-=*")
    print("*=-[2] Login-=*")
    print("*=-[3] Exit-=*")

def main():
    while True:
        menu()
        choice = input('')
        if choice == "1":
            register_user()
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter Password: ")
            print(login_user(username, password))
        elif choice == '3':
            print("Good bye!") 
            break


if __name__ == "__main__":
    main()


