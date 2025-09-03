'''
The Split Squad Challenge
In a land where numbers rule, a wise mathematician faced a peculiar problem. 
He had a list of warriors, each represented by a number. To prepare them for an 
upcoming tournament, he decided to divide them into two squads.
The first squad, made up of the first half of the warriors, was trained to work in
perfect increasing harmony — the weakest to the strongest.
The second squad, comprising the remaining warriors, was trained in reverse — the strongest 
leading the charge down to the weakest.
Your task is to help the mathematician organize his warriors just the way he wants.

Input Format:
The first line contains an integer n, the number of warriors.
The second line contains n space-separated integers — the power levels of each warrior.

Output Format:
Print the final lineup after the squads have been arranged as described.

example:
input:
6
190 34 89 7 9 90
output:
7 9 34 190 90 89
'''

def split_squad(n, warriors):
    warriors.sort()
    mid = n // 2
    first_half = warriors[:mid]            
    second_half = warriors[mid:][::-1]     
    return first_half + second_half


n = int(input())
warriors = list(map(int, input().split()))

result = split_squad(n, warriors)
print(*result)
