X = float(input())

def bbb(X):
    if isinstance(X, float) and X.is_integer():
        return int(X)
    else:
        return X
    
print(bbb(X))
