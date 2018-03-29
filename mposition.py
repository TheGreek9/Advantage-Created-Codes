import pyautogui

x, y = pyautogui.position()

with open("position.log", "a") as f:
    f.write("move_and_click(" + str(x) + ", " + str(y) + ")" + "\n\n")
