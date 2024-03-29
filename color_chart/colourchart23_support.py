#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 8.0v
#  in conjunction with Tcl version 8.6
#    Aug 09, 2023 08:51:07 AM CDT  platform: Linux
#    Aug 09, 2023 10:56:50 AM CDT  platform: Linux
#    Aug 09, 2023 11:02:19 AM CDT  platform: Linux
#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     colourchart22_support.py
#  ------------------------------------------------------
# Created for PAGE and PAGE users.
# Written by G.D. Walters
# Copyright (c) 2023 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# Change Log
#  -----------------------------------------------------
# version 2.1
#    * Changed custom widget to Scrolledwindow to demonstrate how
#        to use Scrolledwindow widget as a ScrolledCanvas widget.
#    * Added function to calculate proper light/dark colour for text
#    * Reads from rgb.txt file rather than hard coded colour names
# version 2.2
#    * modified font to 11 bold
# version 2.2.1𝛽
#    * Changed font to 9 bold
#    * Changed toplevel size to 1423 x 995.  Should still work on most monitors.
#    * Decreased number of buttons in row from 12 to 10
#    * Modified scrollregion to limit x and y size
#    * Reworked rgb.txt file to remove duplicates
#    * Removed old code from support file
#    * Added relief='ridge' and bd=1 to buttons
#    * Found DebianRed in rgb.txt.  Tkinter doesn't support it
#        so neither does PAGE, but added support in code to allow
#        the program to not throw error and to move on.  This is in
#        anticipation of more of these in the future.
# version 2.2.2𝛽
#    * Modified scrollregion to limit x and y size to just the buttons
#    * Modified maxsize (in GUI.py file) to 1425, 1242
#    * Added ability for user to press 'I' to get Toplevel size in terminal.
# version 2.3
#    * first release 12/12/2023
# ======================================================
import sys
import pprint
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import colourchart23

programName = "Tkinter Colour Chart"
version = "2.3"

_debug = True  # False to eliminate debug printing from callback functions.


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = colourchart23.Toplevel1(_top1)
    startup()
    root.mainloop()


def startup():
    _top1.title(f"{programName} {version}")
    global canvas
    canvas = _w1.Scrolledwindow1_f
    data = read_file_into_list("rgb.txt")
    COLORS = prep_data(data)
    d = pprint.pformat(COLORS, depth=5)

    fill_canvas2(COLORS)
    # _w1.Scrolledwindow1.configure(scrollregion=(0, 0, 1405, 1218))
    _w1.Scrolledwindow1.configure(scrollregion=(0, 0, 1455, 1218))
    root.bind("<KeyRelease-I>", on_keypress)


def on_keypress(*args):
    print(args)
    height = root.winfo_height()
    width = root.winfo_width()
    print(f"Width: {width} - Height: {height}")


def read_file_into_list(filename):
    # ======================================================
    # function read_file_into_list()
    # ======================================================
    # Read file, strip \n and put lines into a list
    # ======================================================
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def read_file(filename):
    # ======================================================
    # function read_file()
    # ======================================================
    # Read file, leaving end of lines
    # ======================================================
    with open(filename) as f:
        lines = f.read()

    return lines


def prep_data(data):
    COLORS = []

    print(len(data))
    for d in data:
        # print(d)

        l = d.split()
        # print(l)
        # print(len(l))

        r = l[0]
        g = l[1]
        b = l[2]
        name = f"{l[3]}"
        if len(l) == 6:
            name = f"{l[3]}{l[4]}{l[5]}"
        elif len(l) == 5:
            name = f"{l[3]}{l[4]}"
        elif len(l) > 6:
            print("BAD")
            name = "BAD"
        val = pick_text_color_based_on_bg_simple(int(r), int(g), int(b))
        dat = [int(r), int(g), int(b), name, val]

        COLORS.append(dat)
    return COLORS


def fill_canvas2(COLORS):
    b = {}
    id = {}
    no_buttons_per_row = 10
    row = 0
    for j in range(len(COLORS)):
        # print(f"Working {COLORS[j][3]}")
        bg = str(COLORS[j][3])
        fg = COLORS[j][4]
        row, col = divmod(j, no_buttons_per_row)
        b[j] = tk.Label(canvas, text=bg, height=1, width=17, bd=1, relief="ridge")
        b[j].configure(font="-family {DejaVu Sans} -size 9 -weight bold")
        try:
            b[j].configure(background=bg, foreground=fg)
        except:
            # Error in "translation".  Notify and force the issue
            print(f"Can't do {bg}")
            print(
                f"{COLORS[j][0]}-{COLORS[j][1]}-{COLORS[j][2]}-{COLORS[j][3]}-{COLORS[j][4]}"
            )
            bg = rgb_to_hex(COLORS[j][0], COLORS[j][1], COLORS[j][2])
            b[j].configure(background=bg, foreground=fg)
        b[j].grid(row=row, column=col)
        id[b[j].winfo_id()] = j


def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def pick_text_color_based_on_bg_simple(bgRed, bgGreen, bgBlue):
    # Source for this function is rewritten from a discussion at
    # https://stackoverflow.com/questions/3942878/how-to-decide-font-color-in-white-or-black-depending-on-background-color/3943023#3943023
    target = 150
    darkcolor = "#000000"
    lightcolor = "#ffffff"
    suggestion = (bgRed * 0.299) + (bgGreen * 0.587) + (bgBlue * 0.114)
    if suggestion > target:
        return darkcolor
    else:
        return lightcolor


if __name__ == "__main__":
    colourchart23.start_up()
