print("welcome to the SCA kernel lots of contributors worked on this!")
print("hope you find this program useful!")
while True:
  command = input("command:")
  if command == "help":
    print("help")
    print("info")
    print("echo")
  elif command == "info":
    print("developed by the SCA all right reserved.")
    print("this kernel may not be reproduced in any way.")
    print("you can archive. (make sure the archive is public)")
  elif command == "echo":
    echotxt = input("echo what:")
    print(echotxt)
  else:
    print("not a command type help for a list of commands")
