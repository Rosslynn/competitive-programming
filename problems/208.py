class Trie:
    def __init__(self):
        self.root = [None] * 27

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if node[idx] is None:
                node[idx] = [None] * 27
            
            node = node[idx]
        
        node[-1] = 'XD'

    def find(self, word) -> bool:
        node = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if node[idx] is None:
                return []
            
            node = node[idx]
        
        return node

    def search(self, word: str) -> bool:
        ret = self.find(word)
        return ret[-1] if ret else ret

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)