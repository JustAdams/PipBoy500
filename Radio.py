from pygame import mixer # ------ Music player
import glob

# makes a list of music files
musicList = glob.glob('./Music/*.mp3')

class RadioDevice:

    def __init__(self):
        mixer.pre_init(22050, -16, 2, 1024)
        mixer.init()
        self.songIndex = 0
        self.numSongs = len(musicList)
        mixer.music.load(musicList[self.songIndex])
        self.playing = False
        self.currSongName = musicList[self.songIndex].replace('./Music/', '').replace('.mp3', '')
        self.shutdownNoise = mixer.Sound('./SFX/shutdown.wav')
        self.buttonNoise = mixer.Sound('./SFX/beep.wav')
        self.clickNoise = mixer.Sound('./SFX/click.wav')

    def playSong(self):
        mixer.music.play()
        self.currSongName = musicList[self.songIndex].replace('./Music/', '').replace('.mp3', '')
        self.playing = True

    def changeSong(self, num):
        self.songIndex += num
        # Reset to first song if end is reached
        if self.songIndex == self.numSongs:
            self.songIndex = 0
        elif self.songIndex == -1:
            self.songIndex = self.numSongs - 1
        mixer.music.load(musicList[self.songIndex])

    def stopSong(self):
        mixer.music.stop()
        self.playing = False
        self.currSongName = ''

    def playShutdown(self):
        self.shutdownNoise.play()

    def playButtonNoise(self):
        self.buttonNoise.play()
    
    def playClickNoise(self):
        self.clickNoise.play()