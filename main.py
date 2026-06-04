import sys
from PyQt5.QtWidgets import *
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

h1 = QHBoxLayout()
h1.setAlignment(Qt.AlignCenter)
play_btn = QPushButton("ИГРАТЬ")
play_btn.setFixedSize(250, 60)
play_btn.setFont(QFont("Arial", 16, QFont.Bold))
play_btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
h1.addWidget(play_btn)
layout.addLayout(h1)

h2 = QHBoxLayout()
h2.setAlignment(Qt.AlignCenter)
exit_btn = QPushButton("ВЫХОД")
exit_btn.setFixedSize(200, 50)
exit_btn.setFont(QFont("Arial", 14))
exit_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
h2.addWidget(exit_btn)
layout.addLayout(h2)

# ОКНО ВЫБОРА УРОВНЕЙ
levels_win = QMainWindow()
levels_win.setWindowTitle("Слова из слова - Выбор уровня")
levels_win.setFixedSize(500, 450)
levels_win.setStyleSheet("background-color: #fff5e6;")
levels_win.setWindowIcon(QIcon("images/word.png"))

central2 = QWidget()
levels_win.setCentralWidget(central2)
v2 = QVBoxLayout(central2)
v2.setContentsMargins(20, 20, 20, 20)

top = QHBoxLayout()
back_btn = QPushButton("НАЗАД")
back_btn.setFixedSize(90, 30)
back_btn.setFont(QFont("Arial", 10, QFont.Bold))
back_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 15px;")
top.addWidget(back_btn)
top.addStretch()
v2.addLayout(top)

v2.addStretch()
title2 = QLabel("ВЫБЕРИ УРОВЕНЬ")
title2.setFont(QFont("Arial", 24, QFont.Bold))
title2.setAlignment(Qt.AlignCenter)
title2.setStyleSheet("color: #ffb7b2;")
v2.addWidget(title2)

h_levels = QHBoxLayout()
h_levels.setAlignment(Qt.AlignCenter)
h_levels.setSpacing(30)

btn1 = QPushButton("1")
btn2 = QPushButton("2")
btn3 = QPushButton("3")
for btn in [btn1, btn2, btn3]:
    btn.setFixedSize(100, 100)
    btn.setFont(QFont("Arial", 32, QFont.Bold))
    btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 50px;")
    h_levels.addWidget(btn)

v2.addLayout(h_levels)
v2.addStretch()

# ОКНО 1 УРОВНЯ
level1_win = QMainWindow()
level1_win.setWindowTitle("Слова из слова - Уровень 1")
level1_win.setFixedSize(700, 800)
level1_win.setStyleSheet("background-color: #fff5e6;")
level1_win.setWindowIcon(QIcon("images/word.png"))

central3 = QWidget()
level1_win.setCentralWidget(central3)
v3 = QVBoxLayout(central3)
v3.setContentsMargins(20, 20, 20, 20)

top1 = QHBoxLayout()
back1 = QPushButton("НАЗАД")
back1.setFixedSize(90, 30)
back1.setFont(QFont("Arial", 10, QFont.Bold))
back1.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 15px;")
top1.addWidget(back1)
top1.addStretch()
v3.addLayout(top1)

lbl = QLabel("УРОВЕНЬ 1")
lbl.setFont(QFont("Arial", 24, QFont.Bold))
lbl.setAlignment(Qt.AlignCenter)
lbl.setStyleSheet("color: #ffb7b2;")
v3.addWidget(lbl)

for w in ["ТОК", "КОТ", "КИТ", "БИТ", "БОК", "БИНТ", "КИНО", "ОКНО"]:
    dots = " ".join(["."] * len(w))
    lbl = QLabel(dots)
    lbl.setFont(QFont("Courier", 20, QFont.Bold))
    lbl.setAlignment(Qt.AlignCenter)
    lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")
    lbl.setFixedWidth(len(w) * 50)
    v3.addWidget(lbl, alignment=Qt.AlignCenter)

v3.addStretch()

hint = QLabel("Составь слово из букв:")
hint.setFont(QFont("Arial", 12))
hint.setStyleSheet("color: #d4a5a5;")
v3.addWidget(hint)

# Буквы
h_letters = QHBoxLayout()
h_letters.setAlignment(Qt.AlignCenter)
h_letters.setSpacing(10)
for letter in "БОТИНОК":
    b = QPushButton(letter)
    b.setFixedSize(60, 60)
    b.setFont(QFont("Arial", 18, QFont.Bold))
    b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
    h_letters.addWidget(b)
v3.addLayout(h_letters)

def to_levels():
    main_win.hide()
    levels_win.show()

def back_to_main():
    levels_win.hide()
    main_win.show()

def to_level1():
    levels_win.hide()
    level1_win.show()

def back_from_level1():
    level1_win.hide()
    levels_win.show()

play_btn.clicked.connect(to_levels)
exit_btn.clicked.connect(main_win.close)
back_btn.clicked.connect(back_to_main)
btn1.clicked.connect(to_level1)
back1.clicked.connect(back_from_level1)

main_win.show()
sys.exit(app.exec_())