def is_valid(str):
    brackets = {
        '(':')',
        '{':'}',
        '[':']'
    }
    stack = []

    for bracket in str:
        if bracket in brackets:
            stack.append(bracket)
        else:
            if not stack:
                return False
            if bracket != brackets[stack.pop()]:
                return False
    return (len(stack) == 0)
    # if not stack:
    #     print('Yes')
    #     return True
    # else:
    #     print ('NO')
    #     return False

r = is_valid('()))')
print (r)

def check_brakets(str):
    stack = []
    is_verify = True
    for bracket in str:
        if bracket in '({[':
            stack.append(bracket)
        elif bracket in ']})':
            if len(stack) == 0:
                is_verify = False
                break
            br_p = stack.pop()
            if br_p == '(' and bracket == ')':
                continue
            if br_p == '[' and bracket == ']':
                continue
            if br_p == '{' and bracket == '}':
                continue
            is_verify = False
            break

    if is_verify and len(stack) == 0:
        return True
    else:
        return False

cb = check_brakets('()')
print(cb)