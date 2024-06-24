import subprocess
import os
import sys

print("Welcome to skyOS! Thank you to all the contributors who worked on this!")
print("Hope you find this OS useful!")

command_history = []

while True:
    command = input("command: ").strip().lower()
    command_history.append(command)
    
    if command == "help":
        print("Available commands:")
        print("  help - Show this help message")
        print("  info - Show information about this program")
        print("  echo - Echo back what you type")
        print("  helloworld.app - Run the HelloWorld application")
        print("  simpletext.app - Run the Simple Text app by scratch_fakemon")
        print("  history - Show command history")
    
    elif command == "info":
        print("Developed by the SCA. All rights reserved.")
        print("This kernel may not be reproduced in any way.")
        print("You can archive (make sure the archive is public).")
    
    elif command == "echo":
        echotxt = input("Echo what: ").strip()
        print(echotxt)
    
    elif command == "helloworld.app":
        script_path = os.path.join(os.getcwd(), 'apps', 'helloworldapp.py')
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("helloworldapp.py not found in the 'apps' directory.")
    
    elif command == "simpletext.app":
        script_path = os.path.join(os.getcwd(), 'apps', 'simpletextapp.py')
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("simpletextapp.py not found in the 'apps' directory.")
    
    elif command == "history":
        print("Command History:")
        for index, cmd in enumerate(command_history, start=1):
            print(f"{index}: {cmd}")
    
    else:
        print("Not a valid command. Type 'help' for a list of commands.")
