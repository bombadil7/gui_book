import tkinter as tk
from tkinter import ttk
import os
#import sys
import subprocess
from time import sleep
from threading import Thread

from GUI_tooltip import ToolTip as tt


class Device():
    def __init__(self, _name='', _path='', _entry=''):
       self.name = _name
       self.path = _path
       self.errors = 0
       self.entry = _entry


class WinClass():
    def __init__(self):
        self.win = tk.Tk()

        self.expected_permission = '-rw'
        self.iterations = 0

#        tt.create_ToolTip(self.win, "Checking xdma file permission over multple reboots.")
        self.win.title("XDMA Device Permissions Check")
        self.create_widgets()
        self.devices = [Device('c2h', '/dev/xdma0_c2h_0', self.c2h_errors), 
                        Device('h2c', '/dev/xdma0_h2c_0', self.h2c_errors), 
                        Device('user', '/dev/xdma0_user', self.user_errors), 
                        Device('control', '/dev/xdma0_control', self.control_errors)]
        

    def create_widgets(self):
        self.labels_frame = ttk.LabelFrame(self.win, text='Devices')
        self.errors_frame = ttk.LabelFrame(self.win, text='Permission Errors')
#self.button = ttk.Button(self.win, text="Exit", command=self.win.quit)
        self.button_exit = ttk.Button(self.win, text="Exit", command=self._destroyWindow)
        self.button_start = ttk.Button(self.win, text="Start Loop", command=self.start_loop)

        self.labels_frame.grid(column=0, row=0, padx=10, pady=10)
        self.errors_frame.grid(column=1, row=0, padx=10, pady=10)
        self.button_exit.grid(column=1, row=1, sticky='WE', padx=10, pady=10)
        self.button_start.grid(column=0, row=1, sticky='WE', padx=10, pady=10)

        self.reboots_label = ttk.Label(self.labels_frame, text="NUMBER OF REBOOTS")
        self.c2h_label = ttk.Label(self.labels_frame, text="XDMA_C2H ERRORS")
        self.h2c_label = ttk.Label(self.labels_frame, text="XDMA_H2C ERRORS")
        self.user_label = ttk.Label(self.labels_frame, text="XDMA_USER ERRORS")
        self.control_label = ttk.Label(self.labels_frame, text="XDMA_CONTROL ERRORS")

        self.reboots_label.pack(padx=8, pady=5, anchor='w')        
        self.c2h_label.pack(padx=8, pady=5, anchor='w')        
        self.h2c_label.pack(padx=8, pady=5, anchor='w')
        self.user_label.pack(padx=8, pady=5, anchor='w')
        self.control_label.pack(padx=8, pady=5, anchor='w')

        self.reboots_field = ttk.Label(self.errors_frame, text=str(self.iterations))
#        self.c2h_errors = ttk.Label(self.errors_frame, text=str(self.devices[0].errors))
#        self.h2c_errors = ttk.Label(self.errors_frame, text=str(self.devices[1].errors))
#        self.user_errors = ttk.Label(self.errors_frame, text=str(self.devices[2].errors))
#        self.control_errors = ttk.Label(self.errors_frame, text=str(self.devices[3].errors))
        self.c2h_errors = ttk.Entry(self.errors_frame)
        self.h2c_errors = ttk.Entry(self.errors_frame)
        self.user_errors = ttk.Entry(self.errors_frame)
        self.control_errors = ttk.Entry(self.errors_frame)

        self.reboots_field.pack(padx=8, pady=4)        
        self.c2h_errors.pack(padx=8, pady=4)        
        self.h2c_errors.pack(padx=8, pady=4)
        self.user_errors.pack(padx=8, pady=4)
        self.control_errors.pack(padx=8, pady=4)

    def start_loop(self):
        self.t = Thread(target=self.reboot_loop, daemon=True)    # daemon to ensure graceful shut-down
        self.t.start() 

    def reboot_loop(self):
        while True:
            self.update_counts()
            self.iterations +=1 
            self.reboots_field['text'] = self.iterations 
            os.system("adb root")
            print(subprocess.check_output('adb shell id', shell=True))
#os.system("adb root")
#os.system("adb shell reboot")
#sleep(120)
            sleep(10)

    def update_counts(self):
        for device in self.devices:
            if self.check_device(device.path) == False:
                device.errors += 1 
            print(device.name + ' '+ str(device.errors))
            device.entry.delete(0)
            device.entry.insert(0, str(device.errors))

    def check_device(self, devpath):
        f = subprocess.check_output('adb shell ls -l ' + devpath, shell=True)
        perm = f.split()[0].decode('utf-8')
        print(perm)
        return perm[1:3] == 'rw' and perm[4:6] == 'rw'

    def _destroyWindow(self):
#os.system("adb root")
#os.system("adb shell reboot -p")
        self.win.quit()
        self.win.destroy()

if __name__ == '__main__':
    main_window = WinClass()
    main_window.win.mainloop()
