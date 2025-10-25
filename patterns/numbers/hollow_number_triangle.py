'''
Hollow Number Triangle Pattern.

Example:
Input:
5
Output:
1
2 2
3   3
4     4
5 5 5 5 5
'''

def hollow_number_triangle(n: int) -> None:
    if n <= 0:
        return
    print("1")
    for i in range(2, n):
        inner_spaces = " " * (2 * i - 3)
        print(f"{i}{inner_spaces}{i}")
    if n > 1:
        print(" ".join(str(n) for _ in range(n)))


n = int(input().strip())
hollow_number_triangle(n)
