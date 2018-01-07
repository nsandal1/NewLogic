class Piece():

    def __init__(self, name, num, color):
        self.position = (0,"x")
        self.num = num
        self.name = name
        self.color = color
        self.status = 'queued'
        self.stuckTo = None
        self.lastPos = None
    
    def getPosition(self):
        return self.position

    def getPiece(self):
        return (self.name, self.num, self.color, self.status)
    
    def retLastPos(self):
        return self.lastPos
    
    def playPiece(self):
        self.status = 'inPlay'
        
    def completePiece(self):
        self.status = 'completed'
    
    def movePiece(self, dieRoll):
        self.position += dieRoll
        
    def stickToPiece(self, piece):
        self.stuckTo = piece
    
    def eat(self):
        self.position = (0,"x")
        

    def move(self, coord):
        if type(coord) is tuple:
            self.lastPos = self.position            #need it to undo a bad move
            self.position = int(coord[0]),coord[1]
            #print(self.getPosition()) #debugging
    
            #add logic for case where peices are stuck together
        else: print("coordinate is not tuple")
