import pyautogui
#pyautogui.moveTo(33, 692, duration=1)
currentPos = pyautogui.position()

im = pyautogui.screenshot()
currentPix = im.getpixel(currentPos)

print(pyautogui.position())
print(currentPix)
#print(pyautogui.pixelMatchesColor(33, 692, (6, 110, 73)))
