import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0, 0)     # Disable resizing
monty = ttk.LabelFrame(win, text=' Monty Python ')
monty.grid(column=0, row=0)

# Adding a Label
aLabel = ttk.Label(monty, text="A Label")
aLabel.grid(column=0, row=0)


def clickMe():
    action.configure(text="Hello " + name.get())

# Changing our Label
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky=tk.W)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.bind("<Return>", (lambda event: clickMe()))
nameEntered.grid(column=0, row=1, sticky=tk.W)

# Add Combobox
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
#numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
# To prevent user from typing their own number in the field add 'state' prop:
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()  # Default state is checked
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chVarUn)
check2.deselect() # Default state is unchecked
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
check3.select() # Default state is checked
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]

# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if   radSel == 0: monty.configure(background=colors[0])
    elif radSel == 1: monty.configure(background=colors[1])
    elif radSel == 2: monty.configure(background=colors[2])

# Create three Radiobuttons using one variable
radVar = tk.IntVar()

# Now we select a non-existing index value for radVar
radVar.set(99)
# Now we create all three Radiobutton widgets within one loop
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty, text=colors[col], variable=radVar, 
            value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Using a scrolled Text control
scrolW = 30
scrolH = 3

scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, row=5)
#scr.grid(column=0, columnspan=3, row=5, sticky='WE')
# Adding a Button
action = ttk.Button(monty, text="Click Me!", command=clickMe)
action.configure(state='disabled')  # Disable the Button Widget
# Position Buttion in second row
action.grid(column=2, row=1)

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=20, pady=30)

# Place labels into the container element
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0, sticky='W')
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1, sticky='W')
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2, sticky='W')

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)
nameEntered.focus()

def _quit():
    win.quit()
    win.destroy()
    exit()

menuBar = Menu(win)
win.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

monty.mainloop()
