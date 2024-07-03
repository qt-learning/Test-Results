# encoding: UTF-8

from objectmaphelper import *

address_Book_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book"}
o_QQuickView = {"type": "QQuickView", "unnamed": 1, "visible": True}
o8_Text = {"container": o_QQuickView, "text": 8, "type": "Text", "unnamed": 1, "visible": True}
window_Rectangle = {"container": o_QQuickView, "id": "window", "type": "Rectangle", "unnamed": 1, "visible": True}
o_Text = {"container": o_QQuickView, "text": "×", "type": "Text", "unnamed": 1, "visible": True}
o5_Text = {"container": o_QQuickView, "text": 5, "type": "Text", "unnamed": 1, "visible": True}
o6_Text = {"container": o_QQuickView, "text": 6, "type": "Text", "unnamed": 1, "visible": True}
o7_Text = {"container": o_QQuickView, "text": 7, "type": "Text", "unnamed": 1, "visible": True}
o2_Text = {"container": o_QQuickView, "text": 2, "type": "Text", "unnamed": 1, "visible": True}
o3_Text = {"container": o_QQuickView, "text": 3, "type": "Text", "unnamed": 1, "visible": True}
o_Text_2 = {"container": o_QQuickView, "text": "=", "type": "Text", "unnamed": 1, "visible": True}
o_Text_3 = {"container": o_QQuickView, "text": "+", "type": "Text", "unnamed": 1, "visible": True}
listView_ListView = {"container": o_QQuickView, "id": "listView", "type": "ListView", "unnamed": 1, "visible": True}
listView_Item = {"container": listView_ListView, "index": 2, "type": "Item", "unnamed": 1, "visible": True}
o4_Text = {"container": listView_Item, "text": 4, "type": "Text", "unnamed": 1, "visible": True}
o9_Text = {"container": o_QQuickView, "text": 9, "type": "Text", "unnamed": 1, "visible": True}
o63_Text = {"container": listView_Item, "text": 63, "type": "Text", "unnamed": 1, "visible": True}
address_Book_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow, "windowTitle": "File"}
address_Book_File_QTableWidget = {"aboveWidget": address_Book_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
file_QHeaderView = {"container": address_Book_File_QTableWidget, "orientation": 1, "type": "QHeaderView", "unnamed": 1, "visible": 1}
forename_HeaderViewItem = {"container": file_QHeaderView, "text": "Forename", "type": "HeaderViewItem", "visible": True}
surname_HeaderViewItem = {"container": file_QHeaderView, "text": "Surname", "type": "HeaderViewItem", "visible": True}
address_Book_QMenuBar = {"type": "QMenuBar", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
address_Book_File_QMenu = {"title": "File", "type": "QMenu", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
address_Book_Unnamed_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Unnamed"}
address_Book_Unnamed_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
address_Book_Add_Dialog = {"type": "Dialog", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Add"}
address_Book_Add_Forename_QLabel = {"text": "Forename:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
forename_LineEdit = {"buddy": address_Book_Add_Forename_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Surname_QLabel = {"text": "Surname:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
surname_LineEdit = {"buddy": address_Book_Add_Surname_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Email_QLabel = {"text": "Email:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
email_LineEdit = {"buddy": address_Book_Add_Email_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Phone_QLabel = {"text": "Phone:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
phone_LineEdit = {"buddy": address_Book_Add_Phone_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
address_Book_Unnamed_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow, "windowTitle": "File"}
address_Book_Unnamed_File_QTableWidget = {"aboveWidget": address_Book_Unnamed_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
o4_Text_2 = {"container": o_QQuickView, "text": 4, "type": "Text", "unnamed": 1, "visible": True}
