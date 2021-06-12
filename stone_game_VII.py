"""
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, 
they can remove either the leftmost stone or the rightmost 
stone from the row and receive points equal to the sum of the 
remaining stones' values in the row. The winner is the one with 
the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always 
loses), so he decided to minimize the score's difference. Alice's goal 
is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the 
value of the ith stone from the left, return the difference in Alice 
and Bob's score if they both play optimally.
"""

def stoneGame(stones):
    m = len(stones)

    dpCurr = [0] * m
    dpLast = [0] * m

    for i in range(m - 2, -1, -1):
        total = stones[i]
        dpLast, dpCurr = dpCurr, dpLast
        for j in range(i + 1, m):
            total += stones[j]
            dpCurr[j] = max(total - stones[i] - dpLast[j], total - stones[j] - dpCurr[j-1])

    return dpCurr[-1]

# Test Inputs
stones1 = [5, 3, 1, 4, 2]
# Returns 6
stones2 = [7, 90, 5, 1, 100, 10, 10, 2]
# Returns 122
