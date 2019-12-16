# stackは配列で表現する
stack = []


def push(n):
    stack.append(n)


def pop():
    if len(stack) < 1:
        raise IndexError("index out of range")
    idx = len(stack) - 1
    v = stack[idx]
    del stack[idx]
    return v


def solve(A):
    for i in A:
        if i == '+':
            # 2つpopして足し算、結果をpush
            a = pop()
            b = pop()
            push(a + b)

        elif i == '-':
            # 2つpopして引き算、結果をpush
            a = pop()
            b = pop()
            push(b - a)

        elif i == '*':
            # 2つpopして掛け算、結果をpush
            a = pop()
            b = pop()
            push(a * b)

        else:
            # 数字をpush
            push(int(i))


# main
if __name__ == '__main__':
    solve(input().split(' '))
    print(pop())
