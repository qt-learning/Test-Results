# -*- coding: utf-8 -*-

import names

def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o7_Text))
    mouseClick(waitForObject(names.o_Text))
    mouseClick(waitForObject(names.o9_Text))
    mouseClick(waitForObject(names.o_Text_2))
    test.compare(str(waitForObjectExists(names.o63_Text).text), "69")
