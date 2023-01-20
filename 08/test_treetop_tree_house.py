import unittest
import treetop_tree_house as tth


class TestTreetopTreeHouse(unittest.TestCase):

    example_map = [[3, 0, 3, 7, 3],
                   [2, 5, 5, 1, 2],
                   [6, 5, 3, 4, 2],
                   [3, 3, 5, 4, 9],
                   [3, 5, 3, 9, 0]]

    def test_count_visible_trees(self):

        # Test using example case
        ex_actual = tth.count_visible_trees(self.example_map)
        ex_expected = 21
        self.assertEqual(ex_actual, ex_expected)

        # Test a case where every tree is visible
        map_1 = [[0, 0, 0, 0],
                 [0, 1, 1, 0],
                 [0, 1, 1, 0],
                 [0, 0, 0, 0]]

        actual_1 = tth.count_visible_trees(map_1)
        expected_1 = 16
        self.assertEqual(actual_1, expected_1)

        # Test a case where no inner tree is visible
        map_2 = [[9, 9, 9, 9],
                 [9, 1, 1, 9],
                 [9, 1, 1, 9],
                 [9, 9, 9, 9]]

        actual_2 = tth.count_visible_trees(map_2)
        expected_2 = 12
        self.assertEqual(actual_2, expected_2)


if __name__ == '__main__':

    unittest.main()
