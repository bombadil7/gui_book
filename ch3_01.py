import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"


win = tk.Tk()
win.title("Python GUI")
# r escapes backslashes, so we don't have to type C:\\
win.iconbitmap(r'C:\Users\akniazev\AppData\Local\Programs\Python\Python36\DLLs\pyc.ico')

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both")

monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text='Enter a name:').grid(column=0, row=0, sticky='W')


monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)

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
check1 = tk.Checkbutton(monty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()  # Default state is checked
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty2, text="UnChecked", variable=chVarUn)
check2.deselect() # Default state is unchecked
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty2, text="Enabled", variable=chVarEn)
check3.select() # Default state is checked
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]

# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if   radSel == 0: monty2.configure(text='Blue')
    elif radSel == 1: monty2.configure(text='Gold')
    elif radSel == 2: monty2.configure(text='Red')

# Create three Radiobuttons using one variable
radVar = tk.IntVar()

# Now we select a non-existing index value for radVar
radVar.set(99)
# Now we create all three Radiobutton widgets within one loop
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2, text=colors[col], variable=radVar, 
            value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

#spin = tk.Spinbox(monty, from_=0, to=10, width=5, bd=8, command=_spin)
spin = tk.Spinbox(monty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=_spin)
spin.grid(column=0, row=2)

# Add second spinbox
spin = tk.Spinbox(monty, values=(0, 50, 100), width=5, bd=8, relief=tk.RIDGE, command=_spin)
spin.grid(column=1, row=2)
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
labelsFrame = ttk.LabelFrame(monty2, text=' Labels in a Frame ')
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

def _msgBox():
#    mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\n\
#            The year is 2018.')
#    mBox.showwarning('Python Message Info Box', 'A Python GUI created using tkinter:\n\
#            Warning: There might be a bug in this code.')
#    mBox.showerror('Python Message Info Box', 'A Python GUI created using tkinter:\n\
#            Error: Houston ~ we DO have a serious PROBLEM!')
    answer = mBox.askyesno("Python Message Dual Choice Box", 
            "Are you sure you really wish to do this?")
    print(answer)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

win.mainloop()
