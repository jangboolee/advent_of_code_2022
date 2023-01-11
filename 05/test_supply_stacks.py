import unittest
import supply_stacks


class TestSupplyStacks(unittest.TestCase):

    def test_parse_stacks(self):

        # Test example stack
        raw_1 = ['    [D]    ',
                 '[N] [C]    ',
                 '[Z] [M] [P]']

        actual_1 = supply_stacks.parse_stacks(raw_1, 3)

        expected_1 = {1: ['N', 'Z'],
                      2: ['D', 'C', 'M'],
                      3: ['P']}

        self.assertDictEqual(actual_1, expected_1)

        # Test singular stack
        raw_2 = ['[A]',
                 '[B]',
                 '[C]',
                 '[D]']

        actual_2 = supply_stacks.parse_stacks(raw_2, 1)

        expected_2 = {1: ['A', 'B', 'C', 'D']}

        self.assertDictEqual(actual_2, expected_2)

    def test_operate_crate_mover_9000(self):

        # Test first instruction on example stack
        raw_1 = ['    [D]    ',
                 '[N] [C]    ',
                 '[Z] [M] [P]']

        actual_1 = supply_stacks.parse_stacks(raw_1, 3)

        supply_stacks.operate_crane_mover_9000(actual_1,
                                               'move 1 from 2 to 1')

        expected_1 = {1: ['D', 'N', 'Z'],
                      2: ['C', 'M'],
                      3: ['P']}

        self.assertDictEqual(actual_1, expected_1)

        # Test all remaining instructions on example
        supply_stacks.operate_crane_mover_9000(actual_1,
                                               'move 3 from 1 to 3')
        supply_stacks.operate_crane_mover_9000(actual_1,
                                               'move 2 from 2 to 1')
        supply_stacks.operate_crane_mover_9000(actual_1,
                                               'move 1 from 1 to 2')

        expected_2 = {1: ['C'],
                      2: ['M'],
                      3: ['Z', 'N', 'D', 'P']}

        self.assertDictEqual(actual_1, expected_2)

    def test_operate_crate_mover_9001(self):

        # Test first instruction on example stack
        raw_1 = ['    [D]    ',
                 '[N] [C]    ',
                 '[Z] [M] [P]']

        actual_1 = supply_stacks.parse_stacks(raw_1, 3)

        supply_stacks.operate_crane_mover_9001(actual_1,
                                               'move 1 from 2 to 1')

        expected_1 = {1: ['D', 'N', 'Z'],
                      2: ['C', 'M'],
                      3: ['P']}

        self.assertDictEqual(actual_1, expected_1)

        # Test all remaining instructions on example
        supply_stacks.operate_crane_mover_9001(actual_1,
                                               'move 3 from 1 to 3')
        supply_stacks.operate_crane_mover_9001(actual_1,
                                               'move 2 from 2 to 1')
        supply_stacks.operate_crane_mover_9001(actual_1,
                                               'move 1 from 1 to 2')

        expected_2 = {1: ['M'],
                      2: ['C'],
                      3: ['D', 'N', 'Z', 'P']}

        self.assertDictEqual(actual_1, expected_2)


if __name__ == '__main__':

    unittest.main()
