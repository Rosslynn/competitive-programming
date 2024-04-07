class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviations = {}

        for word in dictionary:
            abbr = self.getAbbreviation(word)

            if abbr not in self.abbreviations:
                self.abbreviations[abbr] = set()
            
            self.abbreviations[abbr].add(word)
            
    
    def getAbbreviation(self, word):
        size = len(word) - 2

        if size <= 0:
            return word
        
        return ''.join([word[0], str(size), word[-1]])
        

    def isUnique(self, word: str) -> bool:
        abbr = self.getAbbreviation(word)
        return (abbr not in self.abbreviations) or (word in self.abbreviations[abbr] and len(self.abbreviations[abbr]) == 1)
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

'''
Input
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
Output
[null, false, true, false, true, true]

'''