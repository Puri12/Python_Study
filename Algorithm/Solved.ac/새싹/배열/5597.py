arr = []

for _ in range(28):
    arr.append(int(input()))

for i in range(1, 31):
    if list(arr).count(i) == 0:
        print(i)
        
# a=list(map(int,open(0).read().split()))
# for i in range(1,31):
#     try:a.index(i)
#     except: print(i)