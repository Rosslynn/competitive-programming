class Solution:
    def is_subsequence(self, word_a, word_b):
        i = j = 0

        while i < len(word_a) and j < len(word_b):
            if word_a[i] == word_b[j]:
                i += 1

            j += 1

        return i == len(word_a)
    
    def is_valid_chain(self, word_a, word_b):
        # b is greater because the words are sorted
        return len(word_b) - len(word_a) == 1 and self.is_subsequence(word_a, word_b)

    def longestStrChain(self, words):
        ret = 0
        memo = {}
        words.sort(key = len)
        
        def dp(i):
            longest_chain = 1
            
            if i in memo:
                return memo[i]

            for j in range(i - 1, -1, -1):
                if self.is_valid_chain(words[j], words[i]):
                    longest_chain = max(longest_chain, dp(j) + 1)
            
            memo[i] = longest_chain

            return memo[i]

        for i in range(len(words)):
            ret = max(ret, dp(i))

        return ret

'''
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
'''