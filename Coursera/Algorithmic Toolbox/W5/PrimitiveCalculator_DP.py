import math
def PrimCalc(n):
    # Create a list to store the minimum number of operations to reach each number from 1 to n
    min_operations = [0] * (n + 1)

    for i in range(2, n + 1):
        # Initialize the minimum operations with the value for adding 1 to the previous number
        min_operations[i] = min_operations[i - 1] + 1

        # Check if dividing by 2 is a valid operation
        if i % 2 == 0:
            min_operations[i] = min(min_operations[i], min_operations[i // 2] + 1)

        # Check if dividing by 3 is a valid operation
        if i % 3 == 0:
            min_operations[i] = min(min_operations[i], min_operations[i // 3] + 1)
    
    sequence = []
    while n > 1:
        sequence.append(n)
        if n % 3 == 0 and min_operations[n] == min_operations[n // 3] + 1:
            n //= 3
        elif n % 2 == 0 and min_operations[n] == min_operations[n // 2] + 1:
            n //= 2
        else:
            n -= 1
    sequence.append(1)

    return list(reversed(sequence)), min_operations[-1]
if __name__ == '__main__':
    Number = list(map(int,input().split()))[0]
    Seq, NumOper = PrimCalc(Number)
    print(NumOper)
    print(' '.join(map(str,Seq)))