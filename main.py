from cgitb import text
import os
from time import sleep
import pyautogui
import webbrowser
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import news
import camera
import texttospeech
import weather
import urllib
import jokes
import subprocess
import gui
import google_search
options = Options()
options.add_argument('start-maximized')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import speech_recognition as sr
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def listen():

    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        #listens for the user's input
        os.system("clear")
        print("Say")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
      
        #error occurs when google could not understand what was said
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "Nothing"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            os.system("mpg321 sounds/nointernet.mp3")
            sleep(80)
            return "Nothing"

class Youtube:

    def __init__(self, var, video):
        if var == True:
            self.browser = webdriver.Chrome(chrome_options=options)
            wait = WebDriverWait(self.browser, 2)
            presence = EC.presence_of_element_located
            visible = EC.visibility_of_element_located
            self.browser.get('https://www.youtube.com/results?search_query={}'.format(str(video)))
            wait.until(visible((By.ID, "video-title")))
            self.browser.find_element_by_id("video-title").click()
            wait.until(visible((By.ID, "player")))
            keyboard = Controller()
            keyboard.press('f')

    def closebrowser(self):
        self.browser.close()

while True:
    say = listen()
    if "Lucy" in say:
        subprocess.Popen("mpg321 sounds/meow.mp3", shell=True)
        gui.showtextgui(text=say, runningtime=3)
        os.system("clear")
        print(say)
        if "YouTube" in say:
            song = say[10:]
            song = song[:-11]
            if say == "Lucy play " + str(song) + " on YouTube":
                br = Youtube(True, song)

        if "Spotify" in say:
            song = say[10:]
            song = song[:-11]
            if say == "Lucy play " + str(song) + " on Spotify":
                spurl = "https://open.spotify.com/search/" + str(song)
                webbrowser.open(spurl, new=0)
                sleep(10)
                pyautogui.moveTo(644, 461)
                sleep(1)
                pyautogui.click()

        if "Lucy what is the meaning of" in say:
            query = say[5:]
            result = google_search.googleanswerbox(query)
            texttospeech.createfilemp3(result)
            subprocess.Popen('./texttospeech.sh', shell=True)
            gui.showtextgui(result)

        if "photo" in say:
            if say == "Lucy click a photo":
                camera.clickphoto()

        if "news" in say:
            if say == "Lucy tell me the news":
                newnews = news.speaknews()
                texttospeech.createfilemp3(newnews)
                subprocess.Popen('./texttospeech.sh', shell=True)
                gui.showtextgui(newnews)

        if "weather" in say:
            city = say[21:]
            if say == "Lucy show weather":
                w = weather.showweather()
                texttospeech.createfilemp3(w)
                subprocess.Popen('./texttospeech.sh', shell=True)
                gui.showtextgui(w)

            if say == "Lucy show weather in " + str(city):
                w = weather.showweather(city)
                if w == None:
                    subprocess.Popen('mpg321 sounds/nocity.mp3', shell = True)
                    gui.showtextgui("Oh beautiful Vartika, that is not a city. Please specify a city only!")
                else:
                    texttospeech.createfilemp3(w)
                    subprocess.Popen('./texttospeech.sh', shell=True)
                    gui.showtextgui(w)

        if "joke" in say:
            if say == "Lucy tell me a joke":
                joke = jokes.getjoke()
                texttospeech.createfilemp3(joke)
                subprocess.Popen('./texttospeech.sh', shell=True)
                gui.showtextgui(joke)

        if "Lucy find the lyrics of" in say:
            partlyrics = say[24:]
            if say == "Lucy find the lyrics of " + str(partlyrics):
                google_search.searchlyrics(partlyrics)

        if "Lucy answer" in say:
            question = say[12:]
            if say == "Lucy answer " + str(question):
                answer = google_search.googleanswerbox(question)
                texttospeech.createfilemp3(answer)
                subprocess.Popen('./texttospeech.sh', shell=True)
                gui.showtextgui(answer)

        if "near me" in say:
            if "Lucy find" in say:
                place = say[10:]
                place = place[:-8]
                if say == "Lucy find " + str(place) + " near me":
                    near = google_search.nearme(place)
                    print(near)
                    texttospeech.texttospeech(near)

        if "video" in say:
            if say == "Lucy capture video":
                camera.makevideo()
            seconds = say[-7:]
            if seconds == "seconds":
                num = say[23:]
                num = num[:-8]
                if say == "Lucy capture video for " + str(num) + " seconds":
                    camera.makevideo(int(num)*1000)
            

        if say == "Lucy close YouTube":
            br.closebrowser()

        if say == "Lucy close music":
            os.system("pkill chromium")
    else:
        print(".")
        os.system("clear")