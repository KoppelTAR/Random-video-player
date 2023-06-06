# Random video player script

## Description
Simple python script that plays a random video from a directory

## Stuff used

Python 3 https://www.python.org/downloads/ (duh)

Python Decouple https://pypi.org/project/python-decouple/ (For storing environmental variables such as the video folder directory)

Tkinter https://docs.python.org/3/library/tkinter.html (For the UI)

## How to run

1. Download the script.

2. Download required packages using pip.

```powershell
pip install -r requirments.txt
```

3. Download tkinter manually (I am too dumb to figure out how to put tkinter in requirments.txt)
```powershell
pip install tk
```

4. Create file named ".env" and add the directory string (example .env is included if you don't want to create your own).

```
DIRECTORY=D:\AlwaysSunny\
```

5. Run script.

If done right this should open a random file in the selected directory. 
NOTE: this will open any type of file in the directory so keep only files you want to be played in the directory.


## Why?

Why make this? Because I wanted to play random video files from a folder but the only option I found was using vlc which I don't like. Maybe this exact script already exists or a better one then I am a fool for not finding it.
