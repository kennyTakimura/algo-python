C = set()


def out():
    print(len(C))


def binary_search(S, t):
    if len(S) == 0:
        return
    mid_index = int(len(S) / 2 - 1)  # 0オリジンなので-1する. ex.) 9 / 2 - 1 = 3
    if t < S[mid_index]:
        binary_search(S[:mid_index], t)
    elif S[mid_index] < t:
        binary_search(S[mid_index + 1:], t)
    else:
        C.add(t)
        return


# main
if __name__ == '__main__':
    n = int(input())
    S = input().split(' ')
    q = int(input())
    T = input().split(' ')
    for t in T:
        binary_search(S, t)
    out()
