# class Solution:
#   def applyOperations(self, nums: list[int]) -> list[int]:
#     ans = [0] * len(nums)

#     for i in range(len(nums) - 1):
#       if nums[i] == nums[i + 1]:
#         nums[i] *= 2
#         nums[i + 1] = 0

#     i = 0
#     for num in nums:
#       if num > 0:
#         ans[i] = num
#         i += 1

#     return ans


class Solution:
  def applyOperations(self, nums: list[int]) -> list[int]:
    j = 0
    for i in range(len(nums)):
      if i + 1 < len(nums) and nums[i] == nums[i + 1]:
        nums[i] *= 2
        nums[i + 1] = 0
      if nums[i] > 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return nums