import sys
import json
import os
import random
from collections import Counter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap

app = QApplication(sys.argv)

def close_on_esc(window):
    shortcut = QShortcut(Qt.Key_Escape, window)
    shortcut.activated.connect(app.quit)

# МАСШТАБИРОВАНИЕ
def get_screen_size():
    screen = app.primaryScreen()
    size = screen.availableGeometry()
    return size.width(), size.height()


SCREEN_W, SCREEN_H = get_screen_size()
BASE_W, BASE_H = 800, 600
SCALE = min(SCREEN_W / BASE_W, SCREEN_H / BASE_H)


def scale(w, h):
    return int(w * SCALE), int(h * SCALE)


def scale_font(size):
    return int(size * SCALE)


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

close_on_esc(main_win)

central = QWidget()
main_win.setCentralWidget(central)
layout = QVBoxLayout(central)
layout.setAlignment(Qt.AlignCenter)
layout.setSpacing(scale_font(40))

title = QLabel("СЛОВА ИЗ СЛОВА")
title.setFont(QFont("Arial", scale_font(48), QFont.Bold))
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("color: #ffb7b2;")
layout.addWidget(title)

h1 = QHBoxLayout()
h1.setAlignment(Qt.AlignCenter)
play_btn = QPushButton("ИГРАТЬ")
play_btn.setFixedSize(*scale(300, 60))
play_btn.setFont(QFont("Arial", scale_font(18), QFont.Bold))
play_btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(30)}px;")
h1.addWidget(play_btn)
layout.addLayout(h1)

h2 = QHBoxLayout()
h2.setAlignment(Qt.AlignCenter)
exit_btn = QPushButton("ВЫХОД")
exit_btn.setFixedSize(*scale(200, 50))
exit_btn.setFont(QFont("Arial", scale_font(16)))
exit_btn.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(25)}px;")
h2.addWidget(exit_btn)
layout.addLayout(h2)

# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ
levels_win = None
btn1 = btn2 = btn3 = None
back_btn = None
total_score_label = None
reset_btn = None
time_btn = None


def create_levels_window():
    global levels_win, btn1, btn2, btn3, back_btn, total_score_label, reset_btn, time_btn

    levels_win = QMainWindow()
    levels_win.setWindowTitle("Слова из слова - Выбор уровня")
    levels_win.showFullScreen()
    levels_win.setStyleSheet("background-color: #fff5e6;")
    levels_win.setWindowIcon(QIcon("images/word.png"))

    close_on_esc(levels_win)

    central2 = QWidget()
    levels_win.setCentralWidget(central2)
    v2 = QVBoxLayout(central2)
    v2.setContentsMargins(scale(20, 20)[0], scale(20, 20)[1],
                          scale(20, 20)[0], scale(20, 20)[1])

    top = QHBoxLayout()
    back_btn = QPushButton("назад")
    back_btn.setFixedSize(*scale(100, 40))
    back_btn.setFont(QFont("Arial", scale_font(16), QFont.Bold))
    back_btn.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(20)}px;")
    top.addWidget(back_btn)
    top.addStretch()

    total_score_label = QLabel("⭐ 0")
    total_score_label.setFont(QFont("Arial", scale_font(18), QFont.Bold))
    total_score_label.setStyleSheet("color: #ffb7b2;")
    top.addWidget(total_score_label)

    v2.addLayout(top)

    v2.addStretch()
    title2 = QLabel("ВЫБЕРИ УРОВЕНЬ")
    title2.setFont(QFont("Arial", scale_font(36), QFont.Bold))
    title2.setAlignment(Qt.AlignCenter)
    title2.setStyleSheet("color: #ffb7b2;")
    v2.addWidget(title2)

    v2.addSpacing(scale_font(50))

    h_levels = QHBoxLayout()
    h_levels.setAlignment(Qt.AlignCenter)
    h_levels.setSpacing(scale_font(30))

    btn1 = QPushButton("1")
    btn2 = QPushButton("2")
    btn3 = QPushButton("3")
    for btn in [btn1, btn2, btn3]:
        btn.setFixedSize(*scale(100, 100))
        btn.setFont(QFont("Arial", scale_font(32), QFont.Bold))
        btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(50)}px;")
        h_levels.addWidget(btn)

    v2.addLayout(h_levels)

    v2.addSpacing(scale_font(20))

    time_btn = QPushButton("Режим \"На время\"")
    time_btn.setFixedSize(*scale(340, 50))
    time_btn.setFont(QFont("Arial", scale_font(14), QFont.Bold))
    time_btn.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(25)}px;")
    v2.addWidget(time_btn, alignment=Qt.AlignCenter)

    v2.addStretch()

    bottom = QHBoxLayout()
    bottom.setAlignment(Qt.AlignRight)

    reset_btn = QPushButton("Сбросить прогресс")
    reset_btn.setFixedSize(*scale(230, 40))
    reset_btn.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    reset_btn.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(20)}px")
    bottom.addWidget(reset_btn)
    v2.addLayout(bottom)

    update_level_buttons()
    update_total_score_display()

    back_btn.clicked.connect(back_to_main)
    reset_btn.clicked.connect(show_reset_dialog)
    btn1.clicked.connect(to_level1)
    btn2.clicked.connect(to_level2)
    btn3.clicked.connect(to_level3)
    time_btn.clicked.connect(open_time_mode)


def update_level_buttons():
    if btn1 is None:
        return
    progress = load_levels_progress()
    unlocked = progress.get("unlocked", [1])
    for i, btn in enumerate([btn1, btn2, btn3], 1):
        if i in unlocked:
            btn.setEnabled(True)
            btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(50)}px;")
        else:
            btn.setEnabled(False)
            btn.setStyleSheet(f"background-color: #d4d4d4; color: #999; border-radius: {scale_font(50)}px;")


def update_total_score_display():
    if total_score_label is None:
        return
    total = get_total_score()
    total_score_label.setText(f"⭐ {total}/145")


def show_reset_dialog():
    dialog = QDialog(levels_win)
    dialog.setWindowTitle("Сброс прогресса")
    dialog.setFixedSize(*scale(550, 200))
    dialog.setModal(True)
    dialog.setWindowIcon(QIcon("images/word.png"))
    dialog.setStyleSheet("background-color: #fff5e6;")

    layout = QVBoxLayout(dialog)
    layout.setSpacing(scale_font(15))
    layout.setContentsMargins(scale(25, 25)[0], scale(20, 20)[1],
                              scale(25, 25)[0], scale(20, 20)[1])

    question = QLabel("Вы уверены, что хотите сбросить весь прогресс?")
    question.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    question.setWordWrap(True)
    question.setStyleSheet("color: #6b9e8a;")
    layout.addWidget(question)

    warn_layout = QHBoxLayout()
    warn_layout.setAlignment(Qt.AlignCenter)
    warn_layout.setSpacing(scale_font(5))

    icon = QLabel()
    pixmap = QPixmap("images/question.png")
    if not pixmap.isNull():
        pixmap = pixmap.scaled(scale(48, 48)[0], scale(48, 48)[1],
                               Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon.setPixmap(pixmap)
    warn_layout.addWidget(icon)

    warning = QLabel("Все очки и разблокированные уровни будут потеряны")
    warning.setFont(QFont("Arial", scale_font(12)))
    warning.setWordWrap(True)
    warning.setStyleSheet("color: #c77d7d;")
    warn_layout.addWidget(warning, 1)

    layout.addLayout(warn_layout)

    btn_layout = QHBoxLayout()
    btn_layout.setAlignment(Qt.AlignCenter)
    btn_layout.setSpacing(scale_font(30))

    yes_btn = QPushButton("ДА")
    yes_btn.setFixedSize(*scale(100, 40))
    yes_btn.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    yes_btn.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(20)}px;")
    yes_btn.clicked.connect(lambda: dialog.done(QMessageBox.Yes))
    btn_layout.addWidget(yes_btn)

    no_btn = QPushButton("НЕТ")
    no_btn.setFixedSize(*scale(100, 40))
    no_btn.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    no_btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(20)}px;")
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
    dialog.setFixedSize(*scale(430, 180))
    dialog.setModal(True)
    dialog.setWindowIcon(QIcon("images/word.png"))
    dialog.setStyleSheet("background-color: #fff5e6;")

    layout = QVBoxLayout(dialog)
    layout.setSpacing(scale_font(15))
    layout.setContentsMargins(scale(25, 25)[0], scale(20, 20)[1],
                              scale(25, 25)[0], scale(20, 20)[1])

    top_layout = QHBoxLayout()
    top_layout.setSpacing(scale_font(15))

    icon = QLabel()
    pixmap = QPixmap("images/success.png")
    if not pixmap.isNull():
        pixmap = pixmap.scaled(scale(32, 32)[0], scale(32, 32)[1],
                               Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon.setPixmap(pixmap)
    top_layout.addWidget(icon)

    text = QLabel("Весь прогресс был успешно сброшен.")
    text.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    text.setWordWrap(True)
    text.setStyleSheet("color: #6b9e8a;")
    top_layout.addWidget(text, 1)

    layout.addLayout(top_layout)

    text2 = QLabel("Теперь вы начинаете игру с первого уровня.")
    text2.setFont(QFont("Arial", scale_font(11)))
    text2.setAlignment(Qt.AlignCenter)
    text2.setWordWrap(True)
    text2.setStyleSheet("color: #c77d7d;")
    layout.addWidget(text2)

    btn_layout = QHBoxLayout()
    btn_layout.setAlignment(Qt.AlignCenter)

    ok_btn = QPushButton("ОК")
    ok_btn.setFixedSize(*scale(100, 40))
    ok_btn.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    ok_btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(20)}px;")
    ok_btn.clicked.connect(dialog.accept)
    btn_layout.addWidget(ok_btn)

    layout.addLayout(btn_layout)

    dialog.exec_()
    update_total_score_display()


# ДАННЫЕ ДЛЯ РЕЖИМА "НА ВРЕМЯ"
time_words = {
    1: ("ОБРАЗОВАНИЕ",
        ["ЗОВ", "РОВ", "БОР", "БАР", "БРА", "РАЗ", "ВОЗ", "ВОР", "ИВА", "НИЗ", "РАНА", "ВАЗА", "ВЕНА", "ВЕРА", "ВИЗА", "ВИНА", "ВИНО", "ЗОНА", "РОЗА",
         "ВОИН", "ЗВОН", "НЕБО", "НЕРВ", "НОРА", "НРАВ", "ОЗОН", "ОБОИ","ВЗОР", "НАВОЗ", "ВЕРБА", "БРАВО", "БАЗАР", "БАРАН", "БАРИН", "БАРОН", "ВОРОН",
          "ВАРАН","ЗАБОР", "ЗЕБРА", "ЗЕРНО", "ОБЗОР", "ОБРАЗ", "ОЗЕРО", "БРЕВНО", "БРОНЗА", "ВОРОНА", "ЗВАНИЕ"]),
    2: ("КАЛЕНДАРЬ",
        ["АД", "КАЛ", "ДАР", "ЕДА", "ЕЛЬ", "АРКА", "ДАЛЬ", "ДАНЬ", "ДЕНЬ", "КАДР", "КАРЕ", "КЕДР", "КЛАД", "КЛАН", "КРАН", "КАРА",
         "ЛАНЬ", "ЛАРЬ", "ЛЕНЬ", "РАДА", "РАК", "РАНА", "РЕКА", "АРЕАЛ", "АРКАН", "ДЕКАН", "ДРАКА", "ДРЕЛЬ", "КАНАЛ", "НЕДРА",
         "ЛЕКАРЬ", "АРЕНДА", "РЕДЬКА"]),
    3: ("СОДЕРЖАНИЕ",
        ["АД", "ОР", "СОР", "ДАР", "ДНО", "ЕДА", "НОЖ", "НОС", "ОСА", "РИС", "РОД", "САД", "СОН", "ЖАР", "ЖИР", "ЖОР", "РОЖА", "ДЖИН", "ЖАНР", "ЖЕНА",
         "НОРА", "ОРДА", "РЖА", "РОСА", "СОРА", "СЕНО", "СОДА", "АДРЕС", "ДЕСНА", "ДРАЖЕ", "ДРЕНАЖ", "НАРОД", "ОРДЕН", "ОСИНА", "РАДИО", "РЕДИС",
         "РОДИНА", "СЕДИНА", "РЖАНИЕ", "СРАЖЕНИЕ"])
}

# ОКНО РЕЖИМА "НА ВРЕМЯ"
time_win = None
back_time = None
timer_label = None
score_label_time = None
record_label_time = None
msg_label_time = None
found_container_time = None
found_layout_time = None
current_word_label_time = None
clear_time = None
check_time = None
h_letters_time = None
letter_btns_time = []
score_time = 0
found_words_time = []
current_word_time = ""
used_indices_time = []
record = 0
time_left = 60
timer = None
random_key = 1
main_word_time = ""
target_words_time = []


def create_time_window():
    global time_win, back_time, timer_label, score_label_time, record_label_time
    global msg_label_time, found_container_time, found_layout_time, current_word_label_time
    global clear_time, check_time, h_letters_time, letter_btns_time

    time_win = QMainWindow()
    time_win.setWindowTitle("Слова из слова - Режим «На время»")
    time_win.showFullScreen()
    time_win.setStyleSheet("background-color: #fff5e6;")
    time_win.setWindowIcon(QIcon("images/word.png"))

    close_on_esc(time_win)

    central_time = QWidget()
    time_win.setCentralWidget(central_time)
    v_time = QVBoxLayout(central_time)
    v_time.setSpacing(scale_font(10))
    v_time.setContentsMargins(scale(30, 30)[0], scale(15, 15)[1],
                              scale(30, 30)[0], scale(15, 15)[1])

    # Верхняя панель
    top_time = QHBoxLayout()
    top_time.setAlignment(Qt.AlignCenter)

    back_time = QPushButton("назад")
    back_time.setFixedSize(*scale(100, 40))
    back_time.setFont(QFont("Arial", scale_font(16), QFont.Bold))
    back_time.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(20)}px;")
    top_time.addWidget(back_time)

    top_time.addStretch()

    timer_label = QLabel("Время 01:00")
    timer_label.setFont(QFont("Arial", scale_font(22), QFont.Bold))
    timer_label.setAlignment(Qt.AlignCenter)
    timer_label.setStyleSheet("color: #ffb7b2;")
    top_time.addWidget(timer_label)

    top_time.addStretch()

    right_panel = QVBoxLayout()
    right_panel.setAlignment(Qt.AlignRight)
    right_panel.setSpacing(scale_font(3))

    score_label_time = QLabel("⭐ 0")
    score_label_time.setFont(QFont("Arial", scale_font(16), QFont.Bold))
    score_label_time.setStyleSheet("color: #ffb7b2;")
    right_panel.addWidget(score_label_time)

    record_label_time = QLabel("🏆 0")
    record_label_time.setFont(QFont("Arial", scale_font(13)))
    record_label_time.setStyleSheet("color: #d4a5a5;")
    right_panel.addWidget(record_label_time)

    top_time.addLayout(right_panel)
    v_time.addLayout(top_time)

    # Сообщение
    msg_label_time = QLabel("")
    msg_label_time.setFont(QFont("Arial", scale_font(24), QFont.Bold))
    msg_label_time.setAlignment(Qt.AlignCenter)
    msg_label_time.setMinimumHeight(scale_font(40))
    v_time.addWidget(msg_label_time)

    found_title = QLabel("Найденные слова:")
    found_title.setFont(QFont("Arial", scale_font(14), QFont.Bold))
    found_title.setStyleSheet("color: #d4a5a5;")
    v_time.addWidget(found_title)

    found_container_time = QWidget()
    found_container_time.setStyleSheet("background-color: #ffe4e9; border-radius: 15px;")
    found_container_time.setFixedWidth(scale_font(400))
    found_layout_time = QGridLayout(found_container_time)
    found_layout_time.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    found_layout_time.setSpacing(scale_font(8))
    found_layout_time.setContentsMargins(scale(10, 10)[0], scale(10, 10)[1],
                                         scale(10, 10)[0], scale(10, 10)[1])

    found_scroll = QScrollArea()
    found_scroll.setWidgetResizable(True)
    found_scroll.setStyleSheet("""
        QScrollArea {
            background-color: #ffe4e9;
            border-radius: 15px;
            border: none;
        }
        QScrollBar:vertical {
            background: #ffe4e9;
            width: 8px;
            border-radius: 4px;
        }
        QScrollBar::handle:vertical {
            background: #c77d7d;
            border-radius: 4px;
        }
    """)
    found_scroll.setWidget(found_container_time)
    found_scroll.setFixedHeight(scale_font(180))
    found_scroll.setFixedWidth(scale_font(400))
    v_time.addWidget(found_scroll, alignment=Qt.AlignCenter)

    v_time.addSpacing(scale_font(5))

    # Текущее слово
    current_word_label_time = QLabel("")
    current_word_label_time.setFont(QFont("Courier", scale_font(32), QFont.Bold))
    current_word_label_time.setAlignment(Qt.AlignCenter)
    current_word_label_time.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 12px; border-radius: 15px;")
    current_word_label_time.setMinimumHeight(scale_font(60))
    v_time.addWidget(current_word_label_time)

    # Кнопки действий
    h_actions = QHBoxLayout()
    h_actions.setAlignment(Qt.AlignCenter)
    h_actions.setSpacing(scale_font(25))

    clear_time = QPushButton("✖")
    clear_time.setFixedSize(*scale(65, 65))
    clear_time.setFont(QFont("Arial", scale_font(30)))
    clear_time.setStyleSheet(f"""
        QPushButton {{
            background-color: #ffb7b2;
            color: white;
            border-radius: {scale_font(32)}px;
        }}
    """)
    h_actions.addWidget(clear_time)

    check_time = QPushButton("✓")
    check_time.setFixedSize(*scale(65, 65))
    check_time.setFont(QFont("Arial", scale_font(30)))
    check_time.setStyleSheet(f"""
        QPushButton {{
            background-color: #a8e6cf;
            color: white;
            border-radius: {scale_font(32)}px;
        }}
    """)
    h_actions.addWidget(check_time)

    v_time.addLayout(h_actions)

    v_time.addSpacing(scale_font(5))

    hint = QLabel("Составь слово из букв:")
    hint.setFont(QFont("Arial", scale_font(12)))
    hint.setStyleSheet("color: #d4a5a5;")
    v_time.addWidget(hint)

    # Буквы
    letters_widget = QWidget()
    h_letters_time = QHBoxLayout(letters_widget)
    h_letters_time.setAlignment(Qt.AlignCenter)
    h_letters_time.setSpacing(scale_font(8))
    h_letters_time.setContentsMargins(scale(5, 5)[0], scale(5, 5)[1],
                                      scale(5, 5)[0], scale(5, 5)[1])

    letters_scroll = QScrollArea()
    letters_scroll.setWidgetResizable(True)
    letters_scroll.setStyleSheet("background: transparent; border: none;")
    letters_scroll.setMaximumHeight(scale_font(80))
    letters_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    letters_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    letters_scroll.setWidget(letters_widget)
    v_time.addWidget(letters_scroll)

    clear_time.clicked.connect(clear_word_time)
    check_time.clicked.connect(check_word_time)
    back_time.clicked.connect(close_time_mode)


def update_found_words_display():
    if found_layout_time is None:
        return

    for i in reversed(range(found_layout_time.count())):
        w = found_layout_time.itemAt(i).widget()
        if w:
            w.deleteLater()

    cols = 6
    for i, word in enumerate(found_words_time):
        lbl = QLabel(word)
        lbl.setFont(QFont("Courier", scale_font(14), QFont.Bold))
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet(f"""
            background-color: #a8e6cf;
            color: #6b9e8a;
            padding: {scale_font(5)}px {scale_font(10)}px;
            border-radius: {scale_font(10)}px;
        """)
        found_layout_time.addWidget(lbl, i // cols, i % cols)


def show_msg_time(text, color):
    if msg_label_time:
        msg_label_time.setText(text)
        msg_label_time.setStyleSheet(f"color: {color}; font-size: {scale_font(24)}px; font-weight: bold;")
        QTimer.singleShot(1500, lambda: msg_label_time.setText(""))


def add_letter_time(idx):
    global current_word_time, used_indices_time
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


def update_letters_time():
    for i, btn in enumerate(letter_btns_time):
        if i in used_indices_time:
            btn.setEnabled(False)
            btn.setStyleSheet(f"background-color: #d4d4d4; color: #999; border-radius: {scale_font(27)}px;")
        else:
            btn.setEnabled(True)
            btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(27)}px;")


def check_word_time():
    global score_time, current_word_time, record, found_words_time
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
        update_found_words_display()
        # ОБНОВЛЯЕМ ОТОБРАЖЕНИЕ СЧЁТА
        if score_label_time:
            score_label_time.setText(f"⭐ {score_time}")
        clear_word_time()
        show_msg_time(f"+{len(word)} очков!", "green")
        if score_time > record:
            record = score_time
            save_record()
            if record_label_time:
                record_label_time.setText(f"🏆 {record}")
        if len(found_words_time) >= len(target_words_time):
            show_msg_time("ВСЕ СЛОВА НАЙДЕНЫ! 🎉", "#6b9e8a")
            QTimer.singleShot(2000, restart_game)
    else:
        show_msg_time("Нельзя составить!", "red")
        clear_word_time()


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
        timer = None
    if time_win is None or not time_win.isVisible():
        return

    for btn in letter_btns_time:
        btn.setEnabled(False)
    clear_time.setEnabled(False)
    check_time.setEnabled(False)

    dialog = QDialog(time_win)
    dialog.setWindowTitle("Время вышло!")
    dialog.setFixedSize(*scale(450, 320))
    dialog.setModal(True)
    dialog.setStyleSheet("background-color: #fff5e6;")

    layout = QVBoxLayout(dialog)
    layout.setSpacing(scale_font(20))
    layout.setContentsMargins(scale(30, 30)[0], scale(30, 30)[1], scale(30, 30)[0], scale(30, 30)[1])

    title = QLabel("ВРЕМЯ ВЫШЛО!")
    title.setFont(QFont("Arial", scale_font(22), QFont.Bold))
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet("color: #ffb7b2;")
    layout.addWidget(title)

    score_lbl = QLabel(f"Ваши очки: {score_time}")
    score_lbl.setFont(QFont("Arial", scale_font(16), QFont.Bold))
    score_lbl.setAlignment(Qt.AlignCenter)
    score_lbl.setStyleSheet("color: #6b9e8a;")
    layout.addWidget(score_lbl)

    record_lbl = QLabel(f"Рекорд: {record}")
    record_lbl.setFont(QFont("Arial", scale_font(14)))
    record_lbl.setAlignment(Qt.AlignCenter)
    record_lbl.setStyleSheet("color: #c77d7d;")
    layout.addWidget(record_lbl)

    if score_time > record and score_time > 0:
        new_rec = QLabel("🎉 НОВЫЙ РЕКОРД! 🎉")
        new_rec.setFont(QFont("Arial", scale_font(14), QFont.Bold))
        new_rec.setAlignment(Qt.AlignCenter)
        new_rec.setStyleSheet("color: #ffb7b2;")
        layout.addWidget(new_rec)

    btn_layout = QHBoxLayout()
    btn_layout.setSpacing(scale_font(20))

    again_btn = QPushButton("Сыграть снова")
    again_btn.setFixedSize(*scale(200, 45))
    again_btn.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    again_btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(20)}px;")
    again_btn.clicked.connect(lambda: [dialog.done(1), restart_game()])
    btn_layout.addWidget(again_btn)

    menu_btn = QPushButton("В главное меню")
    menu_btn.setFixedSize(*scale(200, 45))
    menu_btn.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    menu_btn.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(20)}px;")
    menu_btn.clicked.connect(lambda: [dialog.done(2), close_time_mode()])
    btn_layout.addWidget(menu_btn)

    layout.addLayout(btn_layout)
    dialog.exec_()


def restart_game():
    global random_key, main_word_time, target_words_time, score_time, found_words_time
    global current_word_time, used_indices_time, time_left, timer, record, letter_btns_time

    random_key = random.randint(1, 3)
    main_word_time, target_words_time = time_words[random_key]
    score_time = 0
    found_words_time = []
    current_word_time = ""
    used_indices_time = []
    time_left = 60

    update_found_words_display()
    clear_word_time()
    record_label_time.setText(f"🏆 {record}")
    timer_label.setText("Время 01:00")

    for i in reversed(range(h_letters_time.count())):
        w = h_letters_time.itemAt(i).widget()
        if w:
            w.deleteLater()

    letter_btns_time = []
    for i, letter in enumerate(main_word_time):
        b = QPushButton(letter)
        b.setFixedSize(*scale(55, 55))
        b.setFont(QFont("Arial", scale_font(16), QFont.Bold))
        b.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(27)}px;")
        b.clicked.connect(lambda checked, idx=i: add_letter_time(idx))
        h_letters_time.addWidget(b)
        letter_btns_time.append(b)

    if timer:
        timer.stop()
    timer = QTimer()
    timer.timeout.connect(update_timer)
    timer.start(1000)
    clear_time.setEnabled(True)
    check_time.setEnabled(True)


def open_time_mode():
    global time_win, timer, score_time, found_words_time, current_word_time, used_indices_time, time_left, record
    global random_key, main_word_time, target_words_time, letter_btns_time

    if timer:
        timer.stop()
        timer = None

    if time_win is None:
        create_time_window()

    random_key = random.randint(1, 3)
    main_word_time, target_words_time = time_words[random_key]
    score_time = 0
    found_words_time = []
    current_word_time = ""
    used_indices_time = []
    time_left = 60

    update_found_words_display()
    clear_word_time()
    record_label_time.setText(f"🏆 {record}")
    timer_label.setText("Время 01:00")

    for i in reversed(range(h_letters_time.count())):
        w = h_letters_time.itemAt(i).widget()
        if w:
            w.deleteLater()

    letter_btns_time = []
    for i, letter in enumerate(main_word_time):
        b = QPushButton(letter)
        b.setFixedSize(*scale(55, 55))
        b.setFont(QFont("Arial", scale_font(16), QFont.Bold))
        b.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(27)}px;")
        b.clicked.connect(lambda checked, idx=i: add_letter_time(idx))
        h_letters_time.addWidget(b)
        letter_btns_time.append(b)

    timer = QTimer()
    timer.timeout.connect(update_timer)
    timer.start(1000)
    clear_time.setEnabled(True)
    check_time.setEnabled(True)

    levels_win.hide()
    time_win.show()


def close_time_mode():
    global timer
    if timer:
        timer.stop()
        timer = None
    if time_win:
        time_win.hide()
    levels_win.show()
    update_total_score_display()


# ДАННЫЕ ДЛЯ УРОВНЕЙ
levels_data = {
    1: {"word": "БОТИНОК", "target": ["ТОК", "КОТ", "КИТ", "ТИК", "БОТ", "БОК", "БИНТ", "КИНО", "ОКНО"]},
    2: {"word": "ПРОГРАММА", "target": ["РОГ", "МАГ", "РОМ", "ПАР", "РАМА", "ГОРА", "МАМА", "ГРОМ", "ПОРА", "ГРАММ", "ГАММА", "МРАМОР"]},
    3: {"word": "РЕГИСТРАЦИЯ",
        "target": ["ГИТ", "РИС", "ТИР", "АИСТ", "ГИРЯ", "ИГРА", "СЕРА", "СТАЯ", "ТИГР", "РАЦИЯ", "ИСТЕЦ", "АРЕСТ", "ГРАЦИЯ", "СТАРЕЦ",
                   "РЕГИСТР"]}
}


def show_level_complete_dialog(level_num, win, score):
    dialog = QDialog(win)
    dialog.setWindowTitle("Уровень пройден!")
    dialog.setFixedSize(*scale(450, 300))
    dialog.setModal(True)
    dialog.setWindowIcon(QIcon("images/word.png"))
    dialog.setStyleSheet("background-color: #fff5e6;")

    layout = QVBoxLayout(dialog)
    layout.setSpacing(scale_font(20))
    layout.setContentsMargins(scale(30, 30)[0], scale(30, 30)[1],
                              scale(30, 30)[0], scale(30, 30)[1])

    title = QLabel("УРОВЕНЬ ПРОЙДЕН!")
    title.setFont(QFont("Arial", scale_font(22), QFont.Bold))
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet("color: #ffb7b2;")
    layout.addWidget(title)

    msg = QLabel(f"Вы прошли уровень {level_num}!")
    msg.setFont(QFont("Arial", scale_font(16), QFont.Bold))
    msg.setAlignment(Qt.AlignCenter)
    msg.setStyleSheet("color: #6b9e8a;")
    layout.addWidget(msg)

    score_label = QLabel(f"Набрано очков: {score}")
    score_label.setFont(QFont("Arial", scale_font(14), QFont.Bold))
    score_label.setAlignment(Qt.AlignCenter)
    score_label.setStyleSheet("color: #c77d7d;")
    layout.addWidget(score_label)

    layout.addSpacing(scale_font(20))

    btn_layout = QHBoxLayout()
    btn_layout.setAlignment(Qt.AlignCenter)
    btn_layout.setSpacing(scale_font(20))

    result = [0]

    if level_num < 3:
        next_btn = QPushButton("След. уровень")
        next_btn.setFixedSize(*scale(200, 45))
        next_btn.setFont(QFont("Arial", scale_font(12), QFont.Bold))
        next_btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(20)}px;")
        next_btn.clicked.connect(lambda: [dialog.done(1), result.__setitem__(0, 1)])
        btn_layout.addWidget(next_btn)

    menu_btn = QPushButton("В главное меню")
    menu_btn.setFixedSize(*scale(200, 45))
    menu_btn.setFont(QFont("Arial", scale_font(12), QFont.Bold))
    menu_btn.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(20)}px;")
    menu_btn.clicked.connect(lambda: [dialog.done(2), result.__setitem__(0, 2)])
    btn_layout.addWidget(menu_btn)

    layout.addLayout(btn_layout)

    dialog.exec_()

    return result[0]


def create_level_window(level_num):
    win = QMainWindow()
    win.setWindowTitle(f"Слова из слова - Уровень {level_num}")
    win.showFullScreen()
    win.setStyleSheet("background-color: #fff5e6;")
    win.setWindowIcon(QIcon("images/word.png"))

    close_on_esc(win)

    central = QWidget()
    win.setCentralWidget(central)
    v = QVBoxLayout(central)
    v.setContentsMargins(scale(20, 20)[0], scale(20, 20)[1],
                         scale(20, 20)[0], scale(20, 20)[1])

    progress_data = load_levels_progress()
    score = progress_data.get("scores", {}).get(str(level_num), 0)
    found = progress_data.get("found", {}).get(str(level_num), [])

    top = QHBoxLayout()
    back = QPushButton("назад")
    back.setFixedSize(*scale(100, 40))
    back.setFont(QFont("Arial", scale_font(16), QFont.Bold))
    back.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(20)}px;")
    top.addWidget(back)
    top.addStretch()
    level_title = QLabel(f"УРОВЕНЬ {level_num}")
    level_title.setFont(QFont("Arial", scale_font(24), QFont.Bold))
    level_title.setAlignment(Qt.AlignCenter)
    level_title.setStyleSheet("color: #ffb7b2;")
    top.addWidget(level_title)
    top.addStretch()
    score_lbl = QLabel("⭐ 0")
    score_lbl.setFont(QFont("Arial", scale_font(18), QFont.Bold))
    score_lbl.setStyleSheet("color: #ffb7b2;")
    top.addWidget(score_lbl)
    v.addLayout(top)

    msg_lbl = QLabel("")
    msg_lbl.setFont(QFont("Arial", scale_font(28), QFont.Bold))
    msg_lbl.setAlignment(Qt.AlignCenter)
    msg_lbl.setMinimumHeight(scale_font(50))
    v.addWidget(msg_lbl)

    words = levels_data[level_num]["target"]
    word_labels = []

    words_container = QWidget()
    words_layout = QVBoxLayout(words_container)
    words_layout.setAlignment(Qt.AlignCenter)
    words_layout.setSpacing(scale_font(10))

    for w in words:
        lbl = QLabel(" ".join(["-"] * len(w)))
        lbl.setFont(QFont("Courier", scale_font(20), QFont.Bold))
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 8px; border-radius: 10px;")
        lbl.setMinimumWidth(scale_font(len(w) * 40))
        lbl.setMaximumWidth(scale_font(len(w) * 50))
        words_layout.addWidget(lbl, alignment=Qt.AlignCenter)
        word_labels.append(lbl)

    words_scroll = QScrollArea()
    words_scroll.setWidgetResizable(True)
    words_scroll.setStyleSheet("""
        QScrollArea {
            background: transparent;
            border: none;
        }
        QScrollBar:vertical {
            background: #fff5e6;
            width: 8px;
            border-radius: 4px;
        }
        QScrollBar::handle:vertical {
            background: #c77d7d;
            border-radius: 4px;
            min-height: 30px;
        }
    """)
    words_scroll.setWidget(words_container)
    words_scroll.setMinimumHeight(scale_font(200))
    words_scroll.setMaximumHeight(scale_font(300))
    v.addWidget(words_scroll)

    v.addSpacing(scale_font(10))

    current_word = ""
    used_indices = []
    current_score = score
    found_words = found.copy()

    current_lbl = QLabel("")
    current_lbl.setFont(QFont("Courier", scale_font(32), QFont.Bold))
    current_lbl.setAlignment(Qt.AlignCenter)
    current_lbl.setStyleSheet("background-color: #ffe4e9; color: #c77d7d; padding: 15px; border-radius: 15px;")
    current_lbl.setMinimumHeight(scale_font(70))
    v.addWidget(current_lbl)

    h_btn = QHBoxLayout()
    h_btn.setAlignment(Qt.AlignCenter)
    h_btn.setSpacing(scale_font(30))
    clear_btn = QPushButton("✖")
    clear_btn.setFixedSize(*scale(65, 65))
    clear_btn.setFont(QFont("Arial", scale_font(28)))
    clear_btn.setStyleSheet(f"background-color: #ffb7b2; color: white; border-radius: {scale_font(32)}px;")
    check_btn = QPushButton("✓")
    check_btn.setFixedSize(*scale(65, 65))
    check_btn.setFont(QFont("Arial", scale_font(28)))
    check_btn.setStyleSheet(f"background-color: #a8e6cf; color: white; border-radius: {scale_font(32)}px;")
    h_btn.addWidget(clear_btn)
    h_btn.addWidget(check_btn)
    v.addLayout(h_btn)

    hint = QLabel("Составь слово из букв:")
    hint.setFont(QFont("Arial", scale_font(12)))
    hint.setStyleSheet("color: #d4a5a5;")
    v.addWidget(hint)

    # Буквы с прокруткой
    letters_scroll = QScrollArea()
    letters_scroll.setWidgetResizable(True)
    letters_scroll.setStyleSheet("background: transparent; border: none;")
    letters_scroll.setMaximumHeight(scale_font(80))
    letters_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    letters_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    letters_widget = QWidget()
    h_letters = QHBoxLayout(letters_widget)
    h_letters.setAlignment(Qt.AlignCenter)
    h_letters.setSpacing(scale_font(8))
    h_letters.setContentsMargins(scale(5, 5)[0], scale(5, 5)[1],
                                 scale(5, 5)[0], scale(5, 5)[1])

    letters_scroll.setWidget(letters_widget)
    v.addWidget(letters_scroll)

    letter_btns = []
    main_word = levels_data[level_num]["word"]
    for i, letter in enumerate(main_word):
        b = QPushButton(letter)
        b.setFixedSize(*scale(50, 50))
        b.setFont(QFont("Arial", scale_font(16), QFont.Bold))
        b.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(25)}px;")
        b.clicked.connect(lambda checked, idx=i: add_letter(idx))
        h_letters.addWidget(b)
        letter_btns.append(b)

    def show_msg(txt, col):
        msg_lbl.setText(txt)
        msg_lbl.setStyleSheet(f"color: {col}; font-size: {scale_font(28)}px; font-weight: bold;")
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
                btn.setStyleSheet(f"background-color: #d4d4d4; color: #999999; border-radius: {scale_font(25)}px;")
            else:
                btn.setEnabled(True)
                btn.setStyleSheet(f"background-color: #a8e6cf; color: #6b9e8a; border-radius: {scale_font(25)}px;")

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


# ========== ПЕРЕХОДЫ ==========
level1_win = None
level2_win = None
level3_win = None


def to_levels():
    global levels_win
    if levels_win is None:
        create_levels_window()
    main_win.hide()
    levels_win.show()
    update_total_score_display()


def back_to_main():
    if levels_win:
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


load_record()
play_btn.clicked.connect(to_levels)
exit_btn.clicked.connect(main_win.close)

main_win.show()
sys.exit(app.exec_())