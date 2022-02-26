import requests

jurl = "https://icanhazdadjoke.com/"

def getjoke():
    try:
        r = requests.get(jurl, headers={"Accept": 'application/json'}).json()
        return r['joke']
    except requests.exceptions.ConnectionError:
        return "There is a problem fetching the joke"
