#!/usr/bin/python3
"""Module that calculates the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): 0 = water, 1 = land

    Returns:
        int: perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Check above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
