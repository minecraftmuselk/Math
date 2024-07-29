def spiral_diagonal_sum(n):
    total_sum = 1  # Starting with the center value
    for k in range(1, (n // 2) + 1):
        corners_sum = 4 * (2 * k + 1) ** 2 - 12 * k
        total_sum += corners_sum
    return total_sum


# Calculate the sum for a 1001x1001 spiral
n = 1001
result = spiral_diagonal_sum(n)
print(result)
