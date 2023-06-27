def MainFunction(N,Array):
    max1 = Array[0]
    ind1 = 0
    for ind in range(N):
        if Array[ind] >= max1:
            max1 = Array[ind]
            ind1 = ind
    del Array[ind1]
    
    max2 = Array[0]
    for element in Array:
        if element >= max2:
            max2 = element
    return max1*max2

if __name__ == '__main__':
    N = list(map(int,input().split()))[0]
    Array = list(map(int, input().split()))
    print(MainFunction(N,Array))
    

