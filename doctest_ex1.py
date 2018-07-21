def mul(a, b):
    """
    >>> mul(2, 3)
        6
    >>> mul('a', 2)
        'aa'
    """
    return a * b

if __name__ == "__main__":
    import doctest
    print(doctest.__file__)
#doctest.testmod()
