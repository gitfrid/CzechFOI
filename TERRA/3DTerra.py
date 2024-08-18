#https://stackoverflow.com/questions/55015639/how-to-plot-3-arrays-as-a-surface-plot-in-python



import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy.random import randn
#from scipy import array, newaxis

chunk  = np.loadtxt(r"C:\cov\Czech\Vesely\TERRA\TERRA_VX_UNVX.csv",comments='#',delimiter=',',skiprows=1)
#chunk  = np.loadtxt(r"C:\cov\Czech\Vesely\TERRA\TERRA_VX.csv",comments='#',delimiter=',',skiprows=1)
#chunk  = np.loadtxt(r"C:\cov\Czech\Vesely\TERRA\TERRA_UNVX.csv",comments='#',delimiter=',',skiprows=1)
DATA=np.array(chunk)
Ys = DATA[:,0]
Xs = DATA[:,1]
Zs = DATA[:,2]
VD1 =DATA[:,3]
#Xs = np.genfromtxt(r"C:\cov\Czech\Vesely\UVX_D1\UVX_D1_X.csv", delimiter=',', unpack=True, skip_header=1)
#Ys = np.genfromtxt(r"C:\cov\Czech\Vesely\UVX_D1\UVX_D1_Y.csv", delimiter=',', unpack=True, skip_header=1)
#Zs = np.genfromtxt(r"C:\cov\Czech\Vesely\UVX_D1\UVX_D1_Z.csv", delimiter=',', unpack=True, skip_header=1)
#VD1 = np.genfromtxt(r"C:\cov\Czech\Vesely\UVX_D1\UVX_D1_VD1.csv", delimiter=',', unpack=True, skip_header=1)


#fig = plt.figure()
fig = plt.figure(figsize=(16,10))
ax = fig.add_subplot(111, projection='3d')
ax = fig.add_axes([-0.005, -0.01, 1.05, 1.05], projection='3d')  # (left, bottom, width, height)
ax.set_axis_off()  # hide axis

ax.set_xlabel('Day of Death from 2020-01-01', fontsize=9)
ax.set_ylabel('Age of Death', fontsize=9)
ax.set_zlabel('Number of Deaths', fontsize=9)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)


#cmap=cm.coolwarm cmap=cm.jet cmap=cm.hsv_r cm.coolwarm cmap=cm.YlOrRd_r

#colmap = cm.ScalarMappable(cmap=cm.hsv)
#colmap.set_array(Zs)
#C=cm.hsv(Zs/max(Zs))

surf = ax.plot_trisurf(Xs, Ys, Zs,cmap=cm.hsv, linewidth=0)
fig.colorbar(surf)

ax.xaxis.set_major_locator(MaxNLocator(5))
ax.yaxis.set_major_locator(MaxNLocator(6))
ax.zaxis.set_major_locator(MaxNLocator(5))

fig.tight_layout()

#maximize screen
plt.get_current_fig_manager().window.state('normal')  #method works for Tk backend (default)
ax.set_axis_on()

plt.show()
"""
# Rotate the axes and update
for angle in range(0, 360*4 + 1,15):
    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180

    # Cycle through a full rotation of elevation, then azimuth, roll, and all
    elev = azim = roll = 0
    if angle <= 360:
        elev = angle_norm
    elif angle <= 360*2:
        azim = angle_norm
    elif angle <= 360*3:
        roll = angle_norm
    else:
        elev = azim = roll = angle_norm

    # Update the axis view and title
    ax.view_init(elev, azim, roll)
    #plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll),fontsize=10)

    plt.draw()
    plt.pause(1.0)
 """