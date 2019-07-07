# -------------------------------------------------------------------------------
# Name:         additional_funcs.py
# Purpose:
# Author:       Cristian-Petrisor Dumea
#
# Created:      14.04.2019
# Copyright:    (c) Cristian-Petrisor Dumea 2019
#
# -------------------------------------------------------------------------------


def extract_sections(lst_with_files, extension):
    lst_with_web = []
    for it in lst_with_files:
        if extension in it:
            element = it.split('.'+extension)[0]
            lst_with_web.append(element)
    return lst_with_web
