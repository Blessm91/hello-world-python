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
    banner_width = 30  # Adjust width for centering
    info_message = (
        "=" * banner_width + "\n" +
        f"{'CLASS DETAILS':^30}" + "\n" +
        "=" * banner_width + "\n" +
        f"Class Name  : {class_name}\n" +
        f"Class Code  : {class_code}\n\n" +
        "=" * banner_width + "\n" +
        f"{'STUDENT DETAILS':^30}" + "\n" +
        "=" * banner_width + "\n" +
        f"Student Name: {student_name}\n" +
        f"Student ID  : {student_id}"
    )
    messagebox.showinfo("Student Info", info_message)

# Function to display Python version
def show_python_version():
    banner_width = 30
    version_message = (
        "=" * banner_width + "\n" +
        f"{'PYTHON VERSION':^30}" + "\n" +
        "=" * banner_width + "\n" +
        f"Python Version: {sys.version}"
    )
    messagebox.showinfo("Python Version", version_message)

# Function to display greeting in a formatted pop-up
def show_greeting():
    banner_width = 30
    greeting_message = (
        "=" * banner_width + "\n" +
        f"{'GREETING':^30}" + "\n" +
        "=" * banner_width + "\n" +
        "Hello, World!\n"
    )
    messagebox.showinfo("Greeting", greeting_message)

# Create main window
root = tk.Tk()
root.title("hello-world-py")  # Set window title
root.geometry()  # Set default window size

# Create a formatted label for the greeting
banner_width = 30
greeting_text = (
    "=" * banner_width + "\n" +
    f"{'HELLO WORLD!':^30}" + "\n" +
    "=" * banner_width
)
greeting_label = tk.Label(root, text=greeting_text, font=("Courier", 12, "bold"), justify="center")
greeting_label.pack(pady=10)  # Centered at the top

# Create a frame to hold the buttons side by side
button_frame = tk.Frame(root)
button_frame.pack(pady=10)  # Adds spacing below greeting

# Create buttons
student_button = tk.Button(button_frame, text="Student Info", command=show_student_info, width=20, height=2)
python_button = tk.Button(button_frame, text="Python Version", command=show_python_version, width=20, height=2)

# Place buttons side by side inside the frame
student_button.pack(side="left", padx=10)  # Adds space between buttons
python_button.pack(side="left", padx=10)  # Adds space between buttons

# Run the GUI event loop
root.mainloop()