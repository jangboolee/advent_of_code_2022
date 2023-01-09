import unittest
import supply_stacks


class TestSupplyStacks(unittest.TestCase):

    def test_parse_stacks(self):

        raw_1 = ['    [D]    ',
                 '[N] [C]    ',
                 '[Z] [M] [P]']

        actual_1 = supply_stacks.parse_stacks(raw_1, 3)

        expected_1 = {1: [' ', 'N', 'Z'],
                      2: ['D', 'C', 'M'],
                      3: [' ', ' ', 'P']}

        self.assertDictEqual(actual_1, expected_1)


if __name__ == '__main__':

    unittest.main()
