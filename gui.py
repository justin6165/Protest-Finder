from scrapping import generate_protests_list
from notice_dialog import *
from set_home_dialog import *
from helper import *
import create_posts
import user_data
import sys


class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.set_window()  # Set window title, max size, etc
        self.tool_bar()

        self.top_layout = QHBoxLayout()  # This is the top level layout of the entire application
        self.results_layout = QVBoxLayout()  # Layout that will hold all of the search results, i.e. the posts
        self.save_layout = QVBoxLayout()

        self.tabs = QTabWidget()

        self.results_scroll = QScrollArea()  # Scrollable area where the search results are displayed
        self.save_scroll = QScrollArea()
        self.set_scrollable(self.results_scroll)  # Set scrollable attributes
        self.set_scrollable(self.save_scroll)

        self.main_layout()  # Create main layout of app

        self.search_layout()  # Layout for searching area (left portion of app)
        self.search_results_layout()  # Set up the search results layout
        self.save_results_layout()

        self.create_tabs()
        self.load_saves(self.save_layout)

    def set_window(self):
        self.setWindowTitle("Protest Finder")
        self.setMinimumWidth(800)
        self.setMinimumHeight(800)

    def set_scrollable(self, scroll):
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setWidgetResizable(True)

    def main_layout(self):
        widget = QWidget()  # Central widget of the app
        widget.setLayout(self.top_layout)  # Widget is a container for the top level layout

        self.setCentralWidget(widget)  # Display widget as central widget to be displayed

    def tool_bar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        set_home = QPushButton("Set Home Address")
        set_home.clicked.connect(lambda: self.set_home())
        toolbar.addWidget(set_home)

    def set_home(self):
        SetHomeDialog()

    def search_layout(self):
        search_layout = QFormLayout()

        home_address = QLabel(user_data.get_home_address())
        search_layout.addRow(home_address)

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
            lambda: self.generate_search_results(state.text() + ", " + city.text()))  # Pass in data entered in state line edit

        self.top_layout.addLayout(search_layout, 1)  # Add new layout to top lvl layout

    def search_results_layout(self):
        label = QLabel("Nothing to see here yet")
        label.setFont(QFont("Arial", 18))

        self.results_layout.addWidget(label)  # Initial display when there are no search results yet
        self.results_layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(self.results_layout)  # Widget is a container for the results layout

        self.results_scroll.setWidget(widget)  # Everything in results_layout is placed inside the scrolling area
        # self.top_layout.addWidget(self.results_scroll, 3)  # Scrolling area is added to top level layout

    def save_results_layout(self):
        label = QLabel("You don't have any saved protests")
        label.setFont(QFont("Arial", 18))

        self.save_layout.addWidget(label)  # Initial display when there are no search results yet
        self.save_layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(self.save_layout)  # Widget is a container for the results layout

        self.save_scroll.setWidget(widget)

    def generate_search_results(self, location):
        postings = generate_protests_list(location)  # Web Scraping function that grabs posting information

        if len(postings) == 0:
            delete_widgets(self.results_layout)

            txt = "We couldn't find any scheduled protests in " + location + "."
            label = QLabel(txt)
            label.setFont(QFont("Arial", 16))

            self.results_layout.addWidget(label)
            self.results_layout.setAlignment(Qt.AlignCenter)
        else:
            Window.display_protests(postings, True, self.results_layout, self.save_layout)

    @staticmethod
    def display_protests(protest_list, saving, layout, save_layout):
        delete_widgets(layout)  # Remove any posts in search results when generating new results
        for post in protest_list:
            post_box = create_posts.create_post_layout(post, saving, save_layout)  # Create a layout for each post

            layout.setAlignment(Qt.AlignLeft)  # Align search results to upper left, not middle like initially set
            layout.addWidget(post_box)  # Add that layout to the results_layout

    def create_tabs(self):
        search_tab = QWidget()
        saves_tab = QWidget()

        self.tabs.addTab(search_tab, "Search")
        self.tabs.addTab(saves_tab, "Saves")

        search_tab_layout = QVBoxLayout()
        search_tab_layout.addWidget(self.results_scroll)
        search_tab.setLayout(search_tab_layout)

        saves_tab_layout = QVBoxLayout()
        saves_tab_layout.addWidget(self.save_scroll)
        saves_tab.setLayout(saves_tab_layout)

        self.top_layout.addWidget(self.tabs, 3)

    @staticmethod
    def load_saves(save_layout):
        protest_list = user_data.get_saved_protest_list()
        print(protest_list)

        if protest_list:
            Window.display_protests(protest_list, False, save_layout, save_layout)
        else:
            delete_widgets(save_layout)
            save_layout.setAlignment(Qt.AlignCenter)

            label = QLabel("You don't have any saved protests")
            label.setFont(QFont("Arial", 16))
            save_layout.addWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())