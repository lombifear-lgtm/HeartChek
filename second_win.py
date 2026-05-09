from final_win import Final_win

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.conects()
        self.set_appear()
        self.show()

        def set_appear(self):
            self.setWindowTitle(txt_title)
            self.resize(win_width, win_height)
            self.move(win_x, win_y)

        def initUI(self):
            self.btn_next = QPushButton(txt_sendresuls, self)
            self.btn_test1 = QPushButton(txt_starttest1, self)
            self.btn_test2 = QPushButton(txt_starttest2, self)
            self.btn_test3 = QPushButton(txt_starttest3, self)


        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)



        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QVBoxLayout()

        self.l_line.addWidget(self.text_name,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3,alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next,alignment = Qt.AlignLeft)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_bob)
        self.btn_test3.clicked.connect(self.timer_final)
        self.btn_next.clicked.connect(self.next_click)



        def timer_test1(self):
            self.time = QTime(0,0,15)
            self.timer.timeout.connect(self.timer1Event)
            self.timer.start(1000)

        def timer1Event(self):
            self.time = self.time.addSecs(-1)
            self.text_timer.setText(self.time.toString("hh:mm:ss"))
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
            if self.time.toSpring("hh:mm:ss") == "00:00:00":
                self.timer.stop()
                self.timer.timeout.disconnect()

            
        def timer_test2(self):
            self.time = QTime(0,0,30)
            self.timer.timeout.connect(self.timer2Event)
            self.timer.start(1500)

        def timer2Event(self):
            self.time = self.time.addSecs(-1)
            self.text_timer.setText(self.time.toString("hh:mm:ss")[6:8])
            if self.time.toSpring("hh:mm:ss") == "00:00:00":
                self.timer.stop()
                self.timer.timeout.disconnect()


        def timer_test3(self):
            self.time = QTime(0,12,0)
            self.timer.timeout.connect(self.timer3Event)
            self.timer.start(1000)

        def timer3Event(self):
            self.time = self.time.addSecs(-1)
            curr_t = self.time.toString("hh:mm:ss")
            self.text_timer.setText(curr_t)

            if curr_t >= "00:00:45" or curr_t <= "00:00:15":
                self.text_timer.setStyleSheet("color: rgb)(0,255,0")
            else:
                self.text_timer.setStyleSheet("color: rgb)(0,0,0")

            if curr_t == '00:00:00'
                self.timer.stop()

        def next_click(self):
            self.hide()

            self.exp = Experiment(
                int(self.line_age.text()),
                self.line_test1.text()
                self.line_test2.text()
                self.line_test3.text()
            )
            self.fw = FinalWin(self.exp)
            
