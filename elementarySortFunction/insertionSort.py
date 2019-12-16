def out(A):
    for idx, i in enumerate(A):
        if not idx == len(A) - 1:
            print(i, end=" ")
        else:
            print(i)


def insertion_sort(A, N):
    """insertion sort"""
    for i in range(1, N):
        out(A)
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v


# main
if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    insertion_sort(A, N)
    out(A)
