x = 0
y= 0
sum = x+y
safex =[]
safey =[]
treex = []
treey =[]

def sum_check (x,y):
    i=0
    sx = str(x)
    sy = str(y)
    sum =0
    while i < len(sx):
        string_store = sx[i]
        x1 = int (string_store)
        sum = sum + x1
        i += 1
    i=0
    while i < len(sy):
        string_store = sy[i]
        y1 = int (string_store)
        sum = sum + y1
        i += 1
    if (sum<=21):
        safex.append(x)
        safey.append(y)

    else:
        return False

for x in range (90,105):
    for y in range (90,105):
        sum_check(x,y)

print (safex[0],safey[0])
