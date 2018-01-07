import Piece

class Player():

    def __init__(self,name, color, order):
        self.name=name
        self.color=color
        self.pieces=(Piece.Piece(name,1,color),Piece.Piece(name,2,color),Piece.Piece(name,3,color),Piece.Piece(name,4,color))   #piece should contain player name
        self.order=order
        self.win = 0

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

    
