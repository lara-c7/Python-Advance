stack = []

number = int(input())
for _ in range(number):
    query = input().split()
    if query[0] == '1':
        stack.append(int(query[1]))
    elif stack:
        if query[0] == '2':
            stack.pop()
        elif query[0] == '3':
            print(max(stack))
        elif query[0] == '4':
            print(min(stack))

while stack:
    print(stack.pop(), end='')
    if stack:
        print(', ', end='')
#or simply - print(', '.join(map(str, reversed(stack))))
