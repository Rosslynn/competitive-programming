class TrieNode:
    def __init__(self):
        self.data = None
        self.children = [None] * 26

class Trie:
    def __init__(self, board):
        self.root = TrieNode()
        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    def insert(self, word):
        root = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if root.children[idx] is None:
                root.children[idx] = TrieNode()
            
            root = root.children[idx]
        
        root.data = word

    def solve(self):
        ret = set()

        def backtrack(x, y, root, seen):
            if root.data:
                ret.add(root.data)
            
            for dx, dy in self.directions:
                new_row = x + dx
                new_col = y + dy

                if new_row < 0 or new_col < 0 or new_row >= self.rows or new_col >= self.cols:
                    continue
                
                new_idx = ord(self.board[new_row][new_col]) - ord('a')
                new_root = root.children[new_idx]
                
                if ((new_row, new_col) not in seen) and (new_root is not None):
                    seen.add((new_row, new_col))
                    backtrack(new_row, new_col, new_root, seen)
                    seen.remove((new_row, new_col))
        
        for row in range(self.rows):
            for col in range(self.cols):
                root_idx = ord(self.board[row][col]) - ord('a')

                if self.root.children[root_idx] is not None:
                    backtrack(row, col, self.root.children[root_idx], {(row, col)})

        return ret

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(board)

        for word in words:
            trie.insert(word)
        
        return trie.solve()


