# -------------------------------------------------------------------------------
# Name:         base.py
# Purpose:
# Author:       Cristian-Petrisor Dumea
#
# Created:      11.04.2019
# Copyright:    (c) Cristian-Petrisor Dumea 2019
#
# -------------------------------------------------------------------------------


class BaseClass:
    def __init__(self, title, path):
        self.page_title = title
        self.base_path = path


    def test_prints(self):
        print("Done!")
