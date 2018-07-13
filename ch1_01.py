import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

#win.resizable(0, 0)     # Disable resizing
# Adding a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)


def clickMe():
    action.configure(text="Hello " + name.get())

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.bind("<Return>", (lambda event: clickMe()))
nameEntered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
# Position Buttion in second row
action.grid(column=1, row=1)
nameEntered.focus()

win.mainloop()
