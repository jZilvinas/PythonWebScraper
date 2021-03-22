from task3_files.classes import game

class PSVitaGames(game.Game):
    def __init__(self, name, platform, genre, price, release_date, availability, pegi):
        super().__init__(name, platform, genre, price, release_date, availability, pegi)
    
    @staticmethod
    def allPSVitaGames(self):
        if self.platform == 'PSVITA' or self.platform == 'PSP':
            game.Game.isAdultGame(game.Game)
            game.Game.printGameInfo(self)