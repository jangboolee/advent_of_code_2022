import os
from string import ascii_letters


# Set directories for folder and input file
main_folder = os.path.join(os.getcwd(), '03')
input_file = os.path.join(main_folder, 'input.txt')

# Read in input file as a list
with open(input_file, 'r', encoding='utf-8') as f:
    f_content = [line.rstrip() for line in f.readlines()]

# Create priority mapping dictionary
priority = dict(zip([letter for letter in ascii_letters],
                    range(1, 53)))

# Split each rucksack into two compartments
split_rucksacks = [(i[:len(i)//2], i[len(i)//2:]) for i in f_content]

# Find shared items per split rucksack
shared_split_items = [list(set(j[0]) & set(j[1]))[0] for j in split_rucksacks]

# Calculate sum of priorities for shared items
priority_shared_sum = 0
for shared_split_item in shared_split_items:
    priority_shared_sum += priority[shared_split_item]

# Solution to part 1
print(f'The sum of the priorities of the shared items is '
      f'{priority_shared_sum}.')

# Group rucksacks into groups of three
grouped_rucksacks = list(zip(*[iter(f_content)]*3))

# Find shared items per grouped rucksacks
shared_grouped_items = [list(set(k[0])
                             & set(k[1])
                             & set(k[2]))[0] for k in grouped_rucksacks]

# Calculate sum of priorities for grouped items
priority_grouped_sum = 0
for shared_grouped_item in shared_grouped_items:
    priority_grouped_sum += priority[shared_grouped_item]

# Solution to part 2
print(f'The sum of the priorities of the grouped rucksacks is '
      f'{priority_grouped_sum}.')
