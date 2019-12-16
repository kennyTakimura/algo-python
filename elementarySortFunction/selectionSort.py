count = 0


def out(A):
    for idx, i in enumerate(A):
        if not idx == len(A) - 1:
            print(i, end=" ")
        else:
            print(i)
    print(count)


def selection_sort(A):
    """selection sort"""
    global count
    for i in range(len(A)):  # 0オリジンでのAのサイズ - 1
        mini = i
        for j in range(i, len(A)):
            if A[j] < A[mini]:
                mini = j
        if not i == mini:
            count += 1
            A[i], A[mini] = A[mini], A[i]


# main
if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    selection_sort(A)
    out(A)
