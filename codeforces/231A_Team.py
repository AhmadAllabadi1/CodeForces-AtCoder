n = int(input())
output = 0
for _ in range(n):
    if sum(list(map(int, input().split()))) >= 2:
        output += 1
print(output)