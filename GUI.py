#PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel , QWidget , QVBoxLayout , QHBoxLayout , QGridLayout , QPushButton , QCheckBox , QRadioButton , QButtonGroup , QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(700, 300, 1000, 700)
        #self.checkbox = QCheckBox("Do you Like Food?" , self)
        #self.button = QPushButton("Click Me!" , self)
        #self.label = QLabel("Hello",self)
        #self.line_edit = QLineEdit(self)
        #self.button = QPushButton("Submit" , self)
        

        #self.radio1 = QRadioButton("Visa" , self)
        #self.radio2 = QRadioButton("Master Card" , self)
        #self.radio3 = QRadioButton("In-Store" , self)
        #self.radio4 = QRadioButton("Online" , self)
        #self.button_group1 = QButtonGroup(self)
        #self.button_group2 = QButtonGroup(self)

        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()


     #   self.setWindowIcon(QIcon("bmwgt.jpg"))

     #  label = QLabel("Hello, PyQt5!", self)
     #   label.setFont(QFont("Arial", 20))
     #   label.setGeometry(0, 0, 1280, 720)
      #  label.setStyleSheet("color: orange;" "background-color: cyan;" "font-weight: bold;" "font-style: italic;" "border: 2px solid orange;" "border-radius: 10px;")
        #label.setAlignment(Qt.AlignTop) #Vertically Top
        #label.setAlignment(Qt.AlignBottom) #Vertically Bottom
        #label.setAlignment(Qt.AlignVRight) #Vertically Right
        #label.setAlignment(Qt.AlignVLeft) #Vertically Left
      #  label.setAlignment(Qt.AlignVCenter) #Vertically Center
        #label.setAlignment(Qt.AlignHCenter)#Horizontally Center
        #label.setAlignment(Qt.AlignHTop) #Horizontally Top
        #label.setAlignment(Qt.AlignHBottom) #Horizontally Bottom
        #label.setAlignment(Qt.AlignHRight) #Horizontally Right
        #label.setAlignment(Qt.AlignHLeft) #Horizontally Left
        
     #   pixmap = QPixmap("bmwgt.jpg")
     #   label.setPixmap(pixmap)

    #    label.setScaledContents(True)

        #label.setGeometry()



    def initUI(self):
        #central_widget = QWidget()
        #self.setCentralWidget(central_widget)

        #label1 = QLabel("#1" , self)
        #label2 = QLabel("#2" , self)
        #label3 = QLabel("#3" , self)
        #label4 = QLabel("#4" , self)
        #label5 = QLabel("#5" , self)

        #label1.setStyleSheet("background-color: red")
        #label2.setStyleSheet("background-color: blue")
        #label3.setStyleSheet("background-color: yellow")
        #label4.setStyleSheet("background-color: orange")
        #label5.setStyleSheet("background-color: cyan")

        #vbox = QVBoxLayout()                      #for Horizontal use QHBoxLayout instead of QVBoxLayout

        #vbox.addWidget(label1)                    #for Horizontal replace hbox instead of vbox
        #vbox.addWidget(label2)
        #vbox.addWidget(label3)
        #vbox.addWidget(label4)
        #vbox.addWidget(label5)

        #central_widget.setLayout(vbox)

        #self.button.setGeometry(350 , 200 , 200 , 100)
        #self.button.setStyleSheet("font-size: 30px;")
        #self.button.clicked.connect(self.on_click)

        #self.label.setGeometry(100 , 200 , 200 , 200)
        #self.label.setStyleSheet("font-size: 40px;")

        #self.radio1.setGeometry(0 , 0 , 300 , 50)
        #self.radio2.setGeometry(0 , 50 , 300 , 100)
        #self.radio3.setGeometry(0 , 100 , 300 , 150)
        #self.radio4.setGeometry(0 , 150 , 300 , 200)

        #self.setStyleSheet("QRadioButton{"
        #                   "font-size: 40px;" 
        #                   "font-family: Arial;" 
        #                   "padding: 10px;"
        #                   "}")
        
        #self.button_group1.addButton(self.radio1)
        #self.button_group1.addButton(self.radio2)
        #self.button_group2.addButton(self.radio3)
        #self.button_group2.addButton(self.radio4)

        #self.radio1.toggled.connect(self.radio_button_changed)
        #self.radio2.toggled.connect(self.radio_button_changed)
        #self.radio3.toggled.connect(self.radio_button_changed)
        #self.radio4.toggled.connect(self.radio_button_changed)

        #self.line_edit.setGeometry(10,10,200,40)
        #self.button.setGeometry(110,50,100,40)
        #self.line_edit.setStyleSheet("font-size: 25px;" "font-family: Arial")
        #self.button.setStyleSheet("font-size: 20px;" "font-family: Arial")
        #self.line_edit.setPlaceholderText("Enter Your Name")

        #self.button.clicked.connect(self.submit)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet(""" 
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: red;               
            }
            QPushButton#button2{
                background-color: yellow;               
            }
            QPushButton#button3{
                background-color: cyan;               
            }
            QPushButton#button1:hover{
                background-color: lightcoral;               
            }
            QPushButton#button2:hover{
                background-color: lemonchiffon;               
            }
            QPushButton#button3:hover{
                background-color: aquamarine;               
            }
        """)

    #def submit(self):
        #text = self.line_edit.text()
        #print(f"Hello {text}")                        

    #def radio_button_changed(self):
    #    radio_button = self.sender()
    #    if radio_button.isChecked():
    #        print(f"{radio_button.text()} is selected")

    #def on_click(self):
        #print("Button Clicked!")
        #self.button.setText("Clicked!")
        #self.button.setDisabled(True)

        #self.label.setText("Gooodbye")


        #self.checkbox.setGeometry(20 , 0 , 500 , 100)
        #self.checkbox.setStyleSheet("font-size: 30px;" "font-family: Arial;")

        #self.checkbox.setChecked(False)
        #self.checkbox.stateChanged.connect(self.checkbox_changed)

    #def checkbox_changed(self , state):
        #if state == Qt.Checked:
            #print("You Like Food")
        #else:
            #print("You do not like Food") 


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()