from task3_files.classes import game

class PSGames(game.Game):
    def __init__(self, name, platform, genre, price, release_date, availability, pegi):
        super().__init__(name, platform, genre, price, release_date, availability, pegi)

    @staticmethod
    def allPSgames(self):
        if self.platform == 'Playstation 4' or self.platform == 'Playstation 3':
            game.Game.isAdultGame(game.Game)
            game.Game.printGameInfo(self)
    
    def comparePrices(self, compareList):
        cmplist = []
        for i in compareList:
            cmplist.append(i.name)
            cmplist.append(i.platform)
            cmplist.append(i.price)

        if len(compareList) == 2:
            if cmplist[0] == cmplist[3] and cmplist[1] != cmplist[4]:
                if cmplist[2] > cmplist[5]:
                    print('{} for {} is more expensive than for {}.'.format(cmplist[0], cmplist[1], cmplist[4]))
                    return True
                elif cmplist[2] < cmplist[5]:
                    print('{} for {} is more cheaper than for {}.'.format(cmplist[0], cmplist[1], cmplist[4]))
                    x = False
                    return x
                elif cmplist[2] == cmplist[5]:
                    print('{} prices for {} and {} are equal.'.format(cmplist[0], cmplist[1], cmplist[4]))
                    x = None
                    return x

        else:
            print('Price comparison could be possible only between two products.')


