import numpy as np
import datetime
import matplotlib.pyplot as plt
#from scipy import signal
#from scipy.interpolate import griddata
import math
#from scipy.signal import decimate, convolve
import json 
import re
import glob, os
from time import sleep
filz = np.load("20201120141130.npz")
imagedata = filz.files
def CreateSC(RawImgData):
    LenLinesC = len(filz["signal"])
    nblines = filz["nblines"]
    #NbLinesC = nblines.shape
    #print("nblines:\n ",NbLinesC)
    NbLinesC = 128

    print (LenLinesC,NbLinesC)
    SC = np.zeros((LenLinesC,LenLinesC))+200
    SC += 1
    maxAngle = 60.0
    step = maxAngle/(NbLinesC+1)
    CosAngle = math.cos(math.radians(30))
    Limit = LenLinesC*CosAngle

    points = []
    values = []

    for i in range(LenLinesC):
        for j in range(LenLinesC):
            if (  (j > LenLinesC/2 + i/(2*CosAngle)) or  (j < LenLinesC/2 - i/(2*CosAngle)) ):
                SC[i][j] = 0
                points.append([i,j])
                values.append(0)
            if (  (i > Limit) ):
                if ( (i**2 + (j-LenLinesC/2) ** 2) > LenLinesC**2):
                    SC[i][j] = 0
                    points.append([i,j])
                    values.append(0)
    for i in range(NbLinesC):
        PointAngle = i*step-30
        COS = math.cos(math.radians(PointAngle))
        SIN = math.sin(math.radians(PointAngle))
        for j in range(LenLinesC):

            X = (int)( j*COS)
            Y = (int)(LenLinesC/2 - j*SIN)
            SC[X][Y] = RawImageData[i][j]
            points.append([X,Y])
            values.append([i][j])

    values = np.array(values,dtype=np.float)



    return SC,values,points,LenLinesC


SCH,valuesH,pointsH,LenLinesCH = CreateSC(filz)
grid_xH, grid_yH = np.mgrid[0:LenLinesCH:1, 0:LenLinesCH:1]
grid_z1H = griddata(pointsH, valuesH, (grid_xH, grid_yH), method='linear')
plt.figure(figsize=(10,10))
plt.imshow(((grid_z1H+0.01)**0.5),cmap=plt.get_cmap('gray'))
plt.title("Getting the image out of the acquisition file")
plt.savefig("/SCImage.jpg", bbox_inches='tight')
plt.show()
