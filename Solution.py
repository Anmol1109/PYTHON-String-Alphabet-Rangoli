def gen(n):
    for i in range(n * 2 - 1):
        yield n - abs(i - n + 1)

def print_rangoli(size):
    for i in gen(size):
        print('-'.join(chr(ord('a') + n - j) for j in gen(i)).center(n * 4 - 3, '-'))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
