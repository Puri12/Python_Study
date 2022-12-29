a = list(input())

for i in range(len(a)):
    if ord(a[i]) in range(ord('a'), ord('z') + 1):
        a[i] = a[i].upper()
    elif ord(a[i]) in range(ord('A'), ord('Z') + 1):
        a[i] = a[i].lower()

print(''.join(a))


# print(input().swapcase())