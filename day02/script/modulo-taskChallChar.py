def x():
    v = 424242.8412
    s = str(v).split('.')
    e = int(s[0])
    d = int(s[1])*10**-len(s[1])
    print(e)
    print(d)
x()