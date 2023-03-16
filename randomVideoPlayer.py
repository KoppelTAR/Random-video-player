import os, random
import webbrowser
from decouple import config
basedir = config('DIRECTORY')

file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])

webbrowser.open(os.path.join(basedir, file))