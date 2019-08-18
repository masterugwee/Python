def askey():
    s = input()
    a,b = s.split(',')
    avalue = 0
    bvalue = 0
    for i in range(len(a)):
        avalue += ord(a[i])
    for j in range(len(b)):
        bvalue += ord(b[j])
    if avalue == bvalue:
        print("They are Equal",avalue,bvalue)
    else:
        print("They are not equal",avalue,bvalue)


if __name__=="__main__":
    askey()
