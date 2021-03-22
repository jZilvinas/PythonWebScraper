from task3_files.classes import game
from task3_files.classes import cart
from task3_files.classes import psgames
from task3_files.classes import xboxgames
import readingwriting
import sys

def getJsonFileName(jsonFileName):
    return jsonFileName

def execute():
    for item in games:
        item.printGameInfo()
        print()
        avgPriceList.append(item)
        compareList.append(item)
        cartlist.append(item)
    psgames.PSGames.comparePrices(psgames.PSGames, compareList)
    xboxgames.XboxGames.averagePrice(xboxgames.XboxGames, avgPriceList)
    cart.Cart.addItemToCart(cart.Cart, cartlist, cartItems)
    #cart.Cart.emptyCart(cart.Cart, cartItems)
    cart.Cart.countTotalPrice(cart.Cart, cartItems)
    cart.Cart.countTotalItems(cart.Cart, cartItems)
    print()

#DEMO
jsonFileName = sys.argv[1]
games = []
avgPriceList = []
compareList = []
cartlist = []
cartItems = []

games = readingwriting.dataRead(jsonFileName)
execute()
readingwriting.dataWrite(games, jsonFileName)
