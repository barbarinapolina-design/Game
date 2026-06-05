import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
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

top_panel1 = QHBoxLayout()
back1 = QPushButton("НАЗАД")
back1.setFixedSize(90, 30)
back1.setFont(QFont("Arial", 10, QFont.Bold))
back1.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 15px;")
top_panel1.addWidget(back1)
top_panel1.addStretch()
level_title1 = QLabel("УРОВЕНЬ 1")
level_title1.setFont(QFont("Arial", 24, QFont.Bold))
level_title1.setAlignment(Qt.AlignCenter)
level_title1.setStyleSheet("color: #ffb7b2;")
top_panel1.addWidget(level_title1)
top_panel1.addStretch()
score_label1 = QLabel("⭐ 0")
score_label1.setFont(QFont("Arial", 18, QFont.Bold))
score_label1.setStyleSheet("color: #ffb7b2;")
top_panel1.addWidget(score_label1)
v3.addLayout(top_panel1)

message_label1 = QLabel("")
message_label1.setFont(QFont("Arial", 28, QFont.Bold))
message_label1.setAlignment(Qt.AlignCenter)
v3.addWidget(message_label1)

target_words1 = ["ТОК", "КОТ", "КИТ", "БОТ", "БОК", "БИНТ", "КИНО", "ОКНО"]
found_words1 = []
word_labels1 = []

for w in target_words1:
    dots = " ".join(["."] * len(w))
    lbl = QLabel(dots)
    lbl.setFont(QFont("Courier", 20, QFont.Bold))
    lbl.setAlignment(Qt.AlignCenter)
    lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")
    lbl.setFixedWidth(len(w) * 50)
    v3.addWidget(lbl, alignment=Qt.AlignCenter)
    word_labels1.append(lbl)

v3.addStretch()

current_word1 = ""
current_word_label1 = QLabel("")
current_word_label1.setFont(QFont("Courier", 32, QFont.Bold))
current_word_label1.setAlignment(Qt.AlignCenter)
current_word_label1.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 15px; border-radius: 15px;")
current_word_label1.setMinimumHeight(80)
v3.addWidget(current_word_label1)

buttons_layout1 = QHBoxLayout()
buttons_layout1.setAlignment(Qt.AlignCenter)
buttons_layout1.setSpacing(30)

clear_btn1 = QPushButton("✖")
clear_btn1.setFixedSize(70, 70)
clear_btn1.setFont(QFont("Arial", 28))
clear_btn1.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 35px;")
buttons_layout1.addWidget(clear_btn1)

check_btn1 = QPushButton("✓")
check_btn1.setFixedSize(70, 70)
check_btn1.setFont(QFont("Arial", 28))
check_btn1.setStyleSheet("background-color: #a8e6cf; color: white; border-radius: 35px;")
buttons_layout1.addWidget(check_btn1)

v3.addLayout(buttons_layout1)

hint1 = QLabel("Составь слово из букв:")
hint1.setFont(QFont("Arial", 12))
hint1.setStyleSheet("color: #d4a5a5;")
v3.addWidget(hint1)

h_letters1 = QHBoxLayout()
h_letters1.setAlignment(Qt.AlignCenter)
h_letters1.setSpacing(10)

letter_buttons1 = []
main_word1 = "БОТИНОК"
for letter in main_word1:
    b = QPushButton(letter)
    b.setFixedSize(60, 60)
    b.setFont(QFont("Arial", 18, QFont.Bold))
    b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
    h_letters1.addWidget(b)
    letter_buttons1.append(b)
v3.addLayout(h_letters1)

score1 = 0
used_indices1 = []

def show_message1(text, color):
    message_label1.setText(text)
    message_label1.setStyleSheet(f"color: {color}; font-size: 28px; font-weight: bold;")
    QTimer.singleShot(1500, lambda: message_label1.setText(""))

def update_score1():
    score_label1.setText(f"⭐ {score1}")

def update_words_display1():
    for i, w in enumerate(target_words1):
        if w in found_words1:
            word_labels1[i].setText(" ".join(w))
            word_labels1[i].setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; padding: 8px; border-radius: 10px;")
        else:
            dots = " ".join(["."] * len(w))
            word_labels1[i].setText(dots)
            word_labels1[i].setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")

def update_letters_state1():
    for i, btn in enumerate(letter_buttons1):
        if i in used_indices1:
            btn.setEnabled(False)
            btn.setStyleSheet("background-color: #d4d4d4; color: #999999; border-radius: 30px;")
        else:
            btn.setEnabled(True)
            btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")

def add_letter1(index):
    global current_word1
    if index not in used_indices1:
        current_word1 += main_word1[index].lower()
        used_indices1.append(index)
        current_word_label1.setText(" ".join(current_word1.upper()))
        update_letters_state1()

def clear_word1():
    global current_word1, used_indices1
    current_word1 = ""
    used_indices1 = []
    current_word_label1.setText("")
    update_letters_state1()

def check_word1():
    global score1, current_word1
    word = current_word1.upper()

    if not word:
        show_message1("Собери слово!", "red")
        return

    if word not in target_words1:
        show_message1(f"'{word}' нет в списке!", "red")
        clear_word1()
        return

    if word in found_words1:
        show_message1(f"'{word}' уже найдено!", "orange")
        clear_word1()
        return

    main_counter = {}
    for ch in main_word1:
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
        show_message1(f"'{word}' нельзя составить из букв!", "red")
        clear_word1()
        return

    points = len(word)
    score1 += points
    found_words1.append(word)
    update_score1()
    update_words_display1()
    clear_word1()

    show_message1(f"+{points} очков!", "green")

    if len(found_words1) >= len(target_words1):
        show_message1("УРОВЕНЬ ПРОЙДЕН!", "blue")

for i, btn in enumerate(letter_buttons1):
    btn.clicked.connect(lambda checked, idx=i: add_letter1(idx))

clear_btn1.clicked.connect(clear_word1)
check_btn1.clicked.connect(check_word1)

# ОКНО 2 УРОВНЯ
level2_win = QMainWindow()
level2_win.setWindowTitle("Слова из слова - Уровень 2")
level2_win.setFixedSize(700, 900)
level2_win.setStyleSheet("background-color: #fff5e6;")
level2_win.setWindowIcon(QIcon("images/word.png"))

central4 = QWidget()
level2_win.setCentralWidget(central4)
v4 = QVBoxLayout(central4)
v4.setContentsMargins(20, 20, 20, 20)

top_panel2 = QHBoxLayout()
back2 = QPushButton("НАЗАД")
back2.setFixedSize(90, 30)
back2.setFont(QFont("Arial", 10, QFont.Bold))
back2.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 15px;")
top_panel2.addWidget(back2)
top_panel2.addStretch()
level_title2 = QLabel("УРОВЕНЬ 2")
level_title2.setFont(QFont("Arial", 24, QFont.Bold))
level_title2.setAlignment(Qt.AlignCenter)
level_title2.setStyleSheet("color: #ffb7b2;")
top_panel2.addWidget(level_title2)
top_panel2.addStretch()
score_label2 = QLabel("⭐ 0")
score_label2.setFont(QFont("Arial", 18, QFont.Bold))
score_label2.setStyleSheet("color: #ffb7b2;")
top_panel2.addWidget(score_label2)
v4.addLayout(top_panel2)

message_label2 = QLabel("")
message_label2.setFont(QFont("Arial", 28, QFont.Bold))
message_label2.setAlignment(Qt.AlignCenter)
v4.addWidget(message_label2)

target_words2 = ["РОГ", "МАГ", "РАМА", "ГОРА", "МАМА", "ПОРА", "ГРАММ", "ГАММА", "МРАМОР"]
found_words2 = []
word_labels2 = []

for w in target_words2:
    dots = " ".join(["."] * len(w))
    lbl = QLabel(dots)
    lbl.setFont(QFont("Courier", 20, QFont.Bold))
    lbl.setAlignment(Qt.AlignCenter)
    lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")
    lbl.setFixedWidth(len(w) * 50)
    v4.addWidget(lbl, alignment=Qt.AlignCenter)
    word_labels2.append(lbl)

v4.addStretch()

current_word2 = ""
current_word_label2 = QLabel("")
current_word_label2.setFont(QFont("Courier", 32, QFont.Bold))
current_word_label2.setAlignment(Qt.AlignCenter)
current_word_label2.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 15px; border-radius: 15px;")
current_word_label2.setMinimumHeight(80)
v4.addWidget(current_word_label2)

buttons_layout2 = QHBoxLayout()
buttons_layout2.setAlignment(Qt.AlignCenter)
buttons_layout2.setSpacing(30)

clear_btn2 = QPushButton("✖")
clear_btn2.setFixedSize(70, 70)
clear_btn2.setFont(QFont("Arial", 28))
clear_btn2.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 35px;")
buttons_layout2.addWidget(clear_btn2)

check_btn2 = QPushButton("✓")
check_btn2.setFixedSize(70, 70)
check_btn2.setFont(QFont("Arial", 28))
check_btn2.setStyleSheet("background-color: #a8e6cf; color: white; border-radius: 35px;")
buttons_layout2.addWidget(check_btn2)

v4.addLayout(buttons_layout2)

hint2 = QLabel("Составь слово из букв:")
hint2.setFont(QFont("Arial", 12))
hint2.setStyleSheet("color: #d4a5a5;")
v4.addWidget(hint2)

h_letters2 = QHBoxLayout()
h_letters2.setAlignment(Qt.AlignCenter)
h_letters2.setSpacing(10)

letter_buttons2 = []
main_word2 = "ПРОГРАММА"
for letter in main_word2:
    b = QPushButton(letter)
    b.setFixedSize(60, 60)
    b.setFont(QFont("Arial", 18, QFont.Bold))
    b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
    h_letters2.addWidget(b)
    letter_buttons2.append(b)
v4.addLayout(h_letters2)

score2 = 0
used_indices2 = []

def show_message2(text, color):
    message_label2.setText(text)
    message_label2.setStyleSheet(f"color: {color}; font-size: 28px; font-weight: bold;")
    QTimer.singleShot(1500, lambda: message_label2.setText(""))

def update_score2():
    score_label2.setText(f"⭐ {score2}")

def update_words_display2():
    for i, w in enumerate(target_words2):
        if w in found_words2:
            word_labels2[i].setText(" ".join(w))
            word_labels2[i].setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; padding: 8px; border-radius: 10px;")
        else:
            dots = " ".join(["."] * len(w))
            word_labels2[i].setText(dots)
            word_labels2[i].setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")

def update_letters_state2():
    for i, btn in enumerate(letter_buttons2):
        if i in used_indices2:
            btn.setEnabled(False)
            btn.setStyleSheet("background-color: #d4d4d4; color: #999999; border-radius: 30px;")
        else:
            btn.setEnabled(True)
            btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")

def add_letter2(index):
    global current_word2
    if index not in used_indices2:
        current_word2 += main_word2[index].lower()
        used_indices2.append(index)
        current_word_label2.setText(" ".join(current_word2.upper()))
        update_letters_state2()

def clear_word2():
    global current_word2, used_indices2
    current_word2 = ""
    used_indices2 = []
    current_word_label2.setText("")
    update_letters_state2()

def check_word2():
    global score2, current_word2
    word = current_word2.upper()

    if not word:
        show_message2("Собери слово!", "red")
        return

    if word not in target_words2:
        show_message2(f"'{word}' нет в списке!", "red")
        clear_word2()
        return

    if word in found_words2:
        show_message2(f"'{word}' уже найдено!", "orange")
        clear_word2()
        return

    main_counter = {}
    for ch in main_word2:
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
        show_message2(f"'{word}' нельзя составить из букв!", "red")
        clear_word2()
        return

    points = len(word)
    score2 += points
    found_words2.append(word)
    update_score2()
    update_words_display2()
    clear_word2()

    show_message2(f"+{points} очков!", "green")

    if len(found_words2) >= len(target_words2):
        show_message2("УРОВЕНЬ ПРОЙДЕН!", "blue")

for i, btn in enumerate(letter_buttons2):
    btn.clicked.connect(lambda checked, idx=i: add_letter2(idx))

clear_btn2.clicked.connect(clear_word2)
check_btn2.clicked.connect(check_word2)

# ОКНО 3 УРОВНЯ
level3_win = QMainWindow()
level3_win.setWindowTitle("Слова из слова - Уровень 3")
level3_win.setFixedSize(800, 1100)
level3_win.setStyleSheet("background-color: #fff5e6;")
level3_win.setWindowIcon(QIcon("images/word.png"))

central5 = QWidget()
level3_win.setCentralWidget(central5)
v5 = QVBoxLayout(central5)
v5.setContentsMargins(20, 20, 20, 20)

# Верхняя панель
top_panel3 = QHBoxLayout()
back3 = QPushButton("НАЗАД")
back3.setFixedSize(90, 30)
back3.setFont(QFont("Arial", 10, QFont.Bold))
back3.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 15px;")
top_panel3.addWidget(back3)
top_panel3.addStretch()
level_title3 = QLabel("УРОВЕНЬ 3")
level_title3.setFont(QFont("Arial", 24, QFont.Bold))
level_title3.setAlignment(Qt.AlignCenter)
level_title3.setStyleSheet("color: #ffb7b2;")
top_panel3.addWidget(level_title3)
top_panel3.addStretch()
score_label3 = QLabel("⭐ 0")
score_label3.setFont(QFont("Arial", 18, QFont.Bold))
score_label3.setStyleSheet("color: #ffb7b2;")
top_panel3.addWidget(score_label3)
v5.addLayout(top_panel3)

message_label3 = QLabel("")
message_label3.setFont(QFont("Arial", 28, QFont.Bold))
message_label3.setAlignment(Qt.AlignCenter)
v5.addWidget(message_label3)

target_words3 = ["ГИТ", "РИС", "АИСТ", "ГИРЯ", "ИГРА", "СТАЯ", "ТИГР", "РАЦИЯ", "АРЕСТ", "ГРАЦИЯ", "СТАРЕЦ", "РЕГИСТР"]
found_words3 = []
word_labels3 = []

for w in target_words3:
    dots = " ".join(["."] * len(w))
    lbl = QLabel(dots)
    lbl.setFont(QFont("Courier", 20, QFont.Bold))
    lbl.setAlignment(Qt.AlignCenter)
    lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")
    lbl.setFixedWidth(len(w) * 50)
    v5.addWidget(lbl, alignment=Qt.AlignCenter)
    word_labels3.append(lbl)

v5.addStretch()

# Поле для ввода слова
current_word3 = ""
current_word_label3 = QLabel("")
current_word_label3.setFont(QFont("Courier", 32, QFont.Bold))
current_word_label3.setAlignment(Qt.AlignCenter)
current_word_label3.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 15px; border-radius: 15px;")
current_word_label3.setMinimumHeight(80)
v5.addWidget(current_word_label3)

# Кнопки действий
buttons_layout3 = QHBoxLayout()
buttons_layout3.setAlignment(Qt.AlignCenter)
buttons_layout3.setSpacing(30)

clear_btn3 = QPushButton("✖")
clear_btn3.setFixedSize(70, 70)
clear_btn3.setFont(QFont("Arial", 28))
clear_btn3.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 35px;")
buttons_layout3.addWidget(clear_btn3)

check_btn3 = QPushButton("✓")
check_btn3.setFixedSize(70, 70)
check_btn3.setFont(QFont("Arial", 28))
check_btn3.setStyleSheet("background-color: #a8e6cf; color: white; border-radius: 35px;")
buttons_layout3.addWidget(check_btn3)

v5.addLayout(buttons_layout3)

hint3 = QLabel("Составь слово из букв:")
hint3.setFont(QFont("Arial", 12))
hint3.setStyleSheet("color: #d4a5a5;")
v5.addWidget(hint3)

h_letters3 = QHBoxLayout()
h_letters3.setAlignment(Qt.AlignCenter)
h_letters3.setSpacing(10)

letter_buttons3 = []
main_word3 = "РЕГИСТРАЦИЯ"
for letter in main_word3:
    b = QPushButton(letter)
    b.setFixedSize(60, 60)
    b.setFont(QFont("Arial", 18, QFont.Bold))
    b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
    h_letters3.addWidget(b)
    letter_buttons3.append(b)
v5.addLayout(h_letters3)

# Пока кнопки 3 уровня не активны
def show_message3(text, color):
    message_label3.setText(text)
    message_label3.setStyleSheet(f"color: {color}; font-size: 28px; font-weight: bold;")
    QTimer.singleShot(1500, lambda: message_label3.setText(""))

for i, btn in enumerate(letter_buttons3):
    btn.clicked.connect(lambda checked, idx=i: show_message3("Скоро будет готово!", "orange"))

clear_btn3.clicked.connect(lambda: show_message3("Скоро будет готово!", "orange"))
check_btn3.clicked.connect(lambda: show_message3("Скоро будет готово!", "orange"))

# Переходы
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

play_btn.clicked.connect(to_levels)
exit_btn.clicked.connect(main_win.close)
back_btn.clicked.connect(back_to_main)
btn1.clicked.connect(to_level1)
btn2.clicked.connect(to_level2)
btn3.clicked.connect(to_level3)
back1.clicked.connect(back_from_level1)
back2.clicked.connect(back_from_level2)
back3.clicked.connect(back_from_level3)

main_win.show()
sys.exit(app.exec_())