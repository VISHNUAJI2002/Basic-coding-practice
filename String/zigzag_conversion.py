"""
Zigzag Conversion.
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""

def convert(s,numRows):
    if numRows==1 or numRows>=len(s):
        return s
    rows=[""]*numRows               # List of strings — one for each row
    current_row=0      
    direction=1                       # +1 (down), -1 (up)

    for i in s:
        rows[current_row]+=i
      
        if current_row==0:            # Change direction when you hit top or bottom row
            direction=1
        elif current_row==numRows-1:
            direction=-1
        current_row+=direction
      
    return "".join(rows)


s=input()
numRows=int(input())
print(convert(s,numRows))
