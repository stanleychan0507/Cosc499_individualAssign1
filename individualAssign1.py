from random import randrange

suit = ["Spade", "Heart", "Club", "Diamond"];
rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
cardInHandSuit = []
cardInHandRank = []

def suitRandom():
    return randrange(0,3)
def rankRandom():
    return randrange(0,12)
def num_rank(rank):
    if rank[0] == "A":
         return 0
    if rank[0] == "J":
         return 11
    if rank[0] == "Q":
         return 12
    if rank[0] == "K":
         return 13
    return int(rank)

val = int(input("How many card you wish to generate?"))
i = 0
x = 0
if val == 0:
    print("No cards being drawn.")
    exit()
else:   
    rankSelected = rank[rankRandom()]
    suitSelected = suit[suitRandom()]

    cardInHandSuit.append(suitSelected)
    cardInHandRank.append(rankSelected)
    print("The random generated card is : ")
    #print(cardInHandSuit[i] + " of " + cardInHandRank[i])
    print(cardInHandSuit)
    print(cardInHandRank)

    while i < val-1:
        rankSelected = rank[rankRandom()]
        suitSelected = suit[suitRandom()]
        
        while x <= len(cardInHandRank):
            print("value of x is : ")
            print(x)
            print("length of cardInHandRank is :")
            print(len(cardInHandRank))
            if rankSelected == "Ace":
                cardInHandRank.insert(0, rankSelected)
                cardInHandSuit.insert(0, suitSelected)
                print("Ace")
                x+=1
                break
            elif rankSelected == "Jack":
                cardInHandRank.insert(x, rankSelected)
                cardInHandSuit.insert(x, suitSelected)
                print("Jack")
                x+=1
                break
            elif rankSelected == "Queen":
                cardInHandRank.insert(x, rankSelected)
                cardInHandSuit.insert(x, suitSelected)
                print("Queen")
                x+=1
                break
            elif rankSelected == "King":
                cardInHandRank.append(x, rankSelected)
                cardInHandSuit.append(x, suitSelected)
                print("King")
                x+=1
                break
            elif rankSelected >= cardInHandRank[x]:
                cardInHandSuit.append(suitSelected)
                cardInHandRank.append(rankSelected)
                print("append")
                x+=1
                break
            elif rankSelected < cardInHandRank[x]:
                cardInHandRank.insert(x, rankSelected)
                cardInHandSuit.insert(x, suitSelected)
                print("insert")
                x+=1
                break

        print("The random generated card is : ")
        #print(cardInHandSuit[i] + " of " + cardInHandRank[i])
        print(cardInHandSuit)
        print(cardInHandRank)
        i+=1



