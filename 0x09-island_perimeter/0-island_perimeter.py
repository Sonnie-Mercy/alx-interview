#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list): A list of lists where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Each land cell contributes 4 sides to the perimeter
                perimeter += 4
                
                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Remove 2 sides for the shared edge

                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Remove 2 sides for the shared edge

    return perimeter
