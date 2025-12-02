x, y, z = list(map(int, input().split()))
if (z * y - x) % (1 - z) == 0 and (z * y - x) // (1 - z) >= 0:
    print("Yes")
else:
    print("No")