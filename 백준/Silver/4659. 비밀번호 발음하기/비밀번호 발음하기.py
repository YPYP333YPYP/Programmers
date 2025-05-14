
while True:
    string = str(input())
    if string == 'end':
        break

    if len(string) < 1 or len(string) > 20:
        print(f'{string} is not acceptable.')
        continue

    f = True
    m = ['a','e','i','o','u']

    string_m = []
    for i in string:
        if i not in m:
            string_m.append('X')
        else:
            string_m.append('O')

    if 'O' not in string_m:
        print(f'<{string}> is not acceptable.')
        continue

    for i in range(len(string)-2):
        if string_m[i] == string_m[i+1] == string_m[i+2]:
            f = False
            break

    if not f:
        print(f'<{string}> is not acceptable.')
        continue

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            if string[i] == 'o' or string[i] == 'e':
                continue
            else:
                f = False
                break

    if not f:
        print(f'<{string}> is not acceptable.')
        continue

    print(f'<{string}> is acceptable.')
