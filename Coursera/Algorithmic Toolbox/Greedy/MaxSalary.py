def max_salary(numbers):
    # Convert numbers to strings and sort using a custom sorting key
    sorted_numbers = sorted(map(str, numbers), key=lambda x: x*10, reverse=True)
    return ''.join(sorted_numbers)

if __name__== '__main__':
    N = list(map(int,input().split()))[0]
    Array = list(map(int, input().split()))
    print(max_salary(Array))