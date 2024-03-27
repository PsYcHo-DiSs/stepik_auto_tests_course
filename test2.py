MAX_DIGITS = 12
MAX_SUM = 110

matrix = [[0] * (MAX_SUM + 1) for _ in range(MAX_DIGITS + 1)]

matrix[0][0] = 1

for digits in range(1, MAX_DIGITS + 1):
    for summa in range(MAX_SUM + 1):
        for digit in range(10):
            if summa + digit <= MAX_SUM:
                matrix[digits][summa + digit] += matrix[digits - 1][summa]

s = int(input())
print(matrix[MAX_DIGITS][s])
