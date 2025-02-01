import tkinter as tk

# Functions for the calculator operations
def click(button):
    current = display.get()
    if button == "C":
        display.set("")
    elif button == "=":
        try:
            result = eval(current)
            display.set(result)
        except:
            display.set("Error")
    else:
        display.set(current + button)

# Setting up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Variable to hold the user input and result
display = tk.StringVar()

# Display entry field
entry = tk.Entry(root, textvariable=display, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

# Colors and styles for the buttons
button_colors = {
    'C': 'red',
    '=': 'green',
    '/': 'orange',
    '*': 'orange',
    '-': 'orange',
    '+': 'orange'
}

# Default button style
default_color = 'lightgray'
button_font = ("Arial", 18)

# Placing the buttons on the window
row_val = 1
col_val = 0
for button in buttons:
    color = button_colors.get(button, default_color)
    action = lambda x=button: click(x)
    tk.Button(root, text=button, padx=20, pady=20, font=button_font, bg=color, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Running the application
root.mainloop()
