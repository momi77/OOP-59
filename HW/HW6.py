# Пример 1:
#
# Ввод: nums = [2,7,11,15], цель = 9
#  Вывод: [0,1]
#  Объяснение: Поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].
#
# Пример 2:
#
# Ввод: числа = [3,2,4], цель = 6
#  Вывод: [1,2]
#
# Пример 3:
#
# Ввод: числа = [3,3], цель = 6
#  Вывод: [0,1]



def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print(two_sum([2,7,11,15], 9))  # [0, 1]
print(two_sum([3,2,4], 6))      # [1, 2]
print(two_sum([3,3], 6)) #[0,1]



