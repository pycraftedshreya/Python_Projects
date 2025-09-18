from tkinter import *
import os 

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")  #20- 20sec ma shutdown thase

def log_out():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("Shutdown App")
st.geometry('500x500')
st.config(bg="yellow")


# Restart button
r_btn = Button(st,text="Restart",font=("arial",20),relief=RAISED,
               cursor="plus",command=restart)
r_btn.place(x=150,y=60,height=50,width=200)

# Restart Time button
rt_btn = Button(st,text="Restart Time",font=("arial",20),relief=RAISED,
                cursor="plus",command=restart_time)
rt_btn.place(x=150,y=170,height=50,width=200)

# Log out button
lg_btn = Button(st,text="Log-out",font=("arial",20),relief=RAISED,
                cursor="plus",command=log_out)
lg_btn.place(x=150,y=270,height=50,width=200)

# Shutdown button
st_btn = Button(st,text="ShutDown",font=("arial",20),relief=RAISED,
                cursor="plus",command=shutdown)
st_btn.place(x=150,y=370,height=50,width=200)


st.mainloop()