class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find all rotten fruit, put to queue
        # count all fresh fruit
        # iterate queue
        # check neighbors
        # if neighbour is fresh - rotten and update counter
        # count every iteration as day
        # return days when counter == 0
        # if counter != 0 return -1

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        minutes = 0
        counter = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    counter += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        if counter == 0:
            return 0

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                neighbours = [[0,-1], [0,1], [1,0], [-1,0]]
                for vr, vc in neighbours:
                    nr = r + vr
                    nc = c + vc
                    if(
                        nr < 0 or nc < 0
                        or nr == ROWS
                        or nc == COLS
                        or grid[nr][nc] == 2
                        or grid[nr][nc] == 0
                        ):
                        continue
                    grid[nr][nc] = 2
                    counter -= 1
                    queue.append((nr, nc))
            minutes += 1
            if counter == 0:
                return minutes
                
        return -1
