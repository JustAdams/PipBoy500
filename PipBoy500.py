import PySimpleGUI as sg # ------ GUI 
import time
from Radio import Radio

radio = Radio()

sg.ChangeLookAndFeel('GreenTan')
sg.SetOptions(element_padding=(0, 0))

currTime = time.asctime( time.localtime(time.time()) )
currTemp = 76
currHumidity = 40
currPressure = 80

# ------ Update the time and readings ------
def updateAll():
    currTime = time.asctime( time.localtime(time.time()) )
    window.FindElement('clock').Update(currTime)
    window.FindElement('temperature').Update('Temperature: %d°' %currTemp)
    window.FindElement('humidity').Update('Humidity: %d' %currHumidity)
    window.FindElement('pressure').Update('Atm. Pressure: %d' %currPressure)
    window.FindElement('currSong').Update('Playing: %s' %radio.currSongName)

# ------ Layout Mapping ------
environmentFrame =  [
                        [sg.Text('Temperature: %d°' %currTemp, key='temperature')],
                        [sg.Text('Humidity: %d' %currHumidity, key='humidity')],
                        [sg.Text('Atm. Pressure: %d' %currPressure, key='pressure')]
                    ]

musicFrame =    [
                [sg.Text('Playing: %s' %radio.currSongName, key='currSong')],
                [sg.Text('Play buttons go here')],
                [sg.Button('Radio', button_color=('green', 'pink'), key='radio'), sg.Button('Play', button_color=('green', 'pink'), key='Play'), sg.T(), sg.Button('Stop', button_color=('red', 'white'), key='Stop'), sg.T(), sg.Button('Next', button_color=('green', 'pink'), key='Next')]
]

layout =    [   
                [sg.Text('Username', font=('Arial', 10))],
                [sg.Text(currTime, key='clock', font=('Arial', 15)), sg.T(' ' * 30), sg.Button('Exit', button_color=('white', 'firebrick4'), key='Exit')],
                [sg.T()],
                [sg.Frame('Environment', environmentFrame, font='Arial 12')],
                [sg.Frame('Music', musicFrame, font='Arial 12')],
            ]

# ------ Window creation
window = sg.Window('PipBoy500', layout, size=(480, 320), no_titlebar=False)

# ------ Program Loop --------
while True:
    # ------- Read and update window -------
    event, values = window.Read(timeout=1000) # ------ Update window every second
    updateAll() # Update readings
    if event is None or event == 'Exit': # ------ Close out of the program
        break
    if event == 'Next':
        radio.changeSong(1)
        event = 'Play'
    if event == 'Play':
        radio.playSong()
    if event == 'Stop':
        radio.stopSong()
    
window.close()