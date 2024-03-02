n = int(input())
i = 2


while i <= n//2:
    if n % i == 0:
        print(n, 'is a prime number')
        break
    i += 1
else:
    print(n, 'is not a prime number')


