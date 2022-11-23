# Решаем по условиям задачи
def uniquePathsWithObstacles(obstacleGrid) -> int:
    if not obstacleGrid:    # условие
        return
    m, n = len(obstacleGrid), len(obstacleGrid[0])  # количество строк и столбцов

    paths = [[0] * n for row in range(n)]   # создаем новую матрицу
    paths[0][0] = 1     # поставим робота
    for row in range(m):    # проходимся по строкам
        for col in range(n):    # проходимся по столбцам
            if obstacleGrid[row][col] or (row == 0 and col == 0):   # условие
                continue    # продолжаем
            paths[row][col] = (paths[row-1][col] if row else 0) + (paths[row][col-1] if col else 0)
    return paths[m-1][n-1]

uniquePathsWithObstacles([[0,1],[0,0]])