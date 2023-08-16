matrix = [[int(i) for i in input().split(", ")]for _ in range(int(input()))]

first_diagonal = []
second_diagonal = []

for row in range(len(matrix)):
    first_diagonal.append(matrix[row][row])
    second_diagonal.append(matrix[row][len(matrix) - 1 - row])

print(f"Primary diagonal: {', '.join(str(a) for a in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(b) for b in second_diagonal)}. Sum: {sum(second_diagonal)}")
