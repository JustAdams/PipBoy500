import PySimpleGUI as sg # ------ GUI 
import time
from SoundClass import RadioDevice

radio = RadioDevice()

theme = 'Reds'
backgroundColor = '#F0F0F0'
sg.change_look_and_feel(theme)
sg.SetOptions(element_padding=(0, 0))
screenSize = (800, 480) # -- Display size
stdFont = ('Tlwg Mono', 20) # -- Standard font size
buttFont = ('Tlwg Mono', 20) # -- Button font size
currTime = time.asctime( time.localtime(time.time()) )
currTemp = 76
currHumidity = 40
currPressure = 80
loggedIn = False
username = '                           '
radioActive = False
envActive = False
mapActive = False
users = {'335577': 'Justin', '112233': 'Megan', '998877': 'Brian'}
playButton = './ButtonGraphics/play.png'
stopButton = './ButtonGraphics/stop.png'
backButton = './ButtonGraphics/back.png'
nextButton = './ButtonGraphics/next.png'
exitButton = './ButtonGraphics/exit.png'
weatherMan = './Graphics/weather.png'
mapArea = './Graphics/fxbg.png'

# ------ Update the time and readings ------
def updateAll():
    currTime = time.asctime( time.localtime(time.time()) )
    window.FindElement('clock').Update(currTime)
    window.FindElement('username').Update(username)
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
    radioLayout =   [
                        [sg.Text(currTime, key='clock', font=stdFont), sg.T(' ' * 60), sg.Button('Return', font=buttFont, key='Return')],
                        [sg.T()],
                        [sg.T()],
                        [sg.T()],
                        [sg.Text('Playing: %s' %radio.currSongName, key='currSong',  font=stdFont)],
                    ]
    for i in range (0, 5):
        radioLayout += [ [sg.T()], ]
    radioLayout +=  [
                        [sg.T(' ' * 30), sg.Button('', image_filename=backButton, button_color=('white', sg.LOOK_AND_FEEL_TABLE[theme]['BACKGROUND']), border_width=0, key='Prev'), sg.T(' '),
                        sg.Button('', button_color=('white', sg.LOOK_AND_FEEL_TABLE[theme]['BACKGROUND']), border_width=0,  key='Play', image_filename=playButton), sg.T(' '), sg.Button('', button_color=('white', sg.LOOK_AND_FEEL_TABLE[theme]['BACKGROUND']), border_width=0, image_filename=stopButton,   key='Stop'), sg.T(' '), sg.Button('', button_color=('white', sg.LOOK_AND_FEEL_TABLE[theme]['BACKGROUND']), border_width=0,  image_filename=nextButton,   key='Next')],
                        [sg.T()],
                        [sg.T()],
                        [sg.T()],
                        [sg.T(' ' * 150), sg.T('Kobold Technologies', font=('Tlwg Mono', 10))]
                    ]
    return radioLayout

def getEnvironmentLayout():

    environmentLayout = [
                            [sg.Text(currTime, key='clock', font=stdFont), sg.T(' ' * 60), sg.Button('Return', font=buttFont, key='Return')],
                            [sg.T()],
                            [sg.Text('Environmental Scan', font=stdFont)],
                            [sg.T()],
                            [sg.T()],
                            [sg.Text('Temperature: %d°' %currTemp, key='temperature', font=stdFont)],
                            [sg.T()],
                            [sg.Text('Humidity: %d' %currHumidity, key='humidity',  font=stdFont), sg.T(' ' * 10)],
                            [sg.T()],
                            [sg.Text('Atm. Pressure: %d' %currPressure, key='pressure',  font=stdFont)],
                            [sg.T()],
                            [sg.Text('Results: %sRESULTS VARIABLE HERE')],
                        ]
    for i in range(0, 3):
        environmentLayout += [ [sg.T()], ]
    environmentLayout +=[
                            [sg.T(' ' * 150), sg.T('Kobold Technologies', font=('Tlwg Mono', 10))]
                        ]
    return environmentLayout

def getMapLayout():
    mapLayout = [
                    [sg.Text(currTime, key='clock', font=stdFont), sg.T(' ' * 60), sg.Button('Return', font=buttFont, key='Return')],
                    [sg.Image(mapArea)],
                    [sg.T(' ' * 150), sg.T('Kobold Technologies', font=('Tlwg Mono', 10))]
                ]
    return mapLayout

def getKeypadLayout():
    keypadFrame =  [    
                        [sg.T()],
                        [sg.T(' ' * 4), sg.Text('Enter Passcode', font=('Tlwg', 10))],
                        [sg.T(' ' * 5), sg.Input(size=(25, 1), justification='right', key='input')],
                        [sg.T()],
                        [sg.T(' ' * 10), sg.Button('1', font=stdFont), sg.Button('2', font=stdFont), sg.Button('3', font=stdFont)],
                        [sg.T(' ' * 10), sg.Button('4', font=stdFont), sg.Button('5', font=stdFont), sg.Button('6', font=stdFont)],
                        [sg.T(' ' * 10), sg.Button('7', font=stdFont), sg.Button('8', font=stdFont), sg.Button('9', font=stdFont)],
                        [sg.T(' ' * 22), sg.Button('0', font=stdFont)],
                        [sg.T()],
                        [sg.T(' '), sg.Button('Login', font=buttFont), sg.Button('Clear', font=buttFont)],
                        [sg.Text(size=(15, 1), font=('Arial', 20), text_color='white', key='out')]
                    ]

    keypadLayout =  [   
                        [sg.T()],
                        [sg.T(' ' * 65), sg.Frame('Kobold Technologies', keypadFrame, font=('Tlwg Mono', 15 )), sg.T(' ' * 20)]
                    ]
    return keypadLayout

# ------ Layout Mapping ------

layout =    [   
                [sg.Text(username, key='username', font=stdFont)],
                [sg.Text(currTime, key='clock', font=buttFont)],
            ]

for i in range(0, 13):
    layout += [ [sg.T()], ]

layout +=   [
                [sg.Button('Environment', border_width=2, font=buttFont, key='Environment'), sg.T(' ' * 5), sg.Button('Radio', border_width=2,  font=buttFont, key='Radio'), sg.T(' ' * 5), sg.Button('Map', border_width=2,  font=buttFont, key='Map'), sg.T(' ' * 5), sg.Button('Morale', border_width=2, font=buttFont, key='Motivation'), sg.T(' ' * 15), sg.Button('Logout', button_color=('red', 'black'), border_width=2, font=buttFont, key='Logout'), sg.T(' ' * 30)],
                [sg.T(' ' * 150), sg.T('Kobold Technologies', font=('Tlwg Mono', 10))]
            ]

# ------ Window creation
window = sg.Window('PipBoy500', layout, size=screenSize, no_titlebar=True)

# ------ Program Loop --------
while True:
    if not loggedIn:
        keypadLayout = getKeypadLayout()
        keypadWindow = sg.Window('Login', keypadLayout, size=screenSize, no_titlebar=True)
        keys_entered = ''
        while not loggedIn:
            loginEvent, loginValues = keypadWindow.Read(timeout=1000)
            if loginEvent == 'Clear':
                keys_entered = ''
                radio.playClickNoise()
            elif loginEvent in '1234567890':
                keys_entered = loginValues['input']
                keys_entered += loginEvent
                radio.playClickNoise()
            elif loginEvent == 'Login':
                keys_entered = loginValues['input']
                radio.playButtonNoise()
                if users.get(keys_entered) is not None:
                    username = users[keys_entered]
                    print(username + " has logged in")
                    loggedIn = True
                    radio.playSpeech("Welcome " + username)
                    keypadWindow.hide()
                    break
                else:
                    keys_entered = ''
                    keypadWindow['out'].update('invalid login')
            elif loginEvent is None or loginEvent == 'Exit': # ------ Close out of the program
                radio.playShutdown()
                time.sleep(1)
                exit()

            keypadWindow['input'].update(keys_entered)


    # ------- Read and update window -------
    event, values = window.Read(timeout=1000) # ------ Update window every second
    updateAll() # Update readings

    if event is not '__TIMEOUT__':
        radio.playButtonNoise()
    
    # ------ Environment Window Stuff ------
    if event == 'Environment' and not envActive:
        radio.playSpeech('Scanning environment')
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
                    radio.playButtonNoise()
                    radioWindow.Hide()
                    radioActive = False
                    break
                radio.playClickNoise()
                

    # ------ Map Window Stuff ------
    if event == 'Map' and not mapActive:
        radio.playSpeech('loading map')
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

    # ------ Morale Quotes ------
    if event == 'Motivation':
        radio.playMotivation()
        
    # ------ Logout ------
    if event == 'Logout' and loggedIn:
        radio.playSpeech('Goodbye ' + username)
        loggedIn = False

window.close()