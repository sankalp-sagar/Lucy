import webbrowser
import requests

def playyoutube(video):
    url = "https://www.youtube.com/results?q=" + str(video)
    count = 0
    r = requests.get(url)
    data = r.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            break
    x = lst[count - 5]
    if x == "/results/":
        return "No Video found"

    else:
        vurl = "https://www.youtube.com/" + str(x)
        webbrowser.open(vurl, new = 0)
        return "video opened"