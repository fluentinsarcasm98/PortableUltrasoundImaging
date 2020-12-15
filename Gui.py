from tkinter import * 
import os

def save_info():
    exp_name = name.get()
#     initial_value = initial.get()
#     final_value = final.get()
#     adc_freq = adc.get()
#     pulse_peak = pulse.get()
#     timing_1 = t1.get()
#     timing_2 = t2.get()
#     timing_3 = t3.get()
#     timing_4 = t4.get()
#     timing_5 = t5.get()
#     num_rotate = rotate.get()
#     motor_steps = motor.get()
#     ip_add = ip.get()
#     port_num = port.get()
    
#     print(exp_name,initial_value, final_value, adc_freq, pulse_peak, timing_1, timing_2, timing_3, timing_4, timing_5, num_rotate, motor_steps, id_add, port_num)
    
    print(exp_name)
    file = open("paramaters.json","w")
    
    file.write("Patient Name: " + exp_name)
    file.write("\n")
    
#     file.write("TGC Initial Value: " + str(initial_value))
#     file.write("\n")
    
#     file.write("Final TGC Value:" +str(final_value))
#     file.write("\n")
    
#     file.write("ADC Sampling Frequency: " + str(adc_freq))
#     file.write("\n")
    
#     file.write("Pulse Peak to Peak Voltage: " + str(pulse_peak))
#     file.write("\n")

#     file.write("T1: " + str(timing_1))
#     file.write("\n")

#     file.write("T2: " + str(timing_2))
#     file.write("\n")

#     file.write("T3: " + str(timing_3))
#     file.write("\n")

#     file.write("T4: " + str(timing_4))
#     file.write("\n")

#     file.write("T5: " + str(timing_4))
#     file.write("\n")

#     file.write("Number of Rotations: " + str(num_rotate))
#     file.write("\n")

#     file.write("Motor Steps Per Rotation: " + str(motor_steps))
#     file.write("\n")

#     file.write("IP Address: " + ip_add)
#     file.write("\n")

#     file.write("Port: " + str(port_num))
#     file.write("\n")
    
    file.close()
    
    

root = Tk()

root.geometry("600x800")

root.title("Ultrasound Settings")
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)


#for line in range(800):
#    myList.insert(END,"")
#    myList.pack()
#    scroll.config(command=myList.yview)


#heading = Label(text="Python File Handling in Forms",fg="black",bg="yellow",width="500",height="3",font="10")

#heading.pack()

name_text = Label(text='Experiment Name :', font='bold')
# tgc_text = Label(text="Time Gain Compensation(TGC)", font='bold')
# apply_text = Checkbutton(text="Apply TGC") #need to save check
# initial_text = Label(text='TGC Initial Value')
# value_text = Label(text='TGC Value')
# final_text = Label(text='Final TGC Value')
# acq_text = Label(text='Acquisition Parameters', font='bold')
# adc_text = Label(text='ADC Sampling Frequency')
# freq_text = Label(text='MHz')
# pulse_text = Label(text='Pulse Peak to Peak Voltage')
# volts_text = Label(text='V')
# timing_text = Label(text='Timing Pulse Train', font='bold')
# t1_text = Label(text='T1')
# t2_text = Label(text='T2')
# t3_text = Label(text='T3')
# t4_text = Label(text='T4')
# t5_text = Label(text='T5')
# routine_text = Label(text='Acquisition Routine', font='bold')
# rotate_text = Label(text='Number of Rotations')
# motor_text = Label(text='Motor Steps Per Rotation')
# web_text = Label(text='Web Socket Connection', font='bold')
# ip_text = Label(text='IP Address')
# port_text = Label(text='Port')
para_text = Label(text= 'Save parameters.json to:')
raw_text = Label(text='Save rawData.json to:') 

name_text.place(x=0,y=10)
# tgc_text.place(x=0,y=60)
# apply_text.place(x=15,y=85)
# initial_text.place(x=15,y=105)
# final_text.place(x=15, y=125)
# acq_text.place(x=0,y=175)
# adc_text.place(x=15,y=200)
# freq_text.place(x=205,y=200)
# pulse_text.place(x=15, y=220)
# volts_text.place(x=205,y=220)
# timing_text.place(x=0, y=270)
# t1_text.place(x=15, y=295)
# t2_text.place(x=90, y=295)
# t3_text.place(x=165, y=295)
# t4_text.place(x=240, y=295)
# t5_text.place(x=315, y=295)
# routine_text.place(x=0, y=345)
# rotate_text.place(x=15, y=370)
# motor_text.place(x=15, y=390)
# web_text.place(x=0, y=440)
# ip_text.place(x=15, y=465)
# port_text.place(x=15,y=490)
para_text.place(x=15, y=515)
raw_text.place(x=15, y=540)

#Add Post Signal Processing Things from Thesis Final Tab


name = StringVar()
# initial = IntVar()
# final = IntVar()
# adc = IntVar()
# pulse = IntVar()
# t1 = IntVar()
# t2 = IntVar()
# t3 = IntVar()
# t4 = IntVar()
# t5 = IntVar()
# rotate = IntVar()
# motor = IntVar()
# ip = StringVar()
# port = IntVar()

name_entry = Entry(textvariable=name,width="30")
initial_entry = Entry(textvariable=initial,width="5")
final_entry = Entry(textvariable=final,width="5")
# adc_entry = Entry(textvariable=adc, width="5")
# pulse_entry = Entry(textvariable=pulse, width="5")
# t1_entry = Entry(textvariable=t1, width="5")
# t2_entry = Entry(textvariable=t2, width="5")
# t3_entry = Entry(textvariable=t3, width="5")
# t4_entry = Entry(textvariable=t4, width="5")
# t5_entry = Entry(textvariable=t5, width="5")
# rotate_entry = Entry(textvariable=rotate, width="5")
# motor_entry = Entry(textvariable=motor, width="5")
# ip_entry = Entry(textvariable=ip, width="30")
# port_entry = Entry(textvariable=port, width="5")

name_entry.place(x=140,y=10)
initial_entry.place(x=140,y=105)
final_entry.place(x=140,y=125)
# adc_entry.place(x=170, y=200)
# pulse_entry.place(x=170, y=220)
# t1_entry.place(x=40, y=300)
# t2_entry.place(x=115, y=300)
# t3_entry.place(x=190, y=300)
# t4_entry.place(x=265, y=300)
# t5_entry.place(x=340, y=300)
# rotate_entry.place(x=155, y=370)
# motor_entry.place(x=155, y=390)
# ip_entry.place(x=140, y=465)
# port_entry.place(x=50, y=490)
def run_acq():
    os.startfile('path/to/file/test.py')

button = Button(root, text="Save Parameters", command=save_info, width="15", height="1")
start_button = Button(root, text='Start Acquisition', command=run_acq,  width="15", height="1", bg="grey")

button.place(x=15, y=600)
start_button.place(x=15, y=635)

mainloop()
