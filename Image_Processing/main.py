# -------------------------------------------------------------------------------
# Name:         main.py
# Purpose:      Process an image file (is not working with jpg, jpeg) and generates Robot Studio RAPID code
# Author:       Cristian-Petrisor Dumea
#
# Created:      14.05.2019
# Copyright:    (c) Cristian-Petrisor Dumea 2019
#
# -------------------------------------------------------------------------------
from PIL import Image, ImageOps
from pylab import *
from matplotlib import pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import ntpath
import os


def main():
    # read image to array
    lst_with_imags_extension = ['.bmp', '.png', '.gif', '.tif', '.tiff', '.dib', '.jpe', '.jfif']
    flag = True
    while (flag):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        for ext in lst_with_imags_extension:
            if filename.endswith(ext):
                flag = False
                break
        if flag is True:
            print('Wrong Extension!!!')
    img = Image.open(filename)
    first_size = img.size
    im = array(img.convert('L'))
    # create a new figure
    figure()
    # show contours with origin upper left corner
    contour(im, levels=[1], colors='black', origin='image')
    # contour(im)
    plt.savefig('workspace\\foo2.png')
    img = Image.open('workspace\\foo2.png')
    border = (82, 61, 65, 54)  # left, up, right, bottom
    img = ImageOps.crop(img, border)
    sec_size = img.size
    x_scale = first_size[0] / sec_size[0]
    y_scale = first_size[1] / sec_size[1]
    flag = True
    first_app = 0
    last_app = 0
    pix = img.load()
    for col in range(0, sec_size[0] - 1):
        for line in range(0, sec_size[1] - 1):
            if pix[col, line] == (0, 0, 0, 255):
                first_app = col
                flag = True
                break
        if flag is True:
            break
    flag = False
    for col in range(sec_size[0] - 1, 0, -1):
        for line in range(0, sec_size[1] - 1):
            if pix[col, line] == (0, 0, 0, 255):
                last_app = col
                flag = True
                break
        if flag is True:
            break
    print('The first col with contour is: {} and the last col is: {}'.format(first_app, last_app))
    lst_with_coords = []
    for col in range(first_app, last_app, 3):
        for line in range(0, sec_size[1] - 1):
            if pix[col, line] == (0, 0, 0, 255):
                lst_with_coords.append([int(col), int(line)])
                break
    for col in range(last_app, first_app, -3):
        for line in range(sec_size[1] - 1, 0, -1):
            if pix[col, line] == (0, 0, 0, 255):
                lst_with_coords.append([int(col), int(line)])
                break
    print(lst_with_coords)
    str_targets = ''
    str_movejs = '\n\t\tPROC Path_10()\n\t\t\tMoveJ TargetHome,v200,z100,Efector\WObj:=Workobject_1;'
    str_target_home = '\n\t\tCONST robtarget TargetHome:=[[-227.973795532,131.62088768' \
                      '7,418.490948477],[0.000000095,-0.000' \
                      '000026,1,-0.000000026],[-1,-1,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];'
    i = 0
    for point in lst_with_coords:
        target = 'Target_' + str(i)
        i = i + 1
        str_targets = str_targets + '\n\t\tCONST robtarget ' + target + ':=[[' + str(point[0]/2) + ',' + str(point[1]/2) +\
                      ',115],[0,0,1,0],[-1,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];'
        str_movejs = str_movejs + '\n\t\t\tMovej ' + target +',v200,z100,Efector\WObj:=Workobject_1;'
    str_targets = str_target_home + str_targets
    str_movejs = str_movejs + '\n\t\t\tMovej Target_0 ,v200,z100,Efector\WObj:=Workobject_1;'
    str_movejs = str_movejs + '\n\t\t\tMoveJ TargetHome,v200,z100,Efector\WObj:=Workobject_1;' + '\n\t\tENDPROC'
    str_main = '\n\tPROC main()\n\t\tSetDO DO11_7, 0;\n\t\tSetDO DO11_8, 1;\n\t\tPath_10;\n\tENDPROC'
    str_vars = '\n\t\tPERS tooldata Efector:=[TRUE,[[0,0.033033672,184.3],[1,0,0,0]],[1.5,[0,0,90],[1,0,0,0],0.01,0.01,0.01]];\n\t\tPERS wobjdata Workobject_1:=[FALSE,TRUE,"",[[342.383498332,-1166.025064514,772.5],[0.866024971,0,0,-0.50000075]],[[0,0,22.5],[1,0,0,0]]];'
    content = 'MODULE Module1' + str_targets + str_vars + str_main + str_movejs + '\nENDMODULE'
    with open ('Module1.mod', 'w') as robot_code:
        robot_code.write(content)
    os.remove('workspace\\foo2.png')
    head, tail = ntpath.split(filename)
    name = ntpath.basename(tail).split('.')[0]
    name = 'workspace\\' + name + '_contour' + ext
    img.save(name)


if __name__ == '__main__':
    main()
    print('Done!')
