import sys
import json
import os
import random
from collections import Counter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap

app = QApplication(sys.argv)


# ФУНКЦИИ ДЛЯ СОХРАНЕНИЯ ПРОГРЕССА
def load_levels_progress():
    if os.path.exists("data/progress.json"):
        with open("data/progress.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"unlocked": [1], "scores": {}, "found": {}}


def save_levels_progress(data):
    os.makedirs("data", exist_ok=True)
    with open("data/progress.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_record():
    global record
    if os.path.exists("data/record.json"):
        with open("data/record.json", "r") as f:
            record = json.load(f).get("record", 0)
    else:
        record = 0


def save_record():
    os.makedirs("data", exist_ok=True)
    with open("data/record.json", "w") as f:
        json.dump({"record": record}, f)


def update_level_buttons():
    progress = load_levels_progress()
    unlocked = progress.get("unlocked", [1])
    for i, btn in enumerate([btn1, btn2, btn3], 1):
        if i in unlocked:
            btn.setEnabled(True)
            btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 50px;")
        else:
            btn.setEnabled(False)
            btn.setStyleSheet("background-color: #d4d4d4; color: #999; border-radius: 50px;")


def get_total_score():
    progress = load_levels_progress()
    scores = progress.get("scores", {})
    total = sum(scores.values())
    return total


# ГЛАВНОЕ МЕНЮ
main_win = QMainWindow()
main_win.setWindowTitle("Слова из слова")
main_win.showFullScreen()
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
levels_win.showFullScreen()
levels_win.setStyleSheet("background-color: #fff5e6;")
levels_win.setWindowIcon(QIcon("images/word.png"))

central2 = QWidget()
levels_win.setCentralWidget(central2)
v2 = QVBoxLayout(central2)
v2.setContentsMargins(20, 20, 20, 20)

top = QHBoxLayout()
back_btn = QPushButton("назад")
back_btn.setFixedSize(100, 40)
back_btn.setFont(QFont("Arial", 16, QFont.Bold))
back_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 20px;")
top.addWidget(back_btn)
top.addStretch()

total_score_label = QLabel("⭐ 0")
total_score_label.setFont(QFont("Arial", 18, QFont.Bold))
total_score_label.setStyleSheet("color: #ffb7b2;")
top.addWidget(total_score_label)

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

bottom = QHBoxLayout()
bottom.setAlignment(Qt.AlignRight)

reset_btn = QPushButton("Сбросить прогресс")
reset_btn.setFixedSize(230, 40)
reset_btn.setFont(QFont("Arial", 12, QFont.Bold))
reset_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 20px")
bottom.addWidget(reset_btn)
v2.addLayout(bottom)


def update_total_score_display():
    total = get_total_score()
    total_score_label.setText(f"⭐ {total}/120")


# ФУНКЦИИ ДЛЯ СБРОСА
def show_reset_dialog():
    dialog = QDialog(levels_win)
    dialog.setWindowTitle("Сброс прогресса")
    dialog.setFixedSize(550, 200)
    dialog.setModal(True)
    dialog.setWindowIcon(QIcon("images/word.png"))
    dialog.setStyleSheet("background-color: #fff5e6;")

    layout = QVBoxLayout(dialog)
    layout.setSpacing(15)
    layout.setContentsMargins(25, 20, 25, 20)

    question = QLabel("Вы уверены, что хотите сбросить весь прогресс?")
    question.setFont(QFont("Arial", 12, QFont.Bold))
    question.setWordWrap(True)
    question.setStyleSheet("color: #6b9e8a;")
    layout.addWidget(question)

    warn_layout = QHBoxLayout()
    warn_layout.setAlignment(Qt.AlignCenter)
    warn_layout.setSpacing(5)

    icon = QLabel()
    pixmap = QPixmap("images/question.png")
    pixmap = pixmap.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    icon.setPixmap(pixmap)
    warn_layout.addWidget(icon)

    warning = QLabel("Все очки и разблокированные уровни будут потеряны")
    warning.setFont(QFont("Arial", 12))
    warning.setWordWrap(True)
    warning.setStyleSheet("color: #c77d7d;")
    warn_layout.addWidget(warning, 1)

    layout.addLayout(warn_layout)

    btn_layout = QHBoxLayout()
    btn_layout.setAlignment(Qt.AlignCenter)
    btn_layout.setSpacing(30)

    yes_btn = QPushButton("ДА")
    yes_btn.setFixedSize(100, 40)
    yes_btn.setFont(QFont("Arial", 12, QFont.Bold))
    yes_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 20px;")
    yes_btn.clicked.connect(lambda: dialog.done(QMessageBox.Yes))
    btn_layout.addWidget(yes_btn)

    no_btn = QPushButton("НЕТ")
    no_btn.setFixedSize(100, 40)
    no_btn.setFont(QFont("Arial", 12, QFont.Bold))
    no_btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 20px;")
    no_btn.clicked.connect(lambda: dialog.done(QMessageBox.No))
    btn_layout.addWidget(no_btn)

    layout.addLayout(btn_layout)

    if dialog.exec_() == QMessageBox.Yes:
        reset_all_progress()


def reset_all_progress():
    default_progress = {"unlocked": [1], "scores": {}, "found": {}}
    save_levels_progress(default_progress)
    if os.path.exists("data/record.json"):
        with open("data/record.json", "w") as f:
            json.dump({"record": 0}, f)
    update_level_buttons()

    dialog = QDialog(levels_win)
    dialog.setWindowTitle("Прогресс сброшен")
    dialog.setFixedSize(430, 180)
    dialog.setModal(True)
    dialog.setWindowIcon(QIcon("images/word.png"))
    dialog.setStyleSheet("background-color: #fff5e6;")

    layout = QVBoxLayout(dialog)
    layout.setSpacing(15)
    layout.setContentsMargins(25, 20, 25, 20)

    top_layout = QHBoxLayout()
    top_layout.setSpacing(15)

    icon = QLabel()
    pixmap = QPixmap("images/success.png")
    pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    icon.setPixmap(pixmap)
    top_layout.addWidget(icon)

    text = QLabel("Весь прогресс был успешно сброшен.")
    text.setFont(QFont("Arial", 12, QFont.Bold))
    text.setWordWrap(True)
    text.setStyleSheet("color: #6b9e8a;")
    top_layout.addWidget(text, 1)

    layout.addLayout(top_layout)

    text2 = QLabel("Теперь вы начинаете игру с первого уровня.")
    text2.setFont(QFont("Arial", 11))
    text2.setAlignment(Qt.AlignCenter)
    text2.setWordWrap(True)
    text2.setStyleSheet("color: #c77d7d;")
    layout.addWidget(text2)

    btn_layout = QHBoxLayout()
    btn_layout.setAlignment(Qt.AlignCenter)

    ok_btn = QPushButton("ОК")
    ok_btn.setFixedSize(100, 40)
    ok_btn.setFont(QFont("Arial", 12, QFont.Bold))
    ok_btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 20px;")
    ok_btn.clicked.connect(dialog.accept)
    btn_layout.addWidget(ok_btn)

    layout.addLayout(btn_layout)

    dialog.exec_()
    update_total_score_display()


reset_btn.clicked.connect(show_reset_dialog)
update_level_buttons()
update_total_score_display()

# ДАННЫЕ ДЛЯ РЕЖИМА "НА ВРЕМЯ"
time_words = {
    1: ("ОБРАЗОВАНИЕ",
        ["ЗОВ", "РОВ", "БОР", "БАР", "БРА", "РАЗ", "ВОЗ", "ВОР", "ИВА", "РАНА", "ВАЗА", "ВЕНА", "ВЕРА", "ВИЗА", "ВИНА",
         "ВОИН", "ЗВОН", "НЕБО", "НЕРВ", "НОРА", "НРАВ", "ОБОИ", "ВЕРБА", "БАЗАР", "БАРАН", "БАРИН", "БАРОН", "ВОРОН",
         "ЗАБОР", "ЗЕБРА", "ЗЕРНО", "ОБЗОР", "ОБРАЗ", "ОЗЕРО", "БРЕВНО", "БРОНЗА", "ВОРОНА", "ЗВАНИЕ"]),
    2: ("КАЛЕНДАРЬ",
        ["АД", "ДАР", "ЕДА", "ЕЛЬ", "АРКА", "ДАЛЬ", "ДАНЬ", "ДЕНЬ", "КАДР", "КАРЕ", "КЕДР", "КЛАД", "КЛАН", "КРАН",
         "ЛАНЬ", "РАДА", "РАК", "РАНА", "РЕКА", "АРЕАЛ", "АРЕНДА", "АРКАН", "ДЕКАН", "ДРАКА", "ДРЕЛЬ", "КАНАЛ", "НЕДРА",
         "ЛЕКАРЬ", "РЕДЬКА"]),
    3: ("СОДЕРЖАНИЕ",
        ["АД", "ДНО", "ЕДА", "НОЖ", "НОС", "ОСА", "РИС", "РОД", "САД", "СОН", "ДЖИН", "ЖАНР", "ЖЕНА", "НОРА", "ОРДА",
         "РЖА", "РОСА", "СЕНО", "СОДА", "АДРЕС", "ДЕСНА", "ДРАЖЕ", "НАРОД", "ОРДЕН", "ОСИНА", "РАДИО", "РЕДИС",
         "РОДИНА", "СЕДИНА", "СРАЖЕНИЕ"])
}

# ОКНО РЕЖИМА "НА ВРЕМЯ"
time_win = QMainWindow()
time_win.setWindowTitle("Слова из слова - Режим «На время»")
time_win.showFullScreen()
time_win.setStyleSheet("background-color: #fff5e6;")
time_win.setWindowIcon(QIcon("images/word.png"))

central_time = QWidget()
time_win.setCentralWidget(central_time)
v_time = QVBoxLayout(central_time)
v_time.setContentsMargins(20, 20, 20, 20)

top_time = QHBoxLayout()
top_time.setAlignment(Qt.AlignCenter)

back_time = QPushButton("назад")
back_time.setFixedSize(100, 40)
back_time.setFont(QFont("Arial", 16, QFont.Bold))
back_time.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 20px;")
top_time.addWidget(back_time)

top_time.addStretch()

timer_label = QLabel("Время 01:00")
timer_label.setFont(QFont("Arial", 24, QFont.Bold))
timer_label.setAlignment(Qt.AlignCenter)
timer_label.setStyleSheet("color: #ffb7b2;")
top_time.addWidget(timer_label)

top_time.addStretch()

right_panel = QVBoxLayout()
right_panel.setAlignment(Qt.AlignRight)
right_panel.setSpacing(5)

score_label_time = QLabel("⭐ 0")
score_label_time.setFont(QFont("Arial", 18, QFont.Bold))
score_label_time.setStyleSheet("color: #ffb7b2;")
right_panel.addWidget(score_label_time)

record_label_time = QLabel("🏆 0")
record_label_time.setFont(QFont("Arial", 14))
record_label_time.setStyleSheet("color: #d4a5a5;")
right_panel.addWidget(record_label_time)

top_time.addLayout(right_panel)
v_time.addLayout(top_time)

msg_label_time = QLabel("")
msg_label_time.setFont(QFont("Arial", 28, QFont.Bold))
msg_label_time.setAlignment(Qt.AlignCenter)
v_time.addWidget(msg_label_time)

found_label = QLabel("Найденные слова:")
found_label.setFont(QFont("Arial", 16, QFont.Bold))
found_label.setStyleSheet("color: #d4a5a5; margin-top: 10px;")
v_time.addWidget(found_label)

found_container = QWidget()
found_container.setFixedSize(650, 350)
found_container.setStyleSheet("background-color: #ffe4e9; border-radius: 10px;")
found_grid = QGridLayout(found_container)
found_grid.setSpacing(10)
found_grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
v_time.addWidget(found_container, alignment=Qt.AlignCenter)

v_time.addSpacing(30)

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
v_time.addLayout(h_letters_time)

# Переменные для режима на время
score_time = 0
found_words_time = []
current_word_time = ""
used_indices_time = []
record = 0
time_left = 60
timer = None
random_key = random.randint(1, 3)
main_word_time, target_words_time = time_words[random_key]


def show_msg_time(text, color):
    msg_label_time.setText(text)
    msg_label_time.setStyleSheet(f"color: {color}; font-size: 28px; font-weight: bold;")
    QTimer.singleShot(1500, lambda: msg_label_time.setText(""))


def update_score_time():
    score_label_time.setText(f"⭐ {score_time}")


def update_found_grid():
    for i in reversed(range(found_grid.count())):
        w = found_grid.itemAt(i).widget()
        if w:
            w.deleteLater()

    container_width = found_container.width()
    cols = max(5, container_width // 80)

    for i, w in enumerate(found_words_time):
        lbl = QLabel(w)
        lbl.setFont(QFont("Courier", 13, QFont.Bold))
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; padding: 5px 8px; border-radius: 10px;")
        found_grid.addWidget(lbl, i // cols, i % cols)


def update_letters_time():
    for i, btn in enumerate(letter_btns_time):
        if i in used_indices_time:
            btn.setEnabled(False)
            btn.setStyleSheet("background-color: #d4d4d4; color: #999999; border-radius: 30px;")
        else:
            btn.setEnabled(True)
            btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")


def add_letter_time(idx):
    global current_word_time
    if idx not in used_indices_time:
        current_word_time += main_word_time[idx].lower()
        used_indices_time.append(idx)
        current_word_label_time.setText(" ".join(current_word_time.upper()))
        update_letters_time()


def clear_word_time():
    global current_word_time, used_indices_time
    current_word_time = ""
    used_indices_time = []
    current_word_label_time.setText("")
    update_letters_time()


def check_word_time():
    global score_time, current_word_time, record
    word = current_word_time.upper()
    if not word:
        show_msg_time("Собери слово!", "red")
        return
    if word not in target_words_time:
        show_msg_time(f"'{word}' нет в списке!", "red")
        clear_word_time()
        return
    if word in found_words_time:
        show_msg_time(f"'{word}' уже найдено!", "orange")
        clear_word_time()
        return
    if Counter(word) <= Counter(main_word_time):
        score_time += len(word)
        found_words_time.append(word)
        update_score_time()
        update_found_grid()
        clear_word_time()
        show_msg_time(f"+{len(word)} очков!", "green")
        if score_time > record:
            record = score_time
            save_record()
            record_label_time.setText(f"🏆 {record}")
    else:
        show_msg_time("Нельзя составить!", "red")
        clear_word_time()


clear_time.clicked.connect(clear_word_time)
check_time.clicked.connect(check_word_time)

# Создаём буквы
letter_btns_time = []
for i, letter in enumerate(main_word_time):
    b = QPushButton(letter)
    b.setFixedSize(60, 60)
    b.setFont(QFont("Arial", 18, QFont.Bold))
    b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
    b.clicked.connect(lambda checked, idx=i: add_letter_time(idx))
    h_letters_time.addWidget(b)
    letter_btns_time.append(b)


def start_timer():
    global timer
    timer = QTimer()
    timer.timeout.connect(update_timer)
    timer.start(1000)


def update_timer():
    global time_left, timer
    time_left -= 1
    minutes = time_left // 60
    seconds = time_left % 60
    timer_label.setText(f"Время {minutes:02d}:{seconds:02d}")
    if time_left <= 0:
        timer.stop()
        time_out()


def time_out():
    global timer, score_time, record
    if timer:
        timer.stop()

    dialog = QDialog(time_win)
    dialog.setWindowTitle("Время вышло!")
    dialog.setFixedSize(450, 320)
    dialog.setModal(True)
    dialog.setWindowIcon(QIcon("images/word.png"))
    dialog.setStyleSheet("background-color: #fff5e6;")

    layout = QVBoxLayout(dialog)
    layout.setSpacing(20)
    layout.setContentsMargins(30, 30, 30, 30)

    title = QLabel("ВРЕМЯ ВЫШЛО!")
    title.setFont(QFont("Arial", 22, QFont.Bold))
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet("color: #ffb7b2;")
    layout.addWidget(title)

    score_label = QLabel(f"Ваши очки: {score_time}")
    score_label.setFont(QFont("Arial", 16, QFont.Bold))
    score_label.setAlignment(Qt.AlignCenter)
    score_label.setStyleSheet("color: #6b9e8a;")
    layout.addWidget(score_label)

    record_label = QLabel(f"Рекорд: {record}")
    record_label.setFont(QFont("Arial", 14))
    record_label.setAlignment(Qt.AlignCenter)
    record_label.setStyleSheet("color: #c77d7d;")
    layout.addWidget(record_label)

    if score_time > record and score_time > 0:
        new_record_label = QLabel("🎉 НОВЫЙ РЕКОРД! 🎉")
        new_record_label.setFont(QFont("Arial", 14, QFont.Bold))
        new_record_label.setAlignment(Qt.AlignCenter)
        new_record_label.setStyleSheet("color: #ffb7b2;")
        layout.addWidget(new_record_label)

    layout.addSpacing(20)

    btn_layout = QHBoxLayout()
    btn_layout.setAlignment(Qt.AlignCenter)
    btn_layout.setSpacing(20)

    result = [0]

    again_btn = QPushButton("Сыграть снова")
    again_btn.setFixedSize(200, 45)
    again_btn.setFont(QFont("Arial", 12, QFont.Bold))
    again_btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 20px;")
    again_btn.clicked.connect(lambda: [dialog.done(1), result.__setitem__(0, 1)])
    btn_layout.addWidget(again_btn)

    menu_btn = QPushButton("В главное меню")
    menu_btn.setFixedSize(200, 45)
    menu_btn.setFont(QFont("Arial", 12, QFont.Bold))
    menu_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 20px;")
    menu_btn.clicked.connect(lambda: [dialog.done(2), result.__setitem__(0, 2)])
    btn_layout.addWidget(menu_btn)

    layout.addLayout(btn_layout)

    for btn in letter_btns_time:
        btn.setEnabled(False)
    clear_time.setEnabled(False)
    check_time.setEnabled(False)

    dialog.exec_()

    if result[0] == 1:
        restart_game()
    elif result[0] == 2:
        close_time_mode()


def restart_game():
    global random_key, main_word_time, target_words_time, score_time, found_words_time, current_word_time, used_indices_time, time_left, timer, record, letter_btns_time

    random_key = random.randint(1, 3)
    main_word_time, target_words_time = time_words[random_key]
    score_time = 0
    found_words_time = []
    current_word_time = ""
    used_indices_time = []
    time_left = 60

    update_score_time()
    update_found_grid()
    clear_word_time()
    record_label_time.setText(f"🏆 {record}")

    for i in reversed(range(h_letters_time.count())):
        w = h_letters_time.itemAt(i).widget()
        if w:
            w.deleteLater()

    letter_btns_time = []
    for i, letter in enumerate(main_word_time):
        b = QPushButton(letter)
        b.setFixedSize(60, 60)
        b.setFont(QFont("Arial", 18, QFont.Bold))
        b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
        b.clicked.connect(lambda checked, idx=i: add_letter_time(idx))
        h_letters_time.addWidget(b)
        letter_btns_time.append(b)

    timer_label.setText("Время 01:00")
    if timer:
        timer.stop()
    timer = QTimer()
    timer.timeout.connect(update_timer)
    timer.start(1000)
    clear_time.setEnabled(True)
    check_time.setEnabled(True)


def reset_time_mode():
    restart_game()


load_record()
start_timer()

# ДАННЫЕ ДЛЯ УРОВНЕЙ
levels_data = {
    1: {"word": "БОТИНОК", "target": ["ТОК", "КОТ", "КИТ", "БОТ", "БОК", "БИНТ", "КИНО", "ОКНО"]},
    2: {"word": "ПРОГРАММА", "target": ["РОГ", "МАГ", "РАМА", "ГОРА", "МАМА", "ПОРА", "ГРАММ", "ГАММА", "МРАМОР"]},
    3: {"word": "РЕГИСТРАЦИЯ",
        "target": ["ГИТ", "РИС", "АИСТ", "ГИРЯ", "ИГРА", "СТАЯ", "ТИГР", "РАЦИЯ", "АРЕСТ", "ГРАЦИЯ", "СТАРЕЦ",
                   "РЕГИСТР"]}
}


# ФУНКЦИЯ ДЛЯ ДИАЛОГА ПОСЛЕ УРОВНЯ
def show_level_complete_dialog(level_num, win, score):
    dialog = QDialog(win)
    dialog.setWindowTitle("Уровень пройден!")
    dialog.setFixedSize(450, 300)
    dialog.setModal(True)
    dialog.setWindowIcon(QIcon("images/word.png"))
    dialog.setStyleSheet("background-color: #fff5e6;")

    layout = QVBoxLayout(dialog)
    layout.setSpacing(20)
    layout.setContentsMargins(30, 30, 30, 30)

    title = QLabel("УРОВЕНЬ ПРОЙДЕН!")
    title.setFont(QFont("Arial", 22, QFont.Bold))
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet("color: #ffb7b2;")
    layout.addWidget(title)

    msg = QLabel(f"Вы прошли уровень {level_num}!")
    msg.setFont(QFont("Arial", 16, QFont.Bold))
    msg.setAlignment(Qt.AlignCenter)
    msg.setStyleSheet("color: #6b9e8a;")
    layout.addWidget(msg)

    score_label = QLabel(f"Набрано очков: {score}")
    score_label.setFont(QFont("Arial", 14, QFont.Bold))
    score_label.setAlignment(Qt.AlignCenter)
    score_label.setStyleSheet("color: #c77d7d;")
    layout.addWidget(score_label)

    layout.addSpacing(20)

    btn_layout = QHBoxLayout()
    btn_layout.setAlignment(Qt.AlignCenter)
    btn_layout.setSpacing(20)

    result = [0]

    if level_num < 3:
        next_btn = QPushButton("След. уровень")
        next_btn.setFixedSize(200, 45)
        next_btn.setFont(QFont("Arial", 12, QFont.Bold))
        next_btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 20px;")
        next_btn.clicked.connect(lambda: [dialog.done(1), result.__setitem__(0, 1)])
        btn_layout.addWidget(next_btn)

    menu_btn = QPushButton("В главное меню")
    menu_btn.setFixedSize(200, 45)
    menu_btn.setFont(QFont("Arial", 12, QFont.Bold))
    menu_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 20px;")
    menu_btn.clicked.connect(lambda: [dialog.done(2), result.__setitem__(0, 2)])
    btn_layout.addWidget(menu_btn)

    layout.addLayout(btn_layout)

    dialog.exec_()

    return result[0]


# ОКНО УРОВНЯ (общая функция)
def create_level_window(level_num):
    win = QMainWindow()
    win.setWindowTitle(f"Слова из слова - Уровень {level_num}")
    win.showFullScreen()
    win.setStyleSheet("background-color: #fff5e6;")
    win.setWindowIcon(QIcon("images/word.png"))

    central = QWidget()
    win.setCentralWidget(central)
    v = QVBoxLayout(central)
    v.setContentsMargins(20, 20, 20, 20)

    progress_data = load_levels_progress()
    score = progress_data.get("scores", {}).get(str(level_num), 0)
    found = progress_data.get("found", {}).get(str(level_num), [])

    top = QHBoxLayout()
    back = QPushButton("назад")
    back.setFixedSize(100, 40)
    back.setFont(QFont("Arial", 16, QFont.Bold))
    back.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 20px;")
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
    word_labels = []
    for w in words:
        lbl = QLabel(" ".join(["-"] * len(w)))
        lbl.setFont(QFont("Courier", 20, QFont.Bold))
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")
        lbl.setFixedWidth(len(w) * 50)
        v.addWidget(lbl, alignment=Qt.AlignCenter)
        word_labels.append(lbl)

    v.addStretch()

    current_word = ""
    used_indices = []
    current_score = score
    found_words = found.copy()

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
    for i, letter in enumerate(main_word):
        b = QPushButton(letter)
        b.setFixedSize(60, 60)
        b.setFont(QFont("Arial", 18, QFont.Bold))
        b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
        b.clicked.connect(lambda checked, idx=i: add_letter(idx))
        h_letters.addWidget(b)
        letter_btns.append(b)
    v.addLayout(h_letters)

    def show_msg(txt, col):
        msg_lbl.setText(txt)
        msg_lbl.setStyleSheet(f"color: {col}; font-size: 28px; font-weight: bold;")
        QTimer.singleShot(1500, lambda: msg_lbl.setText(""))

    def update_score():
        score_lbl.setText(f"⭐ {current_score}")

    def update_words():
        for i, w in enumerate(words):
            if w in found_words:
                word_labels[i].setText(" ".join(w))
                word_labels[i].setStyleSheet(
                    "background-color: #a8e6cf; color: #6b9e8a; padding: 8px; border-radius: 10px;")
            else:
                word_labels[i].setText(" ".join(["-"] * len(w)))
                word_labels[i].setStyleSheet(
                    "background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")

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
        nonlocal current_score, current_word
        word = current_word.upper()
        if not word:
            show_msg("Собери слово!", "red")
            return
        if word not in words:
            show_msg(f"'{word}' нет в списке!", "red")
            clear_word()
            return
        if word in found_words:
            show_msg(f"'{word}' уже найдено!", "orange")
            clear_word()
            return
        if Counter(word) <= Counter(main_word):
            current_score += len(word)
            found_words.append(word)
            update_score()
            update_words()
            clear_word()
            show_msg(f"+{len(word)} очков!", "green")

            progress = load_levels_progress()
            progress["scores"][str(level_num)] = current_score
            progress["found"][str(level_num)] = found_words
            save_levels_progress(progress)
            update_total_score_display()

            if len(found_words) >= len(words):
                show_msg("УРОВЕНЬ ПРОЙДЕН!", "blue")

                next_level_num = level_num + 1
                if next_level_num <= 3:
                    progress = load_levels_progress()
                    if next_level_num not in progress.get("unlocked", []):
                        progress["unlocked"].append(next_level_num)
                        progress["unlocked"].sort()
                        save_levels_progress(progress)
                        update_level_buttons()
                        update_total_score_display()

                result = show_level_complete_dialog(level_num, win, current_score)

                if result == 1:
                    if level_num == 1:
                        to_level2()
                    elif level_num == 2:
                        to_level3()
                    return
                elif result == 2:
                    levels_win.show()
                    return
        else:
            show_msg("Нельзя составить!", "red")
            clear_word()
            return

    for i, btn in enumerate(letter_btns):
        btn.clicked.connect(lambda checked, idx=i: add_letter(idx))
    clear_btn.clicked.connect(clear_word)
    check_btn.clicked.connect(check_word)

    def back_to_levels():
        win.hide()
        levels_win.show()

    back.clicked.connect(back_to_levels)

    update_score()
    update_words()

    return win


# ========== СОЗДАЁМ ОКНА УРОВНЕЙ ==========
level1_win = create_level_window(1)
level2_win = create_level_window(2)
level3_win = create_level_window(3)


# ПЕРЕХОДЫ
def to_levels():
    main_win.hide()
    levels_win.show()
    update_total_score_display()


def back_to_main():
    levels_win.hide()
    main_win.show()


def to_level1():
    global level1_win
    level1_win = create_level_window(1)
    levels_win.hide()
    level1_win.show()


def to_level2():
    global level2_win
    level2_win = create_level_window(2)
    levels_win.hide()
    level2_win.show()


def to_level3():
    global level3_win
    level3_win = create_level_window(3)
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
    global score_time, found_words_time, current_word_time, used_indices_time, time_left, random_key, main_word_time, target_words_time, timer

    random_key = random.randint(1, 3)
    main_word_time, target_words_time = time_words[random_key]
    score_time = 0
    found_words_time = []
    current_word_time = ""
    used_indices_time = []
    time_left = 60

    update_score_time()
    update_found_grid()
    clear_word_time()
    record_label_time.setText(f"🏆 {record}")

    for i in reversed(range(h_letters_time.count())):
        w = h_letters_time.itemAt(i).widget()
        if w:
            w.deleteLater()

    letter_btns_time.clear()
    for i, letter in enumerate(main_word_time):
        b = QPushButton(letter)
        b.setFixedSize(60, 60)
        b.setFont(QFont("Arial", 18, QFont.Bold))
        b.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
        b.clicked.connect(lambda checked, idx=i: add_letter_time(idx))
        h_letters_time.addWidget(b)
        letter_btns_time.append(b)

    timer_label.setText("Время 01:00")
    if timer:
        timer.stop()
    timer = QTimer()
    timer.timeout.connect(update_timer)
    timer.start(1000)

    clear_time.setEnabled(True)
    check_time.setEnabled(True)

    levels_win.hide()
    time_win.show()


def close_time_mode():
    time_win.hide()
    levels_win.show()
    update_total_score_display()


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