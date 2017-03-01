import random
# Define numbers to choose from
numbers = ('0','1','2','3','4','5','6','7','8','9')
# Define empty list
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

print_grid(grid)
