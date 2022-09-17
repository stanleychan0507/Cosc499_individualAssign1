from random import randrange

suit = ["Spade", "Heart", "Club", "Diamond"]
rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cardInHandSuit = []
cardInHandRank = []

def sortRank(cardInHandRank, cardInHandSuit, rankSelected, suitSelected):
    i = 0
    while i < len(cardInHandRank):
        if rankSelected > cardInHandRank[i]:
            cardInHandRank.insert(i+1, rankSelected)
            cardInHandSuit.insert(i+1, suitSelected)
            break
        else :
            cardInHandRank.insert(i-1, rankSelected)
            cardInHandSuit.insert(i-1, suitSelected)
            break
        i+=1

i = 0
numOfCard = 3 
cardInHandRank.append(rank[randrange(0,12)])
cardInHandSuit.append(suit[randrange(0,3)])

while i < numOfCard-1:
    rankSelected = rank[randrange(0,12)]
    suitSelected = suit[randrange(0,3)]
    sortRank(cardInHandRank, cardInHandSuit, rankSelected, suitSelected)
    i+=1