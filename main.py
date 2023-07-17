#!/usr/bin/python3
import pystray
from PIL import Image
import sys

def setPortable():
    print("Setting Full Charge")

def setDocked():
    print("Setting Docked")

def createMenu():
    full_charge_item = pystray.MenuItem(
        text="Full Charge",
        action=setPortable
    )
    docked_charge_item = pystray.MenuItem(
        text="Limit to 50% (Docked Mode)",
        action=setDocked
    )
    return pystray.Menu(full_charge_item, docked_charge_item)

def createIcon():
    return pystray.Icon(
        name="ThinkPad Battery Control",
        title="Battery Mode",
        icon=Image.open("assets/StatusIcon.png"),
        menu=createMenu()
    ) 

def main():
    icon = createIcon()
    
    if not icon.HAS_MENU:
        print("Windowing system not supported.")
        sys.exit(1)

    icon.run()

if __name__ == "__main__":
    main()