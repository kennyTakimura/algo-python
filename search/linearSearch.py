C = set()


def out():
    print(len(C))


def linear_search(S, T):
    for s in S:
        for t in T:
            if s == t:
                C.add(t)


# main
if __name__ == '__main__':
    n = int(input())
    S = input().split(' ')
    q = int(input())
    T = input().split(' ')
    linear_search(S, T)
    out()
