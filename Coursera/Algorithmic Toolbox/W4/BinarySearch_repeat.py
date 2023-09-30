import math
def binary_search(n_k, k,q):
    left = 0
    right = n_k - 1
    if k[left] == q:
        return left
    if k[right] == q:
        return right
    while right >= left:
        middle = left + (right - left)//2
        if k[middle] == q:
            middle = find_repeat(k,middle,q)
            return middle
        elif k[middle] < q:
            left = middle + 1
        else:
            right = middle -1
    return -1
def find_repeat(k,middle,q):
    # check left side:
    while middle >=1:
        if k[middle-1] == q:
            middle -=1
        else:
            return middle
    return middle
        


def wrap_binary(n_k,k, n_q, q):
    return_list = []
    for i in range(n_q):
        return_list.append(binary_search(n_k,k,q[i]))
    return return_list



if __name__ == '__main__':
    n_k = list(map(int,input().split()))[0]
    k = list(map(int, input().split()))
    n_q = list(map(int,input().split()))[0]
    q = list(map(int, input().split()))
    print(' '.join(map(str, wrap_binary(n_k,k, n_q, q))))