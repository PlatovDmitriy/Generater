#подключение модулей
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout
from random import randint
#главное окно
app = QApplication([])
my_win = QWidget()
my_win.show()
#виджеты окна: кнопка и надписи
my_win.setWindowTitle('Латерея')
my_win.resize(400,400)
winner = QLabel('Нажми, чтобы участвовать')
num1 = QLabel('?')
num2 = QLabel('?')
button = QPushButton('испытать удачу!')
v_line = QVBoxLayout()
#расположение виджетов
v_line.addWidget(winner, alignment = Qt.AlignCenter)
v_line.addWidget(num1, alignment = Qt.AlignCenter)
v_line.addWidget(num2, alignment = Qt.AlignCenter)
v_line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(v_line)
#функция, которая генерирует и показывает числа
def show_winner():
    number1 = randint(0, 9)
    number2 = randint(0, 9)
    num1.setText(str(number1))
    num2.setText(str(number2))
    if number1 == number2 :
        winner.setText('Ты победил!')
    else :
        winner.setText('Ты проиграл!')
button.clicked.connect(show_winner)
#обработка нажатия на кнопку
app.exec()