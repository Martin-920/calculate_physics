import numpy as np
import pylab as pl

x_step=50
y_step=50
t_step=100 #时间步数
dx=0.2
dy=0.2
dt=0.01
A=1.0
U=np.zeros((t_step+1,x_step+1,y_step+1))
#边界条件
for k in range(t_step):
    for j in range(y_step):
        U[k,j,-1] = -1.0 + np.sin(0.5*(j-50)/np.pi)
        U[k,j,0] = 1.0 + 0.5*np.sin((j-50)/np.pi)
        U[k,-1,j] = 1.0 + 0.5 * np.sin((j - 50) / np.pi)
        U[k,0,j] = -1.0 + np.sin(0.5 * (50 - j) / np.pi)
for k in range(t_step):
    for i in range(1,x_step):
        for j in range(1,y_step):
            U[k+1,i,j] = dt*((U[k,i-1,j]-2*U[k,i,j]+U[k,i+1,j])/dx**2 + \
            (U[k,i,j-1]-2*U[k,i,j]+U[k,i,j+1])/dy**2)+ \
            U[k,i,j]

    #print(U)
fig = pl.figure(figsize=(10,10))
ax1 =fig.add_subplot(2,2,1)
ax2 =fig.add_subplot(2,2,2)
ax3 =fig.add_subplot(2,2,3)
ax4 =fig.add_subplot(2,2,4)
extent = [0,(x_step+1)*dx,0,(y_step+1)*dy]
cs1 = ax1.contourf(U[10,:,:],origin='lower',extent=extent,cmap=pl.cm.hot)
cs2 = ax2.contourf(U[40,:,:],origin='lower',extent=extent,cmap=pl.cm.hot)
cs3 = ax3.contourf(U[80,:,:],origin='lower',extent=extent,cmap=pl.cm.hot)
cs4 = ax4.contourf(U[100,:,:],origin='lower',extent=extent,cmap=pl.cm.hot)
ax1.set_ylabel(r'Y', fontsize=15)
ax3.set_xlabel(r'X', fontsize=15)
ax3.set_ylabel(r'Y', fontsize=15)
ax4.set_xlabel(r'X', fontsize=15)
ax1.set_title('t=10')
ax2.set_title('t=40')
ax3.set_title('t=80')
ax4.set_title('t=100')
pl.show()
#再画一幅三维的
x = np.arange(0,1.02,0.02)
y = np.arange(0,1.02,0.02)
xx, yy = np.meshgrid(x, y)
fig = pl.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xx, yy,U[80,:,:], cmap=pl.get_cmap('hot'))
fig.colorbar(surf, shrink=0.5)
ax.set_xlim3d(0, 1.0)
ax.set_ylim3d(0, 1.0)
ax.set_zlim3d(-2, 2.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
pl.show()
