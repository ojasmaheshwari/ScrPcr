from PIL import ImageGrab
from datetime import datetime
import subprocess
from io import BytesIO
from os import system

def generateName(prefix):
    return prefix + "_" + str(datetime.now().date()) + "_" + datetime.now().strftime("%H:%M") + ".png"

screenshot_dir = "/home/epicman/screenshots/"

screenshot = ImageGrab.grab()

with BytesIO() as output:
    screenshot.save(output, format="PNG")
    data = output.getvalue()

process = subprocess.Popen(['xclip', '-selection', 'clipboard', '-t', 'image/png'], stdin=subprocess.PIPE)
process.communicate(input=data)
screenshot.save(generateName(screenshot_dir+generateName("screenshot")))

system("notify-send -u low -t 2000 -a \"ScrCpr - Screenshot Copier\" -c SUCCESS -e \"SUCCESS\" \"Copied screenshot to clipboard\"")

screenshot.close()

