# Вернуть максимальную сумму денег, которую грабитель может ограбить.
def rob(nums) -> int:
    def robber(nums, start, end): # создаем функцию, которая будет отвечать за грабителя
        sum1 = 0    # первый дом
        sum2 = 0    # второй дом
        for step in range(start, end):  # перебираем с начала до конца
            current_house = nums[step]  # сколько в текущем доме есть денег
            sum1, sum2 = sum2 + current_house, max(sum1, sum2) # пересчитываем
        return max(sum1, sum2)

    if not nums:    # условие
        return 0
    elif len(nums) == 1:    # если количество домов равно 1
        return nums[0]
    else:
        n = len(nums)   # кол-во домов равно длине домов
        return max(robber(nums, 1, n), robber(nums, 0, n - 1)) # максимальное из двух возможных вариантов


rob([1, 2, 3, 4, 5, 6, 7])