class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ret = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def backtrack(i, j, gold):
            nonlocal ret

            ret = max(gold, ret)

            for dx, dy in directions:
                r = i + dx
                c = j + dy

                # invalid cell position
                if r < 0 or c < 0 or r >= rows or c >= cols:
                    continue

                # invalid values
                if grid[r][c] == 0:
                    continue
                
                temp_val = grid[r][c]
                grid[r][c] = 0
                backtrack(r, c, gold + temp_val)
                grid[r][c] = temp_val
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    temp = grid[row][col]
                    grid[row][col] = 0
                    backtrack(row, col, temp)
                    grid[row][col] = temp
        
        return ret

                

                
