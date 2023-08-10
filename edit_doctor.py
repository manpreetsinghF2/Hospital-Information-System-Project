from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import menu
import database
# import database


class Edit_doctor:
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
        
    def editDoctorFrame(self,data):
        print("id",data)
        self.first= Frame(self.root, bg="white")
        self.first.place(x=0,y=0,width="900",height="600")
        
        self.image = Image.open("images/sidepic1.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="300",height="600")
        
        
        #create and place labels 
        self.lab=Label(self.first,text="EDIT DOCTORS",anchor=E,bg="white",fg="black")
        self.lab.place(x=310,y=30, width="370", height="45")
        self.lab.config(font=("calibri",30,"bold"))

        self.lab1=Label(self.first,text="Name",anchor=E,bg="white",fg="black")
        self.lab1.place(x=380,y=100, width="80", height="30")
        self.lab1.config(font=("calibri",18,"bold"))


    
        self.lab1=Label(self.first,text="Specialist",anchor=E,bg="white",fg="black")
        self.lab1.place(x=380,y=150, width="100", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Contact_Number",anchor=E,bg="white",fg="black")
        self.lab1.place(x=350,y=200,width=190,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Qualification",anchor=E,bg="white",fg="black")
        self.lab1.place(x=350,y=250,width=170,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Appiontment_Charges",anchor=E,bg="white",fg="black")
        self.lab1.place(x=310,y=300,width=250,height=30)
        self.lab1.config(font=("calibri",18,"bold"))
        #entries

        # for i in database.get_doctor(data): 
        #     print(i)

        # self.name=StringVar()
        self.name=Entry(self.first)
        self.name.place(x=570,y=100,width=210,height=30)
        
        
        # self.specialist=StringVar()
        self.specialist=Entry(self.first)
        self.specialist.place(x=570,y=150,width=210,height=30)

        self.id=Entry(self.first)
        self.id.place(x=570,y=200,width=210,height=30)
        # self.contact_number=StringVar()
        self.number=Entry(self.first)
        self.number.place(x=570,y=200,width=210,height=30)

        
        # self.qualification=StringVar()
        self.qualification=Entry(self.first)
        self.qualification.place(x=570,y=250,width=210,height=30)
        
        # self.appointment_charges=StringVar()
        self.appointment=Entry(self.first)
        self.appointment.place(x=570,y=300,width=210,height=30)
        
    #buttons
        self.loginButton = Button(self.first, text = "Update", command = self.doctor)
        self.loginButton.place(x=460,y=410,width=100,height=40)

        self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=590,y=410,width=100,height=40)

        # fetchdata
        for i in database.get_doctor(data):
            print(i)
            self.id.insert(0,i[0])
            self.name.insert(0,i[1])
            self.specialist.insert(0,i[2])
            self.number.insert(0,i[3])
            self.qualification.insert(0,i[4])
            self.appointment.insert(0,i[5])


        self.root.mainloop()

    
    def doctor(self):
        data = (
            self.id.get(),
            self.name.get(),
            self.specialist.get(),
            self.number.get(),
            self.qualification.get(),
            self.appointment.get(),
        )
        if self.name.get() == '':
            messagebox.showinfo('Alert', 'Please enter doctor name first')
        elif(self.name.get().isdigit()):
            messagebox.showinfo("Message", "Enter only characters in name")

        elif self.specialist.get() == "":
            messagebox.showinfo('Alert','Please enter doctor specialist')
        elif(self.specialist.get().isdigit()):
            messagebox.showinfo("Message", "Enter only characters in specialist")    

        elif self.number.get() == "":
            messagebox.showinfo('Alert','Please enter contact_number')  
        elif(not(self.number.get().isdigit())):
            messagebox.showinfo("Message", "Enter only digits in contact_number") 
        elif (len(self.number.get()) != 10):
            messagebox.showinfo('Alert', 'Please enter 10 digit contact')  

        elif self.qualification.get() == "":
            messagebox.showinfo('Alert','Please enter doctor qualification')
        elif(self.qualification.get().isdigit()):
            messagebox.showinfo("Message", "Enter only characters in qualification") 
        

        elif self.appointment.get() == "":
            messagebox.showinfo('Alert','Please enter appointment_charges') 
        elif(self.appointment.get().isalpha()):
            messagebox.showinfo("Message", "Enter only digit in appointment_charges") 
        else:
            res = database.updateDoctor(data)
            # print('res')
            if res:
                messagebox.showinfo("Message", "Doctor updated successfully.")
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
    obj1 = Edit_doctor()
    obj1.editDoctorFrame('data')
    
         
    
