"""
This is the hello world program in Python
"""

import sys
import tkinter as tk
from tkinter import messagebox

# Student & Class Information
class_name = "Python Programming"
class_code = "2025SP-CIS-024C-101"
student_name = "Alfredo Servin"
student_id = "1085491"

# Function to display student info
def show_student_info():
    info_message = (
        f"Student Name: {student_name}\n"
        f"Student ID: {student_id}\n"
        f"Class Name: {class_name}\n"
        f"Class Code: {class_code}"
    )
    messagebox.showinfo("Student Info", info_message)

# Function to display Python version
def show_python_version():
    version_message = f"Python Version: {sys.version}"
    messagebox.showinfo("Python Version", version_message)

# Create main window
root = tk.Tk()
root.title("hello-world-py")  # Set window title
root.geometry()  # Set window size

# Create a label for the greeting
greeting_label = tk.Label(root, text="HELLO WORLD", font=("Arial", 16, "bold"))
greeting_label.pack(pady=10)  # Centered at the top

# Create a frame to hold the buttons side by side
button_frame = tk.Frame(root)
button_frame.pack(pady=10)  # Adds spacing below greeting

# Create buttons
student_button = tk.Button(root, text="Student Info", command=show_student_info, width=20, height=2)
python_button = tk.Button(root, text="Python Version", command=show_python_version, width=20, height=2)

# Place buttons side by side inside the frame
student_button.pack(side="left", padx=10)  # Adds space between buttons
python_button.pack(side="left")


# Run the GUI event loop
root.mainloop()

# Print details
print("\n==============================")
print("        CLASS DETAILS        ")
print("==============================")
print("Class Name  :", class_name)
print("Class Code  :", class_code)

print("\n==============================")
print("       STUDENT DETAILS       ")
print("==============================")
print("Student Name:", student_name)
print("Student ID  :", student_id)

print("\n==============================")
print("      PYTHON VERSION         ")
print("==============================")
print("Python Version:", sys.version)

print("\n==============================")
print("        GREETING             ")
print("==============================")
print("Hello, World!\n")
