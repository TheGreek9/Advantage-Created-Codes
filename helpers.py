import pyautogui

def bump_selection():
    pyautogui.click(966, 756)
    text = input("Select the bump chart from now. Move mouse over to position and press enter")
    return pyautogui.position()



def process(week):
    move_and_click(418, 196, 1)
    pyautogui.moveTo(737, 256)
    check_color((232, 231, 228))
    pyautogui.click(737, 256)
    move_and_click(886, 386, 0.6)
    move_and_click(847, 506, 0.6)
    pyautogui.moveTo(30, 689, duration = 1.0)
    check_color((209, 218, 211))
    pyautogui.click(30, 689)
    pyautogui.click(30, 689)
    pyautogui.moveTo(110, 228, duration = 1.0)
    check_color((238, 208, 103))
    move_and_click(89, 324, 0.5); pyautogui.typewrite(week)
    pyautogui.typewrite('\n')
    move_and_click(101, 756, 1)
    move_and_click(435, 259, 1)
    move_and_click(178, 193, 3.2)

def process_all(text):
    move_and_click(418, 196, 1)
    pyautogui.moveTo(737, 256, duration = 1.0)
    check_color((232, 231, 228))
    pyautogui.click(737, 256)
    move_and_click(852, 344, 0.6)
    move_and_click(847, 506, 0.6)
    pyautogui.moveTo(30, 689, duration = 1.0)
    check_color((209, 218, 211))
    pyautogui.click(30, 689)
    pyautogui.click(30, 689)
    pyautogui.moveTo(110, 228, duration = 1.0)
    check_color((238, 208, 103))
    move_and_click(89, 324, 0.5); pyautogui.typewrite(text)
    pyautogui.typewrite('\n')
    move_and_click(101, 756, 1)
    move_and_click(178, 193, 2.2)

def move_and_click(x, y, duration=1.5):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click(x, y)

def focus_terminal(text):
    pyautogui.click(966, 756)
    text = input(text)
    pyautogui.click(541, 192)

def check_color(color):
    x, y = pyautogui.position()
    im = pyautogui.screenshot()

    match = pyautogui.pixelMatchesColor(x, y, color)
    try:
        while match == False:
            match = pyautogui.pixelMatchesColor(x, y, color)
    except KeyboardInterrupt:
        focus_terminal("Paused")
        check_color(color)
