import tkinter as tk
from tkinter import font

# Initialize the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#2c2c2c")  # Dark background for the window

# Global variable to keep track of expression
expression = ""

# Function to update expression in the text entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def equal_press():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Set up the input field with custom styling
equation = tk.StringVar()
expression_field = tk.Entry(root, textvariable=equation, font=('Arial', 24, 'bold'), fg='#ffffff', bg="#333333", bd=10, insertwidth=4, width=14, justify='right')
expression_field.grid(row=0, column=0, columnspan=4, ipady=10)

# Button Styling
button_font = font.Font(family='Arial', size=18, weight='bold')
button_bg = "#4d4d4d"
button_fg = "#ffffff"
highlight_bg = "#666666"

# Creating buttons with improved styling
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

buttons = []
for i, text in enumerate(button_texts):
    if text == "=":
        action = equal_press
    else:
        action = lambda t=text: press(t)
    
    # Create the button with custom styles
    button = tk.Button(root, text=text, padx=20, pady=20, font=button_font, fg=button_fg, bg=button_bg,
                       activebackground=highlight_bg, activeforeground=button_fg, command=action)
    buttons.append(button)

# Arrange buttons in a grid layout
for i, button in enumerate(buttons):
    row = (i // 4) + 1
    col = i % 4
    button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

# Clear button with unique styling
clear_button = tk.Button(root, text="Clear", font=button_font, fg="#ffffff", bg="#e74c3c", 
                         activebackground="#c0392b", activeforeground="#ffffff", command=clear)
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew", ipadx=10, ipady=10)

# Set grid weights to allow button resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
