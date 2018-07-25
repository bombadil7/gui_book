'''
May 2017
@author: Burkhard A. Meier
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import  sleep         # careful - this can freeze the GUI
from tkinter import filedialog as fd
from os import path
from os import makedirs
from server import *

from threading import Thread
from time import sleep
from queue import Queue
from tkinter import messagebox as mBox

import ToolTip as tt
import Queues as bq
import URL as url

from os import getcwd

GLOBAL_CONST = 42
fDir = path.dirname(path.abspath(__file__))
netDir = fDir + '\\Backup'
print("fDir: " + str(fDir))
print("netDir: " + netDir)
#print("path.basename: " + path.basename(__file__))
#print("getcwd: " + getcwd())
#print("dirname: " + path.dirname(path.abspath(__file__)))
#print("abspath: " + path.abspath(__file__))
if not path.exists(netDir):
    makedirs(netDir, exist_ok = True)

#=================================================================== 
class OOP():
    def __init__(self):         # Initializer method
        # Create instance
        self.win = tk.Tk()   
        
        tt.create_ToolTip(self.win, 'Hello GUI')

        # Start TCP/IP server in its own thread
        svrT = Thread(target=startServer, daemon=True)
        svrT.start()
        
        # Add a title       
        self.win.title("Python GUI")      
        self.create_widgets()
        self.defaultFileEntries()
        self.guiQueue = Queue()

    def defaultFileEntries(self):
        self.fileEntry.delete(0, tk.END)
        self.fileEntry.insert(0, fDir)
        if len(fDir) > self.entryLen:
            self.fileEntry.config(width=len(fDir) + 3)
            # Readonly would make it impossible to change to the actual file we
            # want to copy
 #           self.fileEntry.config(state='readonly')

        self.netwEntry.delete(0, tk.END)
        self.netwEntry.insert(0, netDir)
        if len(netDir) > self.entryLen:
            self.netwEntry.config(width=len(netDir) + 3)

    def useQueues(self):
        self.guiQueue = Queue()
        for idx in range(10):
            self.guiQueue.put('Message from a queue' + str(idx))

        while True:
            print(self.guiQueue.get())

    def methodInAThread(self, numOfLoops=10):
        for idx in range(numOfLoops):
            sleep(1)
            self.scr.insert(tk.INSERT, str(idx) + '\n')
        sleep(1)
        print('methodInAThread():', self.runT.isAlive())

        # textBoxes are the Consumers of Queue data
        writeT = Thread(target=self.useQueues, daemon=True)
        writeT.start()


    # Running methods in Threads
    def createThread(self, num):
        self.runT = Thread(target=self.methodInAThread, args=[num])
        self.runT.setDaemon(True)
        self.runT.start()
        print(self.runT)
        print('createThread():', self.runT.isAlive())

        # textBoxes are the consumers of queue data
        writeT = Thread(target=self.useQueues, daemon=True)
        writeT.start()

    # Create Queue instance
    def useQueues(self):
        print(self.guiQueue)
        while True:
            print(self.guiQueue.get())

    # Modified Button Click Function
    def click_me(self): 
        # Passing in the current class instance (self)
        bq.writeToScrol(self)
        sleep(2)
        htmlData = url.getHtml()
        print(htmlData)
        self.scr.insert(tk.INSERT, htmlData)

    # Spinbox callback 
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')
        
    # GUI Callback  
    def checkCallback(self, *ignored_args):
        # only enable one checkbutton
        if self.chVarUn.get(): self.check3.configure(state='disabled')
        else:                  self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disabled')
        else:                  self.check2.configure(state='normal') 
        
    # Radiobutton Callback
    def radCall(self):
        radSel = self.radVar.get()
        if   radSel == 0: self.mighty2.configure(text='Blue')
        elif radSel == 1: self.mighty2.configure(text='Gold')
        elif radSel == 2: self.mighty2.configure(text='Red')          
        
    # update progressbar in callback loop
    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i   # increment progressbar
            self.progress_bar.update()       # have to call update() in loop
        self.progress_bar["value"] = 0       # reset/clear progressbar  
    
    def start_progressbar(self):
        self.progress_bar.start()
        
    def stop_progressbar(self):
        self.progress_bar.stop()
     
    def progressbar_stop_after(self, wait_ms=1000):    
        self.win.after(wait_ms, self.progress_bar.stop)        

    def usingGlobal(self):
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)
                    
    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit() 
                  
    #####################################################################################       
    def create_widgets(self):    
        tabControl = ttk.Notebook(self.win)          # Create Tab Control
        
        tab1 = ttk.Frame(tabControl)            # Create a tab 
        tabControl.add(tab1, text='Tab 1')      # Add the tab
        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Tab 2')      # Make second tab visible
        
        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        
        # LabelFrame using tab1 as the parent
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        
        # Modify adding a Label using mighty as the parent instead of win
        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')
    
    
        # Adding a Textbox Entry widget
        self.name = tk.StringVar()
        name_entered = ttk.Entry(mighty, width=24, textvariable=self.name)
        name_entered.grid(column=0, row=1, sticky='W')               
        
        # Adding a Button
        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)   
        self.action.grid(column=2, row=1)                                
        
        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=14, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)
        
             
        # Adding a Spinbox widget
        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin) # using range
        self.spin.grid(column=0, row=2, sticky='W')
        
        # Using a scrolled Text control    
        scrol_w  = 40
        scrol_h  = 10 
        self.scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)                    
        
        
        # Tab Control 2 ----------------------------------------------------------------------
        # We are creating a container frame to hold all other widgets -- Tab2
        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)
        
        # Creating three checkbuttons
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)                   
        
        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.mighty2, text="UnChecked", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=0, sticky=tk.W)                   
        
        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.mighty2, text="Enabled", variable=chVarEn)
        check3.deselect()
        check3.grid(column=2, row=0, sticky=tk.W)                     
        
        # trace the state of the two checkbuttons
        chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())    
        chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())   
        
        
        # First, we change our Radiobutton global variables into a list
        colors = ["Blue", "Gold", "Red"]   
        
        # create three Radiobuttons using one variable
        self.radVar = tk.IntVar()
        
        # Next we are selecting a non-existing index value for radVar
        self.radVar.set(99)                                 
         
        # Now we are creating all three Radiobutton widgets within one loop
        for col in range(3):                             
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar, 
                                    value=col, command=self.radCall)          
            curRad.grid(column=col, row=1, sticky=tk.W)             # row=6
                
        # Add a Progressbar to Tab 2
        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)         
             
        # Create a container to hold buttons
        buttons_frame = ttk.LabelFrame(self.mighty2, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)        
        
        # Add Buttons for Progressbar commands
        ttk.Button(buttons_frame, text=" Run Progressbar   ", command=self.run_progressbar).grid(column=0, row=0, sticky='W')  
        ttk.Button(buttons_frame, text=" Start Progressbar  ", command=self.start_progressbar).grid(column=0, row=1, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop immediately ", command=self.stop_progressbar).grid(column=0, row=2, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop after second ", command=self.progressbar_stop_after).grid(column=0, row=3, sticky='W')  
         
        for child in buttons_frame.winfo_children():  
            child.grid_configure(padx=2, pady=2) 
         
        for child in self.mighty2.winfo_children():  
            child.grid_configure(padx=8, pady=2) 
            
        # Creating a Menu Bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        
        # Add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

############################################################################
        # Create Manage Files Frame
        mngFilesFrame = ttk.LabelFrame(tab2, text=' Manage Files: ')
        mngFilesFrame.grid(column=0, row=1, sticky='WE', padx=10, pady=5)

        # Button Callback
        def getFileName():
            print('hello from getFileName')
#            fDir = path.dirname(__file__)
            fName = fd.askopenfilename(parent=self.win, initialdir=fDir)
            print("fName: " + fName)
            self.fileEntry.delete(0, tk.END)
            self.fileEntry.insert(0, fName)
            self.fileEntry.config(width=len(fName) + 3)
#            self.fileEntry.config(state='readonly')

        # Add Widgets to Manage Files Frame
        lb = ttk.Button(mngFilesFrame, text="Browse to File...",
                command=getFileName)
        lb.grid(column=0, row=0, sticky=tk.W)

        file = tk.StringVar()
        self.entryLen = scrol_w
        self.fileEntry = ttk.Entry(mngFilesFrame, width=self.entryLen,
                textvariable=file)
        self.fileEntry.bind("<Return>", (lambda event: copyFile()))
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)

        logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(mngFilesFrame, width=self.entryLen,
                textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W)

        def copyFile():
            import shutil
            src = self.fileEntry.get()
            if len(src.split('/')) > 2:
                file = src.split('/')[-1]
            else:
                file = src.split("\\")[-1]

            dst = self.netwEntry.get() + '\\' + file
            try:
                shutil.copy(src, dst)
                mBox.showinfo('Copy File to Network', 
                        'Success: File copied')
            except FileNotFoundError as err:
                mBox.showerror('Copy File to Network',
                        '*** Failed to copy file! ***\n\n' + str(err))
            except Exception as err:
                mBox.showerror('Copy File to Network',
                        '*** Failed to copy file! ***\n\n' + str(err))

        cb = ttk.Button(mngFilesFrame, text="Copy File To :  ",
                command=copyFile)
        cb.grid(column=0, row=1, sticky=tk.E)

        # Add some space around each label
        for child in mngFilesFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)

###########################################################################

        # Display a Message Box
        def _msgBox():
            msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2017.')  
            
        # Add another Menu to the Menu Bar and an item
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        # Change the main windows icon
#       self.win.iconbitmap('pyc.ico')
        
        # It is not necessary to create a tk.StringVar() 
        # strData = tk.StringVar()
        strData = self.spin.get()
        print("Spinbox value: " + strData)
        
        # call function
        self.usingGlobal()
        
#name_entered.focus()     
        tabControl.select(1)
         
#======================
# Start GUI
#======================
oop = OOP()

oop.win.mainloop()
