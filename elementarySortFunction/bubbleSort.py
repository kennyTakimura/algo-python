def out(A):
    for idx, i in enumerate(A):
        if not idx == len(A) - 1:
            print(i, end=" ")
        else:
            print(i)


def bubble_sort(A):
    """bubble sort"""
    for i in range(len(A) - 1):  # 0オリジンでのAのサイズ - 1
        out(A)
        for j in reversed(range(i + 1, len(A))):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


# main
if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    bubble_sort(A)
    out(A)
