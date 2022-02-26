import os
import shutil
import requests
import filecmp
import texttospeech
api_key = "bf6c7131fded47b5976b6cebab94e8b0"

#1
def getnews():
    murl = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api_key
    try:
        shutil.copyfile("News/freshnews.txt", "News/tempnews.txt")
    except FileNotFoundError:
        f = open("News/freshnews.txt", "w")
        f.close()
    news = requests.get(murl).json()
    article = news['articles']
    narticle = []
    for i in article:
        narticle.append(i['title'])

    f = open("News/freshnews.txt", "r+", encoding="utf-8")
    for i in narticle:
        f.write(str(i))
        f.write("\n")
    f.close()
    f1 = "News/freshnews.txt"
    f2 = "News/tempnews.txt"
    res = filecmp.cmp(f1, f2, shallow=False)
    if res == False:
        newnewssoclearold()
        resettrack()
        resettold()
    os.remove("News/tempnews.txt")

def alreadytoldnews(news):
    f = open("News/toldnews.txt", "a", encoding="utf_8")
    f.write(news)
    f.close()

def newnewssoclearold():
    f = open("News/toldnews.txt", "r+", encoding="utf_8")
    f.seek(0)
    f.truncate()
    f.close()

def trackindex(num):
    f = open("News/trackindex.txt", "r+", encoding="utf-8")
    f.write(num)
    f.close()

def resettrack():
    f = open("News/trackindex.txt", "r+", encoding="utf-8")
    f.seek(0)
    f.truncate()
    f.close()

def resettold():
    f = open("News/toldnews.txt", "r+", encoding="utf-8")
    f.seek(0)
    f.truncate()
    f.close()

def readnews():
    f = open("News/freshnews.txt", "r")
    l = f.readlines()
    f.close()
    f = open("News/toldnews.txt", "r")
    told = f.readlines()
    f.close()
    if len(told) == 0:
        alreadytoldnews(l[0])
        trackindex("0")
        return l[0]

    else:
        if len(told) == len(l):
            return "You have read all the news! Please come back later"
        
        else:
            f = open("News/trackindex.txt", "r")
            num = f.read()
            f.close()
            n = int(num) + 1
            alreadytoldnews(l[n])
            trackindex(str(n))
            return l[n]

def speaknews():
    getnews()
    texttospeech.texttospeech("Latest news fetched")
    news = readnews()
    return news