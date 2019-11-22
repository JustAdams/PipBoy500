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
radioActive = False
envActive = False


# ------ Update the time and readings ------
def updateAll():
    currTime = time.asctime( time.localtime(time.time()) )
    window.FindElement('clock').Update(currTime)
def radioUpdateAll():
    currTime = time.asctime( time.localtime(time.time()) )
    radioWindow.FindElement('clock').Update(currTime)
    radioWindow.FindElement('currSong').Update('Playing: %s' %radio.currSongName)

def environmentUpdate():
    currTime = time.asctime( time.localtime(time.time()) )
    environmentWindow.FindElement('clock').Update(currTime)
    environmentWindow.FindElement('temperature').Update('Temperature: %d°' %currTemp)
    environmentWindow.FindElement('humidity').Update('Humidity: %d' %currHumidity)
    environmentWindow.FindElement('pressure').Update('Atm. Pressure: %d' %currPressure)

    

def getRadioLayout():
    musicFrame =    [
                    [sg.Text('Playing: %s' %radio.currSongName, key='currSong')],
                    [sg.T()],
                    [sg.T()],
                    [sg.Button('Radio', button_color=('green', 'pink'), key='Radio'), sg.Button('Play', button_color=('green', 'pink'), key='Play'), sg.T(), sg.Button('Stop', button_color=('red', 'white'), key='Stop'), sg.T(), sg.Button('Next', button_color=('green', 'pink'), key='Next')]
                ]
    radioLayout =   [
                    [sg.Text('Username', font=('Arial', 10))],
                    [sg.Text(currTime, key='clock', font=('Arial', 15)), sg.T(' ' * 30), sg.Button('Return', button_color=('white', 'firebrick4'), key='Return')],
                    [sg.T()],
                    [sg.Frame('Radio', musicFrame)],
                ]
    return radioLayout

def getEnvironmentLayout():
    environmentFrame =  [
                            [sg.Text('Temperature: %d°' %currTemp, key='temperature')],
                            [sg.Text('Humidity: %d' %currHumidity, key='humidity')],
                            [sg.Text('Atm. Pressure: %d' %currPressure, key='pressure')]
                        ]
    environmentLayout = [
                            [sg.Text('Username', font=('Arial', 10))],
                            [sg.Text(currTime, key='clock', font=('Arial', 15)), sg.T(' ' * 30), sg.Button('Return', button_color=('white', 'firebrick4'), key='Return')],
                            [sg.T()],
                            [sg.Frame('Environment', environmentFrame)],
                        ]
    return environmentLayout

# ------ Layout Mapping ------

layout =    [   
                [sg.Text('Username', font=('Arial', 10))],
                [sg.Text(currTime, key='clock', font=('Arial', 15))],
                [sg.T()],
                [sg.Button('Environment', button_color=('white', 'blue'), key='Environment')],
                [sg.T()],
                [sg.Button('Radio', button_color=('white', 'blue'), key='Radio')],
            ]
for i in range(0, 3):
    layout += [ [sg.T()], ]

layout +=   [
                [sg.T(' ' * 90), sg.Button('Exit', button_color=('white', 'firebrick4'), key='Exit')],
            ]

# ------ Window creation
window = sg.Window('PipBoy500', layout, size=(480, 320), no_titlebar=True)

# ------ Program Loop --------
while True:
    # ------- Read and update window -------
    event, values = window.Read(timeout=1000) # ------ Update window every second
    updateAll() # Update readings
    if event is None or event == 'Exit': # ------ Close out of the program
        break
    
    # ------ Environment Window Stuff ------
    if event == 'Environment' and not envActive:
        envActive = True
        environmentLayout = getEnvironmentLayout()
        environmentWindow = sg.Window('Environment', environmentLayout, size=(480, 320), no_titlebar=True)
        while envActive:
            envEvent, envValues = environmentWindow.Read(timeout=1000)
            environmentUpdate()
            if envEvent is None or envEvent == 'Return':
                environmentWindow.Hide()
                envActive = False
                break

    # ------ Radio Window Stuff ------
    if event == 'Radio' and not radioActive:
        radioActive = True
        radioLayout = getRadioLayout()
        radioWindow = sg.Window('Radio', radioLayout, size=(480, 320), no_titlebar=True)
        while radioActive:
            radEvent, radValues = radioWindow.Read(timeout=1000)
            radioUpdateAll()
            if radEvent == 'Next':
                radio.changeSong(1)
                radEvent = 'Play'
            if radEvent == 'Play':
                radio.playSong()
            if radEvent == 'Stop':
                radio.stopSong()
            if radEvent is None or radEvent == 'Return':
                radioWindow.Hide()
                radioActive = False
                break

window.close()