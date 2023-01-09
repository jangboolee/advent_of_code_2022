import os


# Set directories for folder and input file
main_folder = os.path.join(os.getcwd(), '05')
input_file = os.path.join(main_folder, 'input.txt')


def read_input(file_name):
    """Read in the input file and return the following in a tuple:
        - List of the raw stack diagram
        - List of the instructions
        - Integer of the maximum stack count

    Args:
        file_name (str): Full file path of input file

    Returns:
        tuple: Tuple of (raw stacks, instructions, and stack count)
    """

    # Read in input file as a list of lists
    with open(file_name, 'r', encoding='utf-8') as f:
        f_content = [line.rstrip() for line in f.readlines()]

    # Identify blank separator for the stack diagram and the instructions
    for i in range(len(f_content)):
        if f_content[i] == '':
            separator = i

    # Separate the raw stacks, instructions, and find the stack count
    stacks_raw = f_content[0:separator - 1]
    instructions = f_content[separator + 1:]
    stack_count = max([int(num) for num in f_content[separator-1].split()])

    return stacks_raw, instructions, stack_count


def parse_stacks(stacks_raw, stack_count):
    """Parse in list of raw stacks as a dictionary

    Args:
        stacks_raw (list): List of each line as an item
        stack_count (int): Count of stacks identified in the input file

    Returns:
        dict: Dictionary representation of the stacks
    """

    # Extract the stack letters only from each line
    parsed = [line[1::4] for line in stacks_raw]

    # Create an empty dictionary for each stack
    stacks_dict = {k: [] for k in range(1, stack_count+1)}

    # Generate a dictionary of lists representing the stack
    for col in range(1, stack_count + 1):
        for row in range(len(parsed)):
            try:
                stacks_dict[col].append(parsed[row][col - 1])
            except IndexError:
                stacks_dict[col].append(' ')

    return stacks_dict


def main():

    stacks, instructions, stack_count = read_input(input_file)
    parsed_stacks = parse_stacks(stacks, stack_count)


if __name__ == '__main__':

    main()
