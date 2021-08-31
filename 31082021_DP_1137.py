#input
n = int(input())

#recursive algo

def tribonacci(n):
    lst = [-1 for i in range(n+1)]

    def fun(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if lst[n] == -1:
            lst[n] = fun(n-1) + fun(n-2) + fun(n-3)
        return lst[n]
    return fun(n)

print(tribonacci(n))