# PythonOS v0.2.1
# Copylefted by RGB Fusion Studios with GPL 3.0


# Imports
import time
import random
import os
import datetime as dt


# Globals
setup_user = ""
setup_password = ""


# Functions
def user_add_func(username):
    try:
        with open("users.txt", "w") as user_file:
            user_file.write(username + "\n")
    except IOError as e:
        print(f"Error writing username to file: {e}")

def passwd_add_func(password):
    try:
        with open("passwd.txt", "w") as passwd_file:
            passwd_file.write(password + "\n")
    except IOError as e:
        print(f"Error writing password to file: {e}")

def change_setup_status(status="true"):
    try:
        with open("config.txt", "w") as config_file:
            config_file.write(f"setup_completed={status}\n")
    except IOError as e:
        print(f"Error updating setup status: {e}")

def setup_PythonOS():
    global setup_user, setup_password
    print("Setup required")
    time.sleep(1)
    print("Starting setup...")
    time.sleep(1.5)

    setup_user = input("Please add a user: ")
    user_add_func(setup_user)

    while True:
        passwd_add = input("Please enter a password: ")
        passwd_confirm = input("Please confirm your password: ")

        if passwd_add != passwd_confirm:
            print("Passwords do not match. Please try again.")
            time.sleep(1)
        else:
            setup_password = passwd_confirm
            passwd_add_func(setup_password)
            change_setup_status("true")

            print("Setup complete")
            time.sleep(1)

            while True:
                continue_to_login = input("Would you like to proceed to the login screen? [y/n] ").strip().lower()
                if continue_to_login == "y":
                    return
                elif continue_to_login == "n":
                    exit()
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
    print("Setup complete")

def reset_PythonOS():
    files_to_delete = ["config.txt", "users.txt", "passwd.txt"]
    print("\nAttempting to reset PythonOS...")
    for filename in files_to_delete:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"Deleted: {filename}")
            except OSError as e:
                print(f"Error deleting {filename}: {e}")
        else:
            print(f"Skipped: {filename} (not found)")
    print("""Hard reset completed
Please restart PythonOS for reset to apply""")

def help_command():
    print("""
Commands:
help - displays commands
rest - Hard resets this PythonOS installation (all data)
calc - Launches the calculator (2 digits only)
text - Launches the text editor (Coming soon!)
time - Launches the clock (Coming soon!)
musc - Launches the music player (Coming soon!)
caln - Launches the calendar (Coming soon!)""")

def get_number_input(prompt):
	while True:
		try:
			value = float(input(prompt))
			return value
		except ValueError:
			print("Invalid input. Please enter a valid number (e.g., 5, 3.14, -2.5)")

def get_operation_choice():
	while True:
		op = input("""
Operations:
  Add is +
  Subtract is -
  Multiply is *
  Divide is /
Operation: """).strip().lower()
		if op in ["+", "-", "*", "/"]:
			return op
		else:
			print("Not a valid operation. Please choose from +, -, *, or /.")

def get_quit_choice():
	while True:
		calc_quit = input("Would you like to quit the calculator? [y/n] ").strip().lower()
		if calc_quit in ["y", "n"]:
			return calc_quit
		else:
			print("Please enter 'y' for yes or 'n' for no.")


def calc():
	while True:
		x = get_number_input("First number: ")
		y = get_number_input("Second number: ")
		op = get_operation_choice()
		if op == "+":
			print(f"Result: {x} + {y} = {x + y}")
		elif op == "-":
			print(f"Result: {x} - {y} = {x - y}")
		elif op == "*":
			print(f"Result: {x} * {y} = {x * y}")
		elif op == "/":
			if y == 0:
				print("Error: Cannot divide by zero.")
			else:
				print(f"Result: {x} / {y} = {x / y}")
		calc_quit = get_quit_choice()
		if calc_quit == "y":
			break
			CLI()

def CLI():
	while True:
		print("""
	""")
		command = input(user + "@PythonOS_0.2 >>> ")
		if command == "help":
			help_command()
		elif command == "rest":
			reset_PythonOS()
			break
		elif command == "calc":
			calc()
		elif command == "text" or "time" or "musc" or "caln":
 			print("This feature is coming soon in PythonOS v0.3")
		else:
			print("Unknown command. Try help for a list of currently available commands.")



# Main script
if not os.path.exists("config.txt"):
    print("configuration file not found. Initializing setup.")
    change_setup_status("false")
    if os.path.exists("users.txt"):
        os.remove("users.txt")
    if os.path.exists("passwd.txt"):
        os.remove("passwd.txt")

setup_completed = False
try:
    with open("config.txt", "r") as config_file:
        config_data = config_file.read().strip()
        if "setup_completed=true" in config_data:
            setup_completed = True
        elif "setup_completed=false" in config_data:
            setup_completed = False
        else:
            print("Invalid content in config.txt. Forcing setup.")
            setup_completed = False
            change_setup_status("false")
except FileNotFoundError:
    print("config.txt not found (after initial check). Forcing setup.")
    setup_completed = False
    change_setup_status("false")
except IOError as e:
    print(f"Error reading config.txt: {e}. Forcing setup.")
    setup_completed = False


if not setup_completed:
    setup_PythonOS()

user_data = ""
passwd_data = ""

try:
    with open("users.txt", "r") as user_file:
        user_data = user_file.read().strip()
    with open("passwd.txt", "r") as passwd_file:
        passwd_data = passwd_file.read().strip()
except FileNotFoundError:
    print("User or password files not found. Please run setup again.")
    change_setup_status("false")
    exit()
except IOError as e:
    print(f"Error reading user/password files: {e}")
    exit()

while True:
    user = input("Username: ")
    password = input("Password: ")

    if user == user_data and password == passwd_data:
        print("Login successful!")
        break
    else:
        print("Incorrect user or password")


print("\nWelcome to PythonOS CLI!")
help_command()
CLI()
