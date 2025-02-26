# class Solution:
#   def maxAbsoluteSum(self, nums):
#     ans = -math.inf
#     maxSum = 0
#     minSum = 0

#     for num in nums:
#       maxSum = max(num, maxSum + num)
#       minSum = min(num, minSum + num)
#       ans = max(ans, maxSum, -minSum)

#     return ans


class Solution:
  def maxAbsoluteSum(self, nums):
    summ = 0
    maxPrefix = 0
    minPrefix = 0

    for num in nums:
      summ += num
      maxPrefix = max(maxPrefix, summ)
      minPrefix = min(minPrefix, summ)

    return maxPrefix - minPrefix