from os import path
import os

def clickphoto():
    f = open("Photos/photoexists.txt", "r+")
    datapic = f.read()
    i = int(datapic) + 1
    f.seek(0)
    f.truncate()
    f.write(str(i))
    f.close()
    picname = "capture_" + str(i)
    piccommand = "raspistill -o Photos/" + str(picname)
    os.system(piccommand)

def makevideo(seconds = 30000):
    f = open("Videos/videoexists.txt", "r+")
    datavid = f.read()
    i = int(datavid) + 1
    f.seek(0)
    f.truncate()
    f.write(str(i))
    f.close()
    vidname = "vid_" + str(i)
    vidcommand = "raspivid -o Videos/" + str(vidname) +".h264 -t " + str(seconds)
    os.system(vidcommand)