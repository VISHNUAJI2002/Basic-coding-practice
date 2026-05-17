"""
Problem Title: Excel Sheet Column Number
Description:
Given a string columnTitle that represents the column title
as appears in an Excel sheet, return its corresponding column number.
Excel columns follow this pattern:
A  -> 1
B  -> 2
...
Z  -> 26
AA -> 27
AB -> 28

Example 1:
Input:
columnTitle = "A"

Output:
1

Example 2:
Input:
columnTitle = "AB"

Output:
28

Explanation:
A = 1
B = 2
Result:
(1 × 26) + 2 = 28

Example 3:
Input:
columnTitle = "ZY"

Output:
701

Explanation:
Z = 26
Y = 25
Result:
(26 × 26) + 25 = 701
"""

def excel_column_number(column_title):
    result = 0
    for char in column_title:
        value = ord(char) - ord('A') + 1
        result = result * 26 + value
    return result


# Input/Output Section
column_title = input().strip().upper()
print(excel_column_number(column_title))
