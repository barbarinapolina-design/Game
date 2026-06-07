import sys
import json
import os
import random
from collections import Counter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon

app = QApplication(sys.argv)

# ========== ГЛАВНОЕ МЕНЮ ==========
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

# Кнопка ИГРАТЬ
h1 = QHBoxLayout()
h1.setAlignment(Qt.AlignCenter)
play_btn = QPushButton("ИГРАТЬ")
play_btn.setFixedSize(250, 60)
play_btn.setFont(QFont("Arial", 16, QFont.Bold))
play_btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
h1.addWidget(play_btn)
layout.addLayout(h1)

# Кнопка ВЫХОД
h2 = QHBoxLayout()
h2.setAlignment(Qt.AlignCenter)
exit_btn = QPushButton("ВЫХОД")
exit_btn.setFixedSize(200, 50)
exit_btn.setFont(QFont("Arial", 14))
exit_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
h2.addWidget(exit_btn)
layout.addLayout(h2)

# ========== ОКНО ВЫБОРА УРОВНЕЙ ==========
levels_win = QMainWindow()
levels_win.setWindowTitle("Слова из слова - Выбор уровня")
levels_win.setFixedSize(500, 480)
levels_win.setStyleSheet("background-color: #fff5e6;")
levels_win.setWindowIcon(QIcon("images/word.png"))

central2 = QWidget()
levels_win.setCentralWidget(central2)
v2 = QVBoxLayout(central2)
v2.setContentsMargins(20, 20, 20, 20)

top = QHBoxLayout()
back_btn = QPushButton("←")
back_btn.setFixedSize(50, 50)
back_btn.setFont(QFont("Arial", 22, QFont.Bold))
back_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
top.addWidget(back_btn)
top.addStretch()
v2.addLayout(top)

v2.addStretch()
title2 = QLabel("ВЫБЕРИ УРОВЕНЬ")
title2.setFont(QFont("Arial", 24, QFont.Bold))
title2.setAlignment(Qt.AlignCenter)
title2.setStyleSheet("color: #ffb7b2;")
v2.addWidget(title2)

v2.addSpacing(50)

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

v2.addSpacing(20)

time_btn = QPushButton("Режим \"На время\"")
time_btn.setFixedSize(340, 50)
time_btn.setFont(QFont("Arial", 14, QFont.Bold))
time_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
v2.addWidget(time_btn, alignment=Qt.AlignCenter)

v2.addStretch()

# ========== ОКНО РЕЖИМА "НА ВРЕМЯ" ==========
time_win = QMainWindow()
time_win.setWindowTitle("Слова из слова - Режим «На время»")
time_win.setFixedSize(800, 900)
time_win.setStyleSheet("background-color: #fff5e6;")
time_win.setWindowIcon(QIcon("images/word.png"))

central_time = QWidget()
time_win.setCentralWidget(central_time)
v_time = QVBoxLayout(central_time)
v_time.setContentsMargins(20, 20, 20, 20)

top_time = QHBoxLayout()
back_time = QPushButton("←")
back_time.setFixedSize(50, 50)
back_time.setFont(QFont("Arial", 22, QFont.Bold))
back_time.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
top_time.addWidget(back_time)
top_time.addStretch()

score_label_time = QLabel("⭐ 0")
score_label_time.setFont(QFont("Arial", 18, QFont.Bold))
score_label_time.setStyleSheet("color: #ffb7b2;")
top_time.addWidget(score_label_time)
v_time.addLayout(top_time)

timer_label = QLabel("Время 01:00")
timer_label.setFont(QFont("Arial", 22, QFont.Bold))
timer_label.setAlignment(Qt.AlignCenter)
timer_label.setStyleSheet("color: #ffb7b2;")
v_time.addWidget(timer_label)

msg_label_time = QLabel("")
msg_label_time.setFont(QFont("Arial", 28, QFont.Bold))
msg_label_time.setAlignment(Qt.AlignCenter)
v_time.addWidget(msg_label_time)

# Найденные слова — по центру
found_label = QLabel("Найденные слова:")
found_label.setFont(QFont("Arial", 14))
found_label.setStyleSheet("color: #d4a5a5;")
v_time.addWidget(found_label)

found_container = QWidget()
found_container.setFixedSize(650, 400)
found_container.setStyleSheet("background-color: #ffe4e9; border-radius: 10px;")
found_grid = QGridLayout(found_container)
found_grid.setSpacing(8)
found_grid.setAlignment(Qt.AlignCenter)
v_time.addWidget(found_container, alignment=Qt.AlignCenter)

v_time.addStretch()

current_word_label_time = QLabel("")
current_word_label_time.setFont(QFont("Courier", 32, QFont.Bold))
current_word_label_time.setAlignment(Qt.AlignCenter)
current_word_label_time.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 15px; border-radius: 15px;")
current_word_label_time.setMinimumHeight(80)
v_time.addWidget(current_word_label_time)

h_actions = QHBoxLayout()
h_actions.setAlignment(Qt.AlignCenter)
h_actions.setSpacing(30)

clear_time = QPushButton("✖")
clear_time.setFixedSize(70, 70)
clear_time.setFont(QFont("Arial", 28))
clear_time.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 35px;")
h_actions.addWidget(clear_time)

check_time = QPushButton("✓")
check_time.setFixedSize(70, 70)
check_time.setFont(QFont("Arial", 28))
check_time.setStyleSheet("background-color: #a8e6cf; color: white; border-radius: 35px;")
h_actions.addWidget(check_time)

v_time.addLayout(h_actions)

hint_time = QLabel("Составь слово из букв:")
hint_time.setFont(QFont("Arial", 12))
hint_time.setStyleSheet("color: #d4a5a5;")
v_time.addWidget(hint_time)

h_letters_time = QHBoxLayout()
h_letters_time.setAlignment(Qt.AlignCenter)
h_letters_time.setSpacing(10)

# ========== ДАННЫЕ ДЛЯ УРОВНЕЙ ==========
levels_data = {
    1: {"word": "БОТИНОК", "target": ["ТОК", "КОТ", "КИТ", "БОТ", "БОК", "БИНТ", "КИНО", "ОКНО"]},
    2: {"word": "ПРОГРАММА", "target": ["РОГ", "МАГ", "РАМА", "ГОРА", "МАМА", "ПОРА", "ГРАММ", "ГАММА", "МРАМОР"]},
    3: {"word": "РЕГИСТРАЦИЯ", "target": ["ГИТ", "РИС", "АИСТ", "ГИРЯ", "ИГРА", "СТАЯ", "ТИГР", "РАЦИЯ", "АРЕСТ", "ГРАЦИЯ", "СТАРЕЦ", "РЕГИСТР"]}
}

# ========== ОКНО УРОВНЯ (общая функция) ==========
def create_level_window(level_num):
    win = QMainWindow()
    win.setWindowTitle(f"Слова из слова - Уровень {level_num}")
    win.setFixedSize(800, 900 if level_num < 3 else 1100)
    win.setStyleSheet("background-color: #fff5e6;")
    win.setWindowIcon(QIcon("images/word.png"))

    central = QWidget()
    win.setCentralWidget(central)
    v = QVBoxLayout(central)
    v.setContentsMargins(20, 20, 20, 20)

    # Верхняя панель
    top = QHBoxLayout()
    back = QPushButton("←")
    back.setFixedSize(50, 50)
    back.setFont(QFont("Arial", 22, QFont.Bold))
    back.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
    top.addWidget(back)
    top.addStretch()
    level_title = QLabel(f"УРОВЕНЬ {level_num}")
    level_title.setFont(QFont("Arial", 24, QFont.Bold))
    level_title.setAlignment(Qt.AlignCenter)
    level_title.setStyleSheet("color: #ffb7b2;")
    top.addWidget(level_title)
    top.addStretch()
    score_lbl = QLabel("⭐ 0")
    score_lbl.setFont(QFont("Arial", 18, QFont.Bold))
    score_lbl.setStyleSheet("color: #ffb7b2;")
    top.addWidget(score_lbl)
    v.addLayout(top)

    msg_lbl = QLabel("")
    msg_lbl.setFont(QFont("Arial", 28, QFont.Bold))
    msg_lbl.setAlignment(Qt.AlignCenter)
    v.addWidget(msg_lbl)

    words = levels_data[level_num]["target"]
    found = []
    word_labels = []
    for w in words:
        lbl = QLabel(" ".join(["."] * len(w)))
        lbl.setFont(QFont("Courier", 20, QFont.Bold))
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")
        lbl.setFixedWidth(len(w) * 50)
        v.addWidget(lbl, alignment=Qt.AlignCenter)
        word_labels.append(lbl)

    v.addStretch()

    current_word = ""
    used_indices = []
    score = 0

    current_lbl = QLabel("")
    current_lbl.setFont(QFont("Courier", 32, QFont.Bold))
    current_lbl.setAlignment(Qt.AlignCenter)
    current_lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 15px; border-radius: 15px;")
    current_lbl.setMinimumHeight(80)
    v.addWidget(current_lbl)

    h_btn = QHBoxLayout()
    h_btn.setAlignment(Qt.AlignCenter)
    h_btn.setSpacing(30)
    clear_btn = QPushButton("✖")
    clear_btn.setFixedSize(70, 70)
    clear_btn.setFont(QFont("Arial", 28))
    clear_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 35px;")
    check_btn = QPushButton("✓")
    check_btn.setFixedSize(70, 70)
    check_btn.setFont(QFont("Arial", 28))
    check_btn.setStyleSheet("background-color: #a8e6cf; color: white; border-radius: 35px;")
    h_btn.addWidget(clear_btn)
    h_btn.addWidget(check_btn)
    v.addLayout(h_btn)

    hint = QLabel("Составь слово из букв:")
    hint.setFont(QFont("Arial", 12))
    hint.setStyleSheet("color: #d4a5a5;")
    v.addWidget(hint)

    h_letters = QHBoxLayout()
    h_letters.setAlignment(Qt.AlignCenter)
    h_letters.setSpacing(10)

    letter_btns = []
    main_word = levels_data[level_num]["word"]
    for letter in main_word:
        b = QPushButton(letter)
        b.setFixedSize(60, 60)
        b.setFont(QFont("Arial", 18, QFont.Bold))
        b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
        h_letters.addWidget(b)
        letter_btns.append(b)
    v.addLayout(h_letters)

    def show_msg(txt, col):
        msg_lbl.setText(txt)
        msg_lbl.setStyleSheet(f"color: {col}; font-size: 28px; font-weight: bold;")
        QTimer.singleShot(1500, lambda: msg_lbl.setText(""))

    def update_score():
        score_lbl.setText(f"⭐ {score}")

    def update_words():
        for i, w in enumerate(words):
            if w in found:
                word_labels[i].setText(" ".join(w))
                word_labels[i].setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; padding: 8px; border-radius: 10px;")
            else:
                word_labels[i].setText(" ".join(["."] * len(w)))
                word_labels[i].setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")

    def update_letters():
        for i, btn in enumerate(letter_btns):
            if i in used_indices:
                btn.setEnabled(False)
                btn.setStyleSheet("background-color: #d4d4d4; color: #999999; border-radius: 30px;")
            else:
                btn.setEnabled(True)
                btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")

    def add_letter(idx):
        nonlocal current_word
        if idx not in used_indices:
            current_word += main_word[idx].lower()
            used_indices.append(idx)
            current_lbl.setText(" ".join(current_word.upper()))
            update_letters()

    def clear_word():
        nonlocal current_word, used_indices
        for i in used_indices:
            letter_btns[i].setEnabled(True)
        current_word = ""
        used_indices = []
        current_lbl.setText("")
        update_letters()

    def check_word():
        nonlocal score, current_word
        word = current_word.upper()
        if not word:
            show_msg("Собери слово!", "red")
            return
        if word not in words:
            show_msg(f"'{word}' нет в списке!", "red")
            clear_word()
            return
        if word in found:
            show_msg(f"'{word}' уже найдено!", "orange")
            clear_word()
            return
        if Counter(word) <= Counter(main_word):
            score += len(word)
            found.append(word)
            update_score()
            update_words()
            clear_word()
            show_msg(f"+{len(word)} очков!", "green")
            if len(found) >= len(words):
                show_msg("УРОВЕНЬ ПРОЙДЕН!", "blue")
        else:
            show_msg("Нельзя составить!", "red")
            clear_word()

    for i, btn in enumerate(letter_btns):
        btn.clicked.connect(lambda checked, idx=i: add_letter(idx))
    clear_btn.clicked.connect(clear_word)
    check_btn.clicked.connect(check_word)

    def back_to_levels():
        win.hide()
        levels_win.show()

    back.clicked.connect(back_to_levels)

    return win

# ========== СОЗДАЁМ ОКНА УРОВНЕЙ ==========
level1_win = create_level_window(1)
level2_win = create_level_window(2)
level3_win = create_level_window(3)

# ========== ПЕРЕХОДЫ ==========
def to_levels():
    main_win.hide()
    levels_win.show()

def back_to_main():
    levels_win.hide()
    main_win.show()

def to_level1():
    levels_win.hide()
    level1_win.show()

def to_level2():
    levels_win.hide()
    level2_win.show()

def to_level3():
    levels_win.hide()
    level3_win.show()

def back_from_level1():
    level1_win.hide()
    levels_win.show()

def back_from_level2():
    level2_win.hide()
    levels_win.show()

def back_from_level3():
    level3_win.hide()
    levels_win.show()

def open_time_mode():
    levels_win.hide()
    time_win.show()

def close_time_mode():
    time_win.hide()
    levels_win.show()

# Подключаем кнопки
play_btn.clicked.connect(to_levels)
exit_btn.clicked.connect(main_win.close)
back_btn.clicked.connect(back_to_main)
btn1.clicked.connect(to_level1)
btn2.clicked.connect(to_level2)
btn3.clicked.connect(to_level3)
time_btn.clicked.connect(open_time_mode)
back_time.clicked.connect(close_time_mode)

main_win.show()
sys.exit(app.exec_())