class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        n = len(s)
        curr_chars = {}
        ans = left = 0

        for i in range(n):
            if s[i] not in curr_chars:
                curr_chars[s[i]] = 0

            curr_chars[s[i]] += 1
            
            while len(curr_chars) > 2:
                curr_chars[s[left]] -= 1

                if curr_chars[s[left]] == 0:
                    del curr_chars[s[left]]
                
                left += 1
            
            ans = max(i - left + 1, ans)
        
        return ans


