import time
import Rpi.GPIO as GPIO
#import pigpio

DIR = 20 # direction pin on the RPi is pin 20
STEP = 21  # step pin on Rpi
# GPIO 18 PWM0 gen
# PWM 13/19
CW = 1 # clockwise dir
CCW = 0 # counterclockwise dir
SPR = 200 # steps per revolution (360/1.8) where 1.8deg is the step size for full steps

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

MODE = (14, 15) # M0, M1
GPIO.setup(MODE, GPIO.out)
RESOLUTION = {'Full': (0, 0),
              'Half': (1, 0),
              '1/4': (0, 1), # Floating, Low
              '1/8': (0, 1),
              '1/16': (1, 1),
              '1/32': (1, 1)} #Floating, High
step_count = SPR*16
delay = 0.005/16 # 1 second/ SPR = 1/200

GPIO.output(MODE, RESOLUTION['1/16'])
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
