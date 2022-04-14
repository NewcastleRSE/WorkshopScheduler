# imports
from pandastable import *


# Functions called when buttons are pressed
def import_csv():
    print("import csv button pressed")


def export_to_html():
    print("export to HTML pressed ")


def export_to_csv():
    print("export to csv pressed ")


# Root of application
root = Tk()
# MenubarDeclaration
menubar = Menu(root)

# File menu Section declaration
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Import a CSV file", command=import_csv)
filemenu.add_command(label="Export to CSV file", command=export_to_csv)
filemenu.add_command(label="Export to HTML file", command=export_to_html)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# StartTime Label and input field
start_time_label = Label(root, text="start time:", justify=LEFT).pack()
start_time_input_box = Entry(root).pack()

# Frame
frame = Frame(root)
frame.pack(fill=BOTH, expand=1)
# pandastable
pt = Table(frame)
# Import CSV template file
pt.importCSV("schedule-template/Template-schedule.csv")
pt.show()

root.config(menu=menubar)
root.mainloop()
