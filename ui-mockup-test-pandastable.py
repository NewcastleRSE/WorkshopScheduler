from guizero import App, MenuBar, Text, TextBox
import tkinter as tk
from pandastable import Table


def import_csv():
    print("import csv button pressed")


def export_to_html():
    print("export to HTML pressed ")


app = App(title="WorkshopScheduler", layout="grid")
menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [["Import CSV ", import_csv], ["export to HTML", export_to_html]]
                  ])
start_time_label = Text(app, text="start time:", grid=[0, 0])

start_time_input_box = TextBox(app, grid=[2, 0])
f = tk.Frame()
pt = Table(f)
pt.show()

app.display()
