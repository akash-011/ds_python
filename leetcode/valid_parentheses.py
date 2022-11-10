def isValid(s):
    my_stack = []
    for char in s:
        match char:
            case '{' | '(' | '[':
                my_stack.append(char)
            case '}' | ')' | ']':
                if len(my_stack) == 0:
                    return False
                if char is ')' and my_stack.pop() is not '(':
                    return False
                if char is ']' and my_stack.pop() is not '[':
                    return False
                if char is '}' and my_stack.pop() is not '{':
                    return False
                
            case _:
                return False
    if len(my_stack) != 0:
        return False

    return True  