import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

app = QApplication(sys.argv)
# Главное меню
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

# Окно выбора уровней
levels_win = QMainWindow()
levels_win.setWindowTitle("Слова из слова - Выбор уровня")
levels_win.setFixedSize(500, 450)
levels_win.setStyleSheet("background-color: #fff5e6;")

central2 = QWidget()
levels_win.setCentralWidget(central2)

layout2 = QVBoxLayout(central2)
layout2.setAlignment(Qt.AlignCenter)
layout2.setSpacing(30)

title2 = QLabel("ВЫБЕРИ УРОВЕНЬ")
title2.setFont(QFont("Arial", 24, QFont.Bold))
title2.setAlignment(Qt.AlignCenter)
title2.setStyleSheet("color: #ffb7b2;")
layout2.addWidget(title2)

h_back = QHBoxLayout()
h_back.setAlignment(Qt.AlignCenter)
back_btn = QPushButton("← НАЗАД")
back_btn.setFixedSize(200, 50)
back_btn.setFont(QFont("Arial", 14))
back_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
h_back.addWidget(back_btn)
layout2.addLayout(h_back)

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