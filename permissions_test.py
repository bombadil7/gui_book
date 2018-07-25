import tkinter as tk
from tkinter import ttk
import os
#import sys
import subprocess
from time import sleep
from threading import Thread

#from GUI_tooltip import ToolTip as tt


class Device():
    def __init__(self, _name='', _path='', _entry='', _permissions=''):
       self.name = _name
       self.path = _path
       self.errors = 0
       self.entry = _entry
       self.permissions = _permissions 


class WinClass():
    def __init__(self):
        self.win = tk.Tk()

        self.expected_permission = '-rw'
        self.iterations = 0

#        tt.create_ToolTip(self.win, "Checking xdma file permission over multple reboots.")
        self.win.title("XDMA Device Permissions Check")
        self.create_widgets()
        self.devices = [Device('c2h', '/dev/xdma0_c2h_0', self.c2h_errors, self.c2h_perm_val), 
                        Device('h2c', '/dev/xdma0_h2c_0', self.h2c_errors, self.h2c_perm_val), 
                        Device('user', '/dev/xdma0_user', self.user_errors, self.user_perm_val), 
                        Device('control', '/dev/xdma0_control', self.control_errors, self.control_perm_val)]
        

    def create_widgets(self):
        self.labels_frame = ttk.LabelFrame(self.win, text='Devices')
        self.errors_frame = ttk.LabelFrame(self.win, text='Test Statistics')
        self.permissions_frame = ttk.LabelFrame(self.win, text='Device Permissions')
        self.progress_frame = ttk.LabelFrame(self.win, text='Reboot Progress')
        self.button_exit = ttk.Button(self.win, text="Exit", command=self._destroyWindow)
        self.button_start = ttk.Button(self.win, text="Start Loop", command=self.start_loop)
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient='horizontal', length=170, mode='determinate')
        self.progress_label = ttk.Label(self.progress_frame, text='Reboot Progress', width=22)

        self.labels_frame.grid(column=0, row=0, padx=10, pady=6)
        self.errors_frame.grid(column=1, row=0, padx=10, pady=6)
        self.button_exit.grid(column=1, row=3, sticky='WE', padx=10, pady=10)
        self.button_start.grid(column=0, row=3, sticky='WE', padx=10, pady=10)
        self.permissions_frame.grid(column=0, row=2, columnspan=2, sticky='WE', padx=10, pady=4)
        self.progress_frame.grid(column=0, row=1, columnspan=2, sticky='WE', padx=10, pady=4)
        self.progress_bar.grid(column=1, row=0, sticky='WE', padx=10, pady=6)
        self.progress_label.grid(column=0, row=0, sticky='W', padx=10, pady=6)

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
        self.c2h_errors = ttk.Entry(self.errors_frame)
        self.h2c_errors = ttk.Entry(self.errors_frame)
        self.user_errors = ttk.Entry(self.errors_frame)
        self.control_errors = ttk.Entry(self.errors_frame)

        self.reboots_field.pack(padx=8, pady=4)        
        self.c2h_errors.pack(padx=8, pady=4)        
        self.h2c_errors.pack(padx=8, pady=4)
        self.user_errors.pack(padx=8, pady=4)
        self.control_errors.pack(padx=8, pady=4)

        ttk.Label(self.permissions_frame, text="C2H").grid(column=0, row=0, padx=10, pady=10)
        ttk.Label(self.permissions_frame, text="H2C").grid(column=0, row=1, padx=10, pady=10)
        ttk.Label(self.permissions_frame, text="USER").grid(column=2, row=0, padx=10, pady=10, sticky='W')
        ttk.Label(self.permissions_frame, text="CONTROL").grid(column=2, row=1, padx=10, pady=10, sticky='W')
        self.c2h_perm_val = ttk.Label(self.permissions_frame, text="-")
        self.h2c_perm_val = ttk.Label(self.permissions_frame, text="-")
        self.user_perm_val = ttk.Label(self.permissions_frame, text="-")
        self.control_perm_val = ttk.Label(self.permissions_frame, text="-")

        self.c2h_perm_val.grid(column=1, row=0, sticky='W', padx=10, pady=4)
        self.h2c_perm_val.grid(column=1, row=1, sticky='W', padx=10, pady=4)
        self.user_perm_val.grid(column=3, row=0, sticky='W', padx=10, pady=4)
        self.control_perm_val.grid(column=3, row=1, sticky='W', padx=10, pady=4)
        

    def start_loop(self):
        self.t = Thread(target=self.reboot_loop, daemon=True)    # daemon to ensure graceful shut-down
        self.t.start() 

    def reboot_loop(self):
        while True:
            try:
                self.update_counts()
                self.iterations +=1 
                self.reboots_field['text'] = str(self.iterations)
                os.system("adb root")
                os.system("adb shell reboot")
                self.run_progressbar()
            except subprocess.CalledProcessError:
                print("Got subprocess.CalledProcessError.")
                print("Chances are that uSOM is not connected.  Let's check:")
                os.system("adb devices")
                print("Will try to reboot")
                sleep(60)
                os.system("adb root")
                os.system("adb shell reboot")
                sleep(120)
            except:
                print("Got some other error.  Rebooting.")

    def update_counts(self):
        for device in self.devices:
            if self.check_device(device) == False:
                device.errors += 1 
            device.entry.delete(0)
            device.entry.insert(0, str(device.errors))

    def check_device(self, dev):
        f = subprocess.check_output('adb shell ls -l ' + dev.path, shell=True)
        perm = f.split()[0].decode('utf-8')
        dev.permissions['text'] = perm
        return perm[1:3] == 'rw' and perm[4:6] == 'rw'

    def _destroyWindow(self):
#os.system("adb root")
#os.system("adb shell reboot -p")
        self.win.quit()
        self.win.destroy()

    def run_progressbar(self):
        self.progress_bar["maximum"] = 2400
        self.progress_bar["value"] = 0
        self.progress_label['text'] = 'uSOM Booting Up'
        for i in range(2401):
            sleep(0.05)
            self.progress_bar["value"] = i
            self.progress_bar.update()
#if i == 2200:
        self.progress_label['text'] = 'Checking Permissions'

if __name__ == '__main__':
    main_window = WinClass()
    main_window.win.mainloop()
