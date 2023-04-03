# Найти факториал N

n = int(input())
n_fak = 1

for i in range(1, n+1):
    n_fak *= i
    print(n_fak)