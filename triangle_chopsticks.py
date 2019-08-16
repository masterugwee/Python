# We have the three inputs val will be the round. String will store each 3 spaced values .  We will have one more variable with count of the chopsticks in the jar.
# Last String will have that many chopsticks. We need to check how many triangles can be formed, and who will win in each case.
val = int(input())  # First input.
counter = 0
for i in range(val):
    abr = input()  # String to store a , b and r.
    numchopstick = int(input())
    lengthchop = input()
    a, b, r = abr.split()
    sum = int(a) + int(b)
    list = lengthchop.split()
    if numchopstick == len(list):
     for j, last_side in enumerate(list):
        if (sum > int(last_side)):
            counter = counter + 1
     if (counter > int(r)):
        print(counter)
        print("Natsu")
     else:
        print(r)
        print("Grey")
    else:
      raise IOError("Chopstick count is wrong")
