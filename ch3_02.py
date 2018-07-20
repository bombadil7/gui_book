from tkinter import messagebox as mBox
from tkinter import Tk

root = Tk()
root.withdraw() # Remove the debug window
mBox.showinfo('This is a Title', 'A Python GUI created using tkinter:\nThis year is 2018')

