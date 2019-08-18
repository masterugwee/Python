def minimax(arr):
    arr.sort()
    max = 0
    min = 0
    for i in range(len(arr)):
        if i!=0:
            max += arr[i]
        if i!=4:
            min += arr[i]
    print(min,max)
if __name__=="__main__":
    arr = list(map(int, input().rstrip().split()))
    minimax(arr)
