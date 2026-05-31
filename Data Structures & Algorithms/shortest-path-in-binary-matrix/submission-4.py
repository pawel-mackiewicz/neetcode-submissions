class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # start = 0,0
        # end = -1,-1
        # can go in 8 directions
        # can go if 0
        # count length

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        queue.append((0,0))
        visited.add((0,0))
        length = 1

        if grid[0][0] == 1:
            return -1

        while queue:
            length += 1
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbours = [[0,-1],[0,1],[1,0],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
                for vr, vc in neighbours:
                    nr = r + vr
                    nc = c + vc

                    if (
                        nr < 0 or nc < 0
                        or nr == ROWS or nc == COLS
                        or grid[nr][nc] == 1
                        or (nr,nc) in visited
                        ):
                        continue
                    if nr == ROWS-1 and nc == COLS-1:
                        return length
                    queue.append((nr,nc))
                    visited.add((nr,nc))

        return -1