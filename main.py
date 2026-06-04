import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Создаём приложение
app = QApplication(sys.argv)

# Главное окно
window = QMainWindow()
window.setWindowTitle("Слова из слова")
window.setFixedSize(500, 450)
window.setStyleSheet("background-color: #fff5e6;")

# Центральный виджет
central = QWidget()
window.setCentralWidget(central)

# Вертикальное расположение
layout = QVBoxLayout(central)
layout.setAlignment(Qt.AlignCenter)
layout.setSpacing(40)

# Заголовок
title = QLabel("СЛОВА ИЗ СЛОВА")
title.setFont(QFont("Arial", 24, QFont.Bold))
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("color: #ffb7b2;")
layout.addWidget(title)

# Кнопка "ИГРАТЬ"
play_btn = QPushButton("ИГРАТЬ")
play_btn.setFixedSize(250, 60)
play_btn.setFont(QFont("Arial", 16, QFont.Bold))
play_btn.setStyleSheet("background-color: #a8e6cf; color: #6b9e8a; border-radius: 30px;")
layout.addWidget(play_btn)

# Кнопка "ВЫХОД"
exit_btn = QPushButton("ВЫХОД")
exit_btn.setFixedSize(200, 50)
exit_btn.setFont(QFont("Arial", 14))
exit_btn.setStyleSheet("background-color: #ffb7b2; color: white; border-radius: 25px;")
layout.addWidget(exit_btn)

# Действия при нажатии
play_btn.clicked.connect(lambda: print("Игра начнётся позже"))
exit_btn.clicked.connect(window.close)

# Показываем окно
window.show()

# Запускаем приложение
sys.exit(app.exec_())