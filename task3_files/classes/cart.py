from task3_files.classes import game



class Cart(game.Game):
    def __init__(self, name, platform, genre, price, release_date, availability, pegi, totalItems, totalPrice):
        super().__init__(name, platform, genre, price, release_date, availability, pegi)
        self.totalItems = totalItems
        self.totalPrice = totalPrice
    
    def addItemToCart(self, cartlist, cartItems):
        for line in cartlist:
            if line.availability != 'Šiuo metu prekės neturime':
                cartItems.append(line)

    def countTotalPrice(self, cartItems):
        self.totalPrice = 0
        if cartItems != None:
            for i in cartItems:
                if i.availability != 'Šiuo metu prekės neturime':
                    self.totalPrice = self.totalPrice + float(i.price)
        print('Cart total price is: {} Eur'.format(round(self.totalPrice, 2)))
        return self.totalPrice
    
    def countTotalItems(self, cartItems):
        self.totalItems = 0
        if cartItems != None:
            for i in cartItems:
                if i.availability != 'Šiuo metu prekės neturime':
                    self.totalItems = self.totalItems + 1
        print('{} item/items in the cart'.format(self.totalItems))
        return self.totalItems

    def emptyCart(self, cartItems):
        cartItems.clear()
        print(cartItems)
