from pygame import mixer # ------ Music player
import glob

# makes a list of music files
musicList = glob.glob('./Music/*.mp3')

class Radio:

    def __init__(self):
        mixer.init()
        self.songIndex = 0
        self.numSongs = len(musicList)
        mixer.music.load(musicList[self.songIndex])
        self.playing = False
        self.currSongName = musicList[self.songIndex].replace('./Music/', '').replace('.mp3', '')

    def playSong(self):
        mixer.music.play()
        self.currSongName = musicList[self.songIndex].replace('./Music/', '').replace('.mp3', '')
        self.playing = True

    def changeSong(self, num):
        # Reset to first song if end is reached
        if self.songIndex == self.numSongs - 1:
            self.songIndex = 0
        else:
            self.songIndex += num
        mixer.music.load(musicList[self.songIndex])

    def stopSong(self):
        mixer.music.stop()
        self.playing = False
        self.currSongName = ''