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
        "==============================\n"
        "        CLASS DETAILS        \n"
        "==============================\n"
        f"Class Name  : {class_name}\n"
        f"Class Code  : {class_code}\n\n"
        "==============================\n"
        "       STUDENT DETAILS       \n"
        "==============================\n"
        f"Student Name: {student_name}\n"
        f"Student ID  : {student_id}"
    )
    messagebox.showinfo("Student Info", info_message)

# Function to display Python version
def show_python_version():
    version_message = (
        "==============================\n"
        "       PYTHON VERSION         \n"
        "==============================\n"
        f"Python Version: {sys.version}"
    )
    messagebox.showinfo("Python Version", version_message)  

# Function to display greeting in a formatted pop-up
def show_greeting():
    greeting_message = (
        "==============================\n"
        "        GREETING             \n"
        "==============================\n"
        "Hello, World!\n"
    )
    messagebox.showinfo("Greeting", greeting_message)

# Create main window
root = tk.Tk()
root.title("hello-world-py")  # Set window title
root.geometry()  
# Create a formatted label for the greeting
greeting_text = (
    "==============================\n"
    "        Hello, World!         \n"
    "==============================\n"
)
greeting_label = tk.Label(root, text=greeting_text, font=("Courier", 12, "bold"), justify="center")
greeting_label.pack(pady=10)  

# Create a frame to hold the buttons side by side
button_frame = tk.Frame(root)
button_frame.pack(pady=10)  # Adds spacing below greeting

# Create buttons
student_button = tk.Button(button_frame, text="Student Info", command=show_student_info, width=20, height=2)
python_button = tk.Button(button_frame, text="Python Version", command=show_python_version, width=20, height=2)

# Place buttons side by side inside the frame
student_button.pack(side="left", padx=10)  # Adds space between buttons
python_button.pack(side="left")

# Run the GUI event loop
root.mainloop()
