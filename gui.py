from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from scraping import generate_protests_list
import urllib
import sys


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


def create_display_layout(img_link):
    pix = get_img(img_link)  # This is the image from each protest post
    pix = pix.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
    display = QLabel()
    display.setPixmap(QPixmap(pix))  # Setting a QLabel to display the image

    img_layout = QVBoxLayout()  # This layout will hold the image from each protest post
    img_layout.setAlignment(Qt.AlignLeft)
    img_layout.setContentsMargins(0, 0, 0, 0)
    img_layout.addWidget(display)  # Add in image to layout

    return img_layout


def create_title_layout(title):
    title_label = QLabel(title)
    title_label.setMaximumWidth(250)

    title_layout = QVBoxLayout()
    title_layout.addWidget(title_label)

    return title_layout


def create_info_layout(date, descrip):
    info_date = QLabel(date)
    info_date.setMaximumWidth(250)
    info_descrip = QLabel(descrip)
    info_descrip.setMaximumWidth(250)
    info_descrip.setWordWrap(True)

    info_layout = QVBoxLayout()  # Displays title, date, description, etc, in a vertical format
    info_layout.addWidget(info_date)
    info_layout.addWidget(info_descrip)

    return info_layout


def create_link_layout(link):
    link_label = QLabel(link)

    link_layout = QVBoxLayout()
    link_layout.addWidget(link_label)

    return link_layout


def create_post_layout(post):
    # title, date, descrip, link, img_link = post

    title_layout = create_title_layout(post.title)
    img_layout = create_display_layout(post.img)
    info_layout = create_info_layout(post.date, post.description)
    link_layout = create_link_layout(post.link)

    body_layout = QHBoxLayout()
    body_layout.addLayout(img_layout)
    body_layout.addLayout(info_layout)

    post_layout = QVBoxLayout()  # The entire layout post is the image layout with the info layout
    post_layout.addLayout(title_layout)
    post_layout.addLayout(body_layout)
    post_layout.addLayout(link_layout)

    post_box = QGroupBox()
    post_box.setContentsMargins(0,0,0,0)
    post_box.setLayout(post_layout)

    return post_box


class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.set_window()  # Set window title, max size, etc

        self.top_layout = QHBoxLayout()  # This is the top level layout of the entire application
        self.main_layout()  # Create main layout of app

        self.search_layout()  # Layout for searching area (left portion of app)

        self.results_layout = QVBoxLayout()  # Layout that will hold all of the search results, i.e. the posts
        # self.results_layout.setAlignment(Qt.AlignLeft)

        self.results_scroll = QScrollArea()  # Scrollable area where the search results are displayed
        self.set_scrollable()  # Set scrollable attributes

        self.search_results_layout()  # Set up the search results layout

    def set_window(self):
        self.setWindowTitle("Protest Finder")
        self.setMinimumWidth(800)
        self.setMinimumHeight(800)

    def set_scrollable(self):
        self.results_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.results_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.results_scroll.setWidgetResizable(True)

    def main_layout(self):
        widget = QWidget()  # Central widget of the app
        widget.setLayout(self.top_layout)  # Widget is a container for the top level layout

        self.setCentralWidget(widget)  # Display widget as central widget to be displayed

    def search_layout(self):
        search_layout = QFormLayout()

        city = QLineEdit()  # Field for user to enter in city
        city.setMaximumWidth(150)
        search_layout.addRow(QLabel("City:"), city)

        state = QLineEdit()  # Field for user to enter in state
        state.setMaximumWidth(150)
        search_layout.addRow(QLabel("State:"), state)

        search_btn = QPushButton("Search")  # Button to execute search
        search_btn.setMaximumWidth(150)
        search_layout.addWidget(search_btn)
        search_btn.pressed.connect(
            lambda: self.generate_search_results(state.text()))  # Pass in data entered in state line edit

        self.top_layout.addLayout(search_layout, 1)  # Add new layout to top lvl layout

    def search_results_layout(self):
        self.results_layout.addWidget(QLabel("Nothing to see here yet"))  # Initial display when there are no search results yet
        self.results_layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(self.results_layout)  # Widget is a container for the results layout

        self.results_scroll.setWidget(widget)  # Everything in results_layout is placed inside the scrolling area
        self.top_layout.addWidget(self.results_scroll, 3)  # Scrolling area is added to top level layout

    def generate_search_results(self, location):
        delete_widgets(self.results_layout)  # Remove any posts in search results when generating new results
        self.results_layout.setAlignment(Qt.AlignLeft)  # Align search results to upper left, not middle like initially set

        postings = generate_protests_list(location)  # Web Scraping function that grabs posting information
        for post in postings:
            post_box = create_post_layout(post)  # Create a layout for each post
            self.results_layout.addWidget(post_box)  # Add that layout to the results_layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())