import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QImage, QPainter, QPen, QColor, QPolygon, QPalette, QFont
from PyQt6.QtCore import Qt, QPoint, QEvent
from auc_ui import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.area_label = QLabel()
        self.area_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.area_label.setStyleSheet("color: red;")
        font = QFont("Arial", 12)  # Adjust the font size as desired
        self.area_label.setFont(font)
        self.layout.addWidget(self.area_label)

        self.total_area = 0.0
        self.iteration_count = 0  # Add the iteration_count attribute here
        self.line_count = 0
        self.points = []
        self.brushColor = Qt.GlobalColor.black
        self.brushSize = 3

        self.update_label_text()

        self.ui.placeholder_label.deleteLater()  # Remove the placeholder label


    def resizeEvent(self, event):
        self.resize_label()
        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        self.image.fill(Qt.GlobalColor.white)
        super().resizeEvent(event)

    def resize_label(self):
        self.area_label.setFixedHeight(30)

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange and self.windowState() == Qt.WindowState.WindowNoState:
            self.image = QImage(self.size(), QImage.Format.Format_RGB32)
            self.image.fill(Qt.GlobalColor.white)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.lastPoint = event.position()
            self.points.append(event.position())

    def mouseMoveEvent(self, event):
        if (event.buttons() and Qt.MouseButton.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.PenStyle.SolidLine))
            painter.drawLine(self.lastPoint, event.position())
            self.lastPoint = event.position()
            self.points.append(event.position())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
            if len(self.points) > 1:
                area = self.calculate_area()
                self.highlight_area(area)  # Highlight the area under the curve

                self.write_data_to_file(area)
                self.line_count += 1

                # Calculate and update current area and total area
                current_area = abs(area)
                self.total_area += current_area

                self.iteration_count += 1
                self.update_label_text()  # Update label text after each iteration

        self.points.clear()

        # Force the application to update the label immediately
        QApplication.processEvents()


    def update_label_text(self):
        if self.total_area != 0.0:
            label_text = f'Iteration(s): {self.iteration_count}, Current Area: {self.total_area:.2f} sq px, Total Area: {self.total_area:.2f} sq px'
            self.area_label.setText(label_text)

            palette = self.area_label.palette()
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.red)
            self.area_label.setPalette(palette)

            self.area_label.setVisible(True)  # Set the label visibility to True
        else:
            self.area_label.setVisible(False)  # Set the label visibility to False

        self.resize_label()

    def calculate_area(self):
        area = 0.0
        n = len(self.points)
        for i in range(n - 1):
            x0, y0 = self.points[i].x(), self.points[i].y()
            x1, y1 = self.points[i + 1].x(), self.points[i + 1].y()

            # Ignore lines above the x-axis
            if y0 > 0 and y1 > 0:
                continue

            # Handle direction of the line
            if y1 > y0:
                y0 = max(y0, 0)
            else:
                y1 = max(y1, 0)

            dx = x1 - x0
            dy = y1 - y0
            trapezoid_area = abs(0.5 * (y0 + y1) * dx)
            area += trapezoid_area - min(y0, y1) * dx

        return area

    def highlight_area(self, area):
        self.area = abs(area)

        painter = QPainter(self.image)
        painter.setPen(Qt.PenStyle.NoPen)  # No outline pen

        brush_color = QColor(255, 0, 0, 100)  # Set the color and transparency for highlighting (red with 100 alpha)
        painter.setBrush(brush_color)

        # Convert QPointF objects to QPoint objects
        points = [QPoint(round(point.x()), round(point.y())) for point in self.points]

        polygon = QPolygon(points)
        painter.drawPolygon(polygon)  # Draw the highlighted area directly on the original image

        painter.end()

        self.update()  # Update the image

    def write_data_to_file(self, area):
        current_area = abs(area)
        self.total_area += current_area

        with open("drawing_data.txt", "a") as file:
            file.write(
                f"Iteration {self.line_count} --> Current Area: {current_area}, Total Area: {self.total_area}\n")

    def closeEvent(self, event):
        self.write_data_to_file(self.calculate_area())  # Write the final area to the file
        super().closeEvent(event)

    def clear_image(self):
        self.image.fill(Qt.GlobalColor.white)
        self.update()
