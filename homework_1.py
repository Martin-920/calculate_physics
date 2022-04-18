from matplotlib import pylab as pl
import numpy as np
###求一个带电量为Q，半径为1的薄圆盘在平面上的电势分布情况
###二重积分
###[KQ/(pi*R**2)]*1/(np.sqrt(x0-rcos)**2+(y0-rsin)**2)在[0,2pi],[0,1]的二重积分
def f(y0,x0,theta,r):
    cos=np.cos(theta)
    sin=np.sin(theta)
    return 1/(np.sqrt((x0-r*cos)**2+(y0-r*sin)**2))
N1=360
dtheta=2*3.14/N1
dthetas=np.arange(0,2*3.14,dtheta) #theta的积分区间
N2=100
dr=1/N2
drs=np.arange(0,1,dr) #r的积分区间
xaxis=np.arange(-5.0, 5.0, 0.2)
yaxis=np.arange(-5.0, 5.0, 0.2)
field=[]
for x0 in xaxis:
    for y0 in yaxis:
        v = 0.0
        for r in drs:
            vcircle=0.0
            for theta in dthetas:
                vcircle=vcircle+f(x0,y0,theta,r)*dtheta #一个圆环积分电势
            v=v+vcircle*dr
        field.append(v)
        print(v)
afield = np.array(field)
afield.shape = len(xaxis), len(yaxis)
afield_xy = afield.T
extent = [-5.0, 5.0, -5.0, 5.0]
fig = pl.figure(figsize=(9, 4))
ax1 = fig.add_subplot(1, 2, 1)
levels = np.arange(0.0, 5.0, 0.05)
cs = ax1.contour(afield_xy, levels, origin='lower', linewidths=2, extent=extent)
ax1.clabel(cs)
ax2 = fig.add_subplot(1, 2, 2)
cs = ax2.contourf(afield_xy, levels, origin='lower', extent=extent)
ax1.set_xlabel(r'X', fontsize=20)
ax1.set_ylabel(r'Y', fontsize=20)
ax2.set_xlabel(r'X', fontsize=20)
pl.show()