from tkinter import *
from tkinter import messagebox
from subprocess import call

def onClick1():
    messagebox.showinfo("","Start")
    root.destroy()
    call(["python","ProjectPython.py"])
    return True

def onClick2():
    x=messagebox.askquestion("Form","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()


root = Tk()
root.title("Start")
root.geometry("700x600+100+30")


C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\PAWAN SINGH\\Desktop\\project_final_6\\Pawan Project\\Images\\front.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(root, text="Encryption/Decryption of Image",font=("Arial", 20)).place(x=170, y=20)
Label(root, text="Made by: Pawan Singh Koranga").place(x=500, y=60)
Label(root, text="Sec: C").place(x=500, y=80)
Label(root, text="Rollno: 1018541").place(x=500, y=100)
Label(root, text="BTech CSE").place(x=500, y=120)

Button(root,bg='yellow',fg='black', text="Start", command=onClick1 ,height = 1, width = 12).place(x=120, y=300)
Button(root,bg='yellow',fg='black', text="Exit",  command=onClick2 ,height = 1, width = 12).place(x=470, y=300)

C.pack()
root.mainloop()
