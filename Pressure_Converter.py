"""

Program = Pressure Converter

Pressure(atm), Check_Value, Convert
Pascal
Bar
Force
Torr

~by Soham Deepak Satpute

"""
from tkinter import *

program = Tk(className=' Pressure Converter')
program.geometry('550x200')
program.configure(bg="RoyalBlue1")

# Checking Value Validity Function
def value_check():
    try:
        try_variable = float(atm.get())
        if try_variable < 0: 
            return None
    except: 
        popup()
    if convert['state'] == DISABLED:
        convert['state'] = NORMAL
    else:
        convert['state'] = NORMAL

# Main Definition
def pressure_convertion():

    pascal = f'{float(atm.get()) * 101325} Pa'
    pascal_text.delete("1.0",END)
    pascal_text.insert(END,pascal)

    bar = f'{float(atm.get()) * 1.01325} bar'
    bar_text.delete("1.0",END)
    bar_text.insert(END,bar)

    pound_force = f'{float(atm.get()) * 14.6959} psi'
    force_text.delete("1.0",END)
    force_text.insert(END,pound_force)

    torr = f'{float(atm.get()) * 760} mm/Hg'
    torr_text.delete("1.0",END)
    torr_text.insert(END,torr)

    if convert['state'] == NORMAL:
        convert['state'] = DISABLED
    else:
        convert['state'] = DISABLED

def disable_event():
    pass

# Program Objects
atm = StringVar()
main_label = Label(program,text='Pressure (atm): ',height=1,width=20)
main_label.configure(bg="RoyalBlue1")
main_label.grid(row=0,column=0)
pressure = Entry(program,textvariable=atm)
pressure.grid(row=0,column=1)

def popup():
    line2 = f'        "{atm.get()}" is not an acceptable value for "atmospheres".         \n'.center(65) 
    line3 = "             Please input a numberic value and try again.               \n".center(65)
    line4 = '                                                                       \n'.center(65)
    line5 = '                       Press "OK" to continue.                              \n'.center(65)
    string1 = line2 + line3 + line4 + line5 + line4 

    def close_program():
        if check['state'] == DISABLED:
            check['state'] = NORMAL
        else:
            check['state'] = NORMAL
        window.destroy()

    def exit_everything():
        window.destroy()
        program.destroy()
        exit()

    window = Tk(className=" Error Mesaage")
    window.configure(bg="RoyalBlue1")
    #window.geometry("320x200")

    if check['state'] == NORMAL:
        check['state'] = DISABLED
    else:
        check['state'] = DISABLED

    l1 = Label(window,text=string1)
    l1.configure(bg="RoyalBlue1")
    l1.grid(row=1,column=0,columnspan=2)

    l2 = Label(window,text='------------------------------------------------------------------')
    l2.configure(bg="blue1")
    l2.grid(row=0,column=0,columnspan=5)

    window.protocol("WM_DELETE_WINDOW", disable_event)
    ok = Button(window,text="         OK         ",command=close_program)
    ok.configure(bg="#ffb3fe")
    ok.grid(row=3,column=0)

    exit_button = Button(window,text="         Exit         ",command=exit_everything)
    exit_button.configure(bg="#ffb3fe")
    exit_button.grid(row=3,column=1)

    l3 = Label(window,text='------------------------------------------------------------------')
    l3.configure(bg="blue1")
    l3.grid(row=2,column=0,columnspan=5)

    l4 = Label(window,text='___________________________________________________________________')
    l4.configure(bg="blue1")
    l4.grid(row=4,column=0,columnspan=5)

#    window.mainloop()

convert = Button(program,text='Convert               ',state=DISABLED,command=pressure_convertion,bg="black",fg="white")
convert.flash()
convert.grid(row=0,column=4)

check = Button(program,text='Check Value',state=NORMAL,command=value_check,bg="#ffb3fe")
check.grid(row=0,column=3)

label_1 = Label(program,text='------------------------------------------------------------------------------------------------------------------')
label_1.configure(bg="blue1")
label_1.grid(row=1,column=0,columnspan=6)

pascal_label = Label(program,text="Pascal (SI unit): ")
pascal_label.configure(bg="RoyalBlue1")
pascal_label.grid(row=2,column=0)
pascal_text = Text(program,height=1,width=20)
pascal_text.grid(row=2,column=1)

bar_label = Label(program,text="Bar: ")
bar_label.configure(bg="RoyalBlue1")
bar_label.grid(row=3,column=0)
bar_text = Text(program,height=1,width=20)
bar_text.grid(row=3,column=1)

force_label = Label(program,text="Pound Force Per Square Inch: ")
force_label.configure(bg="RoyalBlue1")
force_label.grid(row=4,column=0)
force_text = Text(program,height=1,width=20)
force_text.grid(row=4,column=1)

torr_label = Label(program,text="Torr: ")
torr_label.configure(bg="RoyalBlue1")
torr_label.grid(row=5,column=0)
torr_text = Text(program,height=1,width=20)
torr_text.grid(row=5,column=1)

label_2 = Label(program,text='------------------------------------------------------------------------------------------------------------------')
label_2.configure(bg="blue1")
label_2.grid(row=6,column=0,columnspan=6)

label_3 = Label(program,text='                                                                                                               ~~ SohamS757')
label_3.configure(bg="RoyalBlue1")
label_3.grid(row=7,column=0,columnspan=6)

# Looping 
program.mainloop()