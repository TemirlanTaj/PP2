def has_33(l):
    for i in range(len(l)):
        if l[i] == '3' and l[i + 1] == '3':
            return True
    return False

a = list(input().split())

print(has_33(a))