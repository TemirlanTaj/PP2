def spy_game(l):
    for i in range(len(l)):
        if l[i] == '0' and l[i + 1] == '0' and l[i + 2] == '7':
            return True
    return False

a = list(input(int()).split())

print(spy_game(a))