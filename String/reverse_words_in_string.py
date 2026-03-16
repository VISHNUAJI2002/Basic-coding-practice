"""
Problem Title: Reverse Words in a String

Description:
Given a string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in the output string should be separated by a single space.
Leading or trailing spaces should be removed.

Example 1:
Input:
s = "the sky is blue"
Output:
"blue is sky the"

Example 2:
Input:
s = "  hello world  "
Output:
"world hello"

Example 3:
Input:
s = "a good   example"
Output:
"example good a"
"""


def reverse_words(s):

    words = []
    word = ""

    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    # Reverse words using two-pointer technique
    left = 0
    right = len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)


# -----------------------------
# Using built in functions:
#
# def reverse_words_shortcut(s):
#     return " ".join(s.split()[::-1])
# ------------------------------


# User Input
s = input()
print(reverse_words(s))
