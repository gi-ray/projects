from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLCDNumber, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import uic, QtMultimedia, QtCore
from ui import Ui_MainWindow
import sys
import random


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #Load The UI File
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("BlackJack")

        #Card Labels
        self.p_card_1 = self.findChild(QLabel, "p_card_1")
        self.p_card_2 = self.findChild(QLabel, "p_card_2")
        self.p_card_3 = self.findChild(QLabel, "p_card_3")
        self.p_card_4 = self.findChild(QLabel, "p_card_4")
        self.p_card_5 = self.findChild(QLabel, "p_card_5")
        self.p_card_6 = self.findChild(QLabel, "p_card_6")
        
        self.d_card_1 = self.findChild(QLabel, "d_card_1")
        self.d_card_2 = self.findChild(QLabel, "d_card_2")
        self.d_card_3 = self.findChild(QLabel, "d_card_3")
        self.d_card_4 = self.findChild(QLabel, "d_card_4")
        self.d_card_5 = self.findChild(QLabel, "d_card_5")
        self.d_card_6 = self.findChild(QLabel, "d_card_6")
        
        #Finds Buttons
        self.hitButton = self.findChild(QPushButton, "hitButton")
        self.standButton = self.findChild(QPushButton, "standButton")
        self.surrenderButton = self.findChild(QPushButton, "surrenderButton")
        self.ddButton = self.findChild(QPushButton, "ddButton")

        #Finds Point Labels
        self.playerPoints = self.findChild(QLabel, "playerPoints")
        self.dealerPoints = self.findChild(QLabel, "dealerPoints")

        #Bet Buttons
        self.betButton = self.findChild(QPushButton, "betButton")
        self.chip10Button = self.findChild(QPushButton, "chip10Button")
        self.chip50Button = self.findChild(QPushButton, "chip50Button")
        self.chip100Button = self.findChild(QPushButton, "chip100Button")
        
        self.betLabel = self.findChild(QLCDNumber, "betLabel")
        self.betLabel_2 = self.findChild(QLabel, "betLabel_2")
        self.moneyLabel = self.findChild(QLCDNumber, "moneyLabel")

        #Frame
        self.frame = self.findChild(QFrame, "frame")

        #Message Box Frame
        self.messageBox = self.findChild(QFrame, "messageBox")
        #Message Box Label
        self.messageLabel = self.findChild(QLabel, "messageLabel")
        #Message Box Button
        self.messageButton = self.findChild(QPushButton, "messageButton")

        #Links The Buttons to the Actions
        self.hitButton.clicked.connect(self.playerHit)
        self.standButton.clicked.connect(self.endRound)
        self.messageButton.clicked.connect(self.message)
        self.surrenderButton.clicked.connect(self.surrender)
        self.ddButton.clicked.connect(self.doubleDown)

        self.ddButton.setText("Bahsi İkiye\nKatla")

        #Main Menu
        self.menuFrame = self.findChild(QFrame, "menuFrame")
        self.startButton = self.findChild(QPushButton, "startButton")
        self.moneyInput = self.findChild(QLineEdit, "moneyInput")

        self.menuMessage = self.findChild(QFrame, "menuMessage")
        self.menuMessageLabel = self.findChild(QLabel, "menuMessageLabel")
        self.menuMessageButton = self.findChild(QPushButton, "menuMessageButton")

        self.menuMessageButton.clicked.connect(self.setMoney)

        self.startButton.clicked.connect(self.setMoney)

        #Get The Deck and Deal the First 4 Cards
        self.getDeck()
        self.PLAYER_VALUE = 0
        self.PLAYER_VALUE = 0
        self.menuMessage.hide()
        
        #Show The App
        self.show()

    def resetValue(self):
        self.PLAYER_VALUE = 0
        self.DEALER_VALUE = 0

    def setMoney(self):
        try:
            self.MONEY = int(self.moneyInput.text())
            if len(str(self.MONEY)) > 4:
                self.menuMessage.show()
            if len(str(self.MONEY)) <= 4:
                self.menuFrame.hide()
                self.moneyLabel.display(f"{self.MONEY}")
        except:
            self.menuMessage.show()
        if len(str(self.MONEY)) > 4:
            self.menuMessage.show()    
        button = self.sender()

        if button == self.menuMessageButton:
            self.PLAYER_VALUE = 0
            self.DEALER_VALUE = 0
            self.menuMessage.hide()
    def doubleDown(self):
        self.BET *= 2
        self.betLabel.display(f"{self.BET}")
        self.playerHit()
        self.endRound()
        
    def split(self):
        pass

    def surrender(self):
        self.MONEY -= self.BET/2

        self.messageLabel.setText("Oyuncu Teslim Oldu!")
        self.message()    


    def displayMoney(self):
        self.moneyLabel.display({self.MONEY})

    #Reveals The Card
    def revealCard(self):
        self.hiddenCard
    
        pixmap = QPixmap(f":/image/images/{self.hiddenCard}.png")

        self.d_card_2.setPixmap(pixmap)

    #Determines The Winner
    def determineWinner(self):
        if self.DEALER_VALUE > 21:
                self.messageLabel.setText("Oyuncu Kazandı")
                self.MONEY += self.BET
                self.message()
        elif self.DEALER_VALUE < 22:
            if  self.PLAYER_VALUE > self.DEALER_VALUE:
                self.messageLabel.setText("Oyuncu Kazandı")
                self.MONEY += self.BET
            elif self.PLAYER_VALUE < self.DEALER_VALUE:
                self.messageLabel.setText("Kasa Kazandı")
                self.MONEY -= self.BET
            elif self.PLAYER_VALUE == self.DEALER_VALUE:
                self.messageLabel.setText("Berabere")

        self.dealerPoints.setText(f"Sayı: {self.DEALER_VALUE}")            
    #Message Box
    def message(self):

        self.moneyLabel.display(f"{self.MONEY}")
        self.betLabel.display("0")
        
        for i in range(1):
            self.messageBox.show()
        self.frame.hide()
        button = self.sender()
        if button == self.messageButton:
            self.messageBox.hide()
            self.frame.hide()
            self.chip10Button.show()
            self.chip50Button.show()
            self.chip100Button.show()
            self.betButton.show()
            pixmap = QPixmap("")
            self.p_card_1.setPixmap(pixmap)
            self.p_card_2.setPixmap(pixmap)
            self.p_card_3.setPixmap(pixmap)
            self.p_card_4.setPixmap(pixmap)
            self.p_card_5.setPixmap(pixmap)
            self.p_card_6.setPixmap(pixmap)

            self.d_card_1.setPixmap(pixmap)
            self.d_card_2.setPixmap(pixmap)
            self.d_card_3.setPixmap(pixmap)
            self.d_card_4.setPixmap(pixmap)
            self.d_card_5.setPixmap(pixmap)
            self.d_card_6.setPixmap(pixmap)

            self.PLAYER_SPOT = 0
            self.DEALER_SPOT = 0
            self.PLAYER_VALUE = 0
            self.DEALER_VALUE = 0

            self.playerPoints.setText("Sayı: 0")
            self.dealerPoints.setText("Sayı: 0")

            

            self.BET = 0

    #Ends The Round
    def endRound(self):
        self.PLAYER_VALUE = 0
        self.DEALER_VALUE = 0
        while self.DEALER_VALUE < 17:
            self.dealerHit()
            
        self.revealCard()     
        self.determineWinner()
        self.message()
        self.playerHand.clear()
        self.dealerHand.clear()

    #Confirms The Bet
    def confirmBet(self):
        button = self.sender()
        if button == self.chip10Button:
            self.BET += 10
            self.betLabel.display(self.BET)
        if button == self.chip50Button:
            self.BET += 50
            self.betLabel.display(self.BET)
        if button == self.chip100Button:
            self.BET += 100
            self.betLabel.display(self.BET)
        if button == self.betButton:
            self.chip10Button.hide()
            self.chip50Button.hide()
            self.chip100Button.hide()
            self.betButton.hide()
            self.dealCards()
            self.PLAYER_VALUE = 0
            self.DEALER_VALUE = 0

    #Gets The Bet
    def getBet(self):
        
            self.frame.hide()
            self.chip10Button.show()
            self.chip50Button.show()
            self.chip100Button.show()
            self.betButton.show()
            #Button Clicks
            self.chip10Button.clicked.connect(self.confirmBet)
            self.chip50Button.clicked.connect(self.confirmBet)
            self.chip100Button.clicked.connect(self.confirmBet)
            self.betButton.clicked.connect(self.confirmBet)
            #Empty Bet Label
            
    #Deals The First 2 Cards
    def dealCards(self):
        self.playerHand = []
        self.dealerHand = []
        pixmap = QPixmap("")
        self.p_card_1.setPixmap(pixmap)
        self.p_card_2.setPixmap(pixmap)
        self.p_card_3.setPixmap(pixmap)
        self.p_card_4.setPixmap(pixmap)
        self.p_card_5.setPixmap(pixmap)
        self.p_card_6.setPixmap(pixmap)

        self.d_card_1.setPixmap(pixmap)
        self.d_card_2.setPixmap(pixmap)
        self.d_card_3.setPixmap(pixmap)
        self.d_card_4.setPixmap(pixmap)
        self.d_card_5.setPixmap(pixmap)
        self.d_card_6.setPixmap(pixmap)
        
        self.frame.show()
        for i in range(2):
            self.playerHit()
            self.dealerHit()
        if self.DEALER_VALUE == 21:
            self.messageLabel.setText("Kasa BlackJack Yaparak Kazandı!")
            self.messageLabel.adjustSize()
            self.messageBox.adjustSize()
            self.MONEY -= self.BET
            self.message()
        elif self.PLAYER_VALUE == 21:
            self.messageLabel.setText("Oyuncu BlackJack Yaparak Kazandı!")
            self.messageLabel.adjustSize()
            self.messageBox.adjustSize()
            money = self.MONEY
            bet = self.BET
            self.MONEY = money + (bet*1.5)
            self.message()
        if self.DEALER_VALUE == 21 and self.PLAYER_VALUE == 21:
            self.messageLabel.setText("Hem Oyuncu Hem De Kasa BlackJack Yaptı!\nBerabere.")
            self.messageLabel.adjustSize()
            self.messageBox.adjustSize()

    #Create The Deck
    def getDeck(self):
        self.messageBox.hide()
        self.deck = []
        suits = ["diamonds", "clubs", "hearts", "spades"]
        for _ in range(6):
            values = range(2, 15)
            for suit in suits:
                for value in values:
                    self.deck.append(f"{value}_of_{suit}")
        random.shuffle(self.deck)
        
        self.playerHand = []
        self.dealerHand = []
        self.PLAYER_VALUE = 0
        self.DEALER_VALUE = 0
        self.PLAYER_SPOT = 0
        self.DEALER_SPOT = 0
        self.CARD_COUNT = 0
        self.BET = 0
        self.MONEY = 0
        self.getBet()
        self.hiddenCard = ""
        
    def playerHit(self):
        
        if self.PLAYER_SPOT < 6:
            card = random.choice(self.deck)
            self.playerHand.append(card)
            self.deck.remove(card)
            self.CARD_COUNT += 1
            #Output Cards
            pixmap = QPixmap(f":/image/images/{card}.png")
            if self.PLAYER_SPOT == 0:
                self.p_card_1.setPixmap(pixmap)
            elif self.PLAYER_SPOT == 1:
                self.p_card_2.setPixmap(pixmap)
            elif self.PLAYER_SPOT == 2:
                self.p_card_3.setPixmap(pixmap)
            elif self.PLAYER_SPOT == 3:
                self.p_card_4.setPixmap(pixmap)    
            elif self.PLAYER_SPOT == 4:
                self.p_card_5.setPixmap(pixmap)
            elif self.PLAYER_SPOT == 5:
                self.p_card_6.setPixmap(pixmap)
            self.PLAYER_SPOT += 1 
            
            #Get Hand Value
            self.PLAYER_VALUE = 0
            
            for item in self.playerHand:
                if item[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.PLAYER_VALUE += int(item[0])
                if item[0:2] in ["10", "11", "12", "13"]:
                    self.PLAYER_VALUE += 10
                if item[0:2] in ["14"]:
                    if self.PLAYER_VALUE + 11 <= 21:
                        self.PLAYER_VALUE += 11
                    elif self.PLAYER_VALUE + 11 > 21:
                        self.PLAYER_VALUE += 1
            for item in self.playerHand:
                if item[0:2] in ["14"] and item == self.playerHand[0] and self.PLAYER_VALUE > 21:
                    self.PLAYER_VALUE -= 10
                

            if self.PLAYER_VALUE > 21:
                self.messageLabel.setText("Kasa Kazandı")
                self.messageLabel.adjustSize()
                self.messageBox.adjustSize()
                self.message()
                self.MONEY -= self.BET

            if self.PLAYER_VALUE == 21:
                self.messageLabel.setText("Oyuncu Kazandı")
                self.messageLabel.adjustSize()
                self.messageBox.show()            
            
            self.playerPoints.setText(f"Sayı: {self.PLAYER_VALUE}")       
    def dealerHit(self):
        if self.DEALER_SPOT < 6:
            card = random.choice(self.deck)
            self.dealerHand.append(card)
            self.deck.remove(card)
            self.CARD_COUNT += 1
            #Output Cards
            pixmap = QPixmap(f":/image/images/{card}.png")
            if self.DEALER_SPOT == 0:
                self.d_card_1.setPixmap(pixmap)
            elif self.DEALER_SPOT == 1:
                pixmap = QPixmap(":/image/images/card-back.png")
                self.hiddenCard = card
                
                self.d_card_2.setPixmap(pixmap)
            elif self.DEALER_SPOT == 2:
                self.d_card_3.setPixmap(pixmap)
            elif self.DEALER_SPOT == 3:
                self.d_card_4.setPixmap(pixmap)    
            elif self.DEALER_SPOT == 4:
                self.d_card_5.setPixmap(pixmap)
            elif self.DEALER_SPOT == 5:
                self.d_card_6.setPixmap(pixmap)
            self.DEALER_SPOT += 1        
            self.DEALER_VALUE = 0
            
            #Get Hand Value
            for item in self.dealerHand:
                if item[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.DEALER_VALUE += int(item[0])
                if item[0:2] in ["10", "11", "12", "13"]:
                    self.DEALER_VALUE += 10
                if item[0:2] in ["14"]:
                    if self.DEALER_VALUE + 11 <= 21:
                        self.DEALER_VALUE += 11
                    elif self.DEALER_VALUE + 11 > 21:
                        self.DEALER_VALUE += 1
            for item in self.dealerHand:
                if item[0:2] in ["14"] and item == self.dealerHand[0] and self.DEALER_VALUE > 21:
                    self.DEALER_VALUE -= 10            
            
#Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()