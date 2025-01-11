from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #Load The UI File
        uic.loadUi("game.ui", self)
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
        
        self.hitButton = self.findChild(QPushButton, "hitButton")
        self.standButton = self.findChild(QPushButton, "standButton")

        self.playerPoints = self.findChild(QLabel, "playerPoints")
        
        
        

        self.hitButton.clicked.connect(self.playerHit)
        
        #Get The Deck and Deal the First 4 Cards
        self.getDeck()
        #Show The App
        self.show()





    #Create The Deck
    def getDeck(self):
        self.deck = []
        suits = ["diamonds", "clubs", "hearts", "spades"]
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
        
    
        for i in range(2):
            self.playerHit()
            self.dealerHit()
        print(self.deck)

    
    def playerHit(self):
        if self.PLAYER_SPOT < 6:
            card = random.choice(self.deck)
            self.playerHand.append(card)
            self.deck.remove(card)
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
            print(item[0:2])
            print(self.playerPoints)
            self.playerPoints.setText(f"Sayı: {self.PLAYER_VALUE}")       
    def dealerHit(self):
        if self.DEALER_SPOT < 6:
            card = random.choice(self.deck)
            self.dealerHand.append(card)
            self.deck.remove(card)
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

            #Get Hand Value
            self.DEALER_VALUE = 0
            for item in self.playerHand:
                if item[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.DEALER_VALUE += int(item[0])
                if item[0:2] in ["10", "11", "12", "13"]:
                    self.DEALER_VALUE += 10
                if item[0:2] in ["14"]:
                    if self.DEALER_VALUE + 11 <= 21:
                        self.DEALER_VALUE += 11
                    if self.DEALER_VALUE + 11 > 21:
                        self.DEALER_VALUE += 1        

#Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()