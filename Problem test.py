import sys

sys.setrecursionlimit(100000)
x = 0
y= 0
sum = x+y
safeset =set() #this is the set of walkable coridantes
treeset = set() #coridantes where there are trees

#d is down u is up l is left and r is right

def sum_check (x,y): # this checks to see if the space is a tree or not
    xstr = x
    ystr = y
    if (x<0): #makes absolute value
        xstr = x*-1
    if (y<0):
        ystr = y*-1
    i=0
    sx = str(xstr)
    sy = str(ystr)
    sum =0
    while i < len(sx): #adds up the sum of the digits for x
        string_store = sx[i]
        x1 = abs(int (string_store))
        sum = sum + x1
        i += 1
    i=0
    while i < len(sy): #adds up the sum of the digits for y
        string_store = sy[i]
        y1 = abs(int (string_store))
        sum = sum + y1
        i += 1
    if (sum<=21): #checks if coridantes are safe and adds them if they are
        safeset.add((x,y))
        return True

    else: # adds coridantes to treeset if they are trees
        treeset.add((x,y))
        return False

def check(x,y,safeset): #this checks if the space has already been checked before
    if (x,y) in safeset:
        return False
    else:
        return True

def move (x,y,count): #the recursive function to move
    count+=1
    print (count)
    if check(x, y + 1, safeset) is True and sum_check(x,y+1) is True : #this checks if the space above has already been checked and if there is a tree there
        count = move (x,y + 1,count) #if there is no tree and the space has not been checked then the program moves forward and starts recursion
    if check(x + 1, y, safeset) is True  and sum_check(x+1,y) is True :# same going right
        count = move (x + 1,y,count)
    if check(x - 1, y, safeset) is True  and sum_check(x-1,y) is True: # same going left
        count = move (x - 1,y,count)
    if check(x, y - 1, safeset) is True and sum_check(x,y-1) is True: #same going down
        count = move (x,y - 1,count)
    return count

print (move(0,0,0))

 #initializes the function
