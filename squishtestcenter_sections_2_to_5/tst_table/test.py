# -*- coding: utf-8 -*-

import names

def main():
    startApplication("addressbook")
    mouseClick(waitForObject(names.forename_HeaderViewItem), 77, 14, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.address_Book_File_QTableWidget), 164, 17, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.forename_HeaderViewItem), 66, 11, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.surname_HeaderViewItem), 47, 16, Qt.NoModifier, Qt.LeftButton)
    openContextMenu(waitForObject(names.address_Book_File_QTableWidget), 175, 40, Qt.NoModifier)
    activateItem(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.address_Book_File_QMenu, "New"))
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
    type(waitForObject(names.forename_LineEdit), "p")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "Prashanth ")
    mouseClick(waitForObject(names.surname_LineEdit), 70, 11, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.forename_LineEdit), 75, 10, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "h")
    type(waitForObject(names.forename_LineEdit), "<Backspace>")
    type(waitForObject(names.forename_LineEdit), "john")
    mouseClick(waitForObject(names.surname_LineEdit), 67, 0, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.surname_LineEdit), "joe")
    mouseClick(waitForObject(names.email_LineEdit), 86, 7, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.email_LineEdit), "john.joe")
    sendEvent("QKeyEvent", waitForObject(names.email_LineEdit), QEvent.KeyRelease, 16777248, 0, 33554432, "", False, 1)
    type(waitForObject(names.email_LineEdit), "@email.com")
    mouseClick(waitForObject(names.phone_LineEdit), 74, 10, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.phone_LineEdit), "111-222-4444")
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
    type(waitForObject(names.forename_LineEdit), "joe")
    mouseClick(waitForObject(names.surname_LineEdit), 34, 3, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.surname_LineEdit), "jihn")
    type(waitForObject(names.surname_LineEdit), "<Backspace>")
    type(waitForObject(names.surname_LineEdit), "<Backspace>")
    type(waitForObject(names.surname_LineEdit), "<Backspace>")
    type(waitForObject(names.surname_LineEdit), "<Backspace>")
    type(waitForObject(names.surname_LineEdit), "john")
    mouseClick(waitForObject(names.email_LineEdit), 35, 7, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.email_LineEdit), "joe.john@email.com")
    mouseClick(waitForObject(names.phone_LineEdit), 31, 7, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.phone_LineEdit), "6666-777-8889")
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))
    test.vp("VP1")
