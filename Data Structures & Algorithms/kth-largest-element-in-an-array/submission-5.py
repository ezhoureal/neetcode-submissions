import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1
        l, r = 0, len(nums) - 1
        while l <= r:
            p = random.randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            store = l
            for i in range(l, r):
                if nums[i] > nums[r]:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[store], nums[r] = nums[r], nums[store]
            if store == k:
                return nums[store]
            elif store < k:
                l = store + 1
            else:
                r = store - 1
        return 0