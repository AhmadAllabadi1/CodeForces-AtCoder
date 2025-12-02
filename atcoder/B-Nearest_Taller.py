n = int(input())
arr = list(map(int, input().split()))
res = []
stack = []
for i in range(len(arr)):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    if stack:
        res.append(stack[-1])
    else:
        res.append(-1)
    stack.append(i)
for r in res:
    if r != -1:
        print(r + 1)
    else:
        print(-1)