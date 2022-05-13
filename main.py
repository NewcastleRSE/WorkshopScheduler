# imports
from tkinter import colorchooser
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfilename

from pandastable import *


# Functions called when buttons are pressed
# file menu functions
def new_schedule():
    pt.importCSV("schedule-template/csv/Template-schedule-blank.csv")
    pt.redraw()


def import_csv():
    filetypes = (
        ('csv files', '*.csv'),
    )
    filename = fd.askopenfilename(
        title="choose csv file",
        initialdir='/',
        filetypes=filetypes)
    pt.importCSV(filename)
    config_break_colour(default=True)
    pt.redraw()
    print(pt.model.df)


def export_to_html():
    print("export to HTML pressed ")
    filetypes = [('html Files', '*.html')]
    file = asksaveasfilename(filetypes=filetypes,
                             defaultextension=filetypes,
                             initialdir='/',
                             initialfile="Workshop-schedule.html")

    print(file)
    pt.model.df.to_html(buf=file, index=False)


def export_to_csv():
    print("export to csv pressed ")
    filetypes = [('csv Files', '*.csv')]
    file = asksaveasfilename(filetypes=filetypes,
                             defaultextension=filetypes,
                             initialdir='/',
                             initialfile="Workshop-schedule.csv")

    print(file)
    pt.model.df.to_csv(path_or_buf=file, index=False)


# edit menu

def move_row_up():
    selectedrow = pt.model.df.iloc[pt.getSelectedRow()]
    rowabove = pt.model.df.iloc[pt.getSelectedRow() - 1]
    if selectedrow - 1 == -1:
        pt.addRows(1)
        pt.redraw()
    print("up", selectedrow, selectedrow - 1)
    print(pt.model.index)
    pt.redraw()


def move_row_down():
    selectedrow = pt.model.df.iloc[pt.getSelectedRow()]
    rowbelow = pt.model.df.iloc[pt.getSelectedRow() + 1]
    temp = selectedrow.copy()
    selectedrow = rowbelow
    rowbelow = temp
    print(pt.model.df)
    pt.redraw()


# options meny

def config_break_colour(default=False):
    if not default:
        color_code = colorchooser.askcolor(title="Choose color")
        print(color_code)
    else:
        color_code = ((0, 249, 0), '#00f900')
        print(color_code)

    df = pt.model.df
    breakrows = df.index[df['Episode'] == "Break"].tolist()
    for row in breakrows:
        pt.setRowColors(rows=row, clr=color_code[1], cols='all')
        pt.redraw()


# Root of application
root = Tk()
# MenubarDeclaration
menubar = Menu(root)

# File menu Section declaration
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Schedule", command=new_schedule)
filemenu.add_command(label="Import a CSV file", command=import_csv)
filemenu.add_command(label="Export to CSV file", command=export_to_csv)
filemenu.add_command(label="Export to HTML file", command=export_to_html)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=1)
editmenu.add_command(label="move row up", command=move_row_up)
editmenu.add_command(label="move row down", command=move_row_down)
menubar.add_cascade(label="Edit", menu=editmenu)

optionsmenu = Menu(menubar, tearoff=2)
optionsmenu.add_command(label="Configure colour for break entries", command=config_break_colour)
menubar.add_cascade(label="Options", menu=optionsmenu)

# StartTime Label and input field
start_time_label = Label(root, text="start time:", justify=LEFT)
start_time_label.grid(row=1, column=1)
start_time_input_box = Entry(root, justify=LEFT, width=5)
start_time_input_box.grid(row=1, column=2, sticky=W)

# Frame
frame = Frame(root)
frame.grid(row=3, column=2, sticky=W)
# pandastable Initialisation
pt = Table(frame)
# Import CSV template file
pt.importCSV("schedule-template/csv/Template-schedule-blank.csv")
config_break_colour(default=True)
# show table
pt.show()
#
root.config(menu=menubar)
# add window bar title
root.title("WorkshopScheduler")

root.mainloop()
