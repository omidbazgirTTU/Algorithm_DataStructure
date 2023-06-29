def Fibonacci(N):
    F = list()
    F.append(0)
    F.append(1)
    if N > 1:
        for i in range(2, N+1):
            F.append(F[i-1] + F[i-2])
    return F[N]

if __name__ == '__main__':
    N = list(map(int, input().split()))[0]
    print(Fibonacci(N))
