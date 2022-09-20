a = int(input())
b = int(input())
diff = b - a
if diff >= 5:
    for n1 in range(a, b + 1):
        for n2 in range(a, b + 1):
            for n3 in range(a, b + 1):
                for n4 in range(a, b + 1):
                    for n5 in range(a, b + 1):
                        if a <= n1 < n2 < n3 < n4 < n5 <= b:
                            print(n1, n2, n3, n4, n5)
else:
    print('No')