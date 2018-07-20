import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import subprocess

sh = "adb shell"
fpath = "/data/data/com.android.gles3jni/files"

def list():
    os.system("adb devices")
    os.system("adb root")
#os.system(sh + " ls -l " + fpath)
    text = subprocess.check_output(sh + " ls -l " + fpath, shell=True)
#    print(text)
    return text

win = tk.Tk()
win.title("Blueberry File Manager")

scrolW = 90
scrolH = 20
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, sticky='WE')
files = list()
scr.insert(tk.END, files)
#scr.insert(END, list())

win.mainloop()
