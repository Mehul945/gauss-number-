# special-dice
import random
g=random.randint(1,10)
while 1:
    a=int(input("gause number betwin 1 to 10 : "))
    if a==g:
        print("You gause correctly")
        break
    elif a<g:
        print("You gause very low number ")
    elif a>g:
        print("You gause very high number ")
