import pyautogui
from helpers import *
pyautogui.FAILSAFE = True

def main():
    input('First select the correct products for Store Selling/Markdowns')
    input('Next move mouse to bump chart and press enter when finished.')
    bump_x, bump_y = pyautogui.position()

    input('Finally select Weekly Base Data report and Load. Press enter when finished.')

    move_and_click(165, 196, 0.5)

    move_and_click(1132, 469)
    process('52 Weeks')

    move_and_click(830, 380)
    process('YTD')

    move_and_click(1156, 426)
    process('26 Weeks')

    move_and_click(1152, 388)
    process('13 Weeks')

    move_and_click(1012, 384)
    process('4 Weeks')

    move_and_click(848, 200)
    pyautogui.moveTo(bump_x, bump_y, duration=1.5)
    pyautogui.click(bump_x, bump_y)
    pyautogui.moveTo(544, 615, duration=1.5)
    pyautogui.click(544, 615)
    move_and_click(178, 193, 1)
    move_and_click(1162, 481)
    process('Bump')
    move_and_click(290, 193, 0.5)

    move_and_click(848, 200)
    move_and_click(140, 266, 1)
    move_and_click(138, 346, 1)
    focus_terminal("Click on store selling")
    move_and_click(172, 555)
    move_and_click(1359, 669, 1)
    move_and_click(595, 565, 1)
    move_and_click(299, 194, 1)
    move_and_click(19, 257)
    move_and_click(178, 193, 1)
    move_and_click(1162, 481)
    process_all("Selling")

    move_and_click(848, 200)
    move_and_click(651, 514)
    focus_terminal("Click on Sherlock Store Standard")
    move_and_click(1359, 669, 1)
    move_and_click(595, 565, 1)
    move_and_click(299, 194, 1)
    move_and_click(178, 193, 1)
    move_and_click(1012, 384)
    process_all("Markdown")

    move_and_click(315, 746)
    move_and_click(1248, 641)
    move_and_click(18, 612)
    move_and_click(444, 61)
    move_and_click(560, 111)

    focus_terminal('Finished!')


if __name__ == '__main__':
    main()
