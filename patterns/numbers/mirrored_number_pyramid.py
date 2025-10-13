'''
Mirrored Number Pyramid.

Example:
Input:
5
Output:
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''


def mirrored_number_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print("  " * (n - i), end="")

        # Descending numbers
        for j in range(i, 0, -1):
            print(j, end=" ")

        # Ascending numbers
        for j in range(2, i + 1):
            print(j, end=" ")

        print()


n = int(input())
mirrored_number_pyramid(n)
