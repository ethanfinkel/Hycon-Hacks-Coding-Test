x = 0
y= 0
sum = x+y
safex =[]
safey =[]
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
        safex.append(x)
        safey.append(y)
        return True

    else:
        treex.append(x)
        treey.append(y)
        return False


def move (x,y,count):
    if sum_check(x,y+1) is True:
        count +=1
        y +=1
        move (x,y,count)
    else:
        if sum_check(x+1,y) is True:
            count +=1
            x+= 1
            move (x,y,count)
            print (count)
        else:
            if sum_check(x-1,y) is True:
                count +=1
                x = x-1
                move (x,y,count)
            else:
                if sum_check(x,y-1) is True:
                    count +=1
                    y = y-1
                    move (x,y,count)

move (0,0,1)



for z in range (0,len(treex)):
    print (treex[z],treey[z],safex[z],safey[z])
