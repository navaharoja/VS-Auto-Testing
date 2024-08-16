# Description: This script is used to take a capture of the screen and save it in the folder "Captures" with the name given in the variable "nameCapture"

import os
import pyautogui

def takeCapture(nameCapture, step):
    # Script directory
    script_dir = os.path.dirname(__file__)
    # Capture path
    capture_path = f"{script_dir}/Captures/{nameCapture}_Paso_{step}.png"
    # Take capture of the screen 
    pyautogui.screenshot(capture_path)
    #pyautogui.screenshot(capture_path, region=(0, 0, 1920, 1080))   
    

    print(f"Capture saved in: {capture_path}")









