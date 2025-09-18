from typing import List

class WOFPlayer:
    name: str
    prize_money: int
    prizes = List[str]

    def __init__(self, player_name):
        self.name = player_name
        self.prize_money = 0
        self.prizes = []

    def addMoney(self, amt):
       if amt > 0:
           self.prize_money += amt

    def goBankrupt(self):
        self.prize_money = 0

    def addPrizes(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return f"{self.name} (${self.prize_money})"