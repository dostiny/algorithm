import sys

n = int(sys.stdin.readline())

for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i + 1}: {A + B}')