from guizero import App, MenuBar


def import_csv():
    print("import csv button pressed")


def export_to_html():
    print("export to HTML pressed ")


app = App(title="WorkshopScheduler")
menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [["Import CSV ", import_csv()], ["export to HTML",export_to_html() ]]
                  ])
app.display()
