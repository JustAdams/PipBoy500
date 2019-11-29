import PySimpleGUI as sg # ------ GUI 
import time
from Radio import RadioDevice

radio = RadioDevice()

backgroundColor = '#F0F0F0'
sg.SetOptions(element_padding=(0, 0))
screenSize = (800, 480) # -- Display size
stdFontSize = 30 # -- Standard font size
buttFontSize = 25 # -- Button font size
currTime = time.asctime( time.localtime(time.time()) )
currTemp = 76
currHumidity = 40
currPressure = 80
radioActive = False
envActive = False
mapActive = False
playButton = './ButtonGraphics/play.png'
stopButton = './ButtonGraphics/stop.png'
backButton = './ButtonGraphics/back.png'
nextButton = './ButtonGraphics/next.png'


# ------ Update the time and readings ------
def updateAll():
    currTime = time.asctime( time.localtime(time.time()) )
    window.FindElement('clock').Update(currTime)
    if radioActive:
        radioWindow.FindElement('clock').Update(currTime)
        radioWindow.FindElement('currSong').Update('Playing: %s' %radio.currSongName)
    if envActive:
        environmentWindow.FindElement('clock').Update(currTime)
        environmentWindow.FindElement('temperature').Update('Temperature: %d°' %currTemp)
        environmentWindow.FindElement('humidity').Update('Humidity: %d' %currHumidity)
        environmentWindow.FindElement('pressure').Update('Atm. Pressure: %d' %currPressure)
    if mapActive:
        mapWindow.FindElement('clock').Update(currTime)
    

def getRadioLayout():
    musicFrame =    [
                        [sg.Text('Playing: %s' %radio.currSongName, key='currSong', font=stdFontSize)],
                        [sg.T(' ')],
                        [sg.Button('', image_filename=backButton, button_color=(backgroundColor, backgroundColor), key='Prev'), sg.T(' '),
                        sg.Button('', key='Play', image_filename=playButton, button_color=(backgroundColor, backgroundColor)), sg.T(' '), sg.Button('', image_filename=stopButton, button_color=(backgroundColor, backgroundColor), key='Stop'), sg.T(' '), sg.Button('', image_filename=nextButton, button_color=(backgroundColor, backgroundColor), key='Next')],
                        [sg.T(' ')]
                    ]
    radioLayout =   [
                    [sg.Text('Username', font=('Arial', stdFontSize))],
                    [sg.Text(currTime, key='clock', font=('Arial', stdFontSize)), sg.T(' ' * 30),sg.Button('Return', button_color=('white', 'firebrick4'), key='Return')],
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
                            [sg.Text('Username', font=('Arial', stdFontSize))],
                            [sg.Text(currTime, key='clock', font=('Arial', stdFontSize)), sg.T(' ' * 30), sg.Button('Return', button_color=('white', 'firebrick4'), key='Return')],
                            [sg.Frame('Environment', environmentFrame)],
                        ]
    return environmentLayout

def getMapLayout():
    mapLayout = [
                    [sg.Text('Map Window')],
                    [sg.Text('Username', font=('Arial', stdFontSize))],
                    [sg.Text(currTime, key='clock', font=('Arial', stdFontSize)), sg.T(' ' * 30), sg.Button('Return', button_color=('white', 'firebrick4'), key='Return')],
                ]
    return mapLayout

# ------ Layout Mapping ------

layout =    [   
                [sg.Text('Username', font=('Arial', stdFontSize))],
                [sg.Text(currTime, key='clock', font=('Arial', buttFontSize))],
            ]

for i in range(0, 12):
    layout += [ [sg.T()], ]

layout +=   [
                [sg.Button('Environment', button_color=('white', 'blue'), font=('Arial', buttFontSize), key='Environment'), sg.T(' ' * 5), sg.Button('Radio', button_color=('white', 'blue'), font=('Arial', buttFontSize), key='Radio'), sg.T(' ' * 5), sg.Button('Map', button_color=('white', 'blue'), font=('Arial', buttFontSize), key='Map'), sg.T(' ' * 50), sg.Button('Exit', button_color=('white', 'firebrick4'), font=('Arial', buttFontSize), key='Exit')],
            ]

# ------ Window creation
window = sg.Window('PipBoy500', layout, size=screenSize, no_titlebar=True)

# ------ Program Loop --------
while True:
    # ------- Read and update window -------
    event, values = window.Read(timeout=1000) # ------ Update window every second
    updateAll() # Update readings
    if event is None or event == 'Exit': # ------ Close out of the program
        radio.playShutdown()
        time.sleep(1)
        break

    if event is not '__TIMEOUT__':
        radio.playButtonNoise()
    
    # ------ Environment Window Stuff ------
    if event == 'Environment' and not envActive:
        envActive = True
        environmentLayout = getEnvironmentLayout()
        environmentWindow = sg.Window('Environment', environmentLayout, size=screenSize, no_titlebar=True)
        while envActive:
            envEvent, envValues = environmentWindow.Read(timeout=1000)
            updateAll()
            if envEvent is not '__TIMEOUT__':
                radio.playButtonNoise()
            if envEvent is None or envEvent == 'Return':
                environmentWindow.Hide()
                envActive = False
                break

    # ------ Radio Window Stuff ------
    if event == 'Radio' and not radioActive:
        radioActive = True
        radioLayout = getRadioLayout()
        radioWindow = sg.Window('Radio', radioLayout, size=screenSize, no_titlebar=True)
        while radioActive:
            radEvent, radValues = radioWindow.Read(timeout=1000)
            updateAll()
            if radEvent is not '__TIMEOUT__':
                if radEvent == 'Prev':
                    radio.changeSong(-1)
                    radio.playSong()
                if radEvent == 'Play':
                    radio.playSong()
                if radEvent == 'Next':
                    radio.changeSong(1)
                    radio.playSong()
                if radEvent == 'Stop':
                    radio.stopSong()
                if radEvent is None or radEvent == 'Return':
                    radioWindow.Hide()
                    radioActive = False
                    break
                radio.playClickNoise()
                

    # ------ Map Window Stuff ------
    if event == 'Map' and not mapActive:
        mapActive = True
        mapLayout = getMapLayout()
        mapWindow = sg.Window('Map', mapLayout, size=screenSize, no_titlebar=True)
        while mapActive:
            mapEvent, mapValues = mapWindow.Read(timeout=500)
            updateAll()
            if mapEvent is not '__TIMEOUT__':
                radio.playButtonNoise()
            if mapEvent is None or mapEvent == 'Return':
                mapWindow.Hide()
                mapActive = False
                break

window.close()