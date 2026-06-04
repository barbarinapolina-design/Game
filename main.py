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
level1_win.setFixedSize(700, 850)
level1_win.setStyleSheet("background-color: #fff5e6;")
level1_win.setWindowIcon(QIcon("images/word.png"))

central3 = QWidget()
level1_win.setCentralWidget(central3)
v3 = QVBoxLayout(central3)
v3.setContentsMargins(20, 20, 20, 20)

# Верхняя панель
top_panel = QHBoxLayout()
back1 = QPushButton("НАЗАД")
back1.setFixedSize(90, 30)
back1.setFont(QFont("Arial", 10, QFont.Bold))
back1.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 15px;")
top_panel.addWidget(back1)
top_panel.addStretch()
score_label = QLabel("⭐ 0")
score_label.setFont(QFont("Arial", 18, QFont.Bold))
score_label.setStyleSheet("color: #ffb7b2;")
top_panel.addWidget(score_label)
v3.addLayout(top_panel)

lbl = QLabel("УРОВЕНЬ 1")
lbl.setFont(QFont("Arial", 24, QFont.Bold))
lbl.setAlignment(Qt.AlignCenter)
lbl.setStyleSheet("color: #ffb7b2;")
v3.addWidget(lbl)

target_words = ["ТОК", "КОТ", "КИТ", "БИТ", "БОК", "БИНТ", "КИНО", "ОКНО"]
found_words = []  # отгаданные слова
word_labels = []  # метки с точками-словами

for w in target_words:
    dots = " ".join(["."] * len(w))
    lbl = QLabel(dots)
    lbl.setFont(QFont("Courier", 20, QFont.Bold))
    lbl.setAlignment(Qt.AlignCenter)
    lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")
    lbl.setFixedWidth(len(w) * 50)
    v3.addWidget(lbl, alignment=Qt.AlignCenter)
    word_labels.append(lbl)

v3.addStretch()

# поле для ввода слов
current_word = ""
current_word_label = QLabel("")
current_word_label.setFont(QFont("Courier", 32, QFont.Bold))
current_word_label.setAlignment(Qt.AlignCenter)
current_word_label.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 15px; border-radius: 15px;")
current_word_label.setMinimumHeight(80)
v3.addWidget(current_word_label)

buttons_layout = QHBoxLayout()
buttons_layout.setAlignment(Qt.AlignCenter)
buttons_layout.setSpacing(30)

clear_btn = QPushButton("✖")
clear_btn.setFixedSize(70, 70)
clear_btn.setFont(QFont("Arial", 28))
clear_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 35px;")
buttons_layout.addWidget(clear_btn)

check_btn = QPushButton("✓")
check_btn.setFixedSize(70, 70)
check_btn.setFont(QFont("Arial", 28))
check_btn.setStyleSheet("background-color: #a8e6cf; color: white; border-radius: 35px;")
buttons_layout.addWidget(check_btn)

v3.addLayout(buttons_layout)

hint = QLabel("Составь слово из букв:")
hint.setFont(QFont("Arial", 12))
hint.setStyleSheet("color: #d4a5a5;")
v3.addWidget(hint)

# БУКВЫ
h_letters = QHBoxLayout()
h_letters.setAlignment(Qt.AlignCenter)
h_letters.setSpacing(10)

letter_buttons = []
main_word = "БОТИНОК"

for letter in main_word:
    b = QPushButton(letter)
    b.setFixedSize(60, 60)
    b.setFont(QFont("Arial", 18, QFont.Bold))
    b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
    h_letters.addWidget(b)
    letter_buttons.append(b)

v3.addLayout(h_letters)

score = 0
used_indices = []  # какие кнопки букв уже использованы

def update_score():
    score_label.setText(f"⭐ {score}")

def update_words_display():
    for i, w in enumerate(target_words):
        if w in found_words:
            word_labels[i].setText(" ".join(w))
            word_labels[i].setStyleSheet(
                "background-color: #a8e6cf; color: #6b9e8a; padding: 8px; border-radius: 10px;")
        else:
            dots = " ".join(["."] * len(w))
            word_labels[i].setText(dots)
            word_labels[i].setStyleSheet(
                "background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")

def update_letters_state():
    for i, btn in enumerate(letter_buttons):
        if i in used_indices:
            btn.setEnabled(False)
            btn.setStyleSheet("background-color: #d4d4d4; color: #999999; border-radius: 30px;")
        else:
            btn.setEnabled(True)
            btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")

def add_letter(index):
    global current_word
    if index not in used_indices:
        current_word += main_word[index].lower()
        used_indices.append(index)
        current_word_label.setText(" ".join(current_word.upper()))
        update_letters_state()

def clear_word():
    global current_word, used_indices
    current_word = ""
    used_indices = []
    current_word_label.setText("")
    update_letters_state()

def check_word():
    global score, current_word
    word = current_word.upper()

    if not word:
        print("Собери слово!")
        return

    if word not in target_words:
        print(f"'{word}' нет в списке!")
        clear_word()
        return

    if word in found_words:
        print(f"'{word}' уже найдено!")
        clear_word()
        return

    # можно ли составить слово из букв?
    main_counter = {}
    for ch in main_word:
        main_counter[ch] = main_counter.get(ch, 0) + 1

    word_counter = {}
    for ch in word:
        word_counter[ch] = word_counter.get(ch, 0) + 1

    possible = True
    for ch in word_counter:
        if word_counter[ch] > main_counter.get(ch, 0):
            possible = False
            break

    if not possible:
        print(f"'{word}' нельзя составить из букв!")
        clear_word()
        return

    # Успех
    points = len(word)
    score += points
    found_words.append(word)
    update_score()
    update_words_display()
    clear_word()

    print(f"+{points} очков!")

    # все ли слова отгаданы?
    if len(found_words) >= len(target_words):
        print("УРОВЕНЬ ПРОЙДЕН!")


# назначение действий
for i, btn in enumerate(letter_buttons):
    btn.clicked.connect(lambda checked, idx=i: add_letter(idx))

clear_btn.clicked.connect(clear_word)
check_btn.clicked.connect(check_word)


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