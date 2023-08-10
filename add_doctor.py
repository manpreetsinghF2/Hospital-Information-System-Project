from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import menu
import database
# import database


class Add_doctor:
    def __init__(self):
        self.root=Tk()
        self.root.title("Add doctor")

        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        # 800 x 500 is the size of your screen

        self.width = int((self.fullwidth-900)/2)
        self.height=int((self.fullheight-600)/2)

        s = "900x600+" +str(self.width)+ "+" +str(self.height)
        # s = "200x200"

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
        # self.root.mainloop()
        
    def addDoctorFrame(self):
        self.first= Frame(self.root, bg="white")
        self.first.place(x=0,y=0,width="900",height="600")
        
        self.image = Image.open("images/sidepic1.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="300",height="600")
        
        
        #create and place labels 
        self.lab=Label(self.first,text="ADD DOCTORS",anchor=E,bg="white",fg="black")
        self.lab.place(x=310,y=30, width="370", height="45")
        self.lab.config(font=("calibri",30,"bold"))

        self.lab1=Label(self.first,text="Name",anchor=E,bg="white",fg="black")
        self.lab1.place(x=450,y=100, width="80", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Specialist",anchor=E,bg="white",fg="black")
        self.lab1.place(x=433,y=150, width="100", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Contact",anchor=E,bg="white",fg="black")
        self.lab1.place(x=348,y=200,width=190,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Qualification",anchor=E,bg="white",fg="black")
        self.lab1.place(x=370,y=250,width=170,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="charges",anchor=E,bg="white",fg="black")
        self.lab1.place(x=450,y=300,width=90,height=30)
        self.lab1.config(font=("calibri",18,"bold"))
        #entries

        
        self.name=StringVar()
        self.name=Entry(self.first,textvariable=self.name)
        self.name.place(x=570,y=100,width=210,height=30)
        
        
        self.specialist=StringVar()
        self.specialist=Entry(self.first,textvariable=self.specialist)
        self.specialist.place(x=570,y=150,width=210,height=30)

        
        self.contact=StringVar()
        self.contact=Entry(self.first,textvariable=self.contact)
        self.contact.place(x=570,y=200,width=210,height=30)

        
        self.qualification=StringVar()
        self.qualification=Entry(self.first,textvariable=self.qualification)
        self.qualification.place(x=570,y=250,width=210,height=30)
        
        self.charges=StringVar()
        self.charges=Entry(self.first,textvariable=self.charges)
        self.charges.place(x=570,y=300,width=210,height=30)

        #buttons

        self.loginButton = Button(self.first, text = "Submit", command = self.addDoctor)
        self.loginButton.place(x=460,y=410,width=100,height=40)

        self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=590,y=410,width=100,height=40)


        self.root.mainloop()

    
    def addDoctor(self):
        data = (
            self.name.get(),
            self.specialist.get(),
            self.contact.get(),
            self.qualification.get(),
            self.charges.get(),
        )
        if self.name.get() == '':
            messagebox.showinfo('Alert', 'Please enter doctor name first')
        elif(not(self.name.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in name")

        elif self.specialist.get() == "":
            messagebox.showinfo('Alert','Please enter doctor specialist')
        elif(not(self.specialist.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in specialist")    

        elif self.contact.get() == "":
            messagebox.showinfo('Alert','Please enter contact')  
        elif(not(self.contact.get().isdigit())):
            messagebox.showinfo("Message", "Enter only digits in contact number") 
        elif (len(self.contact.get()) != 10):
            messagebox.showinfo('Alert', 'Please enter 10 digit contact')  

        elif self.qualification.get() == "":
            messagebox.showinfo('Alert','Please enter doctor qualification')
        elif(not(self.qualification.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in qualification") 
        

        elif self.charges.get() == "":
            messagebox.showinfo('Alert','Please enter appointment charges') 
        elif(not(self.charges.get().isdigit())):
            messagebox.showinfo("Message", "Enter only digit in appointment charges") 
        else:
            res = database.add_doctor(data)
            # print('res')
            if res:
                messagebox.showinfo("Message", "Doctor added successfully.")
                self.root.destroy()
                m = menu.AdminNav()
                m.navframe()
            else:
                messagebox.showinfo('Alert', 'Invalid data.')

    def menuWindow(self):
        self.root.destroy()
        obj = menu.AdminNav()
        obj.navframe()

if __name__=='__main__':
    obj1 = Add_doctor()
    obj1.addDoctorFrame()
    
         
    
