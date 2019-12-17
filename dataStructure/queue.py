# queueに入る最大数
MAX = 100000
HEAD = 0
TAIL = 1
# queueは配列で表現できる
queue = ['' for i in range(MAX+1)]  # 0の要素は参照しない
# 結果
res = []


# プロセスを表現するためのクラス
class Process:
    def __init__(self, str):
        v = str.split(' ')
        self.name = v[0]
        self.time = int(v[1])


def enqueue(n):
    global HEAD
    if HEAD == MAX:
        # 現在のHEADがMAXに達したらHEADを0にリセット
        HEAD = 1
        queue[HEAD] = n
    # HEADをインクリメントしてから配列に追加
    HEAD += 1
    queue[HEAD] = n


def dequeue():
    global TAIL
    if TAIL == MAX:
        # 現在のTAILがMAXの場合0にリセット
        v = queue[TAIL]
        TAIL = 1
        return v
    v = queue[TAIL]
    TAIL += 1
    return v


def solve(A):
    for i in A:
        if i == '+':
            # 2つpopして足し算、結果をpush
            # a = pop()
            # b = pop()
            # push(a + b)
            pass

        elif i == '-':
            # 2つpopして引き算、結果をpush
            # a = pop()
            # b = pop()
            # push(b - a)
            pass

        elif i == '*':
            # 2つpopして掛け算、結果をpush
            # a = pop()
            # b = pop()
            # push(a * b)
            pass

        else:
            # 数字をpush
            # push(int(i))
            pass


# main
if __name__ == '__main__':
    first_line = input().split(' ')
    n = int(first_line[0])
    q = int(first_line[1])
    p = [Process(input()) for i in range(n)]
    solve(p)
