"""
You are given an integer array cost where cost[i] is the cost
 of ith step on a staircase. Once you pay the cost, you can 
 either climb one or two steps.

You can either start from the step with index 0, or the step
with index 1.

Return the minimum cost to reach the top of the floor.

Week of June 1st - 7th, 2021
"""

def minCostStairs(cost):
    m = len(cost)
    lookup = [0 for x in range(m + 1)]

    for i in range(2, m + 1):
        lookup[i] = min(lookup[i - 1] + cost[i - 1], lookup[i - 2] + cost[i - 2])

    return lookup[m]

# Test Inputs
costs1 = [10, 15, 20]
costs2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

# ACCEPTED
