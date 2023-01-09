import os


# Set directories for folder and input file
main_folder = os.path.join(os.getcwd(), '04')
input_file = os.path.join(main_folder, 'input.txt')

# Read in input file as a list, with each pair split
with open(input_file, 'r', encoding='utf-8') as f:
    f_content = [line.rstrip().split(',') for line in f.readlines()]


def convert_str_assignment(str_assignment):
    """Helper function to convert assignment string into integers

    Args:
        str_assignment (str): String representation of an assignment
        (ex: '14-28')

    Returns:
        range: A range generator function of the assignment
    """

    # Get a tuple of the beginning and end sections, converted to int
    int_sections = tuple(int(str_section) for str_section
                         in str_assignment.split('-'))

    return range(int_sections[0], int_sections[1] + 1)


# Create a list of tuples of assignments converted to range generators
int_assignments = []
for str_assignment_1, str_assignment_2 in f_content:
    int_assignments.append((convert_str_assignment(str_assignment_1),
                            convert_str_assignment(str_assignment_2)))


def find_complete_overlap(smaller_range, larger_range):
    """Helper function to find assignment pairs where one range
    fully contains the other

    Args:
        smaller_range (range): A range of the smaller range to check if it's
            fully contained within the larger range
        larger_range (range): A range of the larger range to check if it fully
            contains the smaller range

    Returns:
        Boolean: True if the smaller range is fully contained within the larger
            range, False if not
    """

    overlap_removed = set(larger_range) - set(smaller_range)
    length_no_overlap = len(larger_range) - len(smaller_range)

    return len(overlap_removed) == length_no_overlap


# Find all instances of fullly overlaping assignments
complete_overlaps = 0
for first_elf, second_elf in int_assignments:
    if len(first_elf) <= len(second_elf):
        complete_overlaps += find_complete_overlap(first_elf, second_elf)
    else:
        complete_overlaps += find_complete_overlap(second_elf, first_elf)

# Solution to part 1
print(f'There are {complete_overlaps} assignment pairs with full overlaps.')


def find_partial_overlap(range_1, range_2):
    """Check if two ranges share any overlap with each other

    Args:
        range_1 (range): First range to compare
        range_2 (range): Second range to compare

    Returns:
        Boolean: True if there is any overlap, False if not
    """

    return len(set(range_1) - set(range_2)) != len(range_1)


# Find all instances of partial overlaps
partial_overlaps = 0
for first_elf, second_elf in int_assignments:
    partial_overlaps += find_partial_overlap(first_elf, second_elf)

print(f'There are {partial_overlaps} assignment paris with partial overlaps.')
