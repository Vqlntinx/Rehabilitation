N, X = map(int, input().split())
arrN = list(map(int, input().split()))
for i in range(N) :
    if arrN[i] < X :
        print(arrN[i])