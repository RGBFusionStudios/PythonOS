#PythonOS v0.1
#Licensed by RGB Fusion Studios with GPL 3.0


#Imports
import time
import random

#Functions
def user_add_func():
    with open("users.txt", "w") as user_added:
        user_added.write(user_add)
    user_added.close()

def passwd_add_func():
    with open("passwd.txt", "w") as passwd_added:
        passwd_added.write(passwd_confirm)
    passwd_added.close()

def change_setup():
    with open("config.txt", "w") as config_file:
        config_file.write("setup_completed=true")
    config_file.close()

def setup_PythonOS():
    print("Setup not completed")
    time.sleep(1)
    user_add = input("Please add a user: ")
    user_add_func
    while True:
        passwd_add = input("Please enter a password: ")
        passwd_confirm = input("Please confirm your password: ")
        if passwd_add != passwd_confirm:
            print("Passwords do not match. Please try again.")
            passwd_add = ""
            passwd_confirm = ""
            time.sleep(1)
        else:
            passwd_add_func
            change_setup
            print("Setup complete")
            time.sleep(1)
            while True:
                continue_to_login = input("Would you like to proceed to the login screen? [y/n] ")
                if continue_to_login == "y" or "Y":
                    break
                elif continue_to_login == "n" or "N":
                    exit()
        break

#Main script
config_data_open = open("config.txt", "r")
config_data = config_data_open.read()

if "setup_completed=false" in config_data:
    setup_PythonOS()
elif "setup_completed=true" in config_data:
    config_data_open.close()

while True:
    user = input("Username: ")
    password = input("Password: ")

    user_data_open = open("users.txt", "r")
    user_data = user_data_open.read()
    if user in user_data:
        user_data_open.close()
        passwd_data_open = open("passwd.txt", "r")
        passwd_data = passwd_data_open.read()
        if password in passwd_data:
            passwd_data_open.close()
            break
        else:
            print("Incorrect user or password")
            user = ""
            password = ""
    else:
        print("Incorrect user or password")