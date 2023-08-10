from tkinter import *

import database
# import tabledatabase
from tkintertable import TableCanvas
import manage_patient
from tkinter import messagebox
from tkinter.ttk import Treeview
import menu
import edit_doctor

class ManageDoctor:
    def __init__(self):
        self.root=Tk()
        self.root.title("MANAGE DOCTOR")
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth - 900) / 2)
        self.height = int((self.fullheight - 600) / 2)
        s = "1000x500+" + str(self.width) + "+" + str(self.height)
        self.root.resizable(height=False, width=False)

        self.root.geometry(s)

    def managedoc(self):
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="1000", height="500")
      
        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Doctor Name")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="Specialist")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Contact")
        self.tr.column('#3', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#4', text="Qualification")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)


        self.tr.heading('#5', text="Charges")
        self.tr.column('#5', minwidth=0, width=100, stretch=NO)


        self.tr.heading('#6', text="Edit")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#7', text="Delete")
        self.tr.column('#7', minwidth=0, width=80, stretch=NO)

        j = 0
        # print(database.viewmanage_patient())
        for i in database.viewmanage_doctor():
            self.tr.insert('', 0, text=i[0], values=(i[1],i[2],i[3],i[4],i[5], 'Edit', 'Delete'))
            j += 1
        # create double action button
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,width=1000,height=600)
        self.loginButton = Button(self.fr, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=890,y=30,width=100,height=40)
        self.root.mainloop()

    def actions(self, e):
    #      get the values of the selected rows\\
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)
        # print(col)
        # print(self.tr.item(tt))

        gup = (
           self.tr.item(tt).get('text'),
        )
        print(gup)
        if col == '#7':
            res = messagebox.askyesno("ALERT", "Do You Realy Want to delete this item")
            if res:
                rs = database.deletemanage_doctor(gup)
                if rs:
                    messagebox.showinfo("ALERT", "Suuccessfully Deleted")
                self.root.destroy()
                obj = ManageDoctor()
                obj.managedoc()

        if col == '#6':
            # database.get_doctor(gup)
            self.root.destroy()
            obj = edit_doctor.Edit_doctor()
            obj.editDoctorFrame(gup)
        
    #     self.btn = Button(self.fr, text="History", bg="black", fg="white",command=self.openhistory)
    #     self.btn.place(x=820, y=250, width="150", height="30")
    #     self.btn.config(font="impact")

  


    # def openhistory(self):
    #      a=manage_patient.Managepatient()
    #      a.managepat()
    
    def menuWindow(self):
        self.root.destroy()
        obj = menu.AdminNav()
        obj.navframe()

    def select_data(tree):
        curItem=tree.focus()
        value=tree.item(curItem,"values")
        print("selsect",value)


if __name__=='__main__':
    obj = ManageDoctor()
    obj.managedoc()