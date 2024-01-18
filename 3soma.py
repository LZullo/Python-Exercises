#Dada uma matriz inteira nums, retorne todos os trigêmeos [nums[i], nums[j], nums[k]]tais que i != j, i != k, e j != k, e nums[i] + nums[j] + nums[k] == 0.
#Observe que o conjunto de soluções não deve conter trigêmeos duplicados.

def threeSum(nums):
  nums.sort()
  triplets = set()
  for i in range(len(nums) - 2):
      firstNum = nums[i]
      j = i + 1
      k = len(nums) - 1
      while j < k:
          secondNum  = nums[j]
          thirdNum = nums[k]

          potentialSum = firstNum + secondNum + thirdNum
          if potentialSum > 0:
              k -= 1
          elif potentialSum < 0:
              j += 1
          else:
              triplets.add((firstNum , secondNum ,thirdNum))
              j += 1
              k -= 1
  return triplets

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))