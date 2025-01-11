from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLCDNumber
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
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

        #Frame
        self.frame = self.findChild(QFrame, "frame")
        
        
        
        #Links The Buttons to the Actions
        self.hitButton.clicked.connect(self.playerHit)
        self.standButton.clicked.connect(self.endRound)

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
        #Get The Deck and Deal the First 4 Cards
        self.getDeck()
        self.getBet()
        

        
        #Show The App
        self.show()
    
    #Ends The Round
    def endRound(self):
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

        self.getBet()


        
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
        self.betLabel_2.setText(f"Bahis:")
        
        
      
        

    #Deals The First 2 Cards
    def dealCards(self):
        self.frame.show()
        for i in range(2):
            self.playerHit()
            self.dealerHit()

    #Create The Deck
    def getDeck(self):
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
        
    def playerHit(self):
        if self.PLAYER_SPOT < 6:
            card = random.choice(self.deck)
            self.playerHand.append(card)
            self.deck.remove(card)
            self.CARD_COUNT += 1
            #Output Cards
            pixmap = QPixmap(f"assets/images/{card}.png")
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
            print(self.playerHand)

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
                    if self.PLAYER_VALUE + 11 > 21:
                        self.PLAYER_VALUE += 1
            
            self.playerPoints.setText(f"Sayı: {self.PLAYER_VALUE}")       
    def dealerHit(self):
        if self.DEALER_SPOT < 6:
            card = random.choice(self.deck)
            self.dealerHand.append(card)
            self.deck.remove(card)
            self.CARD_COUNT += 1
            #Output Cards
            pixmap = QPixmap(f"assets/images/{card}.png")
            if self.DEALER_SPOT == 0:
                self.d_card_1.setPixmap(pixmap)
            elif self.DEALER_SPOT == 1:
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
                    if self.DEALER_VALUE + 11 > 21:
                        self.DEALER_VALUE += 1

            self.dealerPoints.setText(f"Sayı: {self.DEALER_VALUE}")            
    
#Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()