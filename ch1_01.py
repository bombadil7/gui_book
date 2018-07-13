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

# Add Combobox
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
#numberChosen = ttk.Combobox(win, width=12, textvariable=number)
# To prevent user from typing their own number in the field add 'state' prop:
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()  # Default state is checked
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect() # Default state is unchecked
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select() # Default state is checked
check3.grid(column=2, row=4, sticky=tk.W)


# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.configure(state='disabled')  # Disable the Button Widget
# Position Buttion in second row
action.grid(column=2, row=1)
nameEntered.focus()

win.mainloop()
