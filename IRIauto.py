import pyautogui
i = 1

num = int(input("Amount of Brands: "))
try:
    while i < num:
        pyautogui.moveTo(1264, 372, duration=1.5)
        pyautogui.click(1264, 372)
        pyautogui.moveTo(690, 665, duration=5.5)
        pyautogui.click(690, 665)
        pyautogui.moveTo(752, 620, duration=0.5)
        pyautogui.click(752, 620)
        pyautogui.moveTo(1333, 375, duration=1.5)
        pyautogui.click(1333, 375)
        i += 1
except KeyboardInterrupt:
    print("Done. \n")
