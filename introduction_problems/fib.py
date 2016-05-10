# Uses python3
def calc_fib(n):
    if n < 1:
        return n
    a = [1, 0]
    for i in range(2, n):
        aux = a[0] + a[1]
        a[1] = a[0]
        a[0] = aux
    return a[0] + a[1]


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
