import unittest
import individualAssign1

class TestIndividualAssign1(unittest.TestCase):

    def test_randomRank(self):
        cardInHandRank = [10, 7]
        cardInHandSuit = ['Spade', 'Heart']
        rankSelected = 3
        suitSelected = 'Club'
        
        sorted_rank = individualAssign1.sortRank(cardInHandRank, cardInHandSuit, rankSelected, suitSelected)
        self.assertEqual(sorted_rank, [3, 7, 10])