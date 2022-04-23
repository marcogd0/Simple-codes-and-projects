import PySimpleGUI as sg

# Creating the layout
layout = [
    [sg.Text('User')],
    [sg.Input(key='user')],
    [sg.Text('Password')],
    [sg.Input(key='password')],
    [sg.Button('login')],
    [sg.Text('', key='message')],
]

# Passing the layout to the window
window = sg.Window('Login', layout=layout)

# Logic applied to the window
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        valid_password = '123456'
        valid_user = 'marcogd0'
        user = values['user']
        password = values['password']
        if password == valid_password and user == valid_user:
            window['message'].update('Successful login')
        else: window['message'].update('Invalid user or password')