import PySimpleGUI as sg
import qrcode
import os

def generate_qr_code(link):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    file_name = "qr_code" + ".png"
    path = os.path.join(os.getcwd(), file_name)
    img.save(path)
    return path

sg.theme('Black')

layout = [
    [sg.Image(key='-IMAGE-', size=(300, 300))],
    [sg.Text('Enter a valid URL to generate the QR code')],
    [sg.In(size=(25, 1), key='-URL-')],
    [sg.Column([[sg.Button('Generate QR Code', )]], justification='center')] # sg.Column demands a layout as argument
]

window = sg.Window('QR Code Generator', layout=layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Generate QR Code':
        url = values['-URL-']
        qr_code_image_path = generate_qr_code(url)
        window['-IMAGE-'].update(filename=qr_code_image_path)
window.close()