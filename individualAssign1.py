from random import randrange

suit = ["Spade", "Heart", "Club", "Diamond"]
rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cardInHandSuit = []
cardInHandRank = []


i = 0
val = int(input("How many card you wish to generate?"))
if val == 0:
    print("No cards being drawn.")
    exit()
else:   
    while i < val:
        rankSelected = rank[randrange(0,12)]
        suitSelected = suit[randrange(0,3)]
        #sortRank(rankSelected)
        print(rankSelected)