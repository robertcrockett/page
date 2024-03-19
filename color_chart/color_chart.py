# program taken from http://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix-using-python
#
from tkinter import *

MAX_ROWS = 45
FONT_SIZE = 13 # (pixels)

# COLORS was inserted from the file colors in this directory

COLORS = [
    ['snow', 'black'],
    ['ghost white', 'black'],
    ['GhostWhite', 'black'],
    ['white smoke', 'black'],
    ['WhiteSmoke', 'black'],
    ['gainsboro', 'black'],
    ['floral white', 'black'],
    ['FloralWhite', 'black'],
    ['old lace', 'black'],
    ['OldLace', 'black'],
    ['linen', 'black'],
    ['antique white', 'black'],
    ['AntiqueWhite', 'black'],
    ['papaya whip', 'black'],
    ['PapayaWhip', 'black'],
    ['blanched almond', 'black'],
    ['BlanchedAlmond', 'black'],
    ['bisque', 'black'],
    ['peach puff', 'black'],
    ['PeachPuff', 'black'],
    ['navajo white', 'black'],
    ['NavajoWhite', 'black'],
    ['moccasin', 'black'],
    ['cornsilk', 'black'],
    ['ivory', 'black'],
    ['lemon chiffon', 'black'],
    ['LemonChiffon', 'black'],
    ['seashell', 'black'],
    ['honeydew', 'black'],
    ['mint cream', 'black'],
    ['MintCream', 'black'],
    ['azure', 'black'],
    ['alice blue', 'black'],
    ['AliceBlue', 'black'],
    ['lavender', 'black'],
    ['lavender blush', 'black'],
    ['LavenderBlush', 'black'],
    ['misty rose', 'black'],
    ['MistyRose', 'black'],
    ['white', 'black'],
    ['black', 'white'],
    ['dark slate gray', 'white'],
    ['DarkSlateGray', 'white'],
    ['dim gray', 'white'],
    ['DimGray', 'white'],
    ['slate gray', 'white'],
    ['SlateGray', 'white'],
    ['light slate gray', 'black'],
    ['LightSlateGray', 'black'],
    ['gray', 'black'],
    ['light gray', 'black'],
    ['LightGray', 'black'],
    ['midnight blue', 'white'],
    ['MidnightBlue', 'white'],
    ['navy', 'white'],
    ['navy blue', 'white'],
    ['NavyBlue', 'white'],
    ['cornflower blue', 'black'],
    ['CornflowerBlue', 'black'],
    ['dark slate blue', 'white'],
    ['DarkSlateBlue', 'white'],
    ['slate blue', 'white'],
    ['SlateBlue', 'white'],
    ['medium slate blue', 'black'],
    ['MediumSlateBlue', 'black'],
    ['light slate blue', 'black'],
    ['LightSlateBlue', 'black'],
    ['medium blue', 'white'],
    ['MediumBlue', 'white'],
    ['royal blue', 'white'],
    ['RoyalBlue', 'white'],
    ['blue', 'white'],
    ['dodger blue', 'black'],
    ['DodgerBlue', 'black'],
    ['deep sky blue', 'black'],
    ['DeepSkyBlue', 'black'],
    ['sky blue', 'black'],
    ['SkyBlue', 'black'],
    ['light sky blue', 'black'],
    ['LightSkyBlue', 'black'],
    ['steel blue', 'white'],
    ['SteelBlue', 'white'],
    ['light steel blue', 'black'],
    ['LightSteelBlue', 'black'],
    ['light blue', 'black'],
    ['LightBlue', 'black'],
    ['powder blue', 'black'],
    ['PowderBlue', 'black'],
    ['pale turquoise', 'black'],
    ['PaleTurquoise', 'black'],
    ['dark turquoise', 'black'],
    ['DarkTurquoise', 'black'],
    ['medium turquoise', 'black'],
    ['MediumTurquoise', 'black'],
    ['turquoise', 'black'],
    ['cyan', 'black'],
    ['light cyan', 'black'],
    ['LightCyan', 'black'],
    ['cadet blue', 'black'],
    ['CadetBlue', 'black'],
    ['medium aquamarine', 'black'],
    ['MediumAquamarine', 'black'],
    ['aquamarine', 'black'],
    ['dark green', 'white'],
    ['DarkGreen', 'white'],
    ['dark olive green', 'white'],
    ['DarkOliveGreen', 'white'],
    ['dark sea green', 'black'],
    ['DarkSeaGreen', 'black'],
    ['sea green', 'white'],
    ['SeaGreen', 'white'],
    ['medium sea green', 'black'],
    ['MediumSeaGreen', 'black'],
    ['light sea green', 'black'],
    ['LightSeaGreen', 'black'],
    ['pale green', 'black'],
    ['PaleGreen', 'black'],
    ['spring green', 'black'],
    ['SpringGreen', 'black'],
    ['lawn green', 'black'],
    ['LawnGreen', 'black'],
    ['green', 'black'],
    ['chartreuse', 'black'],
    ['medium spring green', 'black'],
    ['MediumSpringGreen', 'black'],
    ['green yellow', 'black'],
    ['GreenYellow', 'black'],
    ['lime green', 'black'],
    ['LimeGreen', 'black'],
    ['yellow green', 'black'],
    ['YellowGreen', 'black'],
    ['forest green', 'white'],
    ['ForestGreen', 'white'],
    ['olive drab', 'white'],
    ['OliveDrab', 'white'],
    ['dark khaki', 'black'],
    ['DarkKhaki', 'black'],
    ['khaki', 'black'],
    ['pale goldenrod', 'black'],
    ['PaleGoldenrod', 'black'],
    ['light goldenrod yellow', 'black'],
    ['LightGoldenrodYellow', 'black'],
    ['light yellow', 'black'],
    ['LightYellow', 'black'],
    ['yellow', 'black'],
    ['gold', 'black'],
    ['light goldenrod', 'black'],
    ['LightGoldenrod', 'black'],
    ['goldenrod', 'black'],
    ['dark goldenrod', 'black'],
    ['DarkGoldenrod', 'black'],
    ['rosy brown', 'black'],
    ['RosyBrown', 'black'],
    ['indian red', 'black'],
    ['IndianRed', 'black'],
    ['saddle brown', 'white'],
    ['SaddleBrown', 'white'],
    ['sienna', 'white'],
    ['peru', 'black'],
    ['burlywood', 'black'],
    ['beige', 'black'],
    ['wheat', 'black'],
    ['sandy brown', 'black'],
    ['SandyBrown', 'black'],
    ['tan', 'black'],
    ['chocolate', 'black'],
    ['firebrick', 'white'],
    ['brown', 'white'],
    ['dark salmon', 'black'],
    ['DarkSalmon', 'black'],
    ['salmon', 'black'],
    ['light salmon', 'black'],
    ['LightSalmon', 'black'],
    ['orange', 'black'],
    ['dark orange', 'black'],
    ['DarkOrange', 'black'],
    ['coral', 'black'],
    ['light coral', 'black'],
    ['LightCoral', 'black'],
    ['tomato', 'black'],
    ['orange red', 'black'],
    ['OrangeRed', 'black'],
    ['red', 'black'],
    ['hot pink', 'black'],
    ['HotPink', 'black'],
    ['deep pink', 'black'],
    ['DeepPink', 'black'],
    ['pink', 'black'],
    ['light pink', 'black'],
    ['LightPink', 'black'],
    ['pale violet red', 'black'],
    ['PaleVioletRed', 'black'],
    ['maroon', 'white'],
    ['medium violet red', 'white'],
    ['MediumVioletRed', 'white'],
    ['violet red', 'white'],
    ['VioletRed', 'white'],
    ['magenta', 'black'],
    ['violet', 'black'],
    ['plum', 'black'],
    ['orchid', 'black'],
    ['medium orchid', 'black'],
    ['MediumOrchid', 'black'],
    ['dark orchid', 'white'],
    ['DarkOrchid', 'white'],
    ['dark violet', 'white'],
    ['DarkViolet', 'white'],
    ['blue violet', 'white'],
    ['BlueViolet', 'white'],
    ['purple', 'white'],
    ['medium purple', 'black'],
    ['MediumPurple', 'black'],
    ['thistle', 'black'],
    ['snow1', 'black'],
    ['snow2', 'black'],
    ['snow3', 'black'],
    ['snow4', 'black'],
    ['seashell1', 'black'],
    ['seashell2', 'black'],
    ['seashell3', 'black'],
    ['seashell4', 'black'],
    ['AntiqueWhite1', 'black'],
    ['AntiqueWhite2', 'black'],
    ['AntiqueWhite3', 'black'],
    ['AntiqueWhite4', 'black'],
    ['bisque1', 'black'],
    ['bisque2', 'black'],
    ['bisque3', 'black'],
    ['bisque4', 'white'],
    ['PeachPuff1', 'black'],
    ['PeachPuff2', 'black'],
    ['PeachPuff3', 'black'],
    ['PeachPuff4', 'white'],
    ['NavajoWhite1', 'black'],
    ['NavajoWhite2', 'black'],
    ['NavajoWhite3', 'black'],
    ['NavajoWhite4', 'white'],
    ['LemonChiffon1', 'black'],
    ['LemonChiffon2', 'black'],
    ['LemonChiffon3', 'black'],
    ['LemonChiffon4', 'black'],
    ['cornsilk1', 'black'],
    ['cornsilk2', 'black'],
    ['cornsilk3', 'black'],
    ['cornsilk4', 'black'],
    ['ivory1', 'black'],
    ['ivory2', 'black'],
    ['ivory3', 'black'],
    ['ivory4', 'black'],
    ['honeydew1', 'black'],
    ['honeydew2', 'black'],
    ['honeydew3', 'black'],
    ['honeydew4', 'black'],
    ['LavenderBlush1', 'black'],
    ['LavenderBlush2', 'black'],
    ['LavenderBlush3', 'black'],
    ['LavenderBlush4', 'black'],
    ['MistyRose1', 'black'],
    ['MistyRose2', 'black'],
    ['MistyRose3', 'black'],
    ['MistyRose4', 'black'],
    ['azure1', 'black'],
    ['azure2', 'black'],
    ['azure3', 'black'],
    ['azure4', 'black'],
    ['SlateBlue1', 'black'],
    ['SlateBlue2', 'black'],
    ['SlateBlue3', 'white'],
    ['SlateBlue4', 'white'],
    ['RoyalBlue1', 'black'],
    ['RoyalBlue2', 'white'],
    ['RoyalBlue3', 'white'],
    ['RoyalBlue4', 'white'],
    ['blue1', 'white'],
    ['blue2', 'white'],
    ['blue3', 'white'],
    ['blue4', 'white'],
    ['DodgerBlue1', 'black'],
    ['DodgerBlue2', 'black'],
    ['DodgerBlue3', 'white'],
    ['DodgerBlue4', 'white'],
    ['SteelBlue1', 'black'],
    ['SteelBlue2', 'black'],
    ['SteelBlue3', 'black'],
    ['SteelBlue4', 'white'],
    ['DeepSkyBlue1', 'black'],
    ['DeepSkyBlue2', 'black'],
    ['DeepSkyBlue3', 'black'],
    ['DeepSkyBlue4', 'white'],
    ['SkyBlue1', 'black'],
    ['SkyBlue2', 'black'],
    ['SkyBlue3', 'black'],
    ['SkyBlue4', 'white'],
    ['LightSkyBlue1', 'black'],
    ['LightSkyBlue2', 'black'],
    ['LightSkyBlue3', 'black'],
    ['LightSkyBlue4', 'white'],
    ['SlateGray1', 'black'],
    ['SlateGray2', 'black'],
    ['SlateGray3', 'black'],
    ['SlateGray4', 'white'],
    ['LightSteelBlue1', 'black'],
    ['LightSteelBlue2', 'black'],
    ['LightSteelBlue3', 'black'],
    ['LightSteelBlue4', 'white'],
    ['LightBlue1', 'black'],
    ['LightBlue2', 'black'],
    ['LightBlue3', 'black'],
    ['LightBlue4', 'white'],
    ['LightCyan1', 'black'],
    ['LightCyan2', 'black'],
    ['LightCyan3', 'black'],
    ['LightCyan4', 'black'],
    ['PaleTurquoise1', 'black'],
    ['PaleTurquoise2', 'black'],
    ['PaleTurquoise3', 'black'],
    ['PaleTurquoise4', 'black'],
    ['CadetBlue1', 'black'],
    ['CadetBlue2', 'black'],
    ['CadetBlue3', 'black'],
    ['CadetBlue4', 'white'],
    ['turquoise1', 'black'],
    ['turquoise2', 'black'],
    ['turquoise3', 'black'],
    ['turquoise4', 'white'],
    ['cyan1', 'black'],
    ['cyan2', 'black'],
    ['cyan3', 'black'],
    ['cyan4', 'white'],
    ['DarkSlateGray1', 'black'],
    ['DarkSlateGray2', 'black'],
    ['DarkSlateGray3', 'black'],
    ['DarkSlateGray4', 'white'],
    ['aquamarine1', 'black'],
    ['aquamarine2', 'black'],
    ['aquamarine3', 'black'],
    ['aquamarine4', 'white'],
    ['DarkSeaGreen1', 'black'],
    ['DarkSeaGreen2', 'black'],
    ['DarkSeaGreen3', 'black'],
    ['DarkSeaGreen4', 'white'],
    ['SeaGreen1', 'black'],
    ['SeaGreen2', 'black'],
    ['SeaGreen3', 'black'],
    ['SeaGreen4', 'white'],
    ['PaleGreen1', 'black'],
    ['PaleGreen2', 'black'],
    ['PaleGreen3', 'black'],
    ['PaleGreen4', 'white'],
    ['SpringGreen1', 'black'],
    ['SpringGreen2', 'black'],
    ['SpringGreen3', 'black'],
    ['SpringGreen4', 'white'],
    ['green1', 'black'],
    ['green2', 'black'],
    ['green3', 'black'],
    ['green4', 'white'],
    ['chartreuse1', 'black'],
    ['chartreuse2', 'black'],
    ['chartreuse3', 'black'],
    ['chartreuse4', 'white'],
    ['OliveDrab1', 'black'],
    ['OliveDrab2', 'black'],
    ['OliveDrab3', 'black'],
    ['OliveDrab4', 'white'],
    ['DarkOliveGreen1', 'black'],
    ['DarkOliveGreen2', 'black'],
    ['DarkOliveGreen3', 'black'],
    ['DarkOliveGreen4', 'white'],
    ['khaki1', 'black'],
    ['khaki2', 'black'],
    ['khaki3', 'black'],
    ['khaki4', 'black'],
    ['LightGoldenrod1', 'black'],
    ['LightGoldenrod2', 'black'],
    ['LightGoldenrod3', 'black'],
    ['LightGoldenrod4', 'white'],
    ['LightYellow1', 'black'],
    ['LightYellow2', 'black'],
    ['LightYellow3', 'black'],
    ['LightYellow4', 'black'],
    ['yellow1', 'black'],
    ['yellow2', 'black'],
    ['yellow3', 'black'],
    ['yellow4', 'black'],
    ['gold1', 'black'],
    ['gold2', 'black'],
    ['gold3', 'black'],
    ['gold4', 'white'],
    ['goldenrod1', 'black'],
    ['goldenrod2', 'black'],
    ['goldenrod3', 'black'],
    ['goldenrod4', 'white'],
    ['DarkGoldenrod1', 'black'],
    ['DarkGoldenrod2', 'black'],
    ['DarkGoldenrod3', 'black'],
    ['DarkGoldenrod4', 'white'],
    ['RosyBrown1', 'black'],
    ['RosyBrown2', 'black'],
    ['RosyBrown3', 'black'],
    ['RosyBrown4', 'white'],
    ['IndianRed1', 'black'],
    ['IndianRed2', 'black'],
    ['IndianRed3', 'black'],
    ['IndianRed4', 'white'],
    ['sienna1', 'black'],
    ['sienna2', 'black'],
    ['sienna3', 'black'],
    ['sienna4', 'white'],
    ['burlywood1', 'black'],
    ['burlywood2', 'black'],
    ['burlywood3', 'black'],
    ['burlywood4', 'white'],
    ['wheat1', 'black'],
    ['wheat2', 'black'],
    ['wheat3', 'black'],
    ['wheat4', 'black'],
    ['tan1', 'black'],
    ['tan2', 'black'],
    ['tan3', 'black'],
    ['tan4', 'white'],
    ['chocolate1', 'black'],
    ['chocolate2', 'black'],
    ['chocolate3', 'black'],
    ['chocolate4', 'white'],
    ['firebrick1', 'black'],
    ['firebrick2', 'black'],
    ['firebrick3', 'white'],
    ['firebrick4', 'white'],
    ['brown1', 'black'],
    ['brown2', 'black'],
    ['brown3', 'white'],
    ['brown4', 'white'],
    ['salmon1', 'black'],
    ['salmon2', 'black'],
    ['salmon3', 'black'],
    ['salmon4', 'white'],
    ['LightSalmon1', 'black'],
    ['LightSalmon2', 'black'],
    ['LightSalmon3', 'black'],
    ['LightSalmon4', 'white'],
    ['orange1', 'black'],
    ['orange2', 'black'],
    ['orange3', 'black'],
    ['orange4', 'white'],
    ['DarkOrange1', 'black'],
    ['DarkOrange2', 'black'],
    ['DarkOrange3', 'black'],
    ['DarkOrange4', 'white'],
    ['coral1', 'black'],
    ['coral2', 'black'],
    ['coral3', 'black'],
    ['coral4', 'white'],
    ['tomato1', 'black'],
    ['tomato2', 'black'],
    ['tomato3', 'black'],
    ['tomato4', 'white'],
    ['OrangeRed1', 'black'],
    ['OrangeRed2', 'black'],
    ['OrangeRed3', 'white'],
    ['OrangeRed4', 'white'],
    ['red1', 'black'],
    ['red2', 'black'],
    ['red3', 'white'],
    ['red4', 'white'],
    ['DeepPink1', 'black'],
    ['DeepPink2', 'black'],
    ['DeepPink3', 'white'],
    ['DeepPink4', 'white'],
    ['HotPink1', 'black'],
    ['HotPink2', 'black'],
    ['HotPink3', 'black'],
    ['HotPink4', 'white'],
    ['pink1', 'black'],
    ['pink2', 'black'],
    ['pink3', 'black'],
    ['pink4', 'white'],
    ['LightPink1', 'black'],
    ['LightPink2', 'black'],
    ['LightPink3', 'black'],
    ['LightPink4', 'white'],
    ['PaleVioletRed1', 'black'],
    ['PaleVioletRed2', 'black'],
    ['PaleVioletRed3', 'black'],
    ['PaleVioletRed4', 'white'],
    ['maroon1', 'black'],
    ['maroon2', 'black'],
    ['maroon3', 'white'],
    ['maroon4', 'white'],
    ['VioletRed1', 'black'],
    ['VioletRed2', 'black'],
    ['VioletRed3', 'white'],
    ['VioletRed4', 'white'],
    ['magenta1', 'black'],
    ['magenta2', 'black'],
    ['magenta3', 'black'],
    ['magenta4', 'white'],
    ['orchid1', 'black'],
    ['orchid2', 'black'],
    ['orchid3', 'black'],
    ['orchid4', 'white'],
    ['plum1', 'black'],
    ['plum2', 'black'],
    ['plum3', 'black'],
    ['plum4', 'white'],
    ['MediumOrchid1', 'black'],
    ['MediumOrchid2', 'black'],
    ['MediumOrchid3', 'black'],
    ['MediumOrchid4', 'white'],
    ['DarkOrchid1', 'black'],
    ['DarkOrchid2', 'black'],
    ['DarkOrchid3', 'white'],
    ['DarkOrchid4', 'white'],
    ['purple1', 'white'],
    ['purple2', 'white'],
    ['purple3', 'white'],
    ['purple4', 'white'],
    ['MediumPurple1', 'black'],
    ['MediumPurple2', 'black'],
    ['MediumPurple3', 'black'],
    ['MediumPurple4', 'white'],
    ['thistle1', 'black'],
    ['thistle2', 'black'],
    ['thistle3', 'black'],
    ['thistle4', 'black'],
    ['dark gray', 'black'],
    ['DarkGray', 'black'],
    ['dark blue', 'white'],
    ['DarkBlue', 'white'],
    ['dark cyan', 'white'],
    ['DarkCyan', 'white'],
    ['dark magenta', 'white'],
    ['DarkMagenta', 'white'],
    ['dark red', 'white'],
    ['DarkRed', 'white'],
    ['light green', 'black'],
    ['LightGreen', 'black'],
    ['gray0', 'white'],
    ['gray1', 'white'],
    ['gray2', 'white'],
    ['gray3', 'white'],
    ['gray4', 'white'],
    ['gray5', 'white'],
    ['gray6', 'white'],
    ['gray7', 'white'],
    ['gray8', 'white'],
    ['gray9', 'white'],
    ['gray10', 'white'],
    ['gray11', 'white'],
    ['gray12', 'white'],
    ['gray13', 'white'],
    ['gray14', 'white'],
    ['gray15', 'white'],
    ['gray16', 'white'],
    ['gray17', 'white'],
    ['gray18', 'white'],
    ['gray19', 'white'],
    ['gray20', 'white'],
    ['gray21', 'white'],
    ['gray22', 'white'],
    ['gray23', 'white'],
    ['gray24', 'white'],
    ['gray25', 'white'],
    ['gray26', 'white'],
    ['gray27', 'white'],
    ['gray28', 'white'],
    ['gray29', 'white'],
    ['gray30', 'white'],
    ['gray31', 'white'],
    ['gray32', 'white'],
    ['gray33', 'white'],
    ['gray34', 'white'],
    ['gray35', 'white'],
    ['gray36', 'white'],
    ['gray37', 'white'],
    ['gray38', 'white'],
    ['gray39', 'white'],
    ['gray40', 'white'],
    ['gray41', 'white'],
    ['gray42', 'white'],
    ['gray43', 'white'],
    ['gray44', 'white'],
    ['gray45', 'white'],
    ['gray46', 'white'],
    ['gray47', 'white'],
    ['gray48', 'white'],
    ['gray49', 'white'],
    ['gray50', 'white'],
    ['gray51', 'black'],
    ['gray52', 'black'],
    ['gray53', 'black'],
    ['gray54', 'black'],
    ['gray55', 'black'],
    ['gray56', 'black'],
    ['gray57', 'black'],
    ['gray58', 'black'],
    ['gray59', 'black'],
    ['gray60', 'black'],
    ['gray61', 'black'],
    ['gray62', 'black'],
    ['gray63', 'black'],
    ['gray64', 'black'],
    ['gray65', 'black'],
    ['gray66', 'black'],
    ['gray67', 'black'],
    ['gray68', 'black'],
    ['gray69', 'black'],
    ['gray70', 'black'],
    ['gray71', 'black'],
    ['gray72', 'black'],
    ['gray73', 'black'],
    ['gray74', 'black'],
    ['gray75', 'black'],
    ['gray76', 'black'],
    ['gray77', 'black'],
    ['gray78', 'black'],
    ['gray79', 'black'],
    ['gray80', 'black'],
    ['gray81', 'black'],
    ['gray82', 'black'],
    ['gray83', 'black'],
    ['gray84', 'black'],
    ['gray85', 'black'],
    ['gray86', 'black'],
    ['gray87', 'black'],
    ['gray88', 'black'],
    ['gray89', 'black'],
    ['gray90', 'black'],
    ['gray91', 'black'],
    ['gray92', 'black'],
    ['gray93', 'black'],
    ['gray94', 'black'],
    ['gray95', 'black'],
    ['gray96', 'black'],
    ['gray97', 'black'],
    ['gray98', 'black'],
    ['gray99', 'black'],
    ['gray100', 'black'],
]


root = Tk()
root.title("Named colour chart")
row = 0
col = 0
for clist in COLORS:
    color = clist[0]
    text_color = clist[1]
    e = Label(root, text=color, background=color, foreground = text_color,
              font=(None, -FONT_SIZE))
    e.grid(row=row, column=col, sticky=E+W)
    row += 1
    if (row > MAX_ROWS):
        row = 0
        col += 1

root.mainloop()
