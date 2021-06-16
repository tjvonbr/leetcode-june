import heapq

def minRefuelStops(target, startFuel, stops):
    m = len(stops)
    heap = []
    answer = 0

    for i in range(m + 1):
        if i == m:
            dist = target 
        else:
            dist = stops[i][0]

        while startFuel < dist:
            if len(heap) == 0: 
                return -1

            startFuel -= heapq.heappop(heap)
            answer += 1
        if i < m: 
            heapq.heappush(heap, -stops[i][1])

    return answer
