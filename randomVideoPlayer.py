import os, random
import webbrowser
import tkinter as tk
from decouple import config
basedir = config('DIRECTORY')
fileTypes = config('FILETYPES')


def play_video():
    file = random.choice([x for x in os.listdir(basedir) 
    if os.path.isfile(os.path.join(basedir, x))])
    for type in fileTypes:
        if file.endswith(type):
            webbrowser.open(os.path.join(basedir, file))
            break

r = tk.Tk()
r.title('Random video player')
button = tk.Button(r, text='New video', width=25, command=play_video)
button.pack()
r.mainloop()
