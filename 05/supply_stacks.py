import os
import re


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
    stack_count = max([int(num) for num in f_content[separator - 1].split()])

    return stacks_raw, instructions, stack_count


def parse_stacks(stacks_raw, stack_count):
    """Parse in list of raw stacks as a dictionary

    Args:
        stacks_raw (list): List of each stack of crates
        stack_count (int): Count of stacks identified in the input file

    Returns:
        dict: Dictionary representation of the stacks as a list for each stack
    """

    # Extract the stack letters only from each line
    parsed = [line[1::4] for line in stacks_raw]

    # Initialize an empty dictionary for each stack
    stacks_dict = {k: [] for k in range(1, stack_count + 1)}

    # Update the dictionary of lists representing the stack
    for col in range(1, stack_count + 1):
        for row in range(len(parsed)):
            try:
                if parsed[row][col - 1] != ' ':
                    stacks_dict[col].append(parsed[row][col - 1])
            except IndexError:
                pass

    return stacks_dict


def operate_crane_mover_9000(parsed_stacks, instruction):
    """Move crate one by one, reversing order when moving, according to single
    operation instruction

    Args:
        parsed_stacks (dict): Dictionary representation of crate stacks
        instruction (str): Single crate operation instruction
    """

    # Parse key elements from the crane operation instructions
    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)", re.IGNORECASE)
    matches = re.match(pattern, instruction)

    # Extract key elements from parsed result
    if matches:
        count, origin, destination = [int(match) for match in matches.groups()]

    # Move specified count of crates
    while count > 0:

        # Identify the crate to be moved
        move_crate = parsed_stacks[origin][0]

        # Add the crate to the destination and remove it from the origin
        parsed_stacks[destination].insert(0, move_crate)
        parsed_stacks[origin].pop(0)

        count -= 1


def operate_crane_mover_9001(parsed_stacks, instruction):
    """Move crates at once, retaining order when moving, according to single
    operation instruction

    Args:
        parsed_stacks (dict): Dictionary representation of crate stacks
        instruction (str): Single crate operation instruction
    """

    # Parse key elements from the crane operation instructions
    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)", re.IGNORECASE)
    matches = re.match(pattern, instruction)

    # Extract key elements from parsed result
    if matches:
        count, origin, destination = [int(match) for match in matches.groups()]

    # Identify the crates to be moved
    move_crates = parsed_stacks[origin][0:count]

    # Add the crates to the destination and remove them from the origin
    for move_crate in move_crates[::-1]:
        parsed_stacks[destination].insert(0, move_crate)
        parsed_stacks[origin].pop(0)


def main():

    raw_stacks, instructions, stack_count = read_input(input_file)
    parsed_stacks = parse_stacks(raw_stacks, stack_count)
    for instruction in instructions:
        operate_crane_mover_9000(parsed_stacks, instruction)

    # Solution for part 1
    print('The top crates after crane mover 9000 are: ')
    print(''.join([stack[0] for stack in parsed_stacks.values()]))

    parsed_stacks = parse_stacks(raw_stacks, stack_count)
    for instruction in instructions:
        operate_crane_mover_9001(parsed_stacks, instruction)

    # Solution for part 2
    print('The top crates after crane mover 9001 are: ')
    print(''.join([stack[0] for stack in parsed_stacks.values()]))


if __name__ == '__main__':

    main()
