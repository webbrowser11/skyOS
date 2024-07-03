import subprocess
import os
import sys
from datetime import datetime
import pytz

treevalue = 1
print("Welcome to the skyOS! Thank you to all those contributors who worked on this!")
print("Hope you find this OS useful!")
print("SkyOS v1.6 OScore python3")

# Assuming the apps directory is one level up from the KERNEL directory
apps_dir = os.path.join(os.path.dirname(os.getcwd()), 'apps')

command_history = []

while True:
    command = input("command: ").strip().lower()
    command_history.append(command)
    
    if command == "help":
        print("Available commands:")
        print("help - show this help message")
        print("info - show information about this program")
        print("echo - echo back what you type")
        print("helloworld.app - run the helloworld application")
        print("simpletext.app - run the simple text app by scratch_fakemon!")
        print("tree - create a value for tree. use the -p command to print the value.")
        print("history - show all command history")
        print("time - see the time in 12hr format")
        print("shutdown - shutdown the system (asks for OS type)")
    
    elif command == "time":
        # Specify the timezone.
        timezone = pytz.timezone('America/Los_Angeles')

        # Get the current time in the specified timezone
        now = datetime.now(timezone)

        # Format the date and time as a 12-hour clock with AM/PM
        current_time = now.strftime("%I:%M %p")

        # Print the current date and time
        print(current_time)
    
    elif command == "info":
        print("Developed by the SCA. All rights reserved.")
        print("This kernel may not be reproduced in any way.")
        print("You can archive (make sure the archive is public).")
    
    elif command == "echo":
        echotxt = input("Echo what: ").strip()
        print(echotxt)

    elif command == "tree":
        treevalue = input("tree:")
        print("the value of tree is set.")
    elif command == "tree -p":
        print(treevalue)

    elif command == "helloworld.app":
        script_path = os.path.join(apps_dir, 'helloworldapp.py')
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
        script_path = os.path.join(apps_dir, 'simpletextapp.py')
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

    elif command == "shutdown":
        os_type = input("Are you using Windows or Linux? [W/L]: ").strip().lower()
        if os_type == 'w':
            script_path = os.path.join(os.getcwd(), 'shutdown', 'windowsshutdown.c')
            if os.path.isfile(script_path):
                # Compile the C program
                compiled_path = os.path.join(os.getcwd(), 'shutdown', 'windowsshutdown.exe')
                compile_command = f"gcc {script_path} -o {compiled_path}"
                try:
                    subprocess.run(compile_command, shell=True, check=True)
                    # Run the compiled program
                    subprocess.run([compiled_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error compiling or executing the script: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                print("windowsshutdown.c not found in the 'shutdown' directory.")
        elif os_type == 'l':
            script_path = os.path.join(os.getcwd(), 'shutdown', 'linuxshutdown.c')
            if os.path.isfile(script_path):
                # Compile the C program
                compiled_path = os.path.join(os.getcwd(), 'shutdown', 'linuxshutdown')
                compile_command = f"gcc {script_path} -o {compiled_path}"
                try:
                    subprocess.run(compile_command, shell=True, check=True)
                    # Run the compiled program
                    subprocess.run([compiled_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error compiling or executing the script: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                print("linuxshutdown.c not found in the 'shutdown' directory.")
        else:
            print("Invalid option. Please type 'W' for Windows or 'L' for Linux.")
    
    else:
        print("Not a valid command. Type 'help' for a list of commands.")
