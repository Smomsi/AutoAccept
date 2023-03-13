import pyautogui
import time
from threading import Thread
import psutil
from PIL import Image
import requests
from io import BytesIO

response = requests.get("https://i.ibb.co/VxPb70F/acceptbuttonlol.png")
try:
    img = Image.open(BytesIO(response.content))
except:
    print("Failed to load image")
    exit()

pyautogui.FAILSAFE=False

def autoaccept():
    print("Searching for League of Legends...")
    time.sleep(1)
    print("Started the programm! Close League or the Console to close the AutoAccept.")
    while "LeagueClientUxRender.exe" in (i.name() for i in psutil.process_iter()):
        time.sleep(1)
        r=None 
        r=pyautogui.locateOnScreen(img, grayscale=False)
        if(r!=None):
            pyautogui.moveTo(r)
            time.sleep(0.1)
            pyautogui.leftClick(r)
            time.sleep(0.1)
            continue

def main():
    t1 = Thread(target=autoaccept)
    t1.start()

if __name__ == '__main__':
    main()
