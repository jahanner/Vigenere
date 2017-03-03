import random
# Define numbers to choose from
numbers = ('0','1','2','3','4','5','6','7','8','9')
# Define empty list
area = 9
grid = []
# Make rows with len 3
for row in range(3):
    # Append a blank list in each row
    grid.append([])
    for column in range(3):
        # Assign a random number to each spot
        grid[row].append(random.choice(numbers))

# Make function so it will print like a grid
def print_grid(grid):
    for row in grid:
        print' '.join(row)
# Maybe make a list with all possible grid positions as variables and iterate through it...
print_grid(grid)
row1 = grid[0]
row2 = grid[1]
row3 = grid[2]
row1_horz = False
print(row1)
while row1_horz == False:
    if row1[0] + row1[1] or row1[0] + row1[1] + row1[2] == area:
        row1_horz = True
print(row1_horz)
# for col in row1:
#     col += col
# print(col)
