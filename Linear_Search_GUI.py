import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class LinearSearchGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Linear Search GUI")
        self.setGeometry(700, 300, 1000, 700)

        self.arr = [10, 83, 13, 92, 27, 31, 54, 44]  #Fixed Array

        self.current = 0
        self.search_key = None
        self.found = False

        self.initUI()        
        
    def initUI(self):

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter number to search")
        self.input.setStyleSheet("font-size:16px;")

        self.stepButton = QPushButton("Next Step")
        self.stepButton.setStyleSheet("font-size:16px;")
        self.stepButton.clicked.connect(self.nextStep)

        self.resetButton = QPushButton("Reset")
        self.resetButton.setStyleSheet("font-size:16px;")
        self.resetButton.clicked.connect(self.reset)

        self.status = QLabel("NOTE: Enter a number and click Next Step")
        self.status.setFont(QFont("Arial",12))

        h = QHBoxLayout()
        h.addWidget(self.input)
        h.addWidget(self.stepButton)
        h.addWidget(self.resetButton)

        layout = QVBoxLayout()
        layout.addLayout(h)
        layout.addSpacing(20)
        layout.addWidget(self.status, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def reset(self):
        self.current = 0
        self.search_key = None
        self.found = False
        self.input.clear()
        self.status.setText("Enter a number and click Next Step")
        self.update()

    def nextStep(self):

        if self.search_key is None:
            try:
                self.search_key = int(self.input.text())
            except ValueError:
                self.status.setText("Please enter a valid integer.")
                return
            
        if self.found:
            return
        
        if self.current >= len(self.arr):
            self.status.setText("Element Not Found")
            return
        
        if self.arr[self.current] == self.search_key:
            self.found = True
            self.status.setText(f"Element Found at Index {self.current}")
        else:
            self.current += 1

            if self.current == len(self.arr):
                self.status.setText("Element Not Found")
        
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setFont(QFont("Arial", 12, QFont.Bold))

        startX = 40
        y = 120
        w = 70
        h = 50

        for i, value in enumerate(self.arr):

            color = QColor("white")

            if i < self.current:
                color = QColor("lightgray")

            if i == self.current and not self.found:
                color = QColor("yellow")

            if self.found and i == self.current:
                color = QColor("lightgreen")

            painter.setBrush(color)
            painter.drawRect(startX + i * 80, y, w, h)

            painter.drawText(
                startX + i * 80,
                y,
                w,
                h,
                Qt.AlignCenter,
                str(value),
            )

            painter.drawText(
                startX + i * 80 + 25,
                y + 70,
                str(i),
            )


app = QApplication(sys.argv)

window = LinearSearchGUI()
window.show()

sys.exit(app.exec_())