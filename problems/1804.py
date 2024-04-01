from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.data = defaultdict(int)
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertHelper(self, word, index, root):
        if index >= len(word):
            return

        char = word[index]
        
        if char not in root.children:
            root.children[char] = TrieNode()
        
        root.children[char].data[word] += 1
        self.insertHelper(word, index + 1, root.children[char])

    def insert(self, word):
        self.insertHelper(word, 0, self.root)
        
    def find(self, word, index, root):
        if index >= len(word):
            return root.data
        
        char = word[index]

        if char not in root.children:
            return {}
        
        return self.find(word, index + 1, root.children[char])

    def countWordsEqualTo(self, word):
        ret =  self.find(word, 0, self.root)
        return ret[word] if word in ret else 0
        
    def countWordsStartingWith(self, prefix):
        ret = self.find(prefix, 0, self.root)
        return sum(ret.values())
        
    def eraseHelper(self, word, index, root):
        if index >= len(word):
            return True
        
        char = word[index]

        if char not in root.children:
            return False
    
        should_delete = self.eraseHelper(word, index + 1, root.children[char])

        if not should_delete:
            return False
        
        root.children[char].data[word] -= 1
        
        if root.children[char].data[word] == 0:
            del root.children[char].data[word]
        
        if len(root.children[char].data) == 0:
            del root.children[char]

        return True

    def erase(self, word):
        self.eraseHelper(word, 0, self.root)
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)