def printTrib(n):
    ar = []
    for i in range(n):
     ar.append(int(input()))
    noofdiv = 0
    counter = 0
    length = len(ar)
    #print(length)
    i = 0
    while i<len(ar):
        m = printTribRec(counter)
        for div in range(1,m+1):
            if m%div == 0:
                noofdiv += 1
        if(noofdiv<=ar[i]):
            counter = counter+1
            noofdiv = 0
        elif noofdiv > ar[i]:
            print(m)
            noofdiv = 0
            if i < length:
                i = i+1
                counter = 0

def printTribRec(nc):

    if (nc == 0 or nc == 1 or nc == 2):
         return 0
    elif (nc == 3):
        return 1
    else:
        return ((nc - 1) +(nc - 2) +(nc - 3))
    # Driver code

if __name__=="__main__":
    n = int(input())
    printTrib(n)