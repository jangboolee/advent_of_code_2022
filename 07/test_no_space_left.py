import unittest
import os
import no_space_left


class TestNoSpaceLeft(unittest.TestCase):

    def test_change_directory(self):

        self.assertEqual(no_space_left.change_directory('', '$ cd /'), '/')
        self.assertEqual(no_space_left.change_directory('/', '$ cd a'), '/a')
        self.assertEqual(no_space_left.change_directory('/a', '$ cd e'),
                         '/a/e')
        self.assertEqual(no_space_left.change_directory('/a/e', '$ cd ..'),
                         '/a')
        self.assertEqual(no_space_left.change_directory('/a', '$ cd ..'), '/')

    def test_create_system_directory(self):

        # Set directories for folder and input file
        main_folder = os.path.join(os.getcwd(), '07')
        input_file = os.path.join(main_folder, 'sample_input.txt')

        with open(os.path.join(main_folder, input_file), 'r') as f:
            outputs = [line.rstrip() for line in f.readlines()]

        expected = {'/': {'children': ['a', 'd'],
                          'files': [('b.txt', 14848514), ('c.dat', 8504156)],
                          'size': 23352670},
                    '/a': {'children': ['e'],
                           'files': [('f', 29116), ('g', 2557),
                                     ('h.lst', 62596)],
                           'size': 94269},
                    '/a/e': {'children': [], 'files': [('i', 584)],
                             'size': 584},
                    '/d': {'children': [],
                           'files': [('j', 4060174), ('d.log', 8033020),
                                     ('d.ext', 5626152), ('k', 7214296)],
                           'size': 24933642}
                    }

        actual = no_space_left.create_system_directory(outputs)
        self.assertDictEqual(actual, expected)

    def test_calc_total_size(self):

        test_1 = {'/': {'size': 100},
                  '/a': {'size': 10},
                  '/a/b': {'size': 20},
                  '/a/b/c': {'size': 30},
                  '/d': {'size': 40}
                  }

        expected_1 = {'/': 200, '/a': 60, '/a/b': 50, '/a/b/c': 30, '/d': 40}

        self.assertDictEqual(no_space_left.calc_total_size(test_1), expected_1)

    def test_calc_size_below_threshold(self):

        test_1 = {'/': 200, '/a': 60, '/a/b': 50, '/a/b/c': 30, '/d': 40}

        expected_1 = 70
        actual_1 = no_space_left.calc_size_below_threshold(test_1, 45)

        self.assertEqual(expected_1, actual_1)

        expected_2 = 180
        actual_2 = no_space_left.calc_size_below_threshold(test_1, 100)

        self.assertEqual(expected_2, actual_2)

    def test_find_minimum_deletable_directory(self):

        test_1 = {'/': 200, '/a': 60, '/a/b': 50, '/a/b/c': 30, '/d': 40}

        expected_1 = ('/d', 40)
        actual_1 = no_space_left.find_minimum_deletable_directory(test_1,
                                                                  300,
                                                                  135)

        self.assertEqual(expected_1, actual_1)

        expected_2 = ('/a/b/c', 30)
        actual_2 = no_space_left.find_minimum_deletable_directory(test_1,
                                                                  300,
                                                                  130)

        self.assertEqual(expected_2, actual_2)

        expected_3 = ('/a/b', 50)
        actual_3 = no_space_left.find_minimum_deletable_directory(test_1,
                                                                  300,
                                                                  150)

        self.assertEqual(expected_3, actual_3)


if __name__ == '__main__':

    unittest.main()
