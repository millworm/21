import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QMessageBox
import random


class Example(QMainWindow):
    def __init__(self):
		self.masti = ["♥", "♦", "♣", "♠"]
        self.koloda = self.Koloda()
        self.count1 = 0
        self.count2 = 0
        self.numc1 = 0
        self.numc2 = 0
        self.loose = False
        random.shuffle(self.koloda)

        super().__init__()

        self.initUI()

	#Раскидать колоду
	def Koloda(self):
        i = 2
        temp = []
        while i < 12:
            if i == 5:
                i += 1
                continue
            for m in self.masti:
                temp.append([i, m])
            i += 1
        return temp

    def initUI(self):
        ## Кнопка СТАРТ
        self.btnStart = QPushButton("Начать игру", self)
        self.btnStart.setGeometry(140, 250, 200, 100)
        self.btnStart.clicked.connect(self.buttonClicked)

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)

        ##Кнопка РЕСТАРТ
        self.btnRestart = QPushButton("Перезапустить", self)
        self.btnRestart.setGeometry(140, 130, 200, 100)
        self.btnRestart.clicked.connect(self.buttonClicked_Restart)
        self.btnRestart.hide()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnRestart.setFont(font)

        ##Кнопка Хватит
        self.btnStop = QPushButton("Хватит", self)
        self.btnStop.setGeometry(140, 370, 200, 100)
        self.btnStop.clicked.connect(self.buttonClicked_Stop)

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnStop.setFont(font)
        self.btnStop.hide()

        ##Поле очков
        self.Score = QtWidgets.QLabel(self)
        self.Score.setGeometry(QtCore.QRect(360, 260, 91, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Score.setFont(font)
        self.Score.setToolTip("")
        self.Score.setWhatsThis("")
        self.Score.setTextFormat(QtCore.Qt.RichText)
        self.Score.setAlignment(QtCore.Qt.AlignCenter)
        self.Score.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Score.setObjectName("Score")
        self.Score.hide()

        ##Подпись к очкам
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(360, 190, 91, 71))
        self.label.setObjectName("label")
        self.label.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Ваши<br>очки</span></p></body></html>")
        self.label.hide()

        ##Поле очков противника
        self.Score2 = QtWidgets.QLabel(self)
        self.Score2.setGeometry(QtCore.QRect(20, 260, 91, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Score2.setFont(font)
        self.Score2.setToolTip("")
        self.Score2.setWhatsThis("")
        self.Score2.setTextFormat(QtCore.Qt.RichText)
        self.Score2.setAlignment(QtCore.Qt.AlignCenter)
        self.Score2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Score2.setObjectName("Score2")
        self.Score2.hide()

        ##Подпись к очкам противника
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(10, 190, 121, 71))
        self.label2.setObjectName("label2")
        self.label2.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Очки<br>противника</span></p></body></html>")
        self.label2.hide()

        # Выпавшие карты
        self.tbCards = QtWidgets.QTextEdit(self)
        self.tbCards.setGeometry(QtCore.QRect(140, 530, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tbCards.setFont(font)
        self.tbCards.setReadOnly(True)
        self.tbCards.setObjectName("tbCards")
        #
        self.tbCards.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>")
        self.tbCards.hide()

        # подпись к картам
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(160, 490, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("<html><head/><body><p align=\"center\">Выпавшие карты</p></body></html>")
        self.label_2.hide()

        # Кнопка взятия карт
        self.btnMore = QPushButton("Взять карту", self)
        self.btnMore.setGeometry(140, 250, 200, 100)
        self.btnMore.clicked.connect(self.buttonClicked_Card)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnMore.setFont(font)
        self.btnMore.hide()

        # Число карт
        self.Cards1 = QtWidgets.QLabel(self)
        self.Cards1.setGeometry(QtCore.QRect(360, 360, 91, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Cards1.setFont(font)
        self.Cards1.setToolTip("")
        self.Cards1.setWhatsThis("")
        self.Cards1.setTextFormat(QtCore.Qt.RichText)
        self.Cards1.setAlignment(QtCore.Qt.AlignCenter)
        self.Cards1.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Cards1.setObjectName("Cards1")
        self.Cards1.hide()

        self.lcards_1 = QtWidgets.QLabel(self)
        self.lcards_1.setGeometry(QtCore.QRect(360, 420, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcards_1.setFont(font)
        self.lcards_1.setObjectName("lcards_1")
        self.lcards_1.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Число карт</span></p></body></html>")
        self.lcards_1.hide()

        # Число карт противника
        self.Cards2 = QtWidgets.QLabel(self)
        self.Cards2.setGeometry(QtCore.QRect(20, 360, 91, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Cards2.setFont(font)
        self.Cards2.setToolTip("")
        self.Cards2.setWhatsThis("")
        self.Cards2.setTextFormat(QtCore.Qt.RichText)
        self.Cards2.setAlignment(QtCore.Qt.AlignCenter)
        self.Cards2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Cards2.setObjectName("Cards2")
        self.Cards2.hide()

        self.lcards_2 = QtWidgets.QLabel(self)
        self.lcards_2.setGeometry(QtCore.QRect(10, 420, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcards_2.setFont(font)
        self.lcards_2.setObjectName("lcards_2")
        self.lcards_2.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Число карт</span></p></body></html>")
        self.lcards_2.hide()
        ##Основные свойства
        self.statusBar()
        self.resize(480, 640)
        self.setWindowTitle('21')
        self.show()

    def buttonClicked_Restart(self):
        self.Restart()

    ##События кнопок
    def buttonClicked(self):
        sender = self.sender()
        # self.statusBar().showMessage(sender.text() + ' was pressed')
        self.btnStart.hide()
        self.Visible()  # показываем скрытое

    def Visible(self):
        self.Score.show()  # поле очков
        self.label.show()  # надпись над полем очков
        self.tbCards.show()  # выпавшие карты
        self.label_2.show()  # подпись
        self.btnMore.show()  # взятие карт
        self.label2.show()  # подпись очки противника
        self.Score2.show()  # очки противника
        self.btnStop.show()  # кнопка стоп
        self.btnRestart.show()
        self.Cards2.show()
        self.lcards_2.show()

    def buttonClicked_Card(self):
        if self.loose == True:
            return
        card = self.koloda.pop()
        current = card[0]
        if current < 6 or current == 11:
            text = "<html><center>"
            text += self.tbCards.toPlainText()
            if current == 2:
                text = text + "J"
            elif current == 3:
                text = text + "Q"
            elif current == 4:
                text = text + "K"
            elif current == 11:
                text = text + "A"
            self.count1 += current
            self.Score.setText(str(self.count1))
            text = text + card[1] + " " + "</center></html>"
            self.tbCards.setText(text)
        else:
            text = "<html><center>"
            text += self.tbCards.toPlainText()
            self.tbCards.setText(text + str(current)+ card[1]  + " " + "</center></html>")
            self.count1 += current
            self.Score.setText(str(self.count1))

        if self.count1 >= 21:
            self.buttonClicked_Stop()

        # ход противника
        if self.count1 != 0:
            self.II(False)


    def buttonClicked_Stop(self):
        if self.count1 == 0 or self.loose == True:
            return

        if (self.count2 == 0 or self.count2 < 12) and self.count1 < 21:
            self.II(True)

        self.Score2.setText(str(self.count2))
        self.Cards2.setText(str(self.numc2))
        if self.count1 > 21 or self.count2 == 21:
            self.Result("lose")
            return

        if self.count1 == self.count2 and self.count1 != 0 and self.count2 != 0:
            self.Result("draw")
            return

        if self.count1 > self.count2 or self.count2 > 21 or self.count1 == 21:
            self.Result("win")
            return
        else:
            self.Result("lose")
            return

    # Перезапуск игры
    def Restart(self):
        self.Score2.setText("")
        self.Score.setText("")
        self.tbCards.setText("")
        self.Cards2.setText("")
        self.count1 = 0
        self.count2 = 0
        self.numc2 = 0
        if len(self.koloda) < 10:
            self.koloda = self.Koloda()
        random.shuffle(self.koloda)
        self.loose = False

    # Ход компьютера
    def II(self, tr):
        i = 0
        S = True
        while S:
            i += 1
            if self.count2 <= 15:
                card = self.koloda.pop()
                current = card[0]
                self.numc2 += 1
                self.count2 += current
            elif self.count2 > 15 and self.count2 <= 18:
                card = self.koloda.pop()
                current = card[0]
                self.numc2 += 1
                self.count2 += current
            elif self.count2 > 18 and self.count2 <= 20:
                r = random.random()
                if r > 0.65:
                    card = self.koloda.pop()
					current = card[0]
                    self.numc2 += 1
                    self.count2 += current
                S = False
            if i > 8: S = False

            if self.count2 >= 21:
                S = False
                return
            if tr == False:
                S = False
        self.Cards2.setText(str(self.numc2))

    # Вывод сообщения
    def Result(self, Status):
        self.loose = True
        if Status == "win":
            reply = QMessageBox.question(self, 'Сообщение',
                                         "Вы победили. Еще раз?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.Restart()
            return
        elif Status == "lose":
            reply = QMessageBox.question(self, 'Сообщение',
                                         "Вы проиграли. Еще раз?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.Restart()
            return
        elif Status == "draw":
            reply = QMessageBox.question(self, 'Сообщение',
                                         "Ничья. Еще раз?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.Restart()
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
