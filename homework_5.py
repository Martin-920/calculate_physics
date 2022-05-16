#最陡下降优化
import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
def fxy(x,y):
    return x**2 +y**2

x=10
y=10#初始位置
dstep=0.01
xx=[]
yy=[]
for i in np.arange(0, 1000):
    dfdx = 2 * x
    dfdy = 2 * y   # 梯度
    dx = dstep * dfdx  # 搜索步长 x
    dy = dstep * dfdy  # 搜索步长 y
    x = x - dx  # 更新x
    y = y - dy  # 更新y
    xx.append(x)
    yy.append(y)
    if abs(dx) < 1.0e-6 and abs(dy) < 1.0e-6:
        print(x, y)
        break
zz=[]
for i in xx:
    j=0
    zb = fxy(i,yy[j])
    zz.append(zb)
    j+=1
fig = Axes3D(pl.figure())
xp = np.linspace(-10, 10, 100)
yp = np.linspace(-10, 10, 100)
xp, yp = np.meshgrid(xp, yp)
zp = fxy(xp, yp)
fig.plot_surface(xp, yp, zp, rstride=1, cstride=1, cmap=pl.get_cmap('rainbow'))
fig.plot(xx,yy,zz,"ko")
fig.plot(xx,yy,"k")
pl.show()