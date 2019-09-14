def printTribRec(n):
    if (n == 0 or n == 1 or n == 2):
        return 0
    elif (n == 3):
        return 1
    else:
        return (printTribRec(n - 1) +
                printTribRec(n - 2) +
                printTribRec(n - 3))


def tribonacci(n):
    ar = []
    for i in range(n):
        ar.append(int(input()))
    for j in range(n):
        for i in range(1000):
            n = printTribRec(i)
            div = ar[j]
            counter = 0
            for _ in range(1,n+1):
                if n%_ == 0:
                    counter += 1
            if(counter > div):
                print(n)
                break
    # Driver code

if __name__=="__main__":
    n = int(input())
    tribonacci(n)
