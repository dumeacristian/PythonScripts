# -------------------------------------------------------------------------------
# Name:         main.py
# Purpose:
# Author:       Cristian-Petrisor Dumea
#
# Created:      11.04.2019
# Copyright:    (c) Cristian-Petrisor Dumea 2019
#
# -------------------------------------------------------------------------------

import os
from create_html_files import HTML_File
from additional_funcs import *

def main():
    base_path = 'D:\\PythonScripts\\Test_For_WEBgenerator'
    lst_with_files = os.listdir(base_path)
    lst_with_web_sites = extract_sections(lst_with_files, 'txt')
    a = HTML_File("Prima Pagina", base_path)
    a.handle()

if __name__ == "__main__":
    main()
