import os


# Set directories for folder and input file
main_folder = os.path.join(os.getcwd(), '02')
input_file = os.path.join(main_folder, 'input.txt')

# Read in input file as a list of tuples of (opponent_shape, my_shape)
with open(input_file, 'r', encoding='utf-8') as f:
    f_content = [tuple(line.rstrip().split(' ')) for line in f.readlines()]

# Create mapping dictionaries of scores based on strategy guide assumption
#     X = A = Rock
#     Y = B = Paper
#     Z = C = Scissors
shape_score = {'X': 1, 'Y': 2, 'Z': 3}
outcome_score = {('A', 'X'): 3,
                 ('A', 'Y'): 6,
                 ('A', 'Z'): 0,

                 ('B', 'X'): 0,
                 ('B', 'Y'): 3,
                 ('B', 'Z'): 6,

                 ('C', 'X'): 6,
                 ('C', 'Y'): 0,
                 ('C', 'Z'): 3}

# Calculate total score according to the strategy guide assumption
total_score = 0
for round in f_content:
    total_score += shape_score[round[1]]  # Add score for shape selection
    total_score += outcome_score[round]   # Add score for outcome

# Solution to part 1
print(f'The score according to the strategy guide would be {total_score}.')

# Update mapping dictionaries based on true interpretation
#     A = Rock
#     B = Paper
#     C = Scissors
#     -------------
#     X = Lose
#     Y = Draw
#     Z = Win
shape_score = {'A': 1, 'B': 2, 'C': 3}
outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
outcome_shape = {('A', 'X'): 'C',
                 ('A', 'Y'): 'A',
                 ('A', 'Z'): 'B',

                 ('B', 'X'): 'A',
                 ('B', 'Y'): 'B',
                 ('B', 'Z'): 'C',

                 ('C', 'X'): 'B',
                 ('C', 'Y'): 'C',
                 ('C', 'Z'): 'A'}

# Calculate true total score according to actual strategy guide interpretation
true_total_score = 0
for round in f_content:
    true_total_score += outcome_score[round[1]]   # Add score for outcome
    true_total_score += shape_score[outcome_shape[round]]  # Add shape score

# Solution to part 2
print(f'The true score would be {true_total_score}.')
