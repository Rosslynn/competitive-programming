class Solution:
    def maxSubarrayLength(self, nums, k):
        n = len(nums)
        ret = left = 0
        freq = {}

        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]] = 0
                
            freq[nums[i]] += 1

            while freq[nums[i]] > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                
                left += 1
            
            ret = max(ret, i - left + 1)
        
        return ret


'''
Input: nums = [1,2,3,1,2,3,1,2], k = 2
Output: 6
Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.
'''


