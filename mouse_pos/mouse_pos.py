# script to get mosue position

import pyautogui
from time import time, sleep
import re

# regex for numeric only
numeric_pattern = re.compile("[0-9]*$")

# init time delay
next_getInput = time() + 1

# input message
msg = '''\n----------------------------
  Options
    Enter to get current position
    <time>            seconds - to continuously print position
    <position name>   store last cursor position
        q             quit
  Enter command: '''


pos_store = []
while(True):
    # always get location
    curr_mouse_pos = pyautogui.position()
    print( f" x: {curr_mouse_pos.x}".ljust(10), f"y: {curr_mouse_pos.y}".ljust(10) )

    curr_time = time()
    if curr_time > next_getInput:
        command = input(msg)
        print("----------------------------\n")

        if command == "":
            next_getInput = time() + 0.1
        elif numeric_pattern.match(command):
            # keep going until elapsed time
            next_getInput = time() + int(command)
        elif command == "q":
            break
        else:
            pos_store.append([command, curr_mouse_pos])
            next_getInput = time() + 0.5

    sleep(0.1)


if len(pos_store) > 0:
    # print all stored postions - pretty print
    for pos in pos_store:
        print( f"({pos[1].x},{pos[1].y})".ljust(13), f" {pos[0]}" )
    print()

# print(pos_store)


