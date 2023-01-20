import os


def read_input(folder_name: str, file_name: str) -> list:
    """Read in the input file

    Args:
        folder_name (str): Folder name containing the input file
        file_name (str): File name of the input file

    Returns:
        list: A list of lists for the tree map
    """

    # Set directories for folder and input file
    main_folder = os.path.join(os.getcwd(), folder_name)
    input_file = os.path.join(main_folder, file_name)

    # Read in input file as a list of lists
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = [line.rstrip() for line in f.readlines()]
        tree_map = []
        for line in f_content:
            tree_map.append([int(char) for char in line])

    return tree_map


def count_visible_trees(tree_map: list) -> int:

    def max_from_up(tree_map: list, row: int, col: int) -> int:
        """Helper function to return the maximum tree height when looking up

        Args:
            tree_map (list): List of lists representing the tree map
            row (int): Row number for the tree of interest
            col (int): Column number for the tree of interest

        Returns:
            int: Maximum height of the trees above the tree of interest
        """
        return max([tree_row[col] for i, tree_row in enumerate(tree_map)
                    if i < row])

    def max_from_down(tree_map: list, row: int, col: int) -> int:
        """Helper function to return the maximum tree height when looking down

        Args:
            tree_map (list): List of lists representing the tree map
            row (int): Row number for the tree of interest
            col (int): Column number for the tree of interest

        Returns:
            int: Maximum height of the trees below the tree of interest
        """
        return max([tree_row[col] for i, tree_row in enumerate(tree_map)
                    if i > row])

    def max_from_left(tree_map: list, row: int, col: int) -> int:
        """Helper function to return the maximum tree height when looking left

        Args:
            tree_map (list): List of lists representing the tree map
            row (int): Row number for the tree of interest
            col (int): Column number for the tree of interest

        Returns:
            int: Maximum height of the trees left of the tree of interest
        """
        return max(tree_map[row][0:col])

    def max_from_right(tree_map: list, row: int, col: int) -> int:
        """Helper function to return the maximum tree height when looking right

        Args:
            tree_map (list): List of lists representing the tree map
            row (int): Row number for the tree of interest
            col (int): Column number for the tree of interest

        Returns:
            int: Maximum height of the trees right of the tree of interest
        """
        return max(tree_map[row][col+1:])

    # Find the count of visible trees
    visible_count = 0
    for row in range(len(tree_map)):
        for col in range(len(tree_map[row])):

            # Find the value of the current tree being compared
            curr_tree = tree_map[row][col]

            # If the tree is not in the first or last row
            if row > 0 and row < len(tree_map) - 1:
                # If the tree is not int he first or last column
                if col > 0 and col < len(tree_map[row]) - 1:
                    # If the tree is less than or equal to the maximum tree
                    # from all four directions
                    if (max_from_up(tree_map, row, col) >= curr_tree and
                        max_from_down(tree_map, row, col) >= curr_tree and
                        max_from_left(tree_map, row, col) >= curr_tree and
                            max_from_right(tree_map, row, col) >= curr_tree):
                        # The tree is not visible, so skip the tree
                        continue

            # If the tree is not skipped, then it is visible
            visible_count += 1

    return visible_count


if __name__ == '__main__':

    tree_map = read_input('08', 'input.txt')
    visible_trees = count_visible_trees(tree_map)
    print(f'There are {visible_trees} visible trees from outside the grid.')
