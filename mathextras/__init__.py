"""__init__.py
Calls other files in the package.
"""

def prime(num):
    import prime
    return prime.prime(num)

def fac(num):
    import faclist
    out = faclist.getfac(num)
    return out

def lcm(num1, num2, limit=10):
    import lcm
    return lcm.findlcm(num1, num2, limit)

def prime_out(num):
    import prime_out
    return prime_out.prime_out(num)
