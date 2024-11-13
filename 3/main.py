import numpy as np
import matplotlib.pyplot as plt
import random

def initialize_grid(n, blue_ratio=0.45, red_ratio=0.45, empty_ratio=0.1): #Инициализация графа
    cells = ["blue"] * int(n * n * blue_ratio) + ["red"] * int(n * n * red_ratio) + ["empty"] * int(n * n * empty_ratio) # Появление полей
    random.shuffle(cells) # Рандомятся по квадрату
    grid = np.array(cells).reshape(n, n)
    return grid

def is_happy(grid, x, y): # Функция, которая определяет "счастливую клетку"
    cell = grid[x, y]
    if cell == "empty":
        return True

    same_color_neighbors = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] == cell:
                same_color_neighbors += 1

    return same_color_neighbors >= 2

def find_unhappy_cell(grid): # Функция для "несчастливой клетки"
    n = grid.shape[0]
    unhappy_cells = [(x, y) for x in range(n) for y in range(n) if not is_happy(grid, x, y) and grid[x, y] != "empty"]
    return random.choice(unhappy_cells) if unhappy_cells else None

def find_empty_cell(grid):  #Нахождение пустой клетки
    empty_cells = [(x, y) for x in range(grid.shape[0]) for y in range(grid.shape[1]) if grid[x, y] == "empty"]
    return random.choice(empty_cells) if empty_cells else None

def simulate(grid, steps): # Перемещение в пустые клетки
    for step in range(steps):
        unhappy_cell = find_unhappy_cell(grid)
        if unhappy_cell is None:
            break

        empty_cell = find_empty_cell(grid)
        if empty_cell:
            grid[empty_cell], grid[unhappy_cell] = grid[unhappy_cell], "empty"

        if step % 10 == 0 or step == steps - 1:
            plot_grid(grid, title=f"Step {step}")

def plot_grid(grid, title=""): # Визуализация
    color_map = {"blue": 1, "red": 2, "empty": 0}
    mapped_grid = np.vectorize(color_map.get)(grid)
    plt.imshow(mapped_grid, cmap="jet", interpolation="nearest")
    plt.title(title)
    plt.axis("off")
    plt.show()

n = 20 # Количество клеток
steps = 60 # Количество иттераций

grid = initialize_grid(n)
simulate(grid, steps)

