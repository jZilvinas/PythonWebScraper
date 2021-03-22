
class Game:
    def __init__(self, name, platform, genre, price, release_date, availability, pegi):
        self.name = name
        self.genre = genre
        self.platform = platform
        self.price = price
        self.release_date = release_date
        self.availability = availability
        self.pegi = pegi

    def printGameInfo(self):
        warning = self.isAdultGame(self)
        print()
        print('Name:          ' + self.name)
        print('Genre:         ' + self.genre)
        print('Compatible on: ' + self.platform)
        print('Price:         ' + str(self.price) + ' Eur')
        print('Release date:  ' + self.release_date)
        print('Availability:  ' + self.availability)
        if warning == True:
            print('PEGI rating:   ' + self.pegi + ' (Game is for adults only!!)')
        else:
            print('PEGI rating:   ' + self.pegi)
       

        return 'All lines printed'

    def getName(self):
        return self.name
    def getGenre(self):
        return self.genre
    def getPlatform(self):
        return self.platform
    def getPrice(self):
        return self.price
    def getReleaseDate(self):
        return self.release_date
    def getAvailability(self):
        return self.availability
    def getPegi(self):
        return self.pegi


    @staticmethod
    def isAdultGame(self):
        if self.pegi == '18+':
            return True

    '''
    @staticmethod
    def distribution(self):
        if Game.getPlatform(Game) == 'Playstation 4' or Game.getPlatform(Game) == 'Playstation 3':
            psgames.PSGames.allPSgames(Game)
        elif Game.getPlatform(Game) == 'Xbox One' or Game.getPlatform(Game) == 'Xbox 360':
            xboxgames.XboxGames.allXboxgames(Game)
        elif Game.getPlatform(Game) == 'Nintendo Switch' or Game.getPlatform(Game) == 'Nintendo Wii' or Game.getPlatform(Game) == 'Nintendo Wii U':
            nintendogames.NintendoGames.allNintendogames(Game)
        elif Game.getPlatform(Game) == 'PSVITA' or Game.getPlatform(Game) == 'PSP':
            psvitagames.PSVitaGames.allPSVitaGames(Game)
    '''
   