def leap_year(year):   print("Yes") if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))) else print("No")

if __name__=="__main__":
    x = int(input())
    leap_year(x)
