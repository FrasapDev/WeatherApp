import sys
import os

import requests

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)

from dotenv import load_dotenv, dotenv_values

from PyQt5.QtCore import Qt

load_dotenv()

print(os.getenv("WEATHER_APIKEY"))

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()


def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()