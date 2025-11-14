a = list()
max_val = None
max_idx = 0
for i in range(9):
    a.append(int(input()))
    if max_val is None or a[i] > max_val:
        max_val = a[i]
        max_idx = i + 1
print (max_val)
print (max_idx)