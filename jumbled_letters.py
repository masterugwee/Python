count = int(input())
list = []
for j in range(count):
    list.append(input())
for i in range(len(list)):
    s = "".join(list[i])
    s = s.replace(" ", "")
    even = []
    odd = []
    for j in range(len(s)):
        if(j%2!=0):
          even.append(s[j])
        else:
            odd.append((s[j]))
    even.reverse()
    final = "".join(even)
    finalodd = "".join(odd)
    print(finalodd+final)
