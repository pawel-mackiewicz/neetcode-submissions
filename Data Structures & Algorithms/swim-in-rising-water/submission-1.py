class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t = 0
        ROWS, COLS = len(grid), len(grid[0])

        reqT = grid[0][0]
        minHeap = [(reqT, (0,0))]
        visited = set()

        while minHeap:
            reqT,(i,j) = heapq.heappop(minHeap)

            t = max(t, reqT)

            if i == ROWS-1 and j == COLS-1:
                return t

            if i - 1 >= 0 and (i-1,j) not in visited:
                heapq.heappush(minHeap, (grid[i-1][j],(i-1,j)))
                visited.add((i-1,j))
            if i + 1 < ROWS and (i+1,j) not in visited:
                heapq.heappush(minHeap, (grid[i+1][j],(i+1,j)))
                visited.add((i+1,j))
            if j - 1 >= 0 and (i, j-1) not in visited:
                heapq.heappush(minHeap, (grid[i][j-1],(i,j-1)))
                visited.add((i,j-1))
            if j + 1 < COLS and (i, j+1) not in visited:
                heapq.heappush(minHeap, (grid[i][j+1],(i,j+1)))
                visited.add((i,j+1))
        
        return -1