import webbrowser

def searchweb(word):
    url = "https://www.google.com/search?q=" + str(word)
    webbrowser.open(url, new=0)