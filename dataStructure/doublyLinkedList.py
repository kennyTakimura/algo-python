

# 連結リストの先頭の要素
# 先頭の要素は番兵ノードとしての役割のみを持ち、
# データ自体は保持しない特殊な存在
class DummyNode:
    def __init__(self):
        self.prev = None
        self.key = None
        self.next = None


# 連結リストの各要素
class Node:
    def __init__(self, key):
        self.prev = None
        self.key = key
        self.next = None


# 初期化
sentinel_node = DummyNode()


# 連結リストの先頭にNodeを追加する
# 新しいNode n を生成
# if 初めてのNodeの追加
#   sentinel_nodeのprevにnを割り当てる
#   nのnextにsentinel_nodeを割り当てる
# else
#   nのnextにsentinel_nodeのnextを割り当て
#   sentinel_nodeのnextのprevにnを割り当て
# sentinel_nodeのnextにnを割り当て
# nのprevとしてsentinel_nodeを割り当て
def insert(key):
    global sentinel_node
    n = Node(key)
    if sentinel_node.next is None:
        sentinel_node.prev = n
        n.next = sentinel_node
    else:
        n.next = sentinel_node.next
        sentinel_node.next.prev = n
    sentinel_node.next = n
    n.prev = sentinel_node


# 検索結果のノードをt削除する
# tのprevのNodeのnextを、tのnextに設定する
# tのnextのNodeのprevを、tのprevに設定する
def delete(key):
    t = find(key)
    if t is None:
        return None
    t.prev.next = t.next
    t.next.prev = t.prev
    del t  # tを削除しメモリを解放


# 先頭のNode(DummyNodeのnext)を削除する
# 先頭のNodeをnとする
# if n is None(=リストが空の場合)
#   何もせずreturn
# if nのnextがNone(=Nodeが一つだけ)
#   sentinel_nodeのnextにsentinel_nodeのprevを割り当て
#   sentinel_nodeのprevにsentinel_nodeのnextを割り当て
# else
#   nのnextのprevにsentinel_nodeを割り当てる
#   sentinel_nodeのnextにnのnextを割り当てる
# nを削除しメモリを解放
def delete_first():
    global sentinel_node
    n = sentinel_node.next
    if n is None:
        return
    if n.next is None:
        sentinel_node.next = sentinel_node.prev
        sentinel_node.prev = sentinel_node.next
    else:
        n.next.prev = sentinel_node
        sentinel_node.next = n.next
    del n


# 最後のNode(DummyNodeのprev)を削除する
# 最後のNodeをnとする
# if n is None(=リストが空の場合)
#   何もせずreturn
# if nのprevがNone(=Nodeが一つだけ)
#   sentinel_nodeのnextにsentinel_nodeのprevを割り当て
#   sentinel_nodeのprevにsentinel_nodeのnextを割り当て
# else
#   nのprevのnextにsentinel_nodeを割り当てる
#   sentinel_nodeのprevにnのprevを割り当てる
# nを削除しメモリを解放
def delete_last():
    global sentinel_node
    n = sentinel_node.prev
    if n is None:
        return
    if n.prev is None:
        sentinel_node.next = sentinel_node.prev
        sentinel_node.prev = sentinel_node.next
    else:
        n.prev.next = sentinel_node
        sentinel_node.prev = n.prev
    del n


def find(key):
    global sentinel_node
    # DummyNodeのnextをcurrとする
    curr = sentinel_node.next
    while curr is not None and curr.key is not None:
        # 次のNodeがあり、かつkeyが存在する限りループする
        if curr.key == key:
            # keyが一致すればreturn
            return curr
        # keyが一致しなければその次のNodeをcurrとする
        curr = curr.next
    # 一致するkeyがないままループが終了した場合、Noneをreturn
    return None


def debug_all(method):
    global sentinel_node
    # DummyNodeのnextをcurrとする
    curr = sentinel_node.next
    print('=====' + method + '=====')
    while curr.next.key is not None:
        print(curr.key)
        curr = curr.next


def out_all():
    global sentinel_node
    finished = False
    # DummyNodeのnextをcurrとする
    curr = sentinel_node.next
    while not finished:
        if curr.next.key is None:
            print(curr.key)
            finished = True
        else:
            print(curr.key, end=' ')
        curr = curr.next


# main
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        command = input().split(' ')
        if command[0] == 'insert':
            insert(command[1])
        if command[0] == 'delete':
            delete(command[1])
        if command[0] == 'deleteFirst':
            delete_first()
        if command[0] == 'deleteLast':
            delete_last()
    out_all()
