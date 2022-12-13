import time
import os
import Hospital_Base as ho
hosp=ho.Hospital()
def WriteHospital():    #to write patient record
    print("\n******  Please!!! Enter Details in Small letters  ********\n")
    hosp.Input()
    hosp.WriteData()
    print ("\n\n Congratulations! Details Successfully Saved.")
    print("Re-Check Entered Details...\n")
    hosp.Output()
    
def ReadHospital():     #to display all patient records  
    content=hosp.ReadData()
    print(content)
def SearchPatientId(n):       #to search on the basis of patient id
    try:
        file=open("Patient"+n+".txt","r")
        if file:
            print(".... Patient Record is Exits....\n")
            print(file.read())
        file.close()
    except IOError:
        print ("|  ... RECORD... DOES... NOT... EXIST ...  | ")
    
        
        

def SearchPatientName(n):           #to search on the basis of patient name
    try:
        str="PATIENT'S NAME:"+n
        pn=open("Patient_Name.txt","r")
        for record in pn:
            if str in record:
                print("\n",record)
            
        pn.close()
    except IOError:
        print(" Record File Does Not Found!")

def SearchBloodgroup(n):          #to search on the basis of Blood Group
    try:
        str="BLOOD GROUP:"+n
        bg=open("BloodGroup.txt","r")
        for record in bg:
            if str in record:
                print("\n",record)
            
        bg.close()
    except IOError:
        print(" Record File Does Not Found!")
        
        

def SearchGender(n):                         #to search on the basis of gender
    try:
        str="GENDER:"+n
        g=open("Gender.txt","r")
        for record in g:
            if str in record:
                print("\n",record)
            
        g.close()
    except IOError:
        print(" Record File Does Not Found!")

    
def SearchDisease(n):                         #to search on the basis of Disease Name
    try:
        str="DISEASE:"+n
        d=open("Disease.txt","r")
        for record in d:
            if str in record:
                print("\n",record)
            
        d.close()
    except IOError:
        print(" Record File Does Not Found!")

    
def SearchDoctor(n):                         #to search on the basis of Doctors Name
    try:
        str="DOCTOR'S NAME:"+n
        d=open("Doctor.txt","r")
        for record in d:
            if str in record:
                print("\n",record)
            
        d.close()
    except IOError:
        print(" Record File Does Not Found!")


def ModifyPatient(m,n):                 #to modify patient record
    try:
        p=open("Patient"+m+".txt","r")
        content=p.read()
        print("\n")
        print(content)
        p.close()
        mp=open("Modify_Records.txt","a")     #to save all modified records
        if n==1:
            a=input("ENTER NEW PATIENT'S NAME::")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW NAME:"+a)
            mp.write("__________________________________________________________________")
            print("Modified Data Successfully Saved")
        elif n==2:
            a=input("ENTER NEW FATHERS NAME:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW PARENT NAME:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==3: 
            a=input("ENTER NEW PATIENT'S AGE:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW AGE:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==4:
            a=input("ENTER NEW PATIENT'S GENDER(m/f/t):-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW GENDER:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==5:
            a=input("ENTER NEW PATIENT'S HEIGHT:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW HEIGHT:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==6:
            a=input("ENTER NEW PATIENT'S WEIGHT(In Kgs):-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW WEIGHT:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==7:
            a=input("ENTER NEW PATIENT'S BLOOD GROUP:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW BLOOD GROUP:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==8:
            a=input("ENTER NEW ADDRESS:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW ADDRESS:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==9:
            a=input("ENTER NEW CONTACT NUMBER:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW CONTACT NUMBER:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==10:
            a=input("ENTER NEW E-MAIL ADDRESS:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW E-MAIL:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==11:
            a=input("ENTER NEW DOCTOR'S NAME:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW DOCTOR:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==12:
            a=input("ENTER NEW DISEASE NAME:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW DISEASE:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==13:
            a=input("ENTER NEW PRESCRIBED MEDICINE:-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW MAEDICINE/TEST:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==14:
            a=input("ENTER NEW BILL AMOUNT:--> Rs.")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW BILL AMOUNT:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==15:
            a=input("ENTER NEW PAYMENT METHOD(Cash\Cheque\Card):-->")
            mp.write("PATIENT ID:"+m+"\t"+" PATIENT NEW PAYMENT METHOD:"+a)
            mp.write("__________________________________________________________________ ")
            print("Modified Data Successfully Saved")
        elif n==16:
            print ("__________________ENTER THE NEW DETAILS__________________")
            hosp.Input() 
            hosp.WriteModifyData()
            print("Modified Data Successfully Saved")
        else:
            print("Enter Valid Choice!")
        mp.close()

            
            
    except IOError:
        print("Record File Doed Not Found!")
        

    

def DelPatientFile(n):          #to delete patient record
    try:
        os.remove("Patient"+n+".txt")
        print("!! Records Of Patient"+n+" Is Deleted !!")
    except IOError:
        print("    File Does Not Exits!! May Be Patient Id Wrong.     ")
    
