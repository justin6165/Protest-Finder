from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

import urllib


def delete_widgets(layout):
    """
    Removes all widgets and layouts in param layout
    :param layout: A PyQt5 layout; may contain widgets, layouts, or a combination of both
    :return: No return; eliminates all widgets and layouts in param layout
    """
    for i in reversed(range(layout.count())):  # Loop through all objects in layout

        is_widget = isinstance(layout.itemAt(i), QWidgetItem)  # If object is a widget, remove it
        if is_widget:
            layout.itemAt(i).widget().setParent(None)
        else:
            delete_widgets(layout.itemAt(i))  # If object is not a widget, assume it's a layout and call delete_widgets


def get_img(url):
    """
    :param url: url of a given any image online
    :return: A pixmap to be used in a QPixMap object
    """
    data = urllib.request.urlopen(url).read()

    img = QImage()
    img.loadFromData(data)

    return img