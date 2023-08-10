import sqlite3

con = sqlite3.connect('doctorPatient.db')

cursor = con.cursor()

# create a function for admin login
def login(arg):
    try:
        cursor.execute('''SELECT * FROM admin WHERE username = :user and password = :pass''', {
            'user': arg[0],
            'pass': arg[1]
        })
        return cursor.fetchone()
    except:
        return False

def add_doctor(arg):
    try:
        print(arg)

        cursor.execute('''INSERT INTO add_doctor (name,specialist,contact_number,qualification,appointment_charges) VALUES(:name,:specialist,:contact_number,:qualification,:appointment_charges)''',{

            'name': arg[0],
            'specialist': arg[1],
            'contact_number': arg[2],
            'qualification' : arg[3],
            'appointment_charges': arg[4]
             })
        con.commit()
        return True
    except:
        return False        

def add_patient(arg):
    try:
        print(arg)

        cursor.execute('''INSERT INTO add_patient (name,gender,age,address,contact_number,check_in) VALUES (:name,:gender,:age,:address,:contact_number,:check_in)''',{

            'name': arg[0],
            'gender': arg[1],
            'age': arg[2],
            'address' : arg[3],
            'contact_number': arg[4],
            'check_in': arg[5]
             })
        con.commit()
        return True
    except:
        return False        

def viewmanage_patient():
    try:
        cursor.execute('SELECT * FROM add_patient')
        return cursor.fetchall()
    except:
        return False        

def deletemanage_patient(gup):
    try:
        print(gup)
        cursor.execute('''DELETE FROM add_patient where id = :id''',{'id':gup[0]})
        con.commit()
        return True
    except:
        return False



def viewmanage_doctor():
    try:
        cursor.execute('SELECT * FROM add_doctor')
        return cursor.fetchall()
    except:
        return False     

def deletemanage_doctor(gup):
    try:
        print(gup)
        cursor.execute('''DELETE FROM add_doctor where id = :id''',{'id':gup[0]})
        con.commit()
        return True
    except:
        return False


def create_appointment(arg):
    try:
        print("this",arg)

        cursor.execute('''INSERT INTO appointment (doctor,patient,date,time) VALUES(:doctor,:patient,:date,:time)''',{
            'doctor': arg[0],
            'patient': arg[1],
            'date': arg[2],
            'time' : arg[3],
             })
        print(arg)
        con.commit()
        return True
    except:
        return False   

def viewcreate_appointment():
    try:
        cursor.execute('SELECT * FROM appointment')
        return cursor.fetchall()
    except:
        return False     


def deleteappointment_history(gup):
    try:
        print(gup)
        cursor.execute('''DELETE FROM appointment where id = :id''',{'id':gup[0]})
        con.commit()
        return True
    except:
        return False

def get_doctor(gup):
    try:
        print("get",gup)
        cursor.execute('SELECT * FROM add_doctor WHERE id=:id',{'id':gup[0]})
        return cursor.fetchall()
    except:
        return False 

def updateDoctor(gup):
    try:
        print(gup)
        cursor.execute('''UPDATE add_doctor 
                SET  
                name=:name, 
                specialist=:specialist,
                contact_number=:contact_number,
                qualification=:qualification,
                appointment_charges=:appointment_charges 
                
                WHERE id=:id''',
                {
                    'id':gup[0],
                    'name':gup[1],
                    'specialist':gup[2],
                    'contact_number':gup[3],
                    'qualification':gup[4],
                    'appointment_charges':gup[5],
                }
        )
        con.commit()
        # con.close()
        return True
    
    except:
        return False

def get_patient(gup):
    try:
        print("get",gup)
        cursor.execute('SELECT * FROM add_patient WHERE id=:id',{'id':gup[0]})
        return cursor.fetchall()
    except:
        return False 

def updatepatient(gup):
    try:
        print(gup)
        cursor.execute('''UPDATE add_patient 
                SET  
                name=:name, 
                gender=:gender,
                age=:age,
                address=:address,
                contact_number=:contact_number, 
                check_in=:check_in,
                WHERE id=:id''',
                {
                    'id':gup[0],
                    'name':gup[1],
                    'gender':gup[2],
                    'age':gup[3],
                    'address':gup[4],
                    'contact_number':gup[5],
                    'check_in':gup[6],
                }
        )
        con.commit()
        # con.close()
        return True
    
    except:
        return False

def viewdoctor():
    try:
        cursor.execute('SELECT * FROM add_doctor')
        return cursor.fetchall()
    except:
        return False

def viewpatient():
    try:
        cursor.execute('SELECT * FROM add_patient')
        return cursor.fetchall()
    except:
        return False        

def viewappointment():
    try:
        cursor.execute('SELECT * FROM appointment')
        return cursor.fetchall()
    except:
        return False                