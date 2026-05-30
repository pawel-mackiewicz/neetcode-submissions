class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))
        ln = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return ln

                vectors = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
                for vr, vc in vectors:
                    nr = r + vr
                    nc = c + vc
        
                    if (
                        nr < 0 or nc < 0
                        or nr == ROWS or nc == COLS
                        or grid[nr][nc] == 1
                        or (nr, nc) in visit
                        ):
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            ln += 1
        return -1
