mult = 1
count = 8
while mult <= count:
    print (" " * (count - mult) + "*" * mult + "*" * (mult - 1))
    mult = mult + 1

mult = 1
count = 8
while mult <= count:
    print (" " * (count - mult) + "*" * mult)
    mult = mult + 1

mult = 1
count = 8
while mult <= count:
    print ("*" * mult)
    mult = mult + 1

sym = "*"
mult = 1
count = 8
while mult < count:
    print (" " * (count-mult) + (sym * mult) + (sym * (mult - 1)))
    mult +=1
mult -=2
while mult >=1:
    print (" " * (count - mult) + (sym * mult) + (sym * (mult - 1)))
    mult -=1

