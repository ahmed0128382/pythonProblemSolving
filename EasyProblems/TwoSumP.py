from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None  # In case no solution is found

# Example usage:
nums = [2, 12, 11, 7]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]
