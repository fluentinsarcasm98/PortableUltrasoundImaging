from time import sleep
import pigpio

DIR = 20     # Direction GPIO Pin
STEP = 21    # Step GPIO Pin
#SWITCH = 16  # GPIO pin of switch
CW = 1
CCW = 0
# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
#pi.set_mode(SWITCH, pigpio.INPUT)
#pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

MODE = (14, 15)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0),
              'Half': (1, 0),
              '1/4': (0, 1), # Floating, Low
              '1/8': (0, 1),
              '1/16': (1, 1),
              '1/32': (1, 1)} #Floating, High

for i in range(3):
    pi.write(MODE[i], RESOLUTION['1/16'][i])

# Set duty cycle and frequency
pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second
# pi.hardware_PWM(18, frequency, duty_cycle)
try:
    while True:
        pi.write(DIR, 1)  # Set direction
        sleep(.1)

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    pi.set_PWM_dutycycle(STEP, 0)  # PWM off
    pi.stop()
