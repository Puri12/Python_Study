n, x = map(int, input().split())
arr = list(map(int, input().split()))
answer = ""

for i in range(n):
    if arr[i] < x:
        answer += str(arr[i]) + " "

print(answer[:len(answer)-1])

# count, X = map(int, input().split())
# num = map(int, input().split())
# for j in num:
#     if j < X:
#         print("%d " % j, end='')