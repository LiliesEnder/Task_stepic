a= {'global':{"__vars": set()}}

def create(dct, np, par):
    if par in dct:
        dct[par][np] = {"__vars": set()}
        return True
    for k in list(dct.keys()):
        if k == '__vars':
            continue
        res = create(dct[k], np, par)
        if res == True:
            return True
    return False

def add(dct, np, var):
    if np in dct:
        dct[np]['__vars'].add(var)
        return True
    for k in list(dct.keys()):
        if k == '__vars':
            continue
        res = add(dct[k], np, var)
        if res == True:
            return True
    return False

def get(dct, np, var, fnd=False):
    if fnd and np in dct:
        return (True, True)
    elif fnd:
        for k in list(dct.keys()):
            if k == '__vars':
                continue
            res = get(dct[k], np, var, fnd=True)
            if res == (True, True):
                return (True, True)
        return (True, False)
    elif not fnd and var in dct['__vars']:
        if np in dct:
            return (True, True)
        else:
            for k in list(dct.keys()):
                if k == '__vars':
                    continue
                res = get(dct[k], np, var, fnd=True)
                if res == (True, True):
                    return k
            return (True, False)
    elif not fnd:
        if np in dct and var in dct[np]['__vars']:
            return np
        elif np in dct:
            return None
        else:
            for k in list(dct.keys()):
                if k == '__vars':
                    continue
                res = get(dct[k], np, var, fnd=False)
                if res == (True, True):
                    return k
                elif isinstance(k, str):
                    return k
                elif res is None:
                    return None
            return None
    return False
    
        
n = int(input())
for i in range(n):
    cmd, namespace, vp = input().split()
    if cmd == 'create':
        create(a, namespace, vp)
    elif cmd == 'add':
        add(a, namespace, vp)
    elif cmd == 'get':
        res = get(a['global'], namespace, vp)
        print('global' if res == (True, True) else res)
    print(a)


