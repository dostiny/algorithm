import sys

sys.stdin = open('input/11151_input.txt', 'r')

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    for i in range(1, N):
        if max_v < arr[i-1] + arr[i]:
            max_v = arr[i-1] + arr[i]
    print(f'#{test_case} {max_v}')