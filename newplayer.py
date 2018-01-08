import Piece

class Player():

    def __init__(self,name, color, order):
        self.name=name
        self.color=color
        self.order=order
        self.win = 0
        self.pieces = []
        for i in 4:
            self.pieces.append(Piece(name, i, color)
            

    def retPieceN(self,n):          #returns the Nth piece
        return self.pieces[n-1]

    def retOrder(self):
        return self.order

    def retColor(self):
        return self.color

    def retName(self):
        return self.name
    
    def retWin(self):
        return self.win

    
