import webbrowser
import search
from bs4 import BeautifulSoup
import requests
import re
import texttospeech

def googleanswerbox(phrase):
    url = "https://www.google.com/search?q=" + str(phrase)
    h = {"User-Agent":"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36"}
    r = requests.get(url, headers=h)
    soup = BeautifulSoup(r.text, 'lxml')
    answerbox = soup.find(class_ = "hgKElc")
    try:
        return answerbox.text
    except AttributeError:
        try:
            answerbox = soup.find(class_ = "kno-rdesc")
            return answerbox.text
        except AttributeError:
            try:
                answerbox = soup.find(class_ = "iAIpCb PZPZlf")
                return answerbox.text
            except AttributeError:
                try:
                    answerbox = soup.find(class_ = "UdvAnf") #distance
                    return answerbox.text
                except AttributeError:
                    try:
                        answerbox = soup.find(class_ = "LTKOO sY7ric")
                        return answerbox.text
                    except AttributeError:
                        try:
                            answerbox = soup.find(class_ = "VwiC3b MUxGbd yDYNvb")
                            return answerbox.text
                        except AttributeError:
                            try:
                                answerbox = soup.find(class_ = "VwiC3b MUxGbd yDYNvb lEBKkf")
                                return answerbox.text
                            except AttributeError:
                                try:
                                    answerbox = soup.find(class_ = "TrT0Xe")
                                    return answerbox.text
                                except AttributeError:
                                    return "I'm so sorry. Beautiful Vartika. I can't display result to that yet. But don't worry. Report it to Sankalp and he will fix it. Meanwhile you can punish me. I am a bad cat."

def nearme(phrase):
    url = "https://www.google.com/search?q=" + str(phrase) + str(" near me")
    h = {"User-Agent":"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36"}
    r = requests.get(url, headers=h)
    soup = BeautifulSoup(r.text, 'lxml')
    answer = soup.find(class_ = "aGQIYb")
    search.searchweb(phrase + str(" near me"))
    try:
        return answer.text
    except AttributeError:
        try:
            answer = soup.find(class_ = "hNKF2b m9orme")
            return answer.text
        except AttributeError:
            return "I'm so sorry. Beautiful Vartika. I can't display result to that yet. But don't worry. Report it to Sankalp and he will fix it. Meanwhile you can punish me. I am a bad cat."


def searchlyrics(phrase):
    url = "https://www.google.com/search?q=" + str(phrase) + str(" lyrics genius.com")
    h = {"User-Agent":"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36"}
    r = requests.get(url, headers=h)
    soup = BeautifulSoup(r.text, 'lxml')
    for link in soup.find_all('a', href = re.compile("^https://genius")):
        lyricslink = link['href']
        break
    try:
        webbrowser.open(lyricslink, new=0)
        texttospeech.texttospeech("Here are your lyrics. Pretty Vartika")
    except UnboundLocalError:
        texttospeech.texttospeech("I'm so sorry. Beautiful Vartika. I can't display result to that yet. But don't worry. Report it to Sankalp and he will fix it. Meanwhile you can punish me. I am a bad cat.")