import pyautogui as pg
import time

pg.FAILSAFE = True
pg.PAUSE = 0.2

# Open safari
pg.keyDown("command")
pg.keyDown("tab")
pg.keyUp("tab")
pg.keyUp("command")

# Open data tab
pg.moveTo((103, 102))
pg.click()

# Scroll to content
pg.moveTo((1504, 281))
pg.click()

for i in range(1):
    # Click generate button
    pg.moveTo((839, 481))
    pg.click()

    # Select text
    pg.moveTo((394, 637))
    pg.tripleClick()

    # Copy text
    pg.keyDown("commmand")
    pg.keyDown("c")
    pg.keyUp("c")
    pg.keyUp("command") 
