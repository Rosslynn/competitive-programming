class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def backtrack(row, col, index):
            if index >= len(word):
                return True
            
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                # handle invalid cells
                if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols:
                    continue
                # only consider the chars at the correct position
                if board[new_row][new_col] != word[index]:
                    continue
                # save the char in case the next level does not work and update it to a random char
                # remember the condition above
                char = board[row][col]
                board[row][col] = '.'
                
                if backtrack(new_row, new_col, index + 1):
                    return True
                # if the path is not correct then just do the bactrack
                board[row][col] = char
            
            return False

        for row in range(rows):
            for col in range(cols):
                if word[0] == board[row][col] and backtrack(row, col, 1):
                    return True
        
        return False
        
