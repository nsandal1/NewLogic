import Player



class Game():                               

    def __init__(self, number):
        self.noPlayers=number
        self.players=[]
        self.names=[]
        self.allpieces=[]

        #create Player instances
        for i in range(number):
            self.players.append(Player.Player(input("\n\nPlayer {0} name: ".format(i+1)),input("Player {0} color: ".format(i+1)),i+1))

        #fill Names list
        for i in self.players:
            self.names.append(i.retName())
            
        for item in self.players:
            self.allpieces += item.pieces
           
    
    def winCondition(self):
        for i in self.players:
                if i.retWin() == 4:
                        return True
        return False
                    
         
    def roll(self):
 
        ##get roll from front end

    def getNo(self):
        return self.noPlayers
    
    def retPlayers(self):
        print(self.players)

    def retPlayerN(self,n):
        return self.players[n]
    
    def checkValid(self, piece, roll, newcoord): 
        if piece.pos % 1: 
            if piece.pos + roll == newcoord:
                return True
            if piece.pos + roll >= 20:
                if newcoord == 20:
                    return True 
       if (piece.pos - .1) % 1:
            if piece.pos + roll == newcoord: 
                return True
            if piece.pos + roll > 15:
                if piece.poss + roll -.1 == newcoord:
                    return True
       elif (piece.pos - 10) % .7:
            if piece.pos + .7*roll == newcoord:
                return True
            if piece.pos + .7*roll > 14:
                if newcoord == 20:
                    return True
       if piece.pos == 5:
           if piece.pos + 4.1 + roll == newcoord:
                return True
       if piece.pos == 10:
           if piece.pos + .7*roll == newcoord:
                return True
       if piece.pos == 12.1: 
           if piece.pos + .7*roll == newcoord:
                return True
           if piece.pos + .7*roll > 14:
                if newcoord == 20:
                    return True
       else:
           return False
                

    #Game develops from here

    def development(self):
        turn=0
        roll= None
        piece = None
       
            
        while not self.winCondition():
            
            print("\n\n[[[[ It is Player {0}'s turn ]]]] \n\n".format(turn+1))
            #self.whereAre(self.retPlayerN(turn).retName())
            
            roll = [self.roll()]                                #adds first roll value to list
            print("\nYou rolled a {0}!\n".format(roll[0]))
            #roll = int(input("\nroll: "))
            
            while roll[-1] == 5 or roll[-1] ==4:
                roll.append(self.roll())
                print("\nYou rolled a {0}!\n".format(roll[-1]))

            ##print("your options are:{0} ...".format(roll))
            
            #keep rolling until not five
            #values get added to list
            #pop a value in desired order
            #make the move
            #pop another value...etc...until roll == []
            #iterating len(roll) times unless game is over


            for i in range(len(roll)):

                        currRoll = roll.pop(roll.index(int(input("\nchoose your desired roll:{0}...".format(roll)))))
            
                        print("You rolled a {0}!\n".format(currRoll))
                        piece = self.retPlayerN(turn).retPieceN(int(input("Select a Valid Piece to Move: ")))
                        newcoord = (input("Input valid coordinate: ")). ##frontend help
                        if checkValid(piece, roll, newcoor): 
                            for item in self.allpieces:
                                if item.pos == piece.pos:
                                    item.move(newcoor)
                                    if item.pos == 20:
                                        self.retPlayerN(turn).win += 1
                                if item.pos == newcoord:
                                    if item.name != piece.name:
                                        item.pos = 0
                                    
                                    
      ############                      
                       
                         

                        #branching decisions should go here
                        
                        if self.validateMove(piece) == "continue":
                                self.coords.updatePos(piece)
                                print(piece.retLastPos(),"---->",piece.getPosition())

                        elif self.validateMove(piece) == "eat":
                                eaten = self.coords.whoIsThere(piece.getPosition())
                                self.coords.updatePos(piece)
                                print(piece.retLastPos(),"---->",piece.getPosition())
                                player=self.players[self.names.index(eaten[0])]
                                eatenPiece=player.retPieceN(eaten[1])        #redifined what piece is:redefined as piece being eaten...change var name?
                                eatenPiece.eat()
                                self.coords.updatePos(eatenPiece)
                                                                                                                #need to uncombine
                                self.whereAre()
                                print("\n\n",self.retPlayerN(turn).retName(), "ate one of ", player.retName(),"'s pieces!")
 
                        elif self.validateMove(piece) == "promote":
                                self.coords.updatePos(piece)
                                self.player[self.names.index(self.piece.getPiece()[0])].incWin()
                                #self.retPlayerN(turn).incPromoted()

                                print("\n\n !!!!!  Player {0} has {1} Point(s)    !!!!".format(self.names[(turn)],self.retPlayerN(turn).retPromoted()))
                                

                        elif self.validateMove(piece) == "combine":
                        
                                piece.combine()

                        else: print("You should never get here")
                        
    ############
            
            
            turn = (turn + 1) % self.noPlayers



def main():
    
    game1=Game(int(input("How many players? ")))    
    game1.development()
  
    if not(input("restart?... ").lower() == "n"):
        main()
    


if __name__== "__main__":
    main()




