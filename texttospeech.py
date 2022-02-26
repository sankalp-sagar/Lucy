from gtts import gTTS
import os

def createfilemp3(text):
    language = 'en'
    obj = gTTS(text=text, lang=language, slow=False)
    obj.save("tospeech.mp3")

def playgenmp3():
    os.system("mpg321 tospeech.mp3")
    os.system("clear")

def texttospeech(text):
    createfilemp3(text)
    playgenmp3()
    os.remove("tospeech.mp3")

def playthatsound(sound):
    command = "mpg321 " + str(sound)
    os.system(command)
    os.system("clear")