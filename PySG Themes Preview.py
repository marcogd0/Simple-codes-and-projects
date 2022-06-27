import PySimpleGUI as sg

sg.theme("Dark Brown")

layout = [
    [sg.Text("Theme Preview")],
    [sg.Text("Click a theme to see a demo of it")],
    [sg.Listbox(values=sg.theme_list(), size=(20, 12), key="-LIST-", enable_events=True)],
    [sg.Button("Exit")]
]

window = sg.Window("Theme Previewer", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    sg.theme(values["-LIST-"][0])
    sg.popup_get_text("This is " + values["-LIST-"][0])