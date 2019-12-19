# queueに入る最大数
MAX = 100000
# queueは配列で表現できる
queue = []
# 全体の経過時間
total_time = 0


# プロセスを表現するためのクラス
class Process:
    def __init__(self, string):
        v = string.split(' ')
        self.name = v[0]
        self.time = int(v[1])


def enqueue(n):
    global queue
    if len(queue) == MAX:
        raise OverflowError
    queue.append(n)
    return


def dequeue():
    global queue
    if len(queue) == 0:
        return None
    v = queue[0]
    del queue[0]
    return v


def solve(q):
    # 先頭のプロセスを取得し、時間を計算して処理が完了すればコンソールに表示
    # 時間を計算し完了しなければ再度queueの最後に追加
    global total_time
    global queue
    while len(queue) != 0:
        p = dequeue()
        progress = p.time - q
        if progress <= 0:
            print('name: {0}, proceeding time: {1}'.format(p.name, total_time + p.time))
            total_time += p.time
        else:
            total_time += q
            p.time -= q
            enqueue(p)


# main
if __name__ == '__main__':
    # format: n q
    first_line = input().split(' ')
    n = int(first_line[0])
    q = int(first_line[1])
    # format: process_name time
    for i in range(n):
        enqueue(Process(input()))
    solve(q)
