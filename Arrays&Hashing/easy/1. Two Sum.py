from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Sample input
nums = [2, 7, 11, 15]
target = 9

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum function with the provided input
result = solution.twoSum(nums, target)

# Print the result
print(result)