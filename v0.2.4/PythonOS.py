# PythonOS v0.2.4
# Copylefted by RGB Fusion Studios with GPL/GNU 3.0


# Imports
import time
import random
import os
import datetime
import pygame


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
                    clear_screen()
                    return
                elif continue_to_login == "n":
                    exit()
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
    print("Setup complete")

def reset_PythonOS():
    print("\nAttempting to reset PythonOS...")

    current_script_path = os.path.abspath(__file__)
    current_script_name = os.path.basename(current_script_path)

    deleted_count = 0
    skipped_count = 0
    error_count = 0

    for item_name in os.listdir('.'):
        item_path = os.path.join('.', item_name)

        if os.path.isfile(item_path) and item_name != current_script_name:
            try:
                os.remove(item_path)
                print(f"Deleted: {item_name}")
                deleted_count += 1
            except OSError as e:
                print(f"Error deleting {item_name}: {e}")
                error_count += 1
        else:
            print(f"Skipped: {item_name} (directory or self)")
            skipped_count += 1

    print(f"\nHard reset completed.")
    print(f"Summary: {deleted_count} files deleted, {skipped_count} items skipped, {error_count} errors.")
    print("Please restart PythonOS for reset to apply.")

def help_command():
    clear_screen()
    print("""
Commands:
help - displays commands
rest - Hard resets this PythonOS installation (all data)
calc - Launches the calculator
text - Launches the text editor
time - Launches the live clock
musc - Launches the music player
caln - Launches the calendar (Coming soon!)
aris - Launches my own AI made in Python (Work in progress)
optn - Launches the settings menu (Coming soon!)
exit - Closes the PythonOS CLI""")
    CLI()

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
	print("Welcome to the PythonOS Calculator!")
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
			help_command()
		elif calc_quit == 'n':
			clear_screen()

def _get_multiline_input(prompt_message):
    print(prompt_message)
    print("Enter 'DONE' on a new line to finish input.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        lines.append(line)
    return "\n".join(lines)

def _get_filename_input(action):
    # Allowed text-based file extensions
    allowed_extensions = ('.txt', '.py', '.md', '.json', '.csv', '.xml', '.html', '.css', '.js', '.log')
    while True:
        filename = input(f"Enter the filename for {action} (e.g., my_document.txt): ").strip()
        if not filename:
            print("Filename cannot be empty. Please try again.")
        elif filename.endswith(allowed_extensions):
            return filename
        else:
            print(f"Unsupported file type. Please use one of the following extensions: {', '.join(allowed_extensions)}")


def text_editor():
    print("Welcome to the PythonOS Text Editor!")

    protected_files = ["config.txt", "users.txt", "passwd.txt", "PythonOS.py"]

    while True:
        clear_screen()
        print("""
\n--- Menu ---""")
        print("C - Create New File")
        print("V - Open and View File")
        print("E - Edit File (Append/Overwrite)")
        print("D - Delete File")
        print("F - Find and Replace Text")
        print("L - Show All Files in Current Directory")
        print("Q - Exit Editor")

        choice = input("Enter your command (C/V/E/D/F/L/Q): ").strip().upper()

        if choice == 'C':
            filename = _get_filename_input("creating")
            if filename in protected_files:
                print(f"Access Denied: '{filename}' is a protected system file.")
                continue
            try:
                if os.path.exists(filename):
                    confirm = input(f"Warning: File '{filename}' already exists. Overwrite? (yes/no): ").lower()
                    if confirm != 'yes':
                        print("File creation cancelled.")
                        continue

                content = _get_multiline_input("Enter content for the new file:")
                with open(filename, 'w') as f:
                    f.write(content)
                print(f"File '{filename}' created and saved successfully.")
            except IOError as e:
                print(f"Error creating file '{filename}': {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == 'V':
            filename = _get_filename_input("viewing")
            if filename in protected_files:
                print(f"Access Denied: '{filename}' is a protected system file.")
                continue
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                    print(f"\n--- Content of '{filename}' ---")
                    print(content)
                    print(f"--- End of '{filename}' ---")
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found. Please ensure the name is correct and the file exists.")
            except IOError as e:
                print(f"Error reading file '{filename}': {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == 'E':
            filename = _get_filename_input("editing")
            if filename in protected_files:
                print(f"Access Denied: '{filename}' is a protected system file.")
                continue
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' not found. Please ensure the name is correct and the file exists.")
                continue

            try:
                with open(filename, 'r') as f:
                    current_content = f.read()
                    print(f"\n--- Current Content of '{filename}' ---")
                    print(current_content)
                    print(f"--- End of Current Content ---")

                print("\nEdit Options:")
                print("A. Append to file")
                print("O. Overwrite file")
                edit_option = input("Choose an option (A/O): ").lower().strip()

                if edit_option == 'a':
                    new_content = _get_multiline_input("Enter content to append:")
                    with open(filename, 'a') as f:
                        f.write("\n" + new_content if current_content else new_content)
                    print(f"Content appended to '{filename}' successfully.")
                elif edit_option == 'o':
                    confirm = input(f"Warning: This will REPLACE all content in '{filename}'. Continue? (yes/no): ").lower()
                    if confirm != 'yes':
                        print("Overwrite cancelled.")
                        continue
                    new_content = _get_multiline_input("Enter new content to overwrite the file:")
                    with open(filename, 'w') as f:
                        f.write(new_content)
                    print(f"File '{filename}' overwritten successfully.")
                else:
                    print("Invalid edit option. No changes made.")

            except IOError as e:
                print(f"Error editing file '{filename}': {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == 'D':
            filename = _get_filename_input("deleting")
            if filename in protected_files:
                print(f"Access Denied: '{filename}' is a protected system file.")
                continue
            try:
                if os.path.exists(filename):
                    confirm = input(f"Are you sure you want to delete '{filename}'? This cannot be undone. (yes/no): ").lower()
                    if confirm == 'yes':
                        os.remove(filename)
                        print(f"File '{filename}' deleted successfully.")
                    else:
                        print("File deletion cancelled.")
                else:
                    print(f"Error: File '{filename}' not found.")
            except OSError as e:
                print(f"Error deleting file '{filename}': {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == 'F':
            filename = _get_filename_input("finding and replacing in")
            if filename in protected_files:
                print(f"Access Denied: '{filename}' is a protected system file.")
                continue
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' not found. Cannot perform find/replace.")
                continue

            try:
                with open(filename, 'r') as f:
                    content = f.read()

                search_text = input("Enter the text to find: ")
                replace_text = input("Enter the text to replace it with: ")

                if not search_text:
                    print("Text to find cannot be empty. No replacement performed.")
                    continue

                if search_text not in content:
                    print(f"'{search_text}' not found in '{filename}'. No changes made.")
                    continue

                new_content = content.replace(search_text, replace_text)

                confirm = input(f"Found '{search_text}'. Replace all occurrences with '{replace_text}' in '{filename}'? (yes/no): ").lower()
                if confirm == 'yes':
                    with open(filename, 'w') as f:
                        f.write(new_content)
                    print(f"All occurrences of '{search_text}' replaced with '{replace_text}' in '{filename}'.")
                else:
                    print("Find and replace cancelled. No changes made.")

            except FileNotFoundError:
                print(f"Error: File '{filename}' not found. Cannot perform find/replace.")
            except IOError as e:
                print(f"Error accessing file '{filename}': {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


        elif choice == 'L':
            print("\n--- Files in Current Directory ---")
            files = [f for f in os.listdir('.') if os.path.isfile(f) and f not in protected_files]
            if files:
                for f in files:
                    print(f)
            else:
                print("No user files found in the current directory.")
            print("--- End of File List ---")

        elif choice == 'Q':
            break
            help_command()
        else:
            print("Invalid command. Please enter one of C, V, E, D, F, L, or Q.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clock():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Live Clock is running. Press Ctrl+C to stop.")

    try:
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")

            print(f"\rCurrent Time: {current_time}", end="", flush=True)

            time.sleep(1)

    except KeyboardInterrupt:
        help_command()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# --- Audio Player Functions ---
def list_audio_files(directory):
    audio_extensions = ('.mp3', '.wav', '.ogg')
    return [f for f in os.listdir(directory) if f.endswith(audio_extensions)]

def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

        print(f"\nPlaying: {file_path}")
        print("Commands: 'pause' | 'resume' | 'stop' | 'exit' | 'volume [0-100]'")

        while pygame.mixer.music.get_busy() or pygame.mixer.music.get_paused():
            command = input("> ").strip().lower()

            if command == "pause":
                pygame.mixer.music.pause()
                print("Paused.")
            elif command == "resume":
                pygame.mixer.music.unpause()
                print("Resumed.")
            elif command == "stop":
                pygame.mixer.music.stop()
                print("Stopped.")
                break
            elif command == "exit":
                pygame.mixer.music.stop()
                print("Exiting player.")
                break
            elif command.startswith("volume"):
                try:
                    volume_level = int(command.split()[1]) / 100.0
                    if 0.0 <= volume_level <= 1.0:
                        pygame.mixer.music.set_volume(volume_level)
                        print(f"Volume set to {int(volume_level * 100)}%")
                    else:
                        print("Volume must be between 0 and 100.")
                except (IndexError, ValueError):
                    print("Usage: volume [0-100]")
            else:
                print("Unknown command. Please use 'pause', 'resume', 'stop', 'exit', or 'volume [0-100]'.")

    except pygame.error as e:
        print(f"Error playing audio: {e}. Make sure the file exists and is a supported format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if pygame.mixer.get_init():
            pygame.mixer.quit()

def audio_player_main():
    directory = os.getcwd()
    audio_files = list_audio_files(directory)

    if not audio_files:
        print("No audio files found in this directory.")
        return

    print("\nAvailable audio files:")
    for idx, file in enumerate(audio_files, 1):
        print(f"{idx}. {file}")

    while True:
        try:
            choice = int(input("\nEnter the number of the file to play (or 0 to exit): "))

            if choice == 0:
                print("Exiting audio player.")
                break
            elif 1 <= choice <= len(audio_files):
                play_audio(os.path.join(directory, audio_files[choice - 1]))
                another_round = input("\nPlay another file? (yes/no): ").strip().lower()
                if another_round != 'yes':
                    print("Exiting audio player.")
                    break
                else:
                    print("\nAvailable audio files:")
                    for idx, file in enumerate(audio_files, 1):
                        print(f"{idx}. {file}")
            else:
                print("Invalid choice. Please enter a valid number from the list or 0 to exit.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nExiting audio player due to user interruption.")
            break


def CLI():
	while True:
		print('')
		command = input(user + "@PythonOS_v0.2.2 >>> ")
		if command == "help":
			help_command()
		elif command == "rest":
			reset_PythonOS()
			break
		elif command == "calc":
			clear_screen()
			calc()
		elif command == "text":
			clear_screen()
			text_editor()
		elif command == "time":
			clear_screen()
			clock()
		elif command == "musc":
			clear_screen()
			audio_player_main()
		elif command == "exit":
			exit()
		elif command == 'caln' or "optn":
 			print("This feature is coming soon in PythonOS v0.3")
		elif command == 'aris':
			print("This feature is coming in PythonOS v1.0")
		else:
			print("Unknown command. Try help for a list of currently available commands.")


# Main script
clear_screen()
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
        clear_screen()
        break
    else:
        clear_screen()
        print("Incorrect user or password")


print("\nWelcome to PythonOS CLI!")
print("""
Commands:
help - displays commands
rest - Hard resets this PythonOS installation (all data)
calc - Launches the calculator
text - Launches the text editor
time - Launches the live clock
musc - Launches the music player
caln - Launches the calendar (Coming soon!)
aris - Launches my own AI made in Python (Work in progress)
optn - Launches the settings menu (Coming soon!)
exit - Closes the PythonOS CLI""")
CLI()