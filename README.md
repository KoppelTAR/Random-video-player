# Random video player script

## Description
Simple python script that plays a random video from a directory

## Stuff used

Python 3 https://www.python.org/downloads/ (duh)

Python Decouple https://pypi.org/project/python-decouple/ (for storing environmental variables such as the video folder directory)

## How to run

1. Download the script.

2. Download Python Decouple using pip.

```powershell
pip install python-decouple
```

3. create file named ".env" and add the directory string (example .env is included if you don't want to create your own).

```
DIRECTORY=D:\AlwaysSunny\
```

4. Run script.

If done right this should open a random file in the selected directory. 
NOTE: this will open any type of file in the directory so keep only files you want to be played in the directory.


## Why?

Why make this? Because I wanted to play random video files from a folder but the only option I found was using vlc which I don't like. Maybe this exact script already exists or a better one then I am a fool for not finding it.
