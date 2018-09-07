x = 0
y= 0
sum = x+y
safeset =set ()
treex = []
treey =[]

#d is down u is up l is left and r is right

def sum_check (x,y):
    if (x<0):
        x = x*-1
    if (y<0):
        y=y*-1
    i=0
    sx = str(x)
    sy = str(y)
    sum =0
    while i < len(sx):
        string_store = sx[i]
        x1 = abs(int (string_store))
        sum = sum + x1
        i += 1
    i=0
    while i < len(sy):
        string_store = sy[i]
        y1 = abs(int (string_store))
        sum = sum + y1
        i += 1
    if (sum<=21):
        safeset.add((x,y))

        return True

    else:
        treex.append(x)
        treey.append(y)
        return False

def check(x,y,safeset):
    if (x,y) in safeset:
        return False
    else:
        return True


def move (x,y,count):
    print (count)
    if sum_check(x,y+1) is True and check(x,y,safeset) is True:
        count +=1
        y +=1
        print ("f")
        move (x,y,count)
    else:
        if sum_check(x+1,y) is True and check(x,y,safeset) is True:
            count +=1
            x+= 1
            print ("r")
            move (x,y,count)
        else:
            if sum_check(x-1,y) is True and check(x,y,safeset) is True:
                count +=1
                x = x-1
                print ("l")
                move (x,y,count)
            else:
                if sum_check(x,y-1) is True and check(x,y,safeset) is True:
                    count +=1
                    y = y-1
                    print ("d")
                    move (x,y,count)


move (0,0,1)



for z in range (0,len(treex)):
    print (treex[z],treey[z],safeset[z])
