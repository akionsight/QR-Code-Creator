import pyqrcode
import PySimpleGUI as sg 
import random

def Text():
    layout2 = [ [sg.Text('Enter text in QR code')],
                [sg.Input()],
                [sg.OK()]]
    window = sg.Window("text based qr").Layout(layout2)
    while True:
            event, values = window.read()
            if event in (None, 'OK'):	# if user closes window or clicks ok
                qr = pyqrcode.create(values[0])
                qr.png(f'{random.randint(100000,999999)} text.png', scale=8)
                sg.popup(f'the qr code is created with file name:- {random.randint(100000,999999)} text.png')
                break


def Info():
    layout3 = [ [sg.Text('Enter the following info')],
                    [sg.Text('Name:- ')],[sg.Input()],
                    [sg.Text('Organisation:- ')], [sg.Input()],
                    [sg.Text('Email:- ')], [sg.Input()],
                    [sg.Text('Phone no. :- ')], [sg.Input()],
                    [sg.Text("Address:- ")], [sg.Input()],
                    [sg.Text('website URL:- ')], [sg.Input()],
                    [sg.OK()]]
    window = sg.Window('Info QR').Layout(layout3)
    while True:
        event, values = window.read()
        if event in (None, 'OK'):	# if user closes window or clicks cancel
            qr = pyqrcode.create(f'''name:- {values[0]}
                                     Organistion:- {values[1]}
                                     Email:- {values[2]}
                                     Phone no.:- {values[3]}
                                     Address:- {values[4]}
                                     website:- {values[5]}''')

            qr.png(f'{random.randint(100000,999999)} info.png', scale=8)
            sg.popup(f'QR code created with file name :- {random.randint(100000,999999)} info.png')
            break


def option_selection():
    layout = [ [sg.Text("Select option")],
                [sg.Radio('Text/Address/URL', "QR"), sg.Radio('Info', 'QR')],
                [sg.OK()] ]

    window = sg.Window("QR code Generator").Layout(layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'OK'):	# if user closes window or clicks cancel
            break


    if values[0] == True:
        Text()
    if values[0] == False:
        Info()
option_selection()