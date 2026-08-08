class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dirx, diry in directions:
                    nr, nc = dirx + row, diry + col
                    if nr >= ROWS or nr < 0 or nc >= COLS or nc < 0 or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        return islands
        