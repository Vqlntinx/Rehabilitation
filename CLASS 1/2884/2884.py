H, M = map(int, (input().split()))
if M - 45 < 0:
    H -= 1
    M = M + 15
elif M - 45 > 0:
    M = M - 45
else:
    M = 0

if H < 0:
    H = 23
print(H, M)