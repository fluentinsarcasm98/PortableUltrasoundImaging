import numpy as np
import matplotlib.pyplot as plt
# For the scan conversion part
import math
from scipy import signal
from scipy.interpolate import griddata
from scipy.signal import decimate, convolve

# This dataset contains 1000 lines and 5000 pts per line
# sampling speed= 10.6MHz
rf_raw = np.load("tableDataRaw.npz")["tableDataRaw"]
rf_fil = np.load("tableDataFiltered.npz")["tableDataFiltered"]
rf_env = np.load("tableDataH.npz")["tableDataH"]
t = np.load("t.npz")["t"]
np.shape(rf_env)

# Plotting raw vs filtered vs enveloped data

plt.figure(figsize=(15,5))
plt.plot(t[0:3000],rf_raw[110][0:3000],"y", label='Raw signal')
plt.plot(t[0:3000],rf_fil[110][0:3000],"r", label='Filtered signal')
plt.plot(t[0:3000],rf_env[110][0:3000],"b", label='Envelope of the signal')
plt.title("Details of a line")
plt.xlabel("Time in uS")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.savefig("signals_on_one_line.jpg", bbox_inches='tight') 
plt.show()

# the enveloped data will be used for B-mode image
Val = np.average(rf_env) 
Offset = 400 #This is the initial offset. 400 pixels is approx 40 us. We're sortof discarding that to get to the good stuff.
MinTable = 10*np.min(rf_env)
Zeroes = np.zeros((1000,Offset))+Val
BigTable = []
BigTable = np.append(Zeroes, rf_env, axis=1)

#Plotting the table data as an image
IndexLine = 110
plt.figure(figsize=(15,15))
tableData = BigTable[:,:3000+Offset] # important var; used everywhere
plt.imshow((abs(tableData)**0.7), aspect='auto',cmap=plt.get_cmap('gray'))
plt.axhline(IndexLine, color='r', linestyle='--')
plt.title("Mapping the data from the source file.")   
plt.savefig("grayscale_of_data_unmodified.jpg", bbox_inches='tight') 
plt.show()

# The grayscale plot above shows that there are needles in 3 rows on the phantom. So now we separate these three frames so that we can optimize them separately
ListOfPoints= [105, 420, 740] # this was eye-balled from the grayscale that we got above. This is where we seem to have a bunch of white data dots

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))

TmpImg = (abs(tableData[ListOfPoints[0]-100:ListOfPoints[0]+150]))**(1.1)
ax1.imshow(TmpImg,cmap=plt.get_cmap('gray'), aspect='auto')
ax1.axhline(100, color='r', linestyle='--')
TmpImg = (abs(tableData[ListOfPoints[1]-100:ListOfPoints[1]+150]))**(1.1)
ax2.imshow(TmpImg,cmap=plt.get_cmap('gray'), aspect='auto')
ax2.axhline(100, color='r', linestyle='--')
TmpImg = (abs(tableData[ListOfPoints[2]-100:ListOfPoints[2]+150]))**(1.1)
ax3.imshow(TmpImg,cmap=plt.get_cmap('gray'), aspect='auto')
ax3.axhline(100, color='r', linestyle='--')
plt.suptitle('Three images from the initial grayscale')
plt.savefig("grayscale_separated_smallImages.jpg", bbox_inches='tight') 
plt.show()

#This process will reduce the number of points we have to sample. Official terms are Decimating or Downsampling. To do: Understand the concept behind it. Just using an in built function from the scipy library right now.
DecImg = []
for i in range(150):
    tmp = decimate(tableData[ListOfPoints[0]-70+i], 5, ftype='fir')
    tmp += decimate(tableData[ListOfPoints[1]-70+i], 5, ftype='fir')
    tmp += decimate(tableData[ListOfPoints[2]-70+i], 5, ftype='fir')
    DecImg.append(tmp)
SmallImg = []
for i in range(int(len(DecImg)/2)):
    SmallImg.append((DecImg[2*i]+DecImg[2*i+1])/2)

plt.axhline(IndexLine/2, color='r', linestyle='--')

#The **0.7 in line below is used to flatten the image, easier on the human eyes. Luc believes so and so do I
plt.imshow(np.asarray(SmallImg)**(0.7),cmap=plt.get_cmap('gray'), aspect='auto')
plt.suptitle('Downsampled image - appended')
plt.savefig("downsampled_image.jpg", bbox_inches='tight') 
plt.show()

# Scan conversion function to make this flat image conical so that it aligns with what the phantom looks like
def CreateSC(RawImgData):
    LenLinesC = np.shape(RawImgData)[1]
    NbLinesC = np.shape(RawImgData)[0]
    SC = np.zeros((LenLinesC,LenLinesC))+Val
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
            SC[X][Y] = RawImgData[i][j]
            points.append([X,Y])
            values.append(RawImgData[i][j])

    values = np.array(values,dtype=np.int)

    return SC,values,points,LenLinesC

# using this function on our data to get a linear grid
SCH,valuesH,pointsH,LenLinesCH = CreateSC(SmallImg)
grid_xH, grid_yH = np.mgrid[0:LenLinesCH:1, 0:LenLinesCH:1]
grid_z1H = griddata(pointsH, valuesH, (grid_xH, grid_yH), method='linear')

plt.figure(figsize=(15,5))
plt.imshow((grid_z1H**0.7),cmap=plt.get_cmap('gray'))
plt.title("Getting the conical image from the dataset")
plt.savefig("scan_converted.jpg", bbox_inches='tight')
plt.show()


