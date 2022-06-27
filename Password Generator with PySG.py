import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        sg.theme("DarkBlack1")
        layout = [
            [sg.Text("Number of characters"), sg.Combo(values=list(range(31)), key="-TOTAL_CHARS-", default_value=1, size=(3, 1))],
            [sg.Output(size=(32,5))],
            [sg.Button("Generate Password")]
        ]

        self.window = sg.Window("Password Generator", layout=layout)
    
    def generatePassword(self, values):
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!@#$%^&*().'
        combined_chars = lower + upper + numbers + symbols
        password = ''.join(random.sample(combined_chars, k=int(values['-TOTAL_CHARS-'])))
        return password

    def Start(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Generate Password":
                new_password = self.generatePassword(values)
                print(new_password)
                self.savePassword(new_password, values)

    def savePassword(self, new_password, values):
        with open(r"Generated Passwords\passwords.txt", 'a') as file:
            file.write(f"Password: {new_password}\n")

generator = PassGen()
generator.Start()