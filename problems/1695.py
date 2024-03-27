class Solution:
    def maximumUniqueSubarray(self, nums):
        n = len(nums)
        seen = set()
        ret = temp = left = 0

        for i in range(n):
            while nums[i] in seen:
                temp -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            temp += nums[i]
            seen.add(nums[i])
            ret = max(ret, temp)
        
        return ret

'''
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
'''