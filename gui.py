from scrapping import generate_protests_list
# from notice_dialog import NoticeDialog
from create_posts import *
import sys

"""
1. search minnesota
2. get results
3. hit tab saved protests:
    1. whoosh
    2. original method of generating postings but pass in list of saved protests
"""

class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.set_window()  # Set window title, max size, etc
        self.top_layout = QHBoxLayout()  # This is the top level layout of the entire application
        self.results_layout = QVBoxLayout()  # Layout that will hold all of the search results, i.e. the posts
        self.results_scroll = QScrollArea()  # Scrollable area where the search results are displayed

        self.main_layout()  # Create main layout of app
        self.search_layout()  # Layout for searching area (left portion of app)
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

        """TEMPORARY, only here to test your code, Katie"""
        dummy = QPushButton("WOOSH!")
        search_layout.addWidget(dummy)
        dummy.pressed.connect(lambda: delete_widgets(self.results_layout))

        katie = QPushButton("Do ur thing Katie!")
        search_layout.addWidget(katie)
        # katie.pressed.connect(lambda:) your function goes here
        """TEMPORARY, only here to test your code, Katie"""

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
        postings = generate_protests_list(location)  # Web Scraping function that grabs posting information

        if len(postings) == 0:
            txt = "We couldn't find any scheduled protests in " + location + "."
            self.results_layout.addWidget(QLabel(txt))
        else:
            self.display_protests(postings)

    def display_protests(self, protest_list):
        for post in protest_list:
                post_box = create_post_layout(post)  # Create a layout for each post
                self.results_layout.setAlignment(Qt.AlignLeft)  # Align search results to upper left, not middle like initially set
                self.results_layout.addWidget(post_box)  # Add that layout to the results_layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())