a = list(input())
if a[0] != 'F':
    score = float(abs(ord(a[0]) - ord('E')))
    if a[1] == '+':
        score += 0.3
    elif a[1] == '-':
        score -= 0.3
else:
    score = float(0)
print(score)


# A=input()
# T={"A+":4.3, "A0":4.0, "A-":3.7, "B+":3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
#
# print(T[A])
