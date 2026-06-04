import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

app = QApplication(sys.argv)
# ГЛАВНОЕ МЕНЮ
main_win = QMainWindow()
main_win.setWindowTitle("Слова из слова")
main_win.setFixedSize(500, 450)
main_win.setStyleSheet("background-color: #fff5e6;")
main_win.setWindowIcon(QIcon("images/word.png"))

central = QWidget()
main_win.setCentralWidget(central)

layout = QVBoxLayout(central)
layout.setAlignment(Qt.AlignCenter)
layout.setSpacing(40)

title = QLabel("СЛОВА ИЗ СЛОВА")
title.setFont(QFont("Arial", 24, QFont.Bold))
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("color: #ffb7b2;")
layout.addWidget(title)

h_layout1 = QHBoxLayout()
h_layout1.setAlignment(Qt.AlignCenter)
play_btn = QPushButton("ИГРАТЬ")
play_btn.setFixedSize(250, 60)
play_btn.setFont(QFont("Arial", 16, QFont.Bold))
play_btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
h_layout1.addWidget(play_btn)
layout.addLayout(h_layout1)

h_layout2 = QHBoxLayout()
h_layout2.setAlignment(Qt.AlignCenter)
exit_btn = QPushButton("ВЫХОД")
exit_btn.setFixedSize(200, 50)
exit_btn.setFont(QFont("Arial", 14))
exit_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
h_layout2.addWidget(exit_btn)
layout.addLayout(h_layout2)

# ОКНО ВЫБОРА УРОВНЕЙ
levels_win = QMainWindow()
levels_win.setWindowTitle("Слова из слова - Выбор уровня")
levels_win.setFixedSize(500, 450)
levels_win.setStyleSheet("background-color: #fff5e6;")

central2 = QWidget()
levels_win.setCentralWidget(central2)

# Главный вертикальный layout для окна уровней
main_layout = QVBoxLayout(central2)
main_layout.setContentsMargins(20, 20, 20, 20)
# верхняя панель
top_layout = QHBoxLayout()
back_btn = QPushButton("НАЗАД")
back_btn.setFixedSize(90, 30)
back_btn.setFont(QFont("Arial", 10, QFont.Bold))
back_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 15px;")
top_layout.addWidget(back_btn)
top_layout.addStretch()
main_layout.addLayout(top_layout)
# центральная часть
center_layout = QVBoxLayout()
center_layout.setAlignment(Qt.AlignCenter)
center_layout.setSpacing(50)

title2 = QLabel("ВЫБЕРИ УРОВЕНЬ")
title2.setFont(QFont("Arial", 24, QFont.Bold))
title2.setAlignment(Qt.AlignCenter)
title2.setStyleSheet("color: #ffb7b2;")
center_layout.addWidget(title2)
# расположение в ряд
grid = QGridLayout()
grid.setSpacing(30)
grid.setAlignment(Qt.AlignCenter)

btn1 = QPushButton("1")
btn1.setFixedSize(100, 100)
btn1.setFont(QFont("Arial", 32, QFont.Bold))
btn1.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 50px;")

btn2 = QPushButton("2")
btn2.setFixedSize(100, 100)
btn2.setFont(QFont("Arial", 32, QFont.Bold))
btn2.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 50px;")

btn3 = QPushButton("3")
btn3.setFixedSize(100, 100)
btn3.setFont(QFont("Arial", 32, QFont.Bold))
btn3.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 50px;")

grid.addWidget(btn1, 0, 0)
grid.addWidget(btn2, 0, 1)
grid.addWidget(btn3, 0, 2)

center_layout.addLayout(grid)
main_layout.addLayout(center_layout)

btn1.clicked.connect(lambda: print("Уровень 1"))
btn2.clicked.connect(lambda: print("Уровень 2"))
btn3.clicked.connect(lambda: print("Уровень 3"))

def open_levels():
    main_win.hide()
    levels_win.show()

def back_to_menu():
    levels_win.hide()
    main_win.show()

# Действия при нажатии
play_btn.clicked.connect(open_levels)
exit_btn.clicked.connect(main_win.close)
back_btn.clicked.connect(back_to_menu)

# Запуск
main_win.show()
sys.exit(app.exec_())