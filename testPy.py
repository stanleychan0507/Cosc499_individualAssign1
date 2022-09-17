import unittest

class TestIndividualAssign1(unittest.TestCase):

    def test_randomRank(self):
        rank = [10, 7, 3]
        sorted_rank = self(rank)
        self.assertEqual(sorted_rank, [3, 7, 10])