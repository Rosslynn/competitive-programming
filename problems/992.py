class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        print(self.slidingWindowAtMost(nums, k), self.slidingWindowAtMost(nums, k - 1))
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    # Helper function to count the number of subarrays with at most k distinct elements.
    def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
        # To store the occurrences of each element.
        freq_map = defaultdict(int)
        left = 0
        total_count  = 0

        # Right pointer of the sliding window iterates through the array.
        for right in range(len(nums)):
            freq_map[nums[right]] += 1

            # If the number of distinct elements in the window exceeds k,
            # we shrink the window from the left until we have at most k distinct elements.
            while len(freq_map) > distinctK:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            # Update the total count by adding the length of the current subarray.
            total_count  += right - left + 1

        return total_count 

'''
k = 2
Basicamente cuentas todas las posibles combinaciones de maximo k caracteres distintos
[1,1,2,3,4]

Entonces contamos

1 -> 1 -> 2 -> 3 -> 4
1,1 -> 1,1,2 -> 12 -> 23 -> 34

total = 10

Viste que eso incluye repetidos, donde la freq de chars != k
Para arreglar esto basta con encontrar todos los subarrays que no lleguen a k, es decir a k-1 (la longitud de la ventana sea k - 1)
1 -> 1 -> 2 -> 3 -> 4 -> 1,1

total = 6

Esta cantidad se lo restas y ese es el resultado 

ret = 10 - 6 = 4

Basicamente encuentra todo, incluyendo lo bueno y lo malo, luego encuenta solo lo malo y lo resta
'''