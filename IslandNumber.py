#هذا الكود يقوم بحساب عدد الجزر في مصفوفة ثنائية الأبعاد باستخدام البحث في العمق 
# (DFS - Depth-First Search).
matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0]
]

def num_islands(grid):
    if not grid:
        return 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_islands = 0

    def dfs(row, col):
        if row < 0 or row >= num_rows or col < 0 or col >= num_cols or grid[row][col] != 1:
            return
        grid[row][col] = -1
        dfs(row - 1, col)  # Up
        dfs(row + 1, col)  # Down
        dfs(row, col - 1)  # Left
        dfs(row, col + 1)  # Right
        dfs(row - 1, col - 1)  # Up-Left
        dfs(row - 1, col + 1)  # Up-Right
        dfs(row + 1, col - 1)  # Down-Left
        dfs(row + 1, col + 1)  # Down-Right

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                num_islands += 1
                dfs(i, j)

    return num_islands

num_of_islands = num_islands(matrix)
print("Number of islands:", num_of_islands)
