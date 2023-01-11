import os


def read_input(folder_name, file_name):
    """Read in the input file

    Args:
        folder_name (str): Folder name containing the input file
        file_name (str): File name of the input file

    Returns:
        str: String of the datastream
    """

    # Set directories for folder and input file
    main_folder = os.path.join(os.getcwd(), folder_name)
    input_file = os.path.join(main_folder, file_name)

    # Read in input file as a list of lists
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()

    return f_content


def find_first_marker(stream, char_length):
    """Find the first instance of a substring with no repeated characters
    based on the character length of the substring.

    - Start-of-packet: 4 distinct characters
    - Start-of-message: 14 distinct characters

    Args:
        stream (str): Datastream buffer
        char_length (int): Length of the substring to check uniqueness
    """

    for i in range(len(stream)-char_length):
        if len(set(stream[i:i+char_length])) == char_length:
            print(f'The first marker is found after {i + char_length}'
                  f' characters, with the marker being '
                  f'"{stream[i:i + char_length]}"')
            break


if __name__ == '__main__':

    datastream = read_input('06', 'input.txt')
    find_first_marker(datastream, 4)   # Find first start-of-packet marker
    find_first_marker(datastream, 14)  # Find first start-of-message marker
