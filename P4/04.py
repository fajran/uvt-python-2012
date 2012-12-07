class PembagianDenganNol(ZeroDivisionError):
    pass

def bagi(a, b):
    if b == 0:
        raise PembagianDenganNol()
    return a / b

print bagi(4, 2)
print bagi(2, 0)

