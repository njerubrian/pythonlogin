from tkinter import *
root = Tk()

# creating the grid box for the registration
root.geometry("800x500")

# title for the form
Title = Label(root, text="THARAKA NITHI INFRASTUCTURE PROJECTS", font="ar 20 bold")
# displaying the title on the grid box.
Title.grid(row=0, column=2)
# creating labels for data to be filled on the form.
SubCounty = Label(root, text="Sub County")
SchoolName = Label(root, text="School Name")
SchoolEmail_Address = Label(root, text="School Email")
PrincipalsName = Label(root, text="Principals Name")
Principals_Email_Address = Label(root, text="Principal's Email")
Principals_Phone_Number = Label(root, text="Principal's Phone Number")
Principals_TSC_Number = Label(root, text="Principals TSC Number")


#displaying the labels on the grid box.
SubCounty.grid(row=1, column=1)
SchoolName.grid(row=2, column=1)
SchoolEmail_Address.grid(row=3, column=1)
PrincipalsName.grid(row=4, column=1)
Principals_Email_Address.grid(row=5, column=1)
Principals_Phone_Number.grid(row=6, column=1)
Principals_TSC_Number.grid(row=7, column=1)
#creating variables for our entry fields.
N_Subcounty = StringVar
N_SchoolName = StringVar
N_SchoolEmail = StringVar
N_PrincipalsName = StringVar
N_PrincipalsEmail = StringVar
N_PrincipalsPhone = StringVar
N_PrincipalsTSCNO = IntVar
N_CheckValue = IntVar

#Creaating the entry Fileds and displaying them on the GridBox.
SubCounty_Entry = Entry(root, textvariable=N_Subcounty)
SubCounty_Entry.grid(row=1, column=2)
SchoolName_Entry = Entry(root, textvariable=N_SchoolName)
SchoolName_Entry.grid(row=2, column=2)
Schoolemail_Entry = Entry(root, textvariable=N_SchoolEmail)
Schoolemail_Entry.grid(row=3, column=2)
PrincipalsName_Entry = Entry(root, textvariable=N_PrincipalsName)
PrincipalsName_Entry.grid(row=4, column=2)
PrincipalsEmail_Entry = Entry(root, textvariable=N_PrincipalsEmail)
PrincipalsEmail_Entry.grid(row=5, column=2)
PrincipalsPhone_Entry = Entry(root, textvariable=N_PrincipalsPhone)
PrincipalsPhone_Entry.grid(row=6, column=2)
PrincipalsTSCNO_Entry = Entry(root, textvariable=N_SchoolName)
PrincipalsTSCNO_Entry.grid(row=7, column=2)

#creating the remember me checkbutton
Checkbtn = Checkbutton(text = "Remember Me?", variable = N_CheckValue)
Checkbtn.grid(row=8, column=2)

#Submit Button
def getValues():
    print("Records Accepted")
SubmitButton = Button(text= "SUBMIT", command= getValues).grid(row=9, column=2)






root.mainloop()
