n, m = map(int, input().split())
arr = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]

for i in range(2):
    for y in range(n):
            arr[i][y] = map(int, input().split())

for y in range(n):
    arr1 = list(arr[0][y])
    arr2 = list(arr[1][y])
    for x in range(m):
        print(arr1[x] + arr2[x], end=' ')
    print()