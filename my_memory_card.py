from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import randint, shuffle

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3  = wrong3

questions_list = []
questions_list.append(Question('В каком году была основана Москва?', '1147', '1242', '1861', '1943'))
questions_list.append(Question('Какой газ является самым легким?', 'Водород', 'Ксилород', 'Азот', 'Углерод'))
questions_list.append(Question('В каком году закончилась I мировая война?', '1918', '1812', '1753', '1898'))
questions_list.append(Question('Сколько стран в мире?', '252', '251', '145', '146'))
questions_list.append(Question('Какова длинна экватора?', '40 075 км', '42 164 км', '35 925 км', '10 000 км'))
questions_list.append(Question('Сколько длилась столетняя война?', '116 лет', '100 лет', '50 лет', '112 лет'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Викторина')

#Интерфейс приложения MC

question1 = QLabel('')
pbutton1 = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbutton1 = QRadioButton('')
rbutton2 = QRadioButton('')
rbutton3 = QRadioButton('')
rbutton4 = QRadioButton('')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbutton1)
RadioGroup.addButton(rbutton2)
RadioGroup.addButton(rbutton3)
RadioGroup.addButton(rbutton4)

lineH1 = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

lineV1.addWidget(rbutton1)
lineV1.addWidget(rbutton2)
lineV2.addWidget(rbutton3)
lineV2.addWidget(rbutton4)

lineH1.addLayout(lineV1)
lineH1.addLayout(lineV2)

RadioGroupBox.setLayout(lineH1)

AnsGroupBox = QGroupBox('Результат теста')
result1 = QLabel('прав ты или нет?')
correct1 = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(result1, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct1, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()
lineH4 = QHBoxLayout()

lineH2.addWidget(question1, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
lineH3.addWidget(RadioGroupBox)
lineH3.addWidget(AnsGroupBox)
AnsGroupBox.hide()
lineH4.addStretch(1)
lineH4.addWidget(pbutton1, stretch=2)
lineH4.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(lineH2, stretch=2)
layout_card.addLayout(lineH3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(lineH4, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

#функционал работы программы

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    pbutton1.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    pbutton1.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbutton1.setChecked(False)
    rbutton2.setChecked(False)
    rbutton3.setChecked(False)
    rbutton4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbutton1, rbutton2, rbutton3, rbutton4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question1.setText(q.question)
    correct1.setText(q.right_ans)
    show_question()

def show_correct(res):
    result1.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Кол-во заданных вопросов:', window.total)
        print('Кол-во правильных ответов:', window.score)
        print('Процент правильных ответов:', str(window.score/window.total * 100) + '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Кол-во заданных вопросов:', window.total)
            print('Кол-во правильных ответов:', window.score)
            print('Процент правильных ответов:', str(window.score/window.total * 100) + '%')

def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
    questions_list.remove(q)

def click_OK():
    if pbutton1.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.total = 0
window.score = 0
pbutton1.clicked.connect(click_OK)
next_question()

window.setLayout(layout_card)
window.show()
app.exec_()