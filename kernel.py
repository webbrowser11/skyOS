import subprocess
import os
print("welcome to the SCA kernel lots of contributors worked on this!")
print("hope you find this program useful!")
while True:
  command = input("command:")
  if command == "help":
    print("help")
    print("info")
    print("echo")
    print("helloworld.app")
  elif command == "info":
    print("developed by the SCA all right reserved.")
    print("this kernel may not be reproduced in any way.")
    print("you can archive. (make sure the archive is public)")
  elif command == "echo":
    echotxt = input("echo what:")
    print(echotxt)
  elif command == "helloworld.app":
    scripts_to_run = ['helloworldapp.py']
    for s in scripts_to_run:
      subprocess.Popen([os.path.join(os.getcwd(), s)])
    break
  else:
    print("not a command type help for a list of commands")
