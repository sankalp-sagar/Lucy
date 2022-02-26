import speech_recognition as sr
import os
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

def listen():
    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        #listens for the user's input
        os.system("clear")
        print("Say")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            print("You said :", text)
            return text
      
        #error occurs when google could not understand what was said
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
      
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

say = listen()