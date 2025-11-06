'''
Maximum Consecutive Hidden Commits.
Given a list of unique commit IDs in ascending order, determine the maximum number of 
consecutive commits that can be hidden such that the hidden range remains uniquely deducible.
A "hidden" range is deducible if the commit sequence follows a clear arithmetic progression, 
meaning the missing commits can be inferred unambiguously.

Example 1:
Input:
commits = [1, 2, 3, 4, 5]
Output:
4
Explanation:
All commits form a perfect arithmetic progression, so you can hide all but one.

Example 2:
Input:
commits = [2, 3, 4, 7, 8]
Output:
1
Explanation:
The longest arithmetic sequence is [2, 3, 4] or [7, 8].
You must leave both ends visible, so you can hide only 1 commit.
'''

def get_max_consecutive_hidden(commits):
    n = len(commits)
    if n < 2:
        return 0
    max_run = current_run = 1
    prev_val = commits[0] - 0  

    # Identify the longest contiguous arithmetic progression
    for k in range(1, n):
        val = commits[k] - k
        if val == prev_val:
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 1
            prev_val = val

    # Account for the last run
    max_run = max(max_run, current_run)

    # If the entire sequence is arithmetic, all but one commit can be hidden
    if max_run == n:
        return max_run - 1
    
    # Otherwise, leave both ends visible → hide at most max_run - 2
    return max(0, max_run - 2)


commits = list(map(int, input().split()))
print(get_max_consecutive_hidden(commits))
