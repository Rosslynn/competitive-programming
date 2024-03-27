class TrieNode:
    def __init__(self):
        self.data = []
        self.children = {}

class Trie:
    def __init__(self, root):
        self.root = root
    
    def insert(self, i, word, root):
        if i >= len(word):
            return

        char = word[i]

        if char not in root.children:
            root.children[char] = TrieNode()
        
        curr = root.children[char]
        curr.data.append(word)
        
        return self.insert(i + 1, word, curr)
    
    def find(self, i, word, root):
        if i >= len(word):
            return root.data

        char = word[i]

        if char not in root.children:
            return []
        
        return self.find(i + 1, word, root.children[char])
    
    def get_suggestions(self, word, max_suggestions):
        ret = self.find(0, word, self.root)
        return ret[:max_suggestions]

class Solution:
    def suggestedProducts(self, products, searchWord):
        # Build output structure
        n = len(searchWord)
        suggested_products = [[] for _ in range(n)]

        # Order products
        products.sort()

        # Build trie
        trie = Trie(TrieNode())

        for product in products:
            trie.insert(0, product, trie.root)
        
        # Simulation of user typing
        # This can be improved because I already have all the word that the user will type but I want to simulate it
        for i in range(n):
            curr_string = searchWord[: i + 1]
            suggested_products[i] = trie.get_suggestions(curr_string, 3)

        return suggested_products
            
        

solution = Solution()
ret = solution.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], 'mouse')
print(ret)