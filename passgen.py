import random

c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@##$%^&*()?"
len = int(input("pass length: "))
def randgen(inp):
    z = ''.join(random.sample(c,inp))
    print(z)

randgen(len)