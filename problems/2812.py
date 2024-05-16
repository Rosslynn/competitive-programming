class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ret = 0

        if grid[0][0] or grid[n - 1][n - 1]:
            return ret

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        distances = [[inf] * n for _ in range(n)]
        dq = deque()
        
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    root = (row, col)
                    dq.append((root, row, col))
        
        while dq:
            root, x, y = dq.popleft()
            a, b = root

            for dx, dy in directions:
                row = x + dx
                col = y + dy

                if row < 0 or col < 0 or row >= n or col >= n or distances[row][col] != inf:
                    continue
                
                dst = abs(a - row) + abs(b - col)
                distances[row][col] = dst
                dq.append((root, row, col))
        
        max_heap = [(-distances[0][0], 0, 0)]
        seen = {(0, 0)}

        while max_heap:
            dst, x, y = heappop(max_heap)

            if x == n - 1 and y == n -1:
                return -dst
            
            for dx, dy in directions:
                row = x + dx
                col = y + dy

                if row < 0 or col < 0 or row >= n or col >= n or grid[row][col]:
                    continue
                
                if (row, col) not in seen:
                    seen.add((row, col))
                    curr_dst = min(-dst, distances[row][col])
                    node = (-curr_dst, row, col)
                    heappush(max_heap, node)

        return 0
     
        

'''
[
    [2, 1, 0], 
    [3, 2, 1], 
    [4, 3, 2]
]

'''

'''
[
    [3, 2, 1, 0], 
    [2, 3, 2, 1], 
    [1, 2, 3, 2],
    [0, 1, 2, 3]
]
'''