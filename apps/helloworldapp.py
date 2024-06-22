import subprocess
import os
import sys

def main():
    print("Hello, World from hello world app!")
    # Path to the kernel script
    kernel_script = os.path.join(os.getcwd(), 'kernel.py')
    # Run the kernel script as a subprocess
    subprocess.run([sys.executable, kernel_script])

if __name__ == "__main__":
    main()
