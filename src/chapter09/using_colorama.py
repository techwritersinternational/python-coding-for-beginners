# filename: using_colorama.py
from colorama import Fore, Back, Style
import colorama

# Initialize colorama (needed for Windows compatibility)
colorama.init()

# Create a colorful space mission log
print(Fore.GREEN + "Mission Log: " + Style.RESET_ALL + "Day 1")
print(Fore.BLUE + "Captain's Report: " + Style.RESET_ALL + "All systems nominal")
print(Fore.RED + "Warning: " + Style.RESET_ALL + "Asteroid field detected ahead")
print(Back.YELLOW + Fore.BLACK + "ALERT" + Style.RESET_ALL + " Prepare for evasive maneuvers")