import subprocess
import os

print("Welcome to the SCA kernel. Lots of contributors worked on this!")
print("Hope you find this program useful!")

while True:
    command = input("command: ").strip().lower()
    
    if command == "help":
        print("Available commands:")
        print("help - show this help message")
        print("info - show information about this program")
        print("echo - echo back what you type")
        print("helloworld.app - run the helloworld application")
    
    elif command == "info":
        print("Developed by the SCA. All rights reserved.")
        print("This kernel may not be reproduced in any way.")
        print("You can archive (make sure the archive is public).")
    
    elif command == "echo":
        echotxt = input("Echo what: ").strip()
        print(echotxt)
    
    elif command == "helloworld.app":
        script_path = os.path.join(os.getcwd(), 'helloworldapp.py')
        if os.path.isfile(script_path):
            try:
                subprocess.run(['python', script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("helloworldapp.py not found in the current directory.")
        break
    
    else:
        print("Not a valid command. Type 'help' for a list of commands.")
