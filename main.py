from guizero import App , MenuBar
def import_csv():
    print("import csv button pressed")

app = App(title="WorkshopScheduler")
menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [["Import csv ",import_csv()]]
                  ])
app.display()