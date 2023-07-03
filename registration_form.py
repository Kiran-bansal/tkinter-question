from tkinter import *
root=Tk()

def formupdate():
    print("Thanks for submitting")
    
    
root.geometry("500x500")
root.title("My form")

Label(root,text="Registration form",font="arial 15 bold").grid(row=0,column=3)

name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)

namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar

checkvalue=IntVar

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)

nameentry.grid(row=1,column=3)

phoneentry.grid(row=2,column=3)

genderentry.grid(row=3,column=3)

checkbtn=Checkbutton(text="Are u eligible",variable=checkvalue)
checkbtn.grid(row=6,column=2)

button=Button(root,text="Submit Form",comman=formupdate).grid(row=6,column=3)


root.mainloop()
