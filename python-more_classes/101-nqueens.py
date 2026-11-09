#!/usr/bin/python3
"""Solve the N queens puzzle and print every solution."""
import sys


def solve_nqueens(n):
    """Print every way to place n queens so none attack each other.

    Args:
        n (int): Size of the chessboard.
    """
    queens = []

    def is_safe(row, col):
        """Return True if a queen at row, col attacks none already placed.

        Args:
            row (int): Row index of the candidate square.
            col (int): Column index of the candidate square.

        Returns:
            bool: True when the square is safe.
        """
        for placed_row, placed_col in queens:
            same_col = placed_col == col
            same_diag = abs(placed_row - row) == abs(placed_col - col)
            if same_col or same_diag:
                return False
        return True

    def place(row):
        """Place a queen on each remaining row and print complete boards.

        Args:
            row (int): Row that still needs a queen.
        """
        if row == n:
            print(queens)
            return
        for col in range(n):
            if is_safe(row, col):
                queens.append([row, col])
                place(row + 1)
                queens.pop()

    place(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(size)
