import time    
import os
class Hospital:
    def _init_(self):
        self.sno=''
        self.name=' '
        self.age=''
        self.sex=""
        self.email=" "
        self.fname=" "
        self.address=''
        self.city=''
        self.state=''
        self.height=''
        self.weight=''
        self.doctor=''
        self.med=''
        self.bill=''
        self.paymethod=''
        self.pno=''
        self.bgroup=''
        self.dname=''

    def Input(self):                               # to accept input from user
        print("\nFirst, Enter Patient's Personal Data:\n")
        self.sno=input("Enter Patient ID:")
        self.name=input("Enter Patinet's Name:")
        self.fname=input("Enter Fathers/Parent Name:")
        self.age=input("Enter Patient's Age:")
        self.sex=input("Enter Patient's Gender (m/f/t):")
        self.height=input("Enter Patient's Height(In cm):")
        self.weight=input("Enter Patient's Weight(In Kgs):")
        self.bgroup=input("Enter Patient's Blood Group:")
        print("\nNow, Enter Patient's Contact Details:\n")
        self.address=input("Enter Address:")
        self.pno=input("Enter Phone number:")
        self.email=input("Enter E-Mail (optional):")
        print("\nNow, Enter Patient's Treatment Details:\n")
        self.doctor=input("Enter Doctor's Name:")
        self.dname=input("Enter Disease Name:")
        self.med=input("Enter Prescribed Medicine or Test:")
        self.bill=input("Enter Bill Amount: Rs.")
        self.paymethod=input("Enter Payment Method(Cash/Cheque/Card):")

        
    def Output(self):                                             #to display entered details
        print ("\n               PATIENT DETAILS              \n")
        print ("---------------------*********-------------------- \n")
        print ("***PATIENT'S PERSONAL DETAILS***\n")
        print ("PATIENT ID:-",self.sno)
        print ("PATIENT'S NAME:-",self.name)
        print ("FATHERS/PARENT NAME:-",self.fname)
        print ("PATIENT'S AGE:-",self.age)
        print ("PATIENT'S GENDER:-",self.sex)
        print ("PATIENT'S HEIGHT:-",self.height)
        print ("PATIENT'S WEIGHT:-",self.weight)
        print ("PATIENT'S BLOOD GROUP:-",self.bgroup)
        print ("\n***PATIENT'S CONTACT DETAILS***")
        print ("ADDRESS:-",self.address)
        print ("CONTACT NUMBER:-",self.pno)
        print ("E-MAIL ADDRESS:-",self.email)
        print ("\n***PATIENT'S TREATMENT DETAILS***")
        print ("DOCTOR'S NAME:-",self.doctor)
        print ("DISEASE NAME:-",self.dname)
        print ("PRESCRIBED MEDICINES/TEST:-",self.med)
        print ("BILL AMOUNT:-",self.bill)
        print ("PAYMENT METHOD:-",self.paymethod)
        print ("**************************************")
    def WriteData(self):
        try:
            mainfile=open("Hospital.txt","a")                    #to write all patient data in one file
            mainfile.write ("\n              NEW PATIENT DETAILS              \n")
            mainfile.write ("-------------------*********-------------------- \n")
            mainfile.write ("***PATIENT'S PERSONAL DETAILS***\n")
            mainfile.write ("\nPATIENT ID."+self.sno)
            mainfile.write ("\nPATIENT'S NAME:-"+self.name)
            mainfile.write ("\nFATHERS/PARENT NAME:-"+self.fname)
            mainfile.write ("\nPATIENT'S AGE:-"+self.age)
            mainfile.write ("\nPATIENT'S GENDER:-"+self.sex)
            mainfile.write ("\nPATIENT'S HEIGHT:-"+self.height)
            mainfile.write ("\nPATIENT'S WEIGHT:-"+self.weight)
            mainfile.write ("\nPATIENT'S BLOOD GROUP:-"+self.bgroup)
            mainfile.write ("\n***PATIENT'S CONTACT DETAILS***")
            mainfile.write ("\nADDRESS:-"+self.address)
            mainfile.write ("\nCONTACT NUMBER:-"+self.pno)
            mainfile.write ("\nE-MAIL ADDRESS:-"+self.email)
            mainfile.write ("\n***PATIENT'S TREATMENT DETAILS***")
            mainfile.write ("\nDOCTOR'S NAME:-"+self.doctor)
            mainfile.write ("\nDISEASE NAME:-"+self.dname)
            mainfile.write ("\nPRESCRIBED MEDICINES/ TEST:-"+self.med)
            mainfile.write ("\nBILL AMOUNT:-"+self.bill)
            mainfile.write ("\nPAYMENT METHOD:-"+self.paymethod)
            mainfile.write ("\n ***************** RECORD END ********************")
            mainfile.close()
            file=open("Patient"+self.sno+".txt","w")                     #to crete individual file for patient
            file.write ("\n              PATIENT DETAILS              \n")
            file.write ("-------------------*********-----------------\n")
            file.write ("***PATIENT'S PERSONAL DETAILS***\n")
            file.write ("\nPATIENT ID."+self.sno)
            file.write ("\nPATIENT'S NAME:-"+self.name)
            file.write ("\nFATHERS/PARENT NAME:-"+self.fname)
            file.write ("\nPATIENT'S AGE:-"+self.age)
            file.write ("\nPATIENT'S GENDER:-"+self.sex)
            file.write ("\nPATIENT'S HEIGHT:-"+self.height)
            file.write ("\nPATIENT'S WEIGHT:-"+self.weight)
            file.write ("\nPATIENT'S BLOOD GROUP:-"+self.bgroup)
            file.write ("\n***PATIENT'S CONTACT DETAILS***")
            file.write ("\nADDRESS:-"+self.address)
            file.write ("\nCONTACT NUMBER:-"+self.pno)
            file.write ("\nE-MAIL ADDRESS:-"+self.email)
            file.write ("\n***PATIENT'S TREATMENT DETAILS***")
            file.write ("\nDOCTOR'S NAME:-"+self.doctor)
            file.write ("\nDISEASE NAME:-"+self.dname)
            file.write ("\nPRESCRIBED MEDICINES/ TEST:-"+self.med)
            file.write ("\nBILL AMOUNT:-"+self.bill)
            file.write ("\nPAYMENT METHOD:-"+self.paymethod)
            file.write ("\n ***************** RECORD END ********************")
            file.close()
            file_blood=open("BloodGroup.txt","a")                            #to save blood group records
            file_blood.write ("\nBLOOD GROUP:"+self.bgroup+"\t"+"PATIENT ID."+self.sno+"\t"+"PATIENT'S NAME:-"+self.name)
            file_blood.close()
            file_dr=open("Doctor.txt","a")                           # to save doctor records
            file_dr.write ("\nDOCTOR'S NAME:"+self.doctor+"\t"+"PATIENT ID."+self.sno+"\t"+"PATIENT'S NAME:-"+self.name)
            file_dr.close()
            file_name=open("Patient_Name.txt","a")                 #to save patients name only
            file_name.write ("\nPATIENT'S NAME:"+self.name+"\t"+"PATIENT ID."+self.sno)
            file_name.close()
            file_gender=open("Gender.txt","a")                                        #to save gender records
            file_gender.write ("\nGENDER:"+self.sex+"\t"+"PATIENT ID."+self.sno+"\t"+"PATIENT'S NAME:-"+self.name)
            file_gender.close()
            file_disease=open("Disease.txt","a")                                     #to save disease records
            file_disease.write ("\nDISEASE:"+self.dname+"\t"+"PATIENT ID."+self.sno+"\t"+"PATIENT'S NAME:-"+self.name)
            file_disease.close()
        except IOError:
            print(" Record File Does Not Found!")
    def ReadData(self):                                   #to display all patient records
        file=open("Hospital.txt","r")
        file_content=file.read()
        file.close()
        return file_content;
    def WriteModifyData(self):
        try:
            file=open("Modify_Records.txt","a")                    #to save all modified data
            file.write ("\n            NEW PATIENT DETAILS              \n")
            file.write ("-------------------*********-----------------\n")
            file.write ("***PATIENT'S PERSONAL DETAILS***\n")
            file.write ("\nPATIENT ID."+self.sno)
            file.write ("\nPATIENT'S NAME:-"+self.name)
            file.write ("\nFATHERS/PARENT NAME:-"+self.fname)
            file.write ("\nPATIENT'S AGE:-"+self.age)
            file.write ("\nPATIENT'S GENDER:-"+self.sex)
            file.write ("\nPATIENT'S HEIGHT:-"+self.height)
            file.write ("\nPATIENT'S WEIGHT:-"+self.weight)
            file.write ("\nPATIENT'S BLOOD GROUP:-"+self.bgroup)
            file.write ("\n***PATIENT'S CONTACT DETAILS***")
            file.write ("\nADDRESS:-"+self.address)
            file.write ("\nCONTACT NUMBER:-"+self.pno)
            file.write ("\nE-MAIL ADDRESS:-"+self.email)
            file.write ("\n***PATIENT'S TREATMENT DETAILS***")
            file.write ("\nDOCTOR'S NAME:-"+self.doctor)
            file.write ("\nDISEASE NAME:-"+self.dname)
            file.write ("\nPRESCRIBED MEDICINES/ TEST:-"+self.med)
            file.write ("\nBILL AMOUNT:-"+self.bill)
            file.write ("\nPAYMENT METHOD:-"+self.paymethod)
            file.write ("\n ***************** RECORD END ********************")
            file.close()
        except IOError:
            print("Record File Does Not Found!")

