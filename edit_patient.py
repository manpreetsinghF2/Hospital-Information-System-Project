from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import menu 
import database

# import database

class Edit_patient:
    def __init__(self):
        self.root=Tk()
        self.root.title("Edit Patient")

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
        
    
    def editPatientFrame(self,data):
        print("id",data)
        self.first= Frame(self.root, bg="white")
        self.first.place(x=0,y=0,width="900",height="600")
        
        self.image = Image.open("images/sidepic1.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="300",height="600")
        
        
        #create and place labels 
        self.lab=Label(self.first,text="EDIT PATIENTS",anchor=E,bg="white",fg="black")
        self.lab.place(x=370,y=30, width="370", height="45")
        self.lab.config(font=("calibri",30,"bold"))
     
        self.lab1=Label(self.first,text="Name",anchor=E,bg="white",fg='black')
        self.lab1.place(x=430,y=100, width="70", height="30")
        self.lab1.config(font=("calibri",18,"bold"))


    
        self.lab2=Label(self.first,text="Gender",anchor=E,bg="white",fg='black')
        self.lab2.place(x=420,y=150, width="90", height="30")
        self.lab2.config(font=("calibri",18,"bold"))

        self.lab3=Label(self.first,text="Age",anchor=E,bg="white",fg='black')
        self.lab3.place(x=440,y=200,width=40,height=30)
        self.lab3.config(font=("calibri",18,"bold"))

        self.lab4=Label(self.first,text="Address",anchor=E,bg="white",fg='black')
        self.lab4.place(x=420,y=250,width=100,height=30)
        self.lab4.config(font=("calibri",18,"bold"))

        self.lab5=Label(self.first,text="Contact_Number",anchor=E,bg="white",fg='black')
        self.lab5.place(x=370,y=300,width=190,height=30)
        self.lab5.config(font=("calibri",18,"bold"))

        self.lab6=Label(self.first,text="Check_In",anchor=E,bg="white",fg='black')
        self.lab6.place(x=430,y=350,width=100,height=30)
        self.lab6.config(font=("calibri",18,"bold"))

        #entries

        
        
        self.name=Entry(self.first)
        self.name.place(x=570,y=100,width=210,height=30)
        
        
        
        self.gender=Entry(self.first)
        self.gender.place(x=570,y=150,width=210,height=30)

        self.id=Entry(self.first)
        self.id.place(x=570,y=200,width=210,height=30)
        
        self.age=Entry(self.first)
        self.age.place(x=570,y=200,width=210,height=30)

        
    
        self.address=Entry(self.first)
        self.address.place(x=570,y=250,width=210,height=30)
        
    
        self.contact_number=Entry(self.first)
        self.contact_number.place(x=570,y=300,width=210,height=30)

    
        self.check_in=Entry(self.first)
        self.check_in.place(x=570,y=350,width=210,height=30)

        #buttons

        self.loginButton = Button(self.first, text = "Update", command = self.addPatient)
        self.loginButton.place(x=460,y=410,width=100,height=40)

        self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=590,y=410,width=100,height=40)

        for i in database.get_patient(data):
            print(i)
            self.id.insert(0,i[0])
            self.name.insert(0,i[1])
            self.gender.insert(0,i[2])
            self.age.insert(0,i[3])
            self.address.insert(0,i[4])
            self.contact_number.insert(0,i[5])
            self.check_in.insert(0,i[6])

        





        
        self.root.mainloop()

    
    def addPatient(self):
        data = (
            self.id.get(),
            self.name.get(),
            self.gender.get(),
            self.age.get(),
            self.address.get(),
            self.contact_number.get(),
            self.check_in.get(),
            )

        if self.name.get() == '':
            messagebox.showinfo('Alert', 'Please enter patient name first')
        elif(not(self.name.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in name") 

        elif self.gender.get() == "":
            messagebox.showinfo('Alert','Please enter patient gender')
        # elif((self.gender.get()=='male') or not(self.gender.get()=='female')):
        #     messagebox.showinfo("Message", "Enter only male or female in gender")
        elif(not(self.gender.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in gender")

        elif self.age.get() == "":
            messagebox.showinfo('Alert','Please enter patient age')
        elif(not(self.age.get().isdigit())):
            messagebox.showinfo("Message", "Enter only characters in age") 

        elif self.address.get() == "":
            messagebox.showinfo('Alert','Please enter patient address') 
        elif(self.address.get().isdigit()):
            messagebox.showinfo("Message", "Enter only characters in address")    

        elif self.contact_number.get() == "":
            messagebox.showinfo('Alert','Please enter patient contact_number') 
        elif(self.contact_number.get().isalpha()):
            messagebox.showinfo("Message", "Enter only characters in contact_number")

        elif self.check_in.get() == "":
            messagebox.showinfo('Alert','Please enter patient check_in') 
        elif(self.check_in.get().isalpha()):
            messagebox.showinfo("Message", "Enter only digit in check_in")               
        else:
            res = database.updatepatient(data)
            # print('res')
            if res:
                messagebox.showinfo("Message", "patient updated successfully.")
                # self.root.destroy()
                # m = menu.AdminNav()
                # m.navframe()
            else:
                messagebox.showinfo('Alert', 'Invalid data.')




    def menuWindow(self):
        self.root.destroy()
        obj = menu.AdminNav()
        obj.navframe()

if __name__=='__main__':
    obj1 = Edit_patient()
    obj1.editPatientFrame('data')
    
         
    
