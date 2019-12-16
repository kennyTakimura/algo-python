def out(G, cnt, A):
    # first line
    print(len(G))
    # second line
    for idx, g in enumerate(G):
        if not idx == len(G) - 1:
            print(g, end=" ")
        else:
            print(g)
    # third line
    print(cnt)
    # following n lines
    for idx, i in enumerate(A):
        print(i)


def insertion_sort(A, n, g):
    """insertion sort"""
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            cnt += 1
            j -= g
        A[j + g] = v


def shell_sort(A, n):
    # G = [1, 4, 7, 10, 13 ... 3*h+1]の数列を生成
    h = 1
    global G
    while n > h:
        G.append(h)
        h = 3 * h + 1

    for i in reversed(range(len(G))):
        insertion_sort(A, n, G[i])


# main
if __name__ == '__main__':
    N = int(input())
    cnt = 0
    G = []
    A = [int(input()) for i in range(N)]
    shell_sort(A, N)
    out(G, cnt, A)
