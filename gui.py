import tkinter as tk
from tkinter import PhotoImage, Label
import tkinter.font as TkFont

#limitwords = 60
#limitlines = 17

def createlinedtext(text):
    count = 0
    lines = 0
    plustime = 0
    formattedoutput = ""
    for i in text:
        count += 1
        formattedoutput += i
        if i == "\n":
            plustime += int(count/60)*3
            count = 0
        if i == " ":
            if count > 60:
                count = 0
                formattedoutput += "\n"
                plustime += 5
                lines += 1
                if lines == 17:
                    formattedoutput += "............"
                    break
    return formattedoutput, plustime

def showtextgui(text, runningtime = 5, bg = "background.png", fontchosen = "Helvetica", fontsize = 20):
    t = createlinedtext(text)
    runningtime += t[1]
    root = tk.Tk()
    root.after(runningtime*1000, lambda: root.destroy())
    root.wm_attributes('-fullscreen', True)
    filename = PhotoImage(file = bg)
    fonttext = TkFont.Font(family=fontchosen,size=fontsize, slant="italic")
    background_label = Label(root, text=t[0], font = fonttext, image=filename, compound='center')
    background_label.place(x=0, y=0, relheight=1, relwidth=1)
    root.mainloop()
