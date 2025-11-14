N = int(input())
nums = list(map(int, input().split()))
min_Val = 9999999
max_Val = -9999999
for i in range(N):
    if nums[i] <= min_Val:
        min_Val = nums[i]
    if nums[i] >= max_Val:
        max_Val = nums[i]

print(min_Val, max_Val)