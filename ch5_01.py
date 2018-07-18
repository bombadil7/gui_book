from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

#--------------------------------------------------------------
fig = Figure(figsize=(12, 8), facecolor='white')
#--------------------------------------------------------------
# axis = fig.add_subplot(111)   # 1 row, 1 column, only graph
axis = fig.add_subplot(211)   # 2 rows, 1 column, Top graph
#--------------------------------------------------------------
xValues = [1, 2, 3, 4]

yValues0 = [6, 7.5, 8, 7.5]
yValues1 = [5.5, 6.5, 50, 6]
yValues2 = [6.5, 7, 8, 7]

t0, = axis.plot(xValues, yValues0)
t1, = axis.plot(xValues, yValues1)
t2, = axis.plot(xValues, yValues2)

axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')
axis.set_ylim(5, 8)

# axis.grid()   # default line style
axis.grid(linestyle='-')  

fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third line'), 'upper right')
#--------------------------------------------------------------
axis1 = fig.add_subplot(212)   # 2 rows, 1 column, Top graph
#--------------------------------------------------------------
xValues1 = [1, 2, 3, 4]
yValues1 = [7, 5, 8, 6]
axis1.plot(xValues1, yValues1)
axis1.grid()   # default line style
#--------------------------------------------------------------
def _destroyWindow():
    root.quit()
    root.destroy()
#--------------------------------------------------------------
root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)
#--------------------------------------------------------------
canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#--------------------------------------------------------------
root.update()
root.deiconify()
root.mainloop()
