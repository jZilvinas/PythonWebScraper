from task3_files.classes import game

class XboxGames(game.Game):
    def __init__(self, name, platform, genre, price, release_date, availability, pegi, pricesSum, avgPrice):
        super().__init__(name, platform, genre, price, release_date, availability, pegi)
        self.pricesSum = pricesSum
        self.avgPrice = avgPrice

    @staticmethod
    def allXboxgames(self):
        if self.platform == 'Xbox One' or self.platform == 'Xbox 360':
            game.Game.isAdultGame(game.Game)
            game.Game.printGameInfo(self)
    
    def averagePrice(self, avgPriceList):
        self.pricesSum = 0
        counter = 0
        for i in avgPriceList:
            self.pricesSum = self.pricesSum + float(i.price)
            counter +=1
        self.avgPrice = self.pricesSum / counter
        print('Average price of all games is {} Eur'.format(round(self.avgPrice, 2)))
        return round(self.avgPrice, 2)
     