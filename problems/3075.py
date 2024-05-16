class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ret = subtract = 0
        n = len(happiness)
        heapify(happiness)
        # O(N - K) + O(K) + O(log N) - time complexity
        # O(N) 
        # O(1) - space complexity (the input happiness is not added)
        for _ in range(n - k):
            heappop(happiness)

        subtract = k - 1

        for _ in range(k):
            min_num = heappop(happiness) - subtract
            subtract -= 1
            ret += max(min_num, 0)

        return ret