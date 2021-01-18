lst = []
def Fibo(n):
    lst.insert(0,1)
    lst.insert(1,1)
    for i in range(2,n+1):
        lst.insert(i,lst[i-1]+lst[i-2])

def CalculateFibo(n):
    if lst[n] > 0:
        return lst[n]
    if n is 0 or n is 1:
        return 1
    else:
        return lst[n].append(CalculateFibo(n-1)+CalculateFibo(n-2))

Fibo(46)
print(CalculateFibo(5))