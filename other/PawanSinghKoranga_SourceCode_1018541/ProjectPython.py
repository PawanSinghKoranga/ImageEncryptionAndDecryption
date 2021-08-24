from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from subprocess import call

def en(val,key):
    if key==1:
        return (val**7)%33
    elif key==0:
        return (val**3)%33


def encrypt_image():
    file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
    if file1 is not None:
        print(file1)
        file_name=file1.name
        print(file_name)
        key=entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index,values in enumerate(image):
            if values>=1 and values<33:
                image[index]=int(en(values,int(key)))
        fi1 = open(file_name,'wb')
        fi1.write(image)
        fi1.close()

def leave():
    x=messagebox.askquestion("Form","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()

root = Tk()
root.geometry("500x400")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\PAWAN SINGH\\Desktop\\project_final_6\\Pawan Project\\Images\\main.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

b1 = Button(root,text="Choose Files",command=encrypt_image)
b1.place(x=200,y=50)


entry1 = Text(root,height=1,width=15)
entry1.place(x=170,y=100)

b2 = Button(root,width=8,text="leave",command=leave)
b2.place(x=205,y=150)

C.pack()
root.mainloop()


