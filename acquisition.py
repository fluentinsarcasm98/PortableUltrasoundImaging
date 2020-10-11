import spidev
import Rpi.GPIO
import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
import jsonimport time
from unorickDriver import *

### INITIALIZATION ###
GPIO.setwarnings(False)
x = us_spi()
x.init()
# NEED TO WRITE THIS FUNCTION IN DRIVER
x.fpga_initial_config() #default params from config(). 


### PARAMETER SPECIFICATIONS ###
#path parameters that are coming from the JSON file
filename_parameters = str("parameters.json")
with open(filename_parameters, 'r') as json_file:
    data = json.load(json_file)

Experiment_Name = data["ExperimentName"]
tgcValue= int(data["acqParameters"]["tgcValue"])
tgcCurve= int(data["acqParameters"]["tgcBool"])
tgcCurveI= int(data["acqParameters"]["tgcCurveI"])
tgcCurveF= int(data["acqParameters"]["tgcCurveF"])


#timings
t1= int(data["pulseTrain"]["t1"]) # pulse duration
t2= int(data["pulseTrain"]["t2"]) # delay time until damping
t3= int(data["pulseTrain"]["t3"]) # damping time
t4= int(data["pulseTrain"]["t4"]) # delay time until acquisition starts
t5= int(data["pulseTrain"]["t5"]) # acquisition length

# other parameters
V_pp = int(data["acqParameters"]["Vpp"]) # 24V, 48V, 72V

# motor rotation
number_rot = int(data["acqRoutine"]["rotNumber"])

#number of rotations
steps_rot = int(data["acqRoutine"]["rotSteps"]) #motor steps per rot, 1 step = 0.704 degrees

#___lines and sampling params___
multilines = 0  #0: one line, 1: more lines
f = int(dta["acqParameters"]["f"]) # frequency of ADC sampling
n = 1 # number of lines

### FPGA SET UP ###
x.set_tgc_constant(tgcValue) # tgc constant
x.create_tgc_curve(tgcCurveI, tgcCurveF, tgcCurve) # tgc curve
x.set_multi_lines(multilines)
x.set_msps(f) # ADC sampling frequency
x.set_acquisition_number_lines(n) # number of lines
x.set_timings(t1, t2, t3, t4, t5) # set the pulse train 
#---> write this function below
x.updateNacq #to update the number of data points to acquire


### ACQUISITION AND ROTATION ###

# acquire the signal, readout the data, rotate, and repeat
for data_reg in range(0, 2*number_rot, 2):
    print("Line # " +str(data_reg)) # debugging help
    x.do_acquisition()
    #---> write this function below
    x.do_readout(data_reg) # reads the data from the board
    x.rotate(steps_rot, -1) # steps_rot = steps, direction: +1 or -1 for ccw or cw rotation

# rotate 1 step back
x.rotate(5, -1)
x.rotate(6, 1)

# acquire the signal, readout the data, rotate, and repeat
for data_reg in range(2*number_rot-1, -1, -2):
    print("Line # " +str(data_reg)) # debugging help
    x.do_acquisition()
    #---> write this function below
    x.do_readout(data_reg) # reads the data from the board
    x.rotate(steps_rot, 1) # steps_rot = steps, direction: +1 or -1 for ccw or cw rotation

# rotate back
x.rotate(5, 1)
x.rotate(6, -1)

### PROCESSING HEX DATA TO RAW DATA ###
path = "acquired_data"
#---> write this function below
x.do_export(path) # saving signal to json file
    