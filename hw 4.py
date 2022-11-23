# Решаем по условиям задачи. Понять как долго снижалась акция.
def getDescentPeriods(prices) -> int:
    smooth = len(prices) # создаем переменную с массивом
    smooth1, smooth2 = 0, 0     # счётчик
    for i in range(1, len(prices) + 1):     # проходимся по элементам
        if i != len(prices) and prices[i - 1] - prices[i] == 1:    # условие
            smooth1, smooth2 = smooth1 + 1, smooth2 + smooth1
            continue    # продолжаем
        smooth += smooth1 + smooth2
        smooth1, smooth2 = 0, 0
    return smooth
getDescentPeriods([8, 6, 7, 7])