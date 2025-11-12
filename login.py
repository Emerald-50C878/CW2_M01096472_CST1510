import bcrypt
import os

plain_text_pass = "Magic123"

def hash_pass(pwd):
    #Encode the password to bytes, required by bcrypt
    password_bytes = pwd.encode('utf-8')
    #generate a salt and hash password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
	# Decode the hash back to a string to store in a text file
    return hashed.decode('utf-8')

def verify_password(pwd, hashed):
    password_bytes = pwd.encode("utf-8")
    hashed_bytes = hashed.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_pass(password)
    with open('users.txt', 'a') as f:
        f.write(f"{username}, {hashed_password}\n")
    print("User registered successfully")

def login_user(username, password):
    with open('users.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            u_name, hash_with_space = line.strip().split(",")
            hash = hash_with_space.strip()
            if u_name == username:
                is_verified = verify_password(password, hash)
                if is_verified:
                    print(f"Login successful for user: {username}")
                else:
                    print("Login failed: Incorrect password.")
                return is_verified # Exit the function immediately after finding the user
