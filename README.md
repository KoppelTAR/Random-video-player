# Random video player script

## Description
Simple python script that plays a random video from a directory

## Stuff used

Python 3 https://www.python.org/downloads/ (duh)

Tkinter https://docs.python.org/3/library/tkinter.html (For the UI)

## How to run

1. Download the repo.

```powershell
git clone https://github.com/KoppelTAR/Random-video-player.git
```

2. Download tkinter
```powershell
pip install tk
```

4. Create a file named **"data.json"** and add the directory path and what file types you want to randomly access (example json is included if you don't want to create your own).

```
{
    "directory": "/home/user/shows/AlwaysSunny",
    "types": [".mp4",".ts",".mov",".webm"]
}
```

5. Run script.

If done right, this should open a window with 2 buttons. One is for selecting a new directory and the other for playing the video file. Pressing the play video button opens a new video file in the selected directory. Further presses of the play video button close the current file and opens a new one (It may not close the current file on Linux operating systems).  


## Why?

Why make this? Because I wanted to play random video files from a folder, but the only option I found was using VLC which I don't like. Maybe this exact script already exists or a better one then I am a fool for not finding it.
