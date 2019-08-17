#The list is stored as key:Value pair. The student wwith the highest mark comes first and goes in desc order.
def stud_list():
  dicts = {"Caleb":2, "Joe":78, "Garry": 35, "Tyson":13 , "Ray":3 , "Derek": 34, "Draco":90}
  ref = dicts.keys()
  vallist = []
  keylist = []
  sorte = sorted(dicts, key=dicts.get, reverse=True)
  for x in sorte:
    vallist.append(dicts[x])
  for y in ref:
      keylist.append(y)
  newdic = dict(zip(keylist,vallist))
  print(newdic)
if __name__=="__main__":
    stud_list()
