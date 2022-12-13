import time
import FunctionBook as fb
try:
    while True:
        print("\n")
        print("                        !! Hospital Management System !!                      \n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("         System to maintain Record of the Patient's of your Hospital            ")
        print("                                                Developed By,                   ")
        print("                                                2209. Shriyasha Jagadale        ")
        print("                                                2212. Swayamsiddha Mane Deshmukh")
        print("                                                2214. Kshitija Garud            ")
        print("________________________________________________________________________________")
        print("\n")
        print("OPTIONS:")
        print("1.WRITE PATIENT RECORD\n2.SHOW ALL PATIENT'S RECORDS\n3.SEARCH BY PATIENT ID")
        print("4.SEARCH BY PATIENT NAME\n5.SEARCH BY BLOOD GROUP\n6.SEARCH BY GENDER\n7.SEARCH BY DISEASE NAME")
        print("8.SEARCH BY DOCTOR NAME\n9.MODIFYPATIENT RECORDS\n10.DELETE PATIENT RECORD\n11.EXIT")
        print("\n")
        ch=int(input("\nPLEASE ENTER YOUR CHOICE:"))
        if ch==1:
            fb.WriteHospital()
        elif ch==2:
            fb.ReadHospital()
        elif ch==3:
            n=input("\nPLEASE ENTER PATIENT ID TO SEARCH:--")
            fb.SearchPatientId(n)
        elif ch==4:
            n=input("\nPLEASE ENTER PATIENT NAME TO SEARCH:--")
            fb.SearchPatientName(n)
        elif ch==5:
            n=input("\nPLEASE ENTER BLOOD GROUP TO SEARCH:--")
            fb.SearchBloodgroup(n)
        elif ch==6:
            n=input("\nPLEASE ENTER GENDER TO SEARCH (m/f/t):--")
            fb.SearchGender(n)
        elif ch==7:
            n=input("\nPLEASE ENTER DISEASE NAME TO SEARCH:--")
            fb.SearchDisease(n)
        elif ch==8:
            n=input("\nPLEASE ENTER DOCTORS NAME TO SEARCH:--")
            fb.SearchDoctor(n)
        elif ch==9:
            m=input("\nENTER PATIENT ID TO MODIFY RECORDS:--")
            print ("\n")
            print ("WHAT DO YOU WANT TO MODIFY:") 
            print ("1.PATIENT'S NAME")
            print ("2.FATHERS/PARENT NAME:-")
            print ("3.PATIENT'S AGE")
            print ("4.PATIENT'S GENDER")
            print ("5.PATIENT'S HEIGHT")
            print ("6.PATIENT'S WEIGHT")
            print ("7.PATIENT'S BLOOD GROUP:-")
            print ("8.ADDRESS:-")
            print ("9.CONTACT NUMBER:-")
            print ("10.E-MAIL ADDRESS:-")
            print ("11.DOCTOR'S NAME:-")
            print ("12.DISEASE NAME:-")
            print ("13.PRESCRIBED MEDICINES/TEST:-")
            print ("14.BILL AMOUNT:-")
            print ("15.PAYMENT METHOD:-")
            print ("16.ALL")
            n=int(input("Enter Your Choice::--"))
            fb.ModifyPatient(m,n)
        elif ch==10:
            n=input("\nENTER PATIENT ID TO DELETE:-")
            fb.DelPatientFile(n)
        elif ch==11:
            print ("\n")
            print ("EXITING")
            time.sleep(.8)
            print ("."),
            time.sleep(.8)
            print ("."),
            time.sleep(.8)
            print ("."),
            time.sleep(.8)
            print ("."),
            time.sleep(.8)
            print ("."),
            break
        else:
            print ("Analysing your input.")
            time.sleep(.6)
            print ("."),
            time.sleep(.6)
            print ("."),
            time.sleep(.6)
            print ("."),
            time.sleep(.6)
            print ("."),
            time.sleep(.6)
            print (".")
            print("\n\n\n~~~~~~~~~~~~~~~~~~~~WRONG CHOICE!!!~~~~~~~~~~~~~~~~~~~\n\n\n")
            
except KeyboardInterrupt:
    print("Keyboard Interrupt Occured ! May to Press Wrong Key.")
