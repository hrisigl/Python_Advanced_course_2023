rows, cols = [int(i) for i in input().split(", ")]
matrix = [[int(a) for a in input().split(", ")] for _ in range(rows)]

biggest_sum = float("-inf")
nums = []

for row in range(rows - 1):
    for col in range(cols - 1):
        total_sum = sum([matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]])
        if total_sum > biggest_sum:
            biggest_sum = total_sum
            nums = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]

num1, num2, num3, num4 = nums
print(f"{num1} {num2}")
print(f"{num3} {num4}")
print(biggest_sum)
