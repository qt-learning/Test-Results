# -*- coding: utf-8 -*-

import names

def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o4_Text_2))
    mouseClick(waitForObject(names.o5_Text))
    mouseClick(waitForObject(names.o6_Text))
    test.imagePresent("image_1")
