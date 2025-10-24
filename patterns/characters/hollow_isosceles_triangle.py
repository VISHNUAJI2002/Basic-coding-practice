'''
Hollow isosceles triangle.

Example:
Input:
5
Output:
    *
   * *
  *   *
 *     *
*********
'''


def print_hollow_triangle(n):
    if n <= 0:
        return
    for i in range(n):
        print(" " * (n - 1 - i), end="")
        if i == 0:
            print("*")
        elif i == n - 1:
            print("*" * (2 * n - 1))
        else:
            print("*", end="")
            print(" " * (2 * i - 1), end="")
            print("*")


height=int(input())
print_hollow_triangle(height)
