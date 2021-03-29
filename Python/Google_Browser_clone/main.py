#importing the modules
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Creating a navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Creating a back button inside the navbar
        button_previous = QAction('<-', self)
        button_previous.triggered.connect(self.browser.back)
        navbar.addAction(button_previous)

        # Creating a next button inside the navbar
        button_next = QAction('->', self)
        button_next.triggered.connect(self.browser.forward)
        navbar.addAction(button_next)

        # Creating a Refresh button
        refresh_button = QAction('Refresh', self)
        refresh_button.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_button)

        # Creating a Home button
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.home)
        navbar.addAction(home_button)

        # Adding a url typing arena
        self.url_editor = QLineEdit()
        self.url_editor.returnPressed.connect(self.go_to_url)
        navbar.addWidget(self.url_editor)

        self.browser.urlChanged.connect(self.updated_url)

    # function to add home button
    def home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    # function to visit directly to the specified URL
    def go_to_url(self):
        url = self.url_editor.text()
        self.browser.setUrl(QUrl(url))

    # function To update the url
    def updated_url(self, url):
        self.url_editor.setText(url.toString())

# Testing the program

application = QApplication(sys.argv)
QApplication.setApplicationName("Google Chrome")
window = Window()
application.exec_()
