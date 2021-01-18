def decimalToBinary(n):
    if n == 0:
        return ""
    temp = str(n%2)
    bin = decimalToBinary(int(n/2)) + temp
    return bin

print(decimalToBinary(2))