x = 0
y= 0
sum = x+y
safex =[]
safey =[]
treex = []
treey =[]

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

    else:
        treex.append(x)
        treey.append(y)

for x in range (-105,10):
    for y in range (-105,10):
        sum_check(x,y)

for z in range (0,10):
    print (treex[z],treey[z],safex[z],safey[z])
