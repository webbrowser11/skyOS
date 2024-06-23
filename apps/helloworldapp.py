import subprocess
import os
import sys

def main():
    print("Hello, World!")
    print("make an app in the app folder (with the same structure just modified to fit your app code.)")
    # Path to the kernel script in the KERNEL folder
    kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
    # Run the kernel script as a subprocess
    subprocess.run([sys.executable, kernel_script])

if __name__ == "__main__":
    main()
