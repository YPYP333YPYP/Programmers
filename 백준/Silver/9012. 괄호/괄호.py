N = int(input())

def sol(string):
    string = list(string)
    stack = []

    for v in string:
        if v == '(':
            stack.append(v)
        elif v == ')':
            if len(stack) > 0:
                stack.pop(-1)
            else:
                return "NO"

    if len(stack) > 0:
        return "NO"
    else:
        return "YES"





for _ in range(N):
    val = str(input())
    result = sol(val)
    print(result)