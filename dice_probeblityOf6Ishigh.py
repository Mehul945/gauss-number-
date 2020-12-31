import random
g=random.choice([1,2,3,4,5,6,6,6,6,6,6,6])
while 1:
    a=int(input("gause number betwin 1 to 6 : "))
    if a==g:
        print("You gause correctly")
        break
    elif a<g:
        print("You gause very low number ")
    elif a>g:
        print("You gause very high number ")
