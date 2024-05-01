def print_pattern(s):
    n = len(s)
    mid = n // 2

    for i in range(mid + 1):
        for j in range(n):
            if j == i or j == n - i - 1:
                print(s[j], end='')
            else:
                print(' ', end='')
        print()

    for i in range(mid - 1, -1, -1):
        for j in range(n):
            if j == i or j == n - i - 1:
                print(s[j], end='')
            else:
                print(' ', end='')
        print()

# Test the function
print_pattern('12345')