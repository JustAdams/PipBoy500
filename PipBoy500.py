import PySimpleGUI as sg
import time

sg.ChangeLookAndFeel('GreenTan')
sg.SetOptions(element_padding=(0, 0))

currTime = time.asctime( time.localtime(time.time()) )


layout =    [   
                [sg.Text('Welcome User', font=('Arial', 15)) , sg.T(' ' * 15), sg.Text(currTime, key='clock', font=('Arial', 15))],
            ]

layout += [[sg.T('')] for i in range(1, 11)]
layout +=   [
                [sg.T(' ' * 95), sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]
            ]

window = sg.Window('PipBoy500', layout, size=(480, 320), no_titlebar=True)


# ------ Program Loop --------
while True:
    # ------- Read and update window -------
    event, values = window.Read(timeout=1000)
    if event is None or event == 'Exit':
        break
    # ------- Update clock -------
    currTime = time.asctime( time.localtime(time.time()) )
    window.FindElement('clock').Update(currTime)


window.close()