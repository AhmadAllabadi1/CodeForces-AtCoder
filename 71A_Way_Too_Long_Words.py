n = int(input())
words = []
for _ in range(n):
    words.append(input())
for word in words:
    if len(word) > 10:
        print(f'{word[0]}{len(word)}{word[-1]}')
    else:
        print(word)