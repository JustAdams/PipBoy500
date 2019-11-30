# PipBoy500

Project to create a PipBoy in the style of the original Fallout games.

Using PySimpleGui and a Raspberry Pi with touchscreen.
Program sounds are handled using PyGame.
Text-to-speech handled using gTTS(Google Text-to-Speech) library.

***NOTE***
Program will not work unless you add at least one (1) mp3 file to the Music folder.
(A music list is made on instantiation requiring at least one file)

```sh
PySimpleGUI
https://pysimplegui.readthedocs.io/en/latest/
PyGame
https://www.pygame.org/
```

Completed:  
	* Radio Player
		Upload any amount of .mp3 files to the Music folder and the program automatically updates its song list on instantiation. Currently can only Play, Stop, and Skip to the next song. Volume is set to the systems volume.

Current Development:  
	* Environment Scanner
		Determine the ambient temparature and other factors
	* Area Map
		Display a map of the surrounding area

Future Development:  
	* Aesthetic improvements to give a more retro-future feel
