"""
Problem Title: String Compression
Description:
Given a string s, compress it using the following rules:
- Consecutive repeating characters are replaced by the character
  followed by the count of repetitions.
- If a character appears only once, it is kept as is.
Return the compressed string.

Example:
Input:
aabcccaa
Output:
a2bc3a2

Explanation:
- 'a' appears 2 times → a2
- 'b' appears once → b
- 'c' appears 3 times → c3
- 'a' appears 2 times → a2
"""


def string_compression(s):
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1

    # handle last character group
    result.append(s[-1])
    if count > 1:
        result.append(str(count))

    return "".join(result)


s = input().strip()
print(string_compression(s))
