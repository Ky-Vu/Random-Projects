import math, tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

#Set window and title
win = tk.Tk()
win.title('Calculator')

#Create UI frame
frame = tk.Frame(win, bg="skyblue", padx=10)
frame.pack()

entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

#Define each button corresponds to its icon value
def click(num):
    entry.insert(tk.END, num)

# For "DEL" button
def backspace():
    current = entry.get()
    if current: #not empty
        entry.delete(len(current) - 1, tk.END)

# For +/- button
def toggle_sign():
    expr = entry.get()
    if expr.startswith('-'):
        entry.delete(0)
    else:
        entry.insert(0, '-')

def equal():
    try:
        expr = entry.get().replace('^', '**') # interpret ^ as power
        # Restrict eval to math functions and constants only
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        res = str(eval(expr, {"__builtins__": None}, allowed_names))
        entry.delete(0, tk.END)
        entry.insert(0, res)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

#Clear entries
def clear():
    entry.delete(0, tk.END)

#Set buttons
buttons = [
    # Field for formula goes here                                                                   # DEL button goes here#
    ('sqrt', 'sqrt(', 1, 0),('(', '(', 1, 1),       (')', ')', 1, 2), ('n!', 'factorial(', 1, 3),   ('/', '/', 1, 4),
    ('^', '^', 2, 0),       ('7', '7', 2, 1),       ('8', '8', 2, 2), ('9', '9', 2, 3),             ('*', '*', 2, 4),
    ('10^', '10**', 3, 0),  ('4', '4', 3, 1),       ('5', '5', 3, 2), ('6', '6', 3, 3),             ('-', '-', 3, 4),
    ('log', 'log10(', 4, 0),('1', '1', 4, 1),       ('2', '2', 4, 2), ('3', '3', 4, 3),             ('+', '+', 4, 4),
    ('ln', 'log(', 5, 0),   ('+/-', '+/-', 5, 1),   ('0', '0', 5, 2), ('.', '.', 5, 3),             # Equal sign goes here#
]

for display, value, r, c in buttons:
    if value == '+/-':
        tk.Button(frame, text=display, padx=15, pady=5, width=3,
        command=toggle_sign()).grid(row=r, column=c, pady=2)
    else:
        tk.Button(frame, text=display, padx=15, pady=5, width=3,
        command=lambda v=value: click(v)).grid(row=r, column=c, pady=2)

# Backspace delete button
tk.Button(frame, text="Del", padx=10, pady=5, width=4, command=backspace).grid(row=0, column=4, columnspan=1, pady=2)
# Clear field button
tk.Button(frame, text="Clear", padx=10, pady=5, width=4, command=clear).grid(row=5, column=2, columnspan=1, pady=2)
# Execute/calculate formula button
tk.Button(frame, text="=", padx=10, pady=5, width=4, command=equal).grid(row=5, column=4, columnspan=1, pady=2)
