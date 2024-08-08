def comprobar(v):
    n = len(v)
    for i in range(n-1):
        if v[i] > v[i+1]:
            return False
    return True
