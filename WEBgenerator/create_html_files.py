# -------------------------------------------------------------------------------
# Name:         create_html_files.py
# Purpose:
# Author:       Cristian-Petrisor Dumea
#
# Created:      14.04.2019
# Copyright:    (c) Cristian-Petrisor Dumea 2019
#
# -------------------------------------------------------------------------------
import os
from base import BaseClass

class HTML_File (BaseClass):
    def __init__(self, title, path):
        BaseClass.__init__(self, title, path)
        self.b_file = open(self.base_path + "\\Generated\\" + self.page_title + ".html", "w")

    def handle(self):
        self.header = "<html>\n\t<head>\n\t\t" + \
            '<link rel="shertcut icon" href="Data/tab_image.jpg"\n\t\t' + \
            '<link rel="stylesheet" href="Data/styles.css">\n\t\t' + \
            '<title>' + self.page_title + ' generata</title>\n\t' + \
            '</head>\n\t'
        self.body = "<body>\n\t\t<p>Primul Rand Generat</p>\n\n</body>\n"
        self.b_file.write(self.header + self.body + "</html>")
        self.b_file.close()


