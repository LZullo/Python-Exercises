#Dada uma matriz inteira nums, retorne todos os trigêmeos [nums[i], nums[j], nums[k]]tais que i != j, i != k, e j != k, e nums[i] + nums[j] + nums[k] == 0.
#Observe que o conjunto de soluções não deve conter trigêmeos duplicados.

def three_sum(nums):
    nums.sort()
    triplets = set()

    for i in range(len(nums) - 2):
        first_num = nums[i]
        j, k = i + 1, len(nums) - 1

        while j < k:
            second_num, third_num = nums[j], nums[k]
            potential_sum = first_num + second_num + third_num

            if potential_sum > 0:
                k -= 1
            elif potential_sum < 0:
                j += 1
            else:
                triplets.add((first_num, second_num, third_num))
                j += 1
                k -= 1

    return list(triplets)

nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(result)

