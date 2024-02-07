# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(nums, k):
    n = len(nums)
    k %= n  # Trata casos em que k é maior que o comprimento da lista

    # Fatiamento para realizar a rotação
    rotated_nums = nums[-k:] + nums[:-k]

    return rotated_nums

nums = [1, 2]
k = 3
print(rotate(nums, k))
