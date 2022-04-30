

def true_fanction(x):
    """ 
    >>>ture_fanction(0)
    0
     """
    y = sin(pi * x * 0.8) * 10
    return y

if __name__ == '__main__':
    import doctest
    doctest.testmod()