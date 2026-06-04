import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Слова из слова")
window.setFixedSize(500, 450)
window.setStyleSheet("background-color: #fff5e6;")
window.setWindowIcon(QIcon("images/word.png"))

central = QWidget()
window.setCentralWidget(central)

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

# Действия при нажатии
play_btn.clicked.connect(lambda: print("Игра начнётся позже"))
exit_btn.clicked.connect(window.close)
window.show()

# Запускаем приложение
sys.exit(app.exec_())