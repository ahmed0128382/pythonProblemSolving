from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(len(nums)):
            if nums[i] in n:
                return [n[nums[i]],i]
            else:
                n[target-nums[i]]=i
            

# Example usage:
nums = [2, 12, 11, 7]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]
