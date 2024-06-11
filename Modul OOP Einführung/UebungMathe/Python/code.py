# Task 1
def sum(a, b):
    return a + b

# Task 2
def square(a):
    return a**2

# Task 3
def ispositiv(a):
    return "ERROR: 0 not assignable" if a == 0 else True if a > 0 else False
    
# Task 4
def fac(a):
    return 1 if a == 0 else a*fac(a-1)

# Task 6
def fib(a):
    def rec(x, y, count):
        return y if count == a else rec(y, y+x, count + 1)
    return 0 if a == 0 else "ERROR: No Negative Values Accepted" if a < 0 else rec(0, 1, 1)

# Testing
if __name__ == '__main__':

    # Task 1
    a = 5
    b = 1
    print(f'Die Summe aus {a} und {b} ist {sum(a, b)}')

    # Task 2
    c = 9
    print(f'Das Quadrat von {c} ist {square(c)}')

    # Task 3
    d = -3
    print(f'Ist {d} positiv? {ispositiv(d)}')

    # Task 4
    e = 3
    print(f'Die Fakultät von {e} ist {fac(e)}')

    # Task 6
    f = 2
    print(f'Die Fibonacci Zahl zu {f} ist {fib(f)}')
