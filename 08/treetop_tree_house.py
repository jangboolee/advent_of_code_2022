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


def from_up(tree_map: list, row: int, col: int) -> list:
    """Find the trees above the tree of interest

    Args:
        tree_map (list): List of lists representing the tree map
        row (int): Row number for the tree of interest
        col (int): Column number for the tree of interest

    Returns:
        list: List of the trees above the tree of interest
    """
    return [tree_row[col] for i, tree_row in enumerate(tree_map)
            if i < row]


def from_down(tree_map: list, row: int, col: int) -> list:
    """Find the trees below the tree of interest

    Args:
        tree_map (list): List of lists representing the tree map
        row (int): Row number for the tree of interest
        col (int): Column number for the tree of interest

    Returns:
        list: List of the trees below the tree of interest
    """
    return [tree_row[col] for i, tree_row in enumerate(tree_map)
            if i > row]


def from_left(tree_map: list, row: int, col: int) -> list:
    """Find the trees left of the tree of interest

    Args:
        tree_map (list): List of lists representing the tree map
        row (int): Row number for the tree of interest
        col (int): Column number for the tree of interest

    Returns:
        list: List of the trees left the tree of interest
    """
    return tree_map[row][0:col]


def from_right(tree_map: list, row: int, col: int) -> list:
    """Find the trees to the right of the tree of interest

    Args:
        tree_map (list): List of lists representing the tree map
        row (int): Row number for the tree of interest
        col (int): Column number for the tree of interest

    Returns:
        list: List of the trees right of the tree of interest
    """
    return tree_map[row][col+1:]


def is_inner_tree(tree_map: list, row: int, col: int) -> bool:
    """Check if the tree is an inner tree or not

    Args:
        tree_map (list): List of lists representing the tree map
        row (int): Row number for the tree of interest
        col (int): Column number for the tree of interest

    Returns:
        bool: True if inner tree, False if outer tree
    """

    if (row == 0 or row == len(tree_map) - 1
            or col == 0 or col == len(tree_map[row]) - 1):
        return False
    else:
        return True


def count_visible_trees(tree_map: list) -> int:
    """Count the number of visible trees in the map

    Args:
        tree_map (list): List of lists representing the tree map

    Returns:
        int: Number of visible trees in the map
    """

    # Find the count of visible trees
    visible_count = 0
    for row in range(len(tree_map)):
        for col in range(len(tree_map[row])):

            # Find the value of the current tree being compared
            curr_tree = tree_map[row][col]

            # If the tree is an inner tree
            if is_inner_tree(tree_map, row, col):
                # If the tree height is less than or equal to the
                # tallest tree from all four directions
                if (max(from_up(tree_map, row, col)) >= curr_tree and
                    max(from_down(tree_map, row, col)) >= curr_tree and
                    max(from_left(tree_map, row, col)) >= curr_tree and
                        max(from_right(tree_map, row, col)) >= curr_tree):
                    # The tree is not visible, so skip the tree
                    continue

            # If the tree is not skipped, then it is visible
            visible_count += 1

    return visible_count


def calc_scenic_score(tree_map: list, row: int, col: int) -> int:

    def calc_up_scenic_score(tree_map: list, row: int, col: int) -> int:
        """Calculate scenic score for a tree's upper side

        Args:
            tree_map (list): List of lists representing the tree map
            row (int): Row number for the tree of interest
            col (int): Column number for the tree of interest

        Returns:
            int: Upper-side scenic score
        """
        score = 0
        curr_tree = tree_map[row][col]

        for up_tree in from_up(tree_map, row, col)[::-1]:
            if curr_tree > up_tree:
                score += 1
            else:
                score += 1
                break

        return score

    def calc_left_scenic_score(tree_map: list, row: int, col: int) -> int:
        """Calculate scenic score for a tree's left side

        Args:
            tree_map (list): List of lists representing the tree map
            row (int): Row number for the tree of interest
            col (int): Column number for the tree of interest

        Returns:
            int: Left-side scenic score
        """

        score = 0
        curr_tree = tree_map[row][col]

        for left_tree in from_left(tree_map, row, col)[::-1]:
            if curr_tree > left_tree:
                score += 1
            else:
                score += 1
                break

        return score

    def calc_right_scenic_score(tree_map: list, row: int, col: int) -> int:
        """Calculate scenic score for a tree's right side

        Args:
            tree_map (list): List of lists representing the tree map
            row (int): Row number for the tree of interest
            col (int): Column number for the tree of interest

        Returns:
            int: Right-side scenic score
        """
        score = 0
        curr_tree = tree_map[row][col]

        for right_tree in from_right(tree_map, row, col):
            if curr_tree > right_tree:
                score += 1
            else:
                score += 1
                break
        return score

    def calc_down_scenic_score(tree_map: list, row: int, col: int) -> int:
        """Calculate scenic score for a tree's lower side

        Args:
            tree_map (list): List of lists representing the tree map
            row (int): Row number for the tree of interest
            col (int): Column number for the tree of interest

        Returns:
            int: Lower-side scenic score
        """
        score = 0
        curr_tree = tree_map[row][col]

        for down_tree in from_down(tree_map, row, col):
            if curr_tree > down_tree:
                score += 1
            else:
                score += 1
                break

        return score

    # Calculate scenic scores only for inner trees
    if is_inner_tree(tree_map, row, col):

        # Calculate scenic scores for each direction
        up_score = calc_up_scenic_score(tree_map,
                                        row, col)
        left_score = calc_left_scenic_score(tree_map,
                                            row, col)
        right_score = calc_right_scenic_score(tree_map,
                                              row, col)
        down_score = calc_down_scenic_score(tree_map,
                                            row, col)

        # Find total scenic score
        return up_score * left_score * right_score * down_score

    # Assign scenic scores of 0 for trees on the edges
    else:
        return 0


def calc_max_scenic_score(tree_map: list) -> int:
    """Calculate the maximum scenic score for the tree map

    Args:
        tree_map (list): List of lists representing the tree map

    Returns:
        int: Maximum scenic score possible in the tree map
    """

    # Initialize max scenic score tracker
    max_scenic_score = 0

    # Loop through every tree
    for row in range(len(tree_map)):
        for col in range(len(tree_map[row])):

            # Calculate the scenic score for each tree
            curr_tree_score = calc_scenic_score(tree_map, row, col)

            # Update maximum score tracker when needed
            if curr_tree_score > max_scenic_score:
                max_scenic_score = curr_tree_score

    return max_scenic_score


if __name__ == '__main__':

    tree_map = read_input('08', 'input.txt')

    # Solution to part 1
    visible_trees = count_visible_trees(tree_map)
    print(f'There are {visible_trees} visible trees from outside the grid.')

    max_scenic_score = calc_max_scenic_score(tree_map)
    print(f'The highest scenic score possible is {max_scenic_score}.')
