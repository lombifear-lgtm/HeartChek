from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *
     
class MainWin(QWidget):
   def __init__(self):'
       super().__init__()
       self.intUI()
       self.connects()
       self.set_appear()
       self.show()


   def initUI(self):
       self.btn_next = QPushButton(txt_next, self)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)
       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout_line)
  
   def next_click(self):
       self.tw = TestWin()
       self.hide()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)
   
   def set_appear(self):
       self.setWidowTitle(txt_title)
       self.resize(win_wtdth, win_height)
       self.move(win_x, win_y)

class Testwin(QWidget):
    def timer1Event(Self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(Time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 3d, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        time = Qtime(0,0, 30)
        self.time.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer2Event(self):
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])

    def Timer3Event(self):
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(125,0,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,100,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,70)")

    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)


        
app = QApplication([])
mw = MainWin()
app.exec_()
