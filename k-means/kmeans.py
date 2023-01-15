import numpy as np
import matplotlib.pyplot as plt


def data():
    pots = np.zeros([100,2],dtype=np.float64)
    c0x = 0.5
    c0y = 0.3
    
    c1x = 0.3
    c1y = 0.7

    for i in range(50):
        x = c0x-np.random.random([1])[0]*0.1
        y = c0y-np.random.random([1])[0]*0.1
        pots[i,:] = [x,y]

    for i in range(50,100):
        x = c1x-np.random.random([1])[0]*0.1
        y = c1y-np.random.random([1])[0]*0.1
        pots[i,:] = [x,y]
    return pots

data = data()

x0 = 0.1
y0 = 0.5
x1 = 0.2
y1 = 0.3

def distance(p0,p1):
    return (p0[0]-p1[0])*(p0[0]-p1[0]) + (p0[1]-p1[1])*(p0[1]-p1[1])
for i in range (10):
    plt.plot([x0,x1],[y0,y1],'ro')
    plt.plot(data[:,0], data[:,1],'bo')
    plt.show()

    num0 = 0.0
    num1 = 0.0

    tmpx0 = 0.0
    tmpy0 = 0.0
    tmpx1 = 0.0
    tmpy1 = 0.0
    for j in range(100):
        d0 = distance(data[j,:],[x0,y0])
        d1 = distance(data[j,:],[x1,y1])
        print(d0,d1)
        if d0 > d1:
            print("d0")
            num1+=1
            tmpx1 += data[j,0]
            tmpy1 += data[j,1]
        else:
            print("d1")
            num0+=1
            tmpx0 += data[j,0]
            tmpy0 += data[j,1]
    x0 = tmpx0/num0
    y0 = tmpy0/num0
    x1 = tmpx1/num1
    y1 = tmpy1/num1