import os, random, json
import webbrowser
import tkinter as tk
from tkinter import filedialog
basedir = ()

def getPath():
    global basedir
    filename = filedialog.askdirectory()
    basedir = filename
    print(basedir)


def playVideo():
    global basedir
    f = open('data.json')
    data = json.load(f)
    print(basedir)
    if basedir == ():
        basedir = data["directory"]
    file = random.choice([x for x in os.listdir(basedir) 
    if os.path.isfile(os.path.join(basedir, x))])
    for type in data["types"]:
        if file.endswith(type):
            webbrowser.open(os.path.join(basedir, file))
            break

r = tk.Tk()
r.title('Random video player')
button1 = tk.Button(r, text='Path', width=25, command=getPath)
button2 = tk.Button(r, text='New video', width=25, command=playVideo)
button1.pack()
button2.pack()
r.mainloop()
