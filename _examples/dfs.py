from collections import deque

N = 100
color = [[None] * N for i in range(N)]
WHITE = 0
GRAY = 1
BLACK = 2
H = None
W = None
M = None
d = deque()
START = "s"
GOAL = "g"
WALL = "#"


def dfs_init():
    # スタート位置を探しつつ、colorをWHITEで初期化する
    for i in range(H):
        for j in range(W):
            color[i][j] = WHITE
            if M[i][j] is START:
                d.append([i, j])


def next_v(i, j):
    # jは現在の位置
    if j + 1 < W and M[i][j + 1] and M[i][j + 1] is not WALL:  # 右に進める
        return [i, j + 1]
    if i - 1 > -1 and M[i - 1][j] and M[i - 1][j] is not WALL:  # 上に進める
        return [i - 1, j]
    if i + 1 < H and M[i + 1][j] and M[i + 1][j] is not WALL:  # 下に進める
        return [i + 1, j]
    else:
        return -1


def dfs():
    dfs_init()
    while len(d) != 0:
        u = d.pop()  # 訪問中の頂点
        color[u[0]][u[1]] = GRAY  # 訪問中の頂点は1
        v = next_v(u[0], u[1])  # 次の頂点
        if v != -1:
            if color[v[0]][v[1]] is WHITE:
                if M[v[0]][v[1]] is GOAL:
                    print("Yes")
                    return
                color[v[0]][v[1]] = GRAY
                d.append(v)
        else:
            color[u[0]][u[1]] = BLACK
    print("No")


# main
if __name__ == '__main__':
    H, W = map(int, input().split(" "))
    M = [list(input().split(" ")) for i in range(H)]
    dfs()
