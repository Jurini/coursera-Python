def vogal(x):
    if x.__eq__('a') or x.__eq__('A'):
        return True
    elif x.__eq__('e') or x.__eq__('E'):
        return True
    elif x.__eq__('i') or x.__eq__('I'):
        return True
    elif x.__eq__('o') or x.__eq__('O'):
        return True
    elif x.__eq__('u') or x.__eq__('U'):
        return True
    else:
        return False


print(vogal('Q'))
