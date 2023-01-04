import os


# Set directories for folder and input file
main_folder = os.path.join(os.getcwd(), '01')
input_file = os.path.join(main_folder, 'input.txt')

# Read in input file as a list
with open(input_file, 'r', encoding='utf-8') as f:
    f_content = [line.rstrip() for line in f.readlines()]

# Find count of elves and create a dictionary with 0 as default calorie per elf
elf_count = f_content.count('') + 1
calories = dict.fromkeys(range(elf_count), 0)

# Sum up total calories carried per elf
i = 0
for item in f_content:
    if item != '':
        calories[i] += int(item)
    else:
        i += 1

# Find the maximum calorie and the elf carrying that load
max_calorie = max(calories.values())
max_elf = max(calories, key=calories.get)

# Solution to part 1
print(f'Elf #{max_elf} is carrying the maximum calories of {max_calorie}.')

# Sort dictionary based on carried calories
sorted_calories = sorted(calories.items(), key=lambda x: x[1], reverse=True)

# Get the total calories from the top three elves
top_3_total = 0
for elf, calorie in sorted_calories[:3]:
    top_3_total += calorie

# Solution to part 2
print(f'The top three elves are carrying a total of {top_3_total} calories.')
