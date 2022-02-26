# importing library
import requests
from bs4 import BeautifulSoup
import texttospeech
 

def showweather(city = "agra"):
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    try:
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        data = str.split('\n')
        sky = data[1]
        info = "The temperature is " + temp + " and the sky is " + sky + " in " + city
        return info
    except AttributeError:
        return None