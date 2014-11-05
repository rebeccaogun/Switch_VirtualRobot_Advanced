import random
from Tkinter import *
window = Tk()
canvas = Canvas(window, width=800, height=600, bg='#cecece')
canvas.pack()

n = raw_input('Number of obstacles: ')
n = int(n)
cn = int(n)

fx=[]
sx=[]
fy=[]
sy=[]
obj=[]

for i in range(n+1):
    fx.append(0)
    sx.append(0)
    fy.append(0)
    sy.append(0)
    obj.append(0)

i = 1

while int(i) <= int(n):
    size = random.randrange(1,4)
    if size == 1:
        x1 = random.randrange(21, 759)
        y1 = random.randrange(21, 559)
        x2 = x1+20
        y2 = y1+20
        t = 1
        k = 1
        while t == 1 and int(k) < int(i):
            if ((x1 <= (sx[k]+20) and x1 > (fx[k]-40)) and (y1 < (sy[k]+20) and y1 > fy[k]-40)):
                t = 0
            k = k + 1
        if t == 1:
            fx[int(i)]=x1
            sx[int(i)]=x2
            fy[int(i)]=y1
            sy[int(i)]=y2
            obj[int(i)]=1
            i = i+1

    if size == 2:
        x1 = random.randrange(21, 759)
        y1 = random.randrange(21, 559)
        x2 = x1+30
        y2 = y1+30
        t = 1
        k = 1
        while t == 1 and int(k) < int(i):
            if ((x1 <= (sx[k]+30) and x1 > (fx[k]-50)) and (y1 < (sy[k]+30) and y1 > fy[k]-50)):
                t = 0
            k = k + 1
        if t == 1:
            fx[int(i)]=x1
            sx[int(i)]=x2
            fy[int(i)]=y1
            sy[int(i)]=y2
            obj[int(i)]=2
            i = i+1

    if size == 3:
        x1 = random.randrange(21, 759)
        y1 = random.randrange(21, 559)
        x2 = x1+40
        y2 = y1+40
        t = 1
        k = 1
        while t == 1 and int(k) < int(i):
            if ((x1 <= (sx[k]+40) and x1 > (fx[k]-60)) and (y1 < (sy[k]+40) and y1 > fy[k]-60)):
                t = 0
            k = k + 1
        if t == 1:
            fx[int(i)]=x1
            sx[int(i)]=x2
            fy[int(i)]=y1
            sy[int(i)]=y2
            obj[int(i)]=3
            i = i+1

print fx
print sx
print fy
print sy
for i in range(1,int(cn)+1):
    if obj[int(i)] == 1:
        obs = canvas.create_rectangle(fx[int(i)], fy[int(i)], sx[int(i)], sy[int(i)], outline='blue', fill='blue')

    if obj[int(i)] == 2:
        obs = canvas.create_rectangle(fx[int(i)], fy[int(i)], sx[int(i)], sy[int(i)], outline='orange', fill='orange')

    if obj[int(i)] == 3:
        obs = canvas.create_rectangle(fx[int(i)], fy[int(i)], sx[int(i)], sy[int(i)], outline='green', fill='green')
        
window.mainloop()


