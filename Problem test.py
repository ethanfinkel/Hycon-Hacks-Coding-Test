import sys

sys.setrecursionlimit(100000)
x = 0
y= 0
sum = x+y
safeset =set()
treeset = set()

#d is down u is up l is left and r is right

def sum_check (x,y):
    xstr = x
    ystr = y
    if (x<0):
        xstr = x*-1
    if (y<0):
        ystr = y*-1
    i=0
    sx = str(xstr)
    sy = str(ystr)
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
        treeset.add((x,y))
        return False

def check(x,y,safeset):
    if (x,y) in safeset:
        return False
    else:
        return True


def move (x,y,count):
    print (count)
    print (x,y)
    if check(x, y + 1, safeset) is True and sum_check(x,y+1) is True :
        count +=1
        print ("f")
        move (x,y + 1,count)
    if check(x + 1, y, safeset) is True  and sum_check(x+1,y) is True :
        count +=1
        print ("r")
        move (x + 1,y,count)
    if check(x - 1, y, safeset) is True  and sum_check(x-1,y) is True:
        count +=1
        print ("l")
        move (x - 1,y,count)
    if check(x, y - 1, safeset) is True and sum_check(x,y-1) is True:
        count +=1
        print ("d")
        move (x,y - 1,count)



move (0,0,1)
