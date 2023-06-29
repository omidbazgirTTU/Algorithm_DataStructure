def GCD(a,b):
    if a >=b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    while(larger%smaller !=0 & smaller !=1):
        temp = larger%smaller
        larger = smaller
        smaller = temp
    return smaller

if __name__ == '__main__':
    a,b = map(int,input().split())
    print(GCD(a,b))