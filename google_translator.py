from tkinter import *
from tkinter import ttk 
from translate import Translator

# function to translate the text
def change(text="type",src="English",dest="Hindi"):
    try:
        translator = Translator(from_lang=src, to_lang=dest)
        return translator.translate(text)
    except Exception as e:
        return "Translation Error: " + str(e) 

# fetch the data
def data():
    s = combo_sor.get()
    d = combo_dest.get()
    # starting to end data and also remove whitespace
    mesg = sor_text.get(1.0,END).strip()  

    # translate the data
    textget = change(text=mesg,src=s,dest=d)

    # delete the previous data and enter current data
    des_text.delete(1.0,END)
    des_text.insert(END,textget)

root = Tk()
root.title("Medium")    
root.geometry("500x700")   #length = 500 , width = 700
root.config(bg='green')    # background color of container

# label - Displays headings
lab_txt = Label(root,text="Translator",font=("Arial",40))
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source text",font=("Time New Roman",20),fg="black",bg="light green")
lab_txt.place(x=100,y=100,height=20,width=300)

# text - Areas for typing and showing translated text.
sor_text = Text(frame,font=("Time New Roman",20),wrap=WORD)
sor_text.place(x=10,y=130,height=150,width=480)

# it include all languages 
list_text = ["English", "Hindi", "Spanish", "French", "German"]

# Source and  combobox - Dropdown menus to select languages.
combo_sor = ttk.Combobox(frame,values=list_text)    
combo_sor.place(x=10,y=300,height=40,width=150)
combo_sor.set("english")    #title

button_change = Button(frame,text="Translate",relief=RAISED,command=data)  #cleanliness
button_change.place(x=170,y=300,height=40,width=150)

# Destination
combo_dest = ttk.Combobox(frame,values=list_text)    #dropdown option
combo_dest.place(x=330,y=300,height=40,width=150)
combo_dest.set("english")    #title

lab_txt = Label(root,text="Destination text",font=("Time New Roman",20),fg="black",bg="light green")
lab_txt.place(x=100,y=360,height=20,width=300)

des_text = Text(frame,font=("Time New Roman",20),wrap=WORD)
des_text.place(x=10,y=400,height=150,width=480)


root.mainloop()