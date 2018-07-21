import tkinter as tk
from tkinter import ttk
import os
#import sys
import subprocess
from time import sleep
from threading import Thread

from GUI_tooltip import ToolTip as tt


class WinClass():
    def __init__(self):
        self.win = tk.Tk()
        self.c2h_path = '/dev/xdma0_c2h_0'
        self.h2c_path = '/dev/xdma0_h2c_0'
        self.user_path = '/dev/xdma0_user'
        self.control_path = '/dev/xdma0_control'
        devices = [
                    self.c2h_path,
                    self.h2c_path,
                    self.user_path,
                    self.control_path,
                  ]
        
        self.reboots_cnt = 0
        self.c2h_error_cnt = 0
        self.h2c_error_cnt = 0
        self.user_error_cnt = 0
        self.control_error_cnt = 0

        self.expected_permission = '-rw'

#        tt.create_ToolTip(self.win, "Checking xdma file permission over multple reboots.")
        self.win.title("XDMA Device Permissions Check")
        self.create_widgets()
        t = Thread(

    def create_widgets(self):
        self.labels_frame = ttk.LabelFrame(self.win, text='Devices')
        self.errors_frame = ttk.LabelFrame(self.win, text='Permission Errors')
        self.button = ttk.Button(self.win, text="Exit", command=self.win.quit)

        self.labels_frame.grid(column=0, row=0, padx=10, pady=10)
        self.errors_frame.grid(column=1, row=0, padx=10, pady=10)
        self.button.grid(column=0, row=1, columnspan=2, sticky='WE', padx=10, pady=10)

        self.reboots_label = ttk.Label(self.labels_frame, text="NUMBER OF REBOOTS")
        self.c2h_label = ttk.Label(self.labels_frame, text="XDMA_C2H ERRORS")
        self.h2c_label = ttk.Label(self.labels_frame, text="XDMA_H2C ERRORS")
        self.user_label = ttk.Label(self.labels_frame, text="XDMA_USER ERRORS")
        self.control_label = ttk.Label(self.labels_frame, text="XDMA_CONTROL ERRORS")

        self.reboots_label.pack(padx=8, pady=4, anchor='w')        
        self.c2h_label.pack(padx=8, pady=4, anchor='w')        
        self.h2c_label.pack(padx=8, pady=4, anchor='w')
        self.user_label.pack(padx=8, pady=4, anchor='w')
        self.control_label.pack(padx=8, pady=4, anchor='w')

        self.reboots_field = ttk.Entry(self.errors_frame, textvariable=self.reboots_cnt)
        self.c2h_errors = ttk.Entry(self.errors_frame, textvariable=self.c2h_error_cnt)
        self.h2c_errors = ttk.Entry(self.errors_frame, textvariable=self.h2c_error_cnt)
        self.user_errors = ttk.Entry(self.errors_frame, textvariable=self.user_error_cnt)
        self.control_errors = ttk.Entry(self.errors_frame, textvariable=self.control_error_cnt)

        self.reboots_field.pack(padx=8, pady=4)        
        self.c2h_errors.pack(padx=8, pady=4)        
        self.h2c_errors.pack(padx=8, pady=4)
        self.user_errors.pack(padx=8, pady=4)
        self.control_errors.pack(padx=8, pady=4)

    def reboot_loop(self):
        while True:
            self.update_counts()
            # reboot
            time.sleep(120)

    def update_counts(self):
        for device in devices:
            device.errors += 1 if check_device(device.name) == False
            device.text['text'] = str(device.errors)


    def check_device(self, dev):
        f = subprocess.check_output('adb shell ls -l ' + dev, shell=True)
        perm = f.split()[0].decode('utf-8')
        return perm[1:3] == 'rw' and perm[4:6] == 'rw'



            


if __name__ == '__main__':
    main_window = WinClass()
    main_window.win.mainloop()
