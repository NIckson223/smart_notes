from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget, QPushButton, QTextEdit,
                             QLabel, QLineEdit, QListWidget,
                             QVBoxLayout, QHBoxLayout)
import json
app = QApplication([])

notes = {
    "Ласкаво просимо!" : {
        "текст" : "Це найкращий додаток для заміток у світі!",
        "теги" : ["добро", "інструкція"]
    }
}
with open('f.json', 'w') as file:
    json.dump(notes, file)

#параметри вікна
notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)

# Віджети вікна програми
list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')

btn_note_create = QPushButton('Створити замітку')
btn_note_save = QPushButton('Зберегти')
btn_note_delete = QPushButton("Видалити")

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть назву тегу')

field_text = QTextEdit()

btn_tag_add = QPushButton('Додати тег до замітки')
btn_tag_delete = QPushButton('Видалити тег замітки')
btn_tag_search = QPushButton("Шукати замітки по тегу")

list_tags = QListWidget()
list_tags_label = QLabel("Список тегів")

# розташування віджетів

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(field_text)
#додаємо поле із списком заміток та кнопками
col2 = QVBoxLayout()
col2.addWidget(list_notes_label)
col2.addWidget(list_notes)
row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_delete)
row2 = QHBoxLayout()
row2.addWidget(btn_note_save)
col2.addLayout(row1)
col2.addLayout(row2)
#додаємо поле із списком тегів заміток та кнопками
col2.addWidget(list_tags_label)
col2.addWidget(list_tags)
col2.addWidget(field_tag)
row3 = QHBoxLayout()
row3.addWidget(btn_tag_add)
row3.addWidget(btn_tag_delete)
col2.addLayout(row3)
row4 = QHBoxLayout()
row4.addWidget(btn_tag_search)
col2.addLayout(row4)

layout_notes.addLayout(col1)
layout_notes.addLayout(col2)
notes_win.setLayout(layout_notes)
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])


list_notes.itemClicked.connect(show_note)
list_notes.addItems(notes)
notes_win.show()
app.exec_()


