class TrieNode:
    def __init__(self):
        self.words_starting_here = 0
        self.words_ending_here = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            
            curr_node = curr_node.children[char]
            curr_node.words_starting_here += 1
        
        curr_node.words_ending_here += 1

    def find(self, word):
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return {}
            
            curr_node = curr_node.children[char]
        
        return curr_node

    def countWordsEqualTo(self, word: str) -> int:
        ret = self.find(word)

        if not ret:
            return 0
        
        return ret.words_ending_here  

    def countWordsStartingWith(self, prefix: str) -> int:
        ret = self.find(prefix)

        if not ret:
            return 0
        
        return ret.words_starting_here
        
    def erase(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            curr_node = curr_node.children[char]
            curr_node.words_starting_here -= 1
        
        curr_node.words_ending_here -= 1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)