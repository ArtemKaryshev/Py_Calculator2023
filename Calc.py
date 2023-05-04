import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator


class Calc(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(420, 600)
        self.setWindowTitle('Калькулятор')
        self.setWindowIcon(QtGui.QIcon('./Calculator.png'))
        self.setStyleSheet('background-color: rgb(240, 255, 240)')
        self.main_layout = QVBoxLayout()

        self.setFocusPolicy(Qt.StrongFocus)
        self.line_input = QLineEdit('0')
        self.line_input.setStyleSheet('border-radius: 10px;'
                                      'background-color: rgb(250, 250, 210);'
                                      'board: 10px;'
                                      'border: 2px solid #094065;')
        self.line_input.setFixedSize(380, 70)
        self.line_input.setAlignment(Qt.AlignRight)
        self.line_input.setLayoutDirection(Qt.RightToLeft)
        self.line_input.returnPressed.connect(self.ravno)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.line_input.setFont(font)
        regex = QRegExp("[0-9+-/*()]*")
        validator = QRegExpValidator(regex, self.line_input)
        self.error = False
        self.ar_symbol = False
        self.but_error = False

        self.line_input.setValidator(validator)
        self.layout = QVBoxLayout()

        self.line1_layout = QHBoxLayout()
        self.line2_layout = QHBoxLayout()
        self.line3_layout = QHBoxLayout()
        self.line4_layout = QHBoxLayout()
        self.line5_layout = QHBoxLayout()

        self.b1 = QPushButton(self)
        self.b1.clicked.connect(self.sk_l)
        self.b1.setFixedSize(90, 90)
        self.b1.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b1.setText('(')

        self.b2 = QPushButton(self)
        self.b2.clicked.connect(self.sk_r)
        self.b2.setFixedSize(90, 90)
        self.b2.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b2.setText(')')

        self.b3 = QPushButton(self)
        self.b3.clicked.connect(self.cancel)
        self.b3.setFixedSize(90, 90)
        self.b3.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b3.setText('C')

        self.b4 = QPushButton(self)
        self.b4.clicked.connect(self.delete)
        self.b4.setFixedSize(90, 90)
        self.b4.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b4.setText('CE')

        self.b5 = QPushButton(self)
        self.b5.clicked.connect(self.seven)
        self.b5.setFixedSize(90, 90)
        self.b5.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b5.setText('7')

        self.b6 = QPushButton(self)
        self.b6.clicked.connect(self.eight)
        self.b6.setFixedSize(90, 90)
        self.b6.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b6.setText('8')

        self.b7 = QPushButton(self)
        self.b7.clicked.connect(self.nine)
        self.b7.setFixedSize(90, 90)
        self.b7.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b7.setText('9')

        self.b8 = QPushButton(self)
        self.b8.clicked.connect(self.pl)
        self.b8.setFixedSize(90, 90)
        self.b8.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b8.setText('+')

        self.b9 = QPushButton(self)
        self.b9.clicked.connect(self.four)
        self.b9.setFixedSize(90, 90)
        self.b9.setStyleSheet('border-radius: 10px;'
                              'font-size: 50px;'
                              'background-color: rgb(250, 250, 210);'
                              'board: 10px;'
                              'border: 2px solid #094065;')
        self.b9.setText('4')

        self.b10 = QPushButton(self)
        self.b10.clicked.connect(self.five)
        self.b10.setFixedSize(90, 90)
        self.b10.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b10.setText('5')

        self.b11 = QPushButton(self)
        self.b11.clicked.connect(self.six)
        self.b11.setFixedSize(90, 90)
        self.b11.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b11.setText('6')

        self.b12 = QPushButton(self)
        self.b12.clicked.connect(self.minus)
        self.b12.setFixedSize(90, 90)
        self.b12.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b12.setText('-')

        self.b13 = QPushButton(self)
        self.b13.clicked.connect(self.one)
        self.b13.setFixedSize(90, 90)
        self.b13.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b13.setText('1')

        self.b14 = QPushButton(self)
        self.b14.clicked.connect(self.two)
        self.b14.setFixedSize(90, 90)
        self.b14.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b14.setText('2')

        self.b15 = QPushButton(self)
        self.b15.clicked.connect(self.three)
        self.b15.setFixedSize(90, 90)
        self.b15.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b15.setText('3')

        self.b16 = QPushButton(self)
        self.b16.clicked.connect(self.umn)
        self.b16.setFixedSize(90, 90)
        self.b16.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b16.setText('*')

        self.b17 = QPushButton(self)
        self.b17.clicked.connect(self.toch)
        self.b17.setFixedSize(90, 90)
        self.b17.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b17.setText('.')

        self.b18 = QPushButton(self)
        self.b18.clicked.connect(self.zero)
        self.b18.setFixedSize(90, 90)
        self.b18.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b18.setText('0')

        self.b19 = QPushButton(self)
        self.b19.clicked.connect(self.ravno)
        self.b19.setFixedSize(90, 90)
        self.b19.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b19.setText('=')

        self.b20 = QPushButton(self)
        self.b20.clicked.connect(self.delit)
        self.b20.setFixedSize(90, 90)
        self.b20.setStyleSheet('border-radius: 10px;'
                               'font-size: 50px;'
                               'background-color: rgb(250, 250, 210);'
                               'board: 10px;'
                               'border: 2px solid #094065;')
        self.b20.setText('/')

        self.line1_layout.addStretch(1)
        self.line1_layout.addWidget(self.b1)
        self.line1_layout.addWidget(self.b2)
        self.line1_layout.addWidget(self.b3)
        self.line1_layout.addWidget(self.b4)
        self.line1_layout.addStretch(1)

        self.line2_layout.addStretch(1)
        self.line2_layout.addWidget(self.b5)
        self.line2_layout.addWidget(self.b6)
        self.line2_layout.addWidget(self.b7)
        self.line2_layout.addWidget(self.b8)
        self.line2_layout.addStretch(1)

        self.line3_layout.addStretch(1)
        self.line3_layout.addWidget(self.b9)
        self.line3_layout.addWidget(self.b10)
        self.line3_layout.addWidget(self.b11)
        self.line3_layout.addWidget(self.b12)
        self.line3_layout.addStretch(1)

        self.line4_layout.addStretch(1)
        self.line4_layout.addWidget(self.b13)
        self.line4_layout.addWidget(self.b14)
        self.line4_layout.addWidget(self.b15)
        self.line4_layout.addWidget(self.b16)
        self.line4_layout.addStretch(1)

        self.line5_layout.addStretch(1)
        self.line5_layout.addWidget(self.b17)
        self.line5_layout.addWidget(self.b18)
        self.line5_layout.addWidget(self.b19)
        self.line5_layout.addWidget(self.b20)
        self.line5_layout.addStretch(1)

        self.layout.addLayout(self.line1_layout)
        self.layout.addLayout(self.line2_layout)
        self.layout.addLayout(self.line3_layout)
        self.layout.addLayout(self.line4_layout)
        self.layout.addLayout(self.line5_layout)
        self.main_layout.addWidget(self.line_input, alignment=Qt.AlignCenter)
        self.main_layout.addLayout(self.layout)

        self.setLayout(self.main_layout)

        self.show()

    def one(self):
        if self.line_input.text() == '0':
            self.line_input.setText('1')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '1')
        else:
            self.line_input.setText('1')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def two(self):
        if self.line_input.text() == '0':
            self.line_input.setText('2')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '2')
        else:
            self.line_input.setText('2')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def three(self):
        if self.line_input.text() == '0':
            self.line_input.setText('3')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '3')
        else:
            self.line_input.setText('3')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def four(self):
        if self.line_input.text() == '0':
            self.line_input.setText('4')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '4')
        else:
            self.line_input.setText('4')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def five(self):
        if self.line_input.text() == '0':
            self.line_input.setText('5')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '5')
        else:
            self.line_input.setText('5')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def six(self):
        if self.line_input.text() == '0':
            self.line_input.setText('6')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '6')
        else:
            self.line_input.setText('6')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def seven(self):
        if self.line_input.text() == '0':
            self.line_input.setText('7')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '7')
        else:
            self.line_input.setText('7')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def eight(self):
        if self.line_input.text() == '0':
            self.line_input.setText('8')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '8')
        else:
            self.line_input.setText('8')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def nine(self):
        if self.line_input.text() == '0':
            self.line_input.setText('9')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '9')
        else:
            self.line_input.setText('9')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def zero(self):
        if self.line_input.text() == '0':
            self.line_input.setText('0')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '0')
        else:
            self.line_input.setText('0')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def sk_l(self):
        if self.line_input.text() == '0':
            self.line_input.setText('(')
        elif self.line_input.text() != 'Ошибка':
            self.line_input.setText(self.line_input.text() + '(')
        else:
            self.line_input.setText('(')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def sk_r(self):
        if self.line_input.text() == '0':
            self.line_input.setText(self.line_input.text())
        elif self.line_input.text() != 'Ошибка':
            if str(self.line_input.text()).count('(') != 0 and str(self.line_input.text()).count('(') > str(
                    self.line_input.text()).count(')'):
                self.line_input.setText(self.line_input.text() + ')')
            else:
                self.line_input.setText(self.line_input.text())
        else:
            self.line_input.setText(self.line_input.text())
        self.ar_symbol = False

    def cancel(self):
        self.line_input.setText('')
        if self.line_input.text() == '':
            self.line_input.setText('0')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def delete(self):
        text = self.line_input.text()
        self.line_input.setText(text[:-1])
        if text == '':
            self.line_input.setText('0')
        elif text != 'Ошибка':
            self.line_input.setText(text[:-1])
        else:
            self.line_input.setText('0')
        self.ar_symbol = False
        if self.line_input.text() != 'Ошибка':
            self.not_error()

    def pl(self):
        if not self.ar_symbol:
            if self.line_input.text() != 'Ошибка':
                self.line_input.setText(self.line_input.text() + '+')
                self.ar_symbol = True
            else:
                self.line_input.setText(self.line_input.text())

    def minus(self):
        if not self.ar_symbol:
            if self.line_input.text() != 'Ошибка':
                self.line_input.setText(self.line_input.text() + '-')
                self.ar_symbol = True
            else:
                self.line_input.setText(self.line_input.text())

    def umn(self):
        if not self.ar_symbol:
            if self.line_input.text() != 'Ошибка':
                self.line_input.setText(self.line_input.text() + '*')
                self.ar_symbol = True
            else:
                self.line_input.setText(self.line_input.text())

    def delit(self):
        if not self.ar_symbol:
            if self.line_input.text() != 'Ошибка':
                self.line_input.setText(self.line_input.text() + '/')
                self.ar_symbol = True
            else:
                self.line_input.setText(self.line_input.text())

    def toch(self):
        if not self.ar_symbol:
            if self.line_input.text() != 'Ошибка':
                self.line_input.setText(self.line_input.text() + '.')
                self.ar_symbol = True
            else:
                self.line_input.setText(self.line_input.text())

    def ravno(self):
        if self.line_input.text() == '':
            self.line_input.setText('0')
        try:
            s = str(self.line_input.text()).split('+')
            mas1 = []
            mas2 = []
            mas3 = []
            mas4 = []
            mas5 = []
            for item in s:
                mas1.extend(item.split('-'))
            for item in mas1:
                mas2.extend(item.split('*'))
            for item in mas2:
                mas3.extend(item.split('/'))
            for item in mas3:
                mas4.extend(item.split('('))
            for item in mas4:
                mas5.extend(item.split(')'))
            point_count = 0
            for item in mas5:
                if '.' in item:
                    num_digits = len(item.split('.')[-1])
                    point_count = max(point_count, num_digits)

            result = round(eval(self.line_input.text()), point_count)
            self.line_input.setText(str(result))
            self.error = False
        except:
            self.line_input.setText('Ошибка')
            self.error = True
        self.ar_symbol = False
        if self.line_input.text() == 'Ошибка':
            if not self.but_error:
                self.but_error = True
                self.b2.setStyleSheet('border-radius: 10px;'
                                      'font-size: 50px;'
                                      'background-color: rgb(255, 255, 245);'
                                      'board: 10px;'
                                      'border: 2px solid #094065;')
                self.b8.setStyleSheet('border-radius: 10px;'
                                      'font-size: 50px;'
                                      'background-color: rgb(255, 255, 245);'
                                      'board: 10px;'
                                      'border: 2px solid #094065;')
                self.b12.setStyleSheet('border-radius: 10px;'
                                       'font-size: 50px;'
                                       'background-color: rgb(255, 255, 245);'
                                       'board: 10px;'
                                       'border: 2px solid #094065;')
                self.b16.setStyleSheet('border-radius: 10px;'
                                       'font-size: 50px;'
                                       'background-color: rgb(255, 255, 245);'
                                       'board: 10px;'
                                       'border: 2px solid #094065;')
                self.b17.setStyleSheet('border-radius: 10px;'
                                       'font-size: 50px;'
                                       'background-color: rgb(255, 255, 245);'
                                       'board: 10px;'
                                       'border: 2px solid #094065;')
                self.b19.setStyleSheet('border-radius: 10px;'
                                       'font-size: 50px;'
                                       'background-color: rgb(255, 255, 245);'
                                       'board: 10px;'
                                       'border: 2px solid #094065;')
                self.b20.setStyleSheet('border-radius: 10px;'
                                       'font-size: 50px;'
                                       'background-color: rgb(255, 255, 245);'
                                       'board: 10px;'
                                       'border: 2px solid #094065;')
            self.but_error = False

    def not_error(self):
        if not self.but_error:
            self.b2.setStyleSheet('border-radius: 10px;'
                                  'font-size: 50px;'
                                  'background-color: rgb(250, 250, 210);'
                                  'board: 10px;'
                                  'border: 2px solid #094065;')
            self.b8.setStyleSheet('border-radius: 10px;'
                                  'font-size: 50px;'
                                  'background-color: rgb(250, 250, 210);'
                                  'board: 10px;'
                                  'border: 2px solid #094065;')
            self.b12.setStyleSheet('border-radius: 10px;'
                                   'font-size: 50px;'
                                   'background-color: rgb(250, 250, 210);'
                                   'board: 10px;'
                                   'border: 2px solid #094065;')
            self.b16.setStyleSheet('border-radius: 10px;'
                                   'font-size: 50px;'
                                   'background-color: rgb(250, 250, 210);'
                                   'board: 10px;'
                                   'border: 2px solid #094065;')
            self.b17.setStyleSheet('border-radius: 10px;'
                                   'font-size: 50px;'
                                   'background-color: rgb(250, 250, 210);'
                                   'board: 10px;'
                                   'border: 2px solid #094065;')
            self.b19.setStyleSheet('border-radius: 10px;'
                                   'font-size: 50px;'
                                   'background-color: rgb(250, 250, 210);'
                                   'board: 10px;'
                                   'border: 2px solid #094065;')
            self.b20.setStyleSheet('border-radius: 10px;'
                                   'font-size: 50px;'
                                   'background-color: rgb(250, 250, 210);'
                                   'board: 10px;'
                                   'border: 2px solid #094065;')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.ravno()
            if self.error:
                self.error = False
                self.line_input.setText('0')
        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Calc()
    sys.exit(app.exec())
