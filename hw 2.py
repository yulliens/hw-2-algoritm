# Мы получаем целое число n, которое отвечает за размерность массива. Задача решалась по формулам из условий.
# Сложность O(n)
def getMaximumGenerated(n: int) -> int:
    nums = [] # массив
    for i in range(n + 1):    # проходимся по списку
        if 0 <= i <= 1:     # условие задачи
            nums.append(i)    # добавляем массив
        elif i % 2 == 0:    # условие задачи
            nums.append(nums[i // 2])    # если четное
        else:
            nums.append(nums[i // 2] + nums[i // 2 + 1])   # если нечетное
    return max(nums)

getMaximumGenerated(3)