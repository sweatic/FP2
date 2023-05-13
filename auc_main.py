import sys
from PyQt6.QtCore import Qt, QPoint, QEvent
from PyQt6.QtGui import QPainter, QImage, QPen
from PyQt6.QtWidgets import QMainWindow, QApplication

from auc_ui import Ui_MainWindow
from auc_controller import Window  # Add this line

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


