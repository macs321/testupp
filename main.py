from PyQt6.QtWidgets import (QApplication, QWidget,
                             QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout,
                             QMessageBox, QRadioButton)

App =QApplication([])
win = QWidget()
win.setWindowTitle("не ростраюйся")
win.resize(260, 250)

question = QLabel("Як звуть Ліну Костенко")
# 1
answer1 = QRadioButton("Ліна")
answer2 = QRadioButton("Клеопатра")
answer3 =QRadioButton("Віктор Янукович")
answer4 =QRadioButton("ківа")



main_layout = QVBoxLayout()


main_layout.addWidget(question)


h_line_1 = QHBoxLayout()
h_line_1.addWidget(answer1)
h_line_1.addWidget(answer2)




main_layout.addLayout(h_line_1)

h_line_2 = QHBoxLayout()

h_line_2.addWidget(answer3)
h_line_2.addWidget(answer4)


main_layout.addLayout(h_line_2)


def show_win():
    massadge_box = QMessageBox()
    massadge_box.setText("Правильно Молодець за розвиток культури з тебе 20 грн")
    massadge_box.exec()

def show_lose():
    massadge_box = QMessageBox()
    massadge_box.setText("Неправильноб НЕ РОСТРАЮЙСЯ за те що ти нічо не знаєш з тебе 2 грн")
    massadge_box.exec()

answer1.clicked.connect(show_win)
answer2.clicked.connect(show_lose)
answer3.clicked.connect(show_lose)
answer4.clicked.connect(show_lose)

























































































































































win.setLayout(main_layout)

win.show()
App.exec()