def countdown(n, txt):
    for i in range(int(n), 1, 1):
        return f'{i}' + f'{txt}' + '!'

print(countdown(16, "Shoot"))