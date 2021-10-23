import random

def memorize_func(f):
    memo = dict()

    def func(*args):
        #print(f'Run with args={args}, memo={memo}')
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return func

@memorize_func
def isPalindrome(n):
    try:
        int(n)
        n = str(n)
        return n == n[::-1]
    except ValueError:
        return False

@memorize_func
def threeLists(n):
    divideTwo = []
    divideThree = []
    divideFive = []

    for el in n:
        if el % 2 == 0:
            divideTwo.append(el)
        if el % 3 == 0:
            divideThree.append(el)
        if el % 5 == 0:
            divideFive.append(el)

    return divideTwo, divideThree, divideFive

@memorize_func
def reverseNumber(n):
    isPositive = None

    if n > 0:
        isPositive = True
    else:
        isPositive = False
        n = -n

    result = 0

    while n > 0:
        digit = n % 10
        n = n // 10
        result = result * 10
        result = result + digit

    if isPositive == True:
        return result
    else:
        return -result

@memorize_func
def nthRoot(number, power):
    xPre = random.randint(1, 101) % 10

    eps = 0.001

    delX = 2147483647

    xK = 0.0

    while (delX > eps):
        xK = ((power - 1.0) * xPre +
              number / pow(xPre, power - 1)) / power
        delX = abs(xK - xPre)
        xPre = xK

    return xK

#обновленный isPrime(a)
@memorize_func
def isPrime(a):
    print('First function call')
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    print(isPalindrome(10))
    print(isPalindrome(101))
    print(isPalindrome('a'))

    print(threeLists([2, 5, 10, 6, 15, 7]))

    print(reverseNumber(-123))
    print(reverseNumber(120))
    print(reverseNumber(0))
    print(reverseNumber(123))

    print(nthRoot(10, 3))

    print(isPrime(7))
    print(isPrime(13))
    print(isPrime(15))

    print(isPrime(7))
    print(isPrime(13))
    print(isPrime(7))
    print(isPrime(13))
