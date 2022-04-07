from tkinter import *
from pandastable import Table
def import_csv():
    print("import csv button pressed")


def export_to_html():
    print("export to HTML pressed ")


def export_to_csv():
    print("export to csv pressed ")


root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Import a CSV file", command=import_csv)
filemenu.add_command(label="Export to CSV file", command=export_to_csv)
filemenu.add_command(label="Export to HTML file", command=export_to_html)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

start_time_label = Label(root, text="start time:", justify=LEFT)

start_time_label.pack()

start_time_input_box = Entry(root).pack()

pt = Table(parent=root)
pt.show()

root.config(menu=menubar)
root.mainloop()
