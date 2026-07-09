def card_conv(x: int, r: int) -> str:

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))

    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print(' +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} ... {x % r}')
        else:
            print(f'    {x // r:{n}d} ... {x % r}')
        d += dchar [x%r]
        x //= r

    return d[::-1]