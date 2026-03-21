"""
Problem Title: Duplicate Transaction Detection

Description:
You are given a list of transactions. Each transaction contains:
Sender, Receiver, Amount, Timestamp

You need to detect duplicate transactions.

A transaction is considered duplicate if:
- Sender, Receiver, and Amount are the same
- But Timestamp is different

Example:
Input:
3
A B 100 1
A B 100 2
C D 200 5

Output:
A B 100 2

Explanation:
The first and second transactions have the same sender, receiver, and amount,
but different timestamps → duplicate.
"""


def detect_duplicates(transactions):

    hashmap = {}
    result = []

    for t in transactions:
        sender, receiver, amount, timestamp = t

        key = (sender, receiver, amount)

        if key in hashmap:
            if hashmap[key] != timestamp:
                result.append((sender, receiver, amount, timestamp))
        else:
            hashmap[key] = timestamp

    return result


# Input/Output Section
n = int(input("Enter number of transactions: "))

transactions = []

for _ in range(n):
    data = input("Enter transaction (sender receiver amount timestamp): ").split()
    transactions.append(data)

duplicates = detect_duplicates(transactions)

print("Duplicate transactions:")
for d in duplicates:
    print(*d)
