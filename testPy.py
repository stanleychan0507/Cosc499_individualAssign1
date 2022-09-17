import unittest
import individualAssign1

class TestIndividualAssign1(unittest.TestCase):

    def test_randomRank(self):
        rank = [10, 7, 3]
        sorted_rank = individualAssign1.sortCard(rank)
        self.assertEqual(sorted_rank, [3, 7, 10])