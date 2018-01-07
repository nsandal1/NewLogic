class Coordinates():                    #dictionary of (name,pieceNo) and (coordinate)

    def __init__(self,players):
        
        self.locations= {}                  #dictionary for location of pieces
        for i in range(len(players)):
            for j in range(4):              #loops 4 times bc 4 pieces
                self.locations[(players[i].retName(), j+1 )] = players[i].retPieceN(j).getPosition()
            
    def getDict(self):
        return self.locations

    def piece2grid(self):                 #takes in mouse click and moves to nearest square testing if valid
        pass

    def checkIfEmpty(self,position):
        ####3
        #print(position)
        #print(self.locations.values())
        #####
        return not(position in self.locations.values())

    def whoIsThere(self,position):
        return next((k for k, v in self.locations.items() if v == position), None)
 
        #returns tuple for (name, pieceNo)

        

    def updatePos(self,piece):
        
        self.locations[piece.getPiece()]=piece.getPosition()
        
