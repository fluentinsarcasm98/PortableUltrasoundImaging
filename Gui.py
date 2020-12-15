from tkinter import * 
import os


def save_info():
    exp_name = name.get()
    p_sex = sex.get()
    p_age = age.get()
    p_reason = reason.get()
    print(exp_name, p_sex, p_age, p_reason)
    
    parent_dir = "/home/akanksha/Documents/Fall2020"
    path = os.path.join(parent_dir, exp_name)
    os.mkdir(path)
    os.chdir(path)
    
    file = open( "Patient_info.json","w")
    file.write("Patient Name: " + exp_name)
    #file.write("\nPath: " + path)
    file.write("\nSex: " + p_sex)
    file.write("\nAge: " + str(p_age))
    file.write("\nReason for visit: " + p_reason)
    file.write("\n")    
    file.close()
    
root = Tk()

root.geometry("400x500")

root.title("Ultrasound Settings")
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)


name_text = Label(text='Patient Name :', font='bold')
sex_text = Label(text= 'Sex :', font = 'bold')
age_text = Label(text= 'Age :', font = 'bold')
reason_text = Label(text = 'Reason for Visit :', font = 'bold')

name_text.place(x=0,y=10)
sex_text.place(x=0, y= 30)
age_text.place(x=0, y=50)
reason_text.place(x=0, y=70)

name = StringVar()
sex = StringVar()
age = IntVar()
reason = StringVar()

name_entry = Entry(textvariable= name, width="30")
sex_entry = Entry(textvariable= sex, width="15")
age_entry = Entry(textvariable= age, width="5")
reason_entry = Entry(textvariable = reason, width="40")

name_entry.place(x=140,y=10)
sex_entry.place(x=140, y=30)
age_entry.place(x=140, y=50)
reason_entry.place(x=140, y=70)

def run_acq():
    os.system('python3 /home/akanksha/Documents/Fall2020/Capstone_Project/test.py')


button = Button(root, text="Save Parameters", command=save_info, width="15", height="1")
start_button = Button(root, text='Start Acquisition', command=run_acq,  width="15", height="1", bg="grey")

button.place(x=15, y=300)
start_button.place(x=15, y=335)

mainloop()
