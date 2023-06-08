# Random video player script

## Description
Simple python script that plays a random video from a directory

## Stuff used

Python 3 https://www.python.org/downloads/ (duh)

Python Decouple https://pypi.org/project/python-decouple/ (For storing environmental variables such as the video folder directory)

Tkinter https://docs.python.org/3/library/tkinter.html (For the UI)

## How to run

1. Download the repo.

```powershell
git clone https://github.com/KoppelTAR/Random-video-player.git
```

2. Download required packages using pip.

```powershell
pip install -r requirments.txt
```

3. Download tkinter manually (I am too dumb to figure out how to put tkinter in requirments.txt)
```powershell
pip install tk
```

4. Create a file named **".env"** and add the directory path and what file types you want to randomly access (example .env is included if you don't want to create your own).

```
DIRECTORY=D:\AlwaysSunny\
FILETYPES=[".mp4",".ts",".mov"]
```

5. Run script.

If done right, this should open a window with a button that on press opens a new file in the selected directory. Further presses of the button close the current file and opens a new one (It may not close the current file on Linux operating systems).  
NOTE: this will open any type of file in the directory so keep only the files you want to be played in the directory.


## Why?

Why make this? Because I wanted to play random video files from a folder, but the only option I found was using VLC which I don't like. Maybe this exact script already exists or a better one then I am a fool for not finding it.
