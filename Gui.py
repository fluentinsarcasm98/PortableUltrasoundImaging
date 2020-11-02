import tkinter as tk
from tkinter import ttk


form = tk.Tk()
form.title("Ultrasound Settings")
form.geometry("800x500")
bold = ("bold")

tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Parameters")
tab_parent.add(tab2, text="Web")
tab_parent.add(tab3, text="Processing")

# === WIDGETS FOR TAB ONE
exp = ttk.Label(tab1, text="Experiment Name:", font=bold)
tgc = ttk.Label(tab1, text="Time Gain Compensation(TGC)", font=bold)
apply_tgc = ttk.Checkbutton(tab1, text="Apply TGC")
initial_tgc = ttk.Label(tab1, text="TGC Initial Value:")
value_tgc = ttk.Label(tab1, text="TGC Value:")
final_tgc = ttk.Label(tab1, text="Final TGC Value:")

acq = ttk.Label(tab1, text="Acquisition Parameters", font=bold)
samplef = ttk.Label(tab1, text='ADC Sampling Frequency')
freqs = ttk.Combobox(tab1, values=["16", "18", "20"])
f = ttk.Label(tab1, text="MHz")

pulse_peak = ttk.Label(tab1, text='Pulse Peak-to-Peak Voltage')
voltages = ttk.Combobox(tab1, values=["60", "70", "80"])
v = ttk.Label(tab1, text="V")

timing = ttk.Label(tab1, text="Timing Pulse Train", font=bold)
t1 = ttk.Label(tab1, text="T1")
t2 = ttk.Label(tab1, text="T2")
t3 = ttk.Label(tab1, text="T3")

#freqs = ttk.Menu(tab1)
#freqs.add_command(label="16kHz")
#freqs.add_command(label="18kHz")
#freqs.add_command(label="20kHz")
#tab1.config(freqs=freqs)

routine = ttk.Label(tab1, text="Acquisition Routine", font=bold)
rnumber = ttk.Label(tab1, text="Number of Rotations")
msteps = ttk.Label(tab1, text="Motor Steps Per Rotation")
save = ttk.Label(tab1, text="Save All Parameters to Json File", font=bold)
json = ttk.Label(tab1, text="Save to:")

exp_entry = tk.Entry(tab1)
initial_entry = tk.Entry(tab1, width=5)
value_entry = tk.Entry(tab1, width=5)
final_entry = tk.Entry(tab1, width=5)
t1_entry = tk.Entry(tab1, width=5)
t2_entry = tk.Entry(tab1, width=5)
t3_entry = tk.Entry(tab1, width=5)
rnumber_entry = tk.Entry(tab1, width=5)
msteps_entry = tk.Entry(tab1, width=5)
json_entry = tk.Entry(tab1, width=30)


buttonBrowse = tk.Button(tab1, text="Browse")
buttonBack = tk.Button(tab1, text="Back")

# === ADD WIDGETS TO GRID ON TAB ONE
#exp.grid(row=0, column=0)
exp.grid(pady=15, sticky='W')
exp_entry.grid(row=0, column=1, sticky='W')

tgc.grid(row=1, column=0, sticky='W')
apply_tgc.grid(row=2, column=0, sticky='W')


initial_tgc.grid(row=3, column=0, sticky='W')
initial_entry.grid(row=3, column=1, sticky='W')

value_tgc.grid(row=4, column=0, sticky='W')
value_entry.grid(row=4, column=1, sticky='W')

final_tgc.grid(row=5, column=0, sticky='W')
final_entry.grid(row=5, column=1,sticky='W')

acq.grid(row=6, column=0,pady=15, sticky='W')
samplef.grid(row=7, column=0, sticky='W')
freqs.grid(row=7, column=1, sticky='W')
f.grid(row=7, column=1, padx=145, sticky='W')

pulse_peak.grid(row=8, column=0, sticky='W')
voltages.grid(row=8, column=1, sticky='W')
v.grid(row=8, column=1, padx=145, sticky='W')

timing.grid(row=9, column=0, pady=15, sticky='W')

t1.grid(row=10, column=0, padx=15, sticky='W')
t1_entry.grid(row=10,column=0,padx=40, sticky='W')

t2.grid(row=10,column=0,padx=90, sticky='W')
t2_entry.grid(row=10,column=0,padx=115, sticky='W')

#t3.grid(row=10,column=0,padx=165, sticky='W')
#t3_entry.grid(row=10,column=0,padx=190, sticky='W')

routine.grid(row=11, column=0, pady=10, sticky='W')
rnumber.grid(row=12, column=0, sticky='W')
rnumber_entry.grid(row=12, column=1, sticky='W')

msteps.grid(row=13, column=0,sticky='W')
msteps_entry.grid(row=13, column=1, sticky='W')

save.grid(row=14, column=0, pady=15, sticky='W')
json.grid(row=15, column=0, sticky='W')
json_entry.grid(row=15, column=0, padx=50, sticky='W')


#buttonBack.grid(row=6, column=0, padx=15, pady=15)
buttonBrowse.grid(row=15, column=1, sticky='W')


# === WIDGETS FOR TAB TWO
IP = tk.Label(tab2, text="IP Address:")
port = tk.Label(tab2, text="Port:")
location = tk.Label(tab2, text="Location of Parameters:")

IP_entry = tk.Entry(tab2)
port_entry = tk.Entry(tab2)
location_entry = tk.Entry(tab2)

imgLabelTabTwo = tk.Label(tab2)

buttonCommit = tk.Button(tab2, text="Browse")
buttonAddImage = tk.Button(tab2, text="Browse Again")

# === ADD WIDGETS TO GRID ON TAB TWO
IP.grid(sticky='W')
IP_entry.grid(row=0, column=1, sticky='W')


port.grid(row=1, column=0, pady=15, sticky='W')
port_entry.grid(row=1, column=1, pady=15, sticky='W')

location.grid(row=2, column=0, pady=15)
location_entry.grid(row=2, column=1, pady=15, sticky='W')

buttonCommit.grid(row=4, column=1, padx=15, pady=15)
buttonAddImage.grid(row=4, column=2, padx=15, pady=15)

tab_parent.pack(expand=1, fill='both')

form.mainloop()

