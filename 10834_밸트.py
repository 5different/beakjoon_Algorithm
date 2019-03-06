T = int(input())
result = 1
direction = 0
for i in range(T):
    A = list(map(int, input().split()))
    result = (result / A[0]) * A[1]
    direction += A[2]

print('{} {}'.format(direction%2,int(result)))


