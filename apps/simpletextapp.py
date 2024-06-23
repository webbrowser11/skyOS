import subprocess
import os
import sys

def main():
    print("Simple Text")
    print("(What did you expect from an app called simpletext?)")
    print("Oh, and by the way... 10 + 20 = " + 10+20 +"! How cool!")
    print("thanks, scratch_fakemon!")
    # Path to the kernel script in the KERNEL folder
    kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
    # Run the kernel script as a subprocess
    subprocess.run([sys.executable, kernel_script])

if __name__ == "__main__":
    main()
