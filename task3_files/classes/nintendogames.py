from task3_files.classes import game

class NintendoGames(game.Game):
    def __init__(self, name, platform, genre, price, release_date, availability, pegi):
        super().__init__(name, platform, genre, price, release_date, availability, pegi)
    
    @staticmethod
    def allNintendogames(self):
        if self.platform == 'Nintendo Switch' or self.platform == 'Nintendo Wii' or self.platform == 'Nintendo Wii U':
            game.Game.isAdultGame(game.Game)
            game.Game.printGameInfo(self)