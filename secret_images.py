def secret_images():
    #Enter your code here..
    f = open("/home/masterugwee/projects/bi0s/challenges!/python/file.txt","r")
    countpng = 0
    countjpeg = 0
    countbmp = 0
    counter = 0
    first_line = int(f.readline())
    contents = f.readlines()
    for x in contents:
      if(counter<first_line):
        counter = counter+1
        s = "".join(x)
        if(s[-4:-1] == "png"):
            countpng = countpng+1
        elif(s[-4:-1] == "bmp"):
            countbmp = countbmp+1
        elif(s[-5:-1] == "jpeg"):
            countjpeg = countjpeg+1
      else:
          break
    print(countjpeg)
    print(countbmp)
    print(countpng)





if __name__=="__main__":
    secret_images()
