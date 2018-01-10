class Piece():
    

    def __init__(self, name, num, color):
        self.pos = 0
        self.num = num
        self.name = name
        self.color = color
    
    def getPosition(self):
        return self.position

    def getPiece(self):
        return (self.name, self.num, self.color)
    
    def movePiece(self, coord):
        self.position = coord
        
  
