import os
from pathlib import Path
import shutil

os.chdir(r"C:\Users\herme\Desktop")
if not os.path.exists("Oyunlar"):
    os.mkdir("Oyunlar")

uygulama = (".lnk")

def is_uygulama(file):
    return os.path.splitext(file)[1] in uygulama

for file in os.listdir():
    full_path = os.path.join(os.getcwd(), file)
    if os.path.isfile(full_path) and is_uygulama(file):
        shutil.move(file, r"C:\Users\herme\Desktop\Oyunlar")