'''
Continuous Number Hollow Triangle.
Print a hollow triangle of height n where numbers are assigned continuously
(left-to-right, row-by-row). For middle rows we only print the first and last
numbers; the inner numbers are consumed to keep numbering continuous.

Example: 
Input: 
5
Output:
1
2 3
4   6
7     9
10 11 12 13 14
'''

def continuous_number_hollow_triangle(n):
    if n <= 0:
        return

    counter = 1
    print(counter)
    counter += 1

    for i in range(2, n):
        row_nums = [counter + k for k in range(i)]
        counter += i
        if i == 2:
            print(f"{row_nums[0]} {row_nums[1]}")
        else:
            inner_spaces = " " * (2 * i - 3)
            print(f"{row_nums[0]}{inner_spaces}{row_nums[-1]}")
    if n > 1:
        last_row = [str(counter + k) for k in range(n)]
        print(" ".join(last_row))


n = int(input().strip())
continuous_number_hollow_triangle(n)
