from PyQt5.QtWidgets import*

menu_win = QWidget()
le_quest = QLabel("Введіть запитання")
le_right_ans = QLabel("Введіть правильну відповідь")
le_wrong_ans1 = QLabel("Введіть першу хибну відповідь")
le_wrong_ans2 = QLabel("Введіть другу хибну відповідь")
le_wrong_ans3 = QLabel("Введіть третю хибну відповідь")
le_quest = QLine_Edit()
le_right_ans = QLine_Edit()
le_wrong_ans1 = QLine_Edit()
le_wrong_ans2 = QLine_Edit()
le_wrong_ans3 = QLine_Edit()
lb_header_stat = QLabel("Статистика")
lb_header_stat.setStyleSheet("font-seze: 19; font-weight: bold; ")
lb_statistick = QLabel()



vl_labels = QVBoxLayout()
vl_labels.addwidget(lb_quest)
vl_labels.addwidget(lb_right_ans)
vl_labels.addwidet(lb_wrong_ans1)
vl_labels.addwidet(lb_wrong_ans2)
vl_labels.addwidet(lb_wrong_ans3)


hl_question = QHBoxLayout()
hl_question.addlayout(vl_labels)
hl_question.addlayout(vl_lineEdits)

btn_back = QPushButton("Назад")
btn_add_question = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")
hl_buttons = QHBoxLayout()
hl_buttons.addwidget(btn_add_question)
hl_buttons.addwidget(btn_clear)
