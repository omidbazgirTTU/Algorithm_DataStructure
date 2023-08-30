def MaxAdvert(N, Price, Clicks):
    Price = sorted(Price)
    Clicks = sorted(Clicks)

    Value = 0
    for i in range(N):
        Value += Price[i]*Clicks[i]

    return Value



if __name__== '__main__':
    N = list(map(int,input().split()))[0]
    Prices = list(map(int, input().split()))
    Clicks = list(map(int, input().split()))
    print(MaxAdvert(N,Prices,Clicks))