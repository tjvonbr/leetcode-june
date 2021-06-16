def maximumUnits(boxTypes, truckSize):
    m = len(boxTypes)

    boxTypes.sort(key=lambda x: x[1], reverse=True)

    dp = [[0 for _ in range(len(boxTypes) + 1)] for _ in range(truckSize + 1)]
    
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = max(boxTypes[i - 1][1] + dp[i - 1][j], dp[i - 1][j])

    return dp[m][truckSize]

    

    

# Test Inputs
boxTypes = [[3, 1], [1, 3], [2, 2]]
truckSize = 4

print(maximumUnits(boxTypes, truckSize))