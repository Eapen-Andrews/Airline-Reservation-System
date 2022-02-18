#importing all required modules
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image
import datetime
import mysql.connector
import webbrowser
root = Tk()

root.title('FORTITUDE AIRLINES')



#functions
def __init__(self,master):
    self.master=master
    
def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("The name is : " + name)
    print("The password is : " + password)
     
    name_var.set("")
    passw_var.set("")


def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

def book():
    root1=Tk()
    root1.title("Welcome,Search flights")
    inputtxt = Text(root1,height = 1,width = 20)
    Label(root1,text="Enter Passenger Name").pack()
    e = Entry(root1)
    e.pack()
    e.focus_set()
    inp = inputtxt.get(1.0, "end-1c")
    Label(root1,text="Select Flight").pack()
    w2=ttk.Combobox(root1,height=5,width=50,values=["1.(COK)COCHIN-(DXB)DUBAI","2.(ABD)ABU-DHABI-(MB)MUMBAI","3.(DXB)DUBAI-(LDN)LONDON","4.(COK)COCHIN-(SG)SINGAPORE"])
    w2.pack()
    Label(root1,text="Choose Cabin Class").pack()
    w3=ttk.Combobox(root1,text="Cabin Class",height=5,width=15,values=["Economy",'Business','First'])
    w3.pack()
    def select():
        a=e.get()
        b=w2.get()
        c=w3.get()
        if a=='' or b=='' or c=='':
            messagebox.showerror("Error","Cant leave any field empty")
        sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123456789',database='airlinedb')
        if sqlcon.is_connected():
            messagebox.showinfo('Loading...')
            crsobj=sqlcon.cursor()
            if b=='1.(COK)COCHIN-(DXB)DUBAI':
                crsobj.execute(f'INSERT INTO FA9725 (PASSENGER,CLASS) VALUES("{a}","{c}")')
                sqlcon.commit()
                messagebox.showinfo('showinfo',"Ticket Succesfully Reserved")
            elif b=="2.(ABD)ABU-DHABI-(MB)MUMBAI":
                crsobj.execute(f'INSERT INTO FA2517 (PASSENGER,CLASS) VALUES("{a}","{c}")')
                sqlcon.commit()
                messagebox.showinfo('showinfo',"Ticket Succesfully Reserved")
            elif b=="3.(DXB)DUBAI-(LDN)LONDON":
                crsobj.execute(f'INSERT INTO FA2550 (PASSENGER,CLASS) VALUES("{a}","{c}")')
                sqlcon.commit()
                messagebox.showinfo('showinfo',"Ticket Succesfully Reserved")
            elif b=="4.(COK)COCHIN-(SG)SINGAPORE":
                crsobj.execute(f'INSERT INTO FA9711 (PASSENGER,CLASS) VALUES("{a}","{c}")')
                sqlcon.commit()
                messagebox.showinfo('showinfo',"Ticket Succesfully Reserved")
            else:
                messagebox.showerror("showinfo",'Error')
            crsobj.close()
            sqlcon.close()
    Bs=Button(root1,text="SELECT",command=select).pack()
    root1.mainloop()
                
def check():
    root2=Tk()
    root2.title("Check In")
    inputtxt = Text(root2,height = 1,width = 20)
    Label(root2,text="Enter Passenger Name").pack()
    e = Entry(root2)
    e.pack()
    e.focus_set()
    Label(root2,text="Select Flight").pack()
    w2=ttk.Combobox(root2,height=5,width=50,values=["1.(COK)COCHIN-(DXB)DUBAI","2.(ABD)ABU-DHABI-(MB)MUMBAI","3.(DXB)DUBAI-(LDN)LONDON","4.(COK)COCHIN-(SG)SINGAPORE"])
    w2.pack()
    def select2():
        a=e.get()
        b=w2.get()
        if a=='' or b=='':
            messagebox.showerror("Error","Cant leave any field empty")
        sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123456789',database='airlinedb')
        if sqlcon.is_connected():
            messagebox.showinfo('Loading...')
            crsobj=sqlcon.cursor()
            if b=='1.(COK)COCHIN-(DXB)DUBAI':
                crsobj.execute(f'UPDATE FA9725 SET STATUS="CHECKED IN" WHERE PASSENGER="{a}"')
                sqlcon.commit()
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root2,text=x).pack()
            elif b=="2.(ABD)ABU-DHABI-(MB)MUMBAI":
                crsobj.execute(f'UPDATE FA2517 SET STATUS="CHECKED IN" WHERE PASSENGER="{a}"')
                sqlcon.commit()
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA2517 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root2,text=x).pack()
            elif b=="3.(DXB)DUBAI-(LDN)LONDON":
                crsobj.execute(f'UPDATE FA2550 SET STATUS="CHECKED IN" WHERE PASSENGER="{a}"')
                sqlcon.commit()
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root2,text=x).pack()
            elif b=="4.(COK)COCHIN-(SG)SINGAPORE":
                crsobj.execute(f'UPDATE FA9711 SET STATUS="CHECKED IN" WHERE PASSENGER="{a}"')
                sqlcon.commit()
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root2,text=x).pack()
                
            else:
                messagebox.showerror("showinfo",'Error')
            crsobj.close()
            sqlcon.close()
    Bs=Button(root2,text="SELECT",command=select2).pack()
    root2.mainloop()
            
def cancel():
    root3=Tk()
    root3.title("Cancel")
    inputtxt = Text(root3,height = 1,width = 20)
    Label(root3,text="Enter Passenger Name").pack()
    e = Entry(root3)
    e.pack()
    e.focus_set()
    Label(root3,text="Select Flight").pack()
    w2=ttk.Combobox(root3,height=5,width=50,values=["1.(COK)COCHIN-(DXB)DUBAI","2.(ABD)ABU-DHABI-(MB)MUMBAI","3.(DXB)DUBAI-(LDN)LONDON","4.(COK)COCHIN-(SG)SINGAPORE"])
    w2.pack()
    def select3():
        a=e.get()
        b=w2.get()
        if a=='' or b=='':
            messagebox.showerror("Error","Cant leave any field empty")
        sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123456789',database='airlinedb')
        if sqlcon.is_connected():
            messagebox.showinfo('Loading...')
            crsobj=sqlcon.cursor()
            if b=='1.(COK)COCHIN-(DXB)DUBAI':
                crsobj.execute(f'UPDATE FA9725 SET STATUS="CANCELED" WHERE PASSENGER="{a}"')
                sqlcon.commit()
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root3,text=x).pack()
            elif b=="2.(ABD)ABU-DHABI-(MB)MUMBAI":
                crsobj.execute(f'UPDATE FA2517 SET STATUS="CANCELED" WHERE PASSENGER="{a}"')
                sqlcon.commit()
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA2517 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root3,text=x).pack()
            elif b=="3.(DXB)DUBAI-(LDN)LONDON":
                crsobj.execute(f'UPDATE FA2550 SET STATUS="CANCELED" WHERE PASSENGER="{a}"')
                sqlcon.commit()
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root3,text=x).pack()
            elif b=="4.(COK)COCHIN-(SG)SINGAPORE":
                crsobj.execute(f'UPDATE FA9711 SET STATUS="CANCELED" WHERE PASSENGER="{a}"')
                sqlcon.commit()
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root3,text=x).pack()
                
            else:
                messagebox.showerror("showinfo",'Error')
            crsobj.close()
            sqlcon.close()
    Bs=Button(root3,text="SELECT",command=select3).pack()
    root3.mainloop()
    
def view():
    root4=Tk()
    root4.title("View Ticket")
    
    inputtxt = Text(root4,height = 1,width = 20)
    Label(root4,text="Enter Passenger Name").pack()
    e = Entry(root4)
    e.pack()
    e.focus_set()
    Label(root4,text="Select Flight").pack()
    w2=ttk.Combobox(root4,height=5,width=50,values=["1.(COK)COCHIN-(DXB)DUBAI","2.(ABD)ABU-DHABI-(MB)MUMBAI","3.(DXB)DUBAI-(LDN)LONDON","4.(COK)COCHIN-(SG)SINGAPORE"])
    w2.pack()
    def select4():
        a=e.get()
        b=w2.get()
        if a=='' or b=='':
            messagebox.showerror("Error","Cant leave any field empty")
        sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123456789',database='airlinedb')
        if sqlcon.is_connected():
            messagebox.showinfo('Loading...')
            crsobj=sqlcon.cursor()
            if b=='1.(COK)COCHIN-(DXB)DUBAI':
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root4,text=x).pack()
            elif b=="2.(ABD)ABU-DHABI-(MB)MUMBAI":
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA2517 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root4,text=x).pack()
            elif b=="3.(DXB)DUBAI-(LDN)LONDON":
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root4,text=x).pack()
            elif b=="4.(COK)COCHIN-(SG)SINGAPORE":
                crsobj.execute(f'select PASSENGER,DESTINATION,CLASS,STATUS FROM FA9725 WHERE PASSENGER="{a}"')
                x=crsobj.fetchone()
                label=Label(root4,text=x).pack()
                
            else:
                messagebox.showerror("showinfo",'Error')
            crsobj.close()
            sqlcon.close()
    Bs=Button(root4,text="SELECT",command=select4).pack()
    root4.mainloop()
            
def staff():
    root5=Tk()
    root5.title("Staff")
    inputtxt = Text(root5,height = 1,width = 20)
    Label(root5,text="USER ID").pack()
    e1= Entry(root5)
    e1.pack()
    e1.focus_set()
    inputtxt2 = Text(root5,height = 1,width = 20)
    Label(root5,text="PASSWORD").pack()
    e2= Entry(root5)
    e2.pack()
    e2.focus_set()
    def select5():
        a=e1.get()
        b=e2.get()
        if a=='admin' and b=='admin123':
            root6=Tk()
            root6.title("staff")
            Label(root6,text="Choose Action").pack()
            w2=ttk.Combobox(root6,height=5,width=50,values=["1.Remove Passenger","2.View"])
            w2.pack()
            c=w2.get()
            def select6():
                c=w2.get()
                if c=="2.View":
                    root8=Tk()
                    Label(root8,text="Choose Flight").pack()
                    w3=ttk.Combobox(root8,height=5,width=50,values=["1.(COK)COCHIN-(DXB)DUBAI","2.(ABD)ABU-DHABI-(MB)MUMBAI","3.(DXB)DUBAI-(LDN)LONDON","4.(COK)COCHIN-(SG)SINGAPORE"])
                    w3.pack()
                    def select8():
                        c1=w3.get()
                        sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123456789',database='airlinedb')
                        if sqlcon.is_connected():
                            messagebox.showinfo('Loading...')
                            crsobj=sqlcon.cursor()
                            if c1=='1.(COK)COCHIN-(DXB)DUBAI':
                                crsobj.execute(f'SELECT * FROM FA9725')
                                x=crsobj.fetchall()
                                for i in x:
                                    label=Label(root8,text=i).pack()
                            elif c1=="2.(ABD)ABU-DHABI-(MB)MUMBAI":
                                crsobj.execute(f'SELECT * FROM FA2517')
                                x=crsobj.fetchall()
                                for i in x:
                                    label=Label(root8,text=i).pack()
                            elif c1=="3.(DXB)DUBAI-(LDN)LONDON":
                                crsobj.execute(f'SELECT * FROM FA2550')
                                x=crsobj.fetchall()
                                for i in x:
                                    label=Label(root8,text=i).pack()
                            elif c1=="4.(COK)COCHIN-(SG)SINGAPORE":
                                crsobj.execute(f'SELECT * FROM FA9711')
                                x=crsobj.fetchall()
                                for i in x:
                                    label=Label(root8,text=i).pack()
                            
                
                        else:
                            messagebox.showerror("showerror",'Error')
                        crsobj.close()
                        sqlcon.close()
                    bs3=Button(root8,text="OK",command=select8).pack()

                elif c=="1.Remove Passenger":
                    root7=Tk()
                    root7.title("Remove")
                    inputtxt = Text(root7,height = 1,width = 20)
                    Label(root7,text="Enter Passenger Name").pack()
                    e = Entry(root7)
                    e.pack()
                    e.focus_set()
                    Label(root7,text="Choose Flight").pack()
                    w3=ttk.Combobox(root7,height=5,width=50,values=["1.(COK)COCHIN-(DXB)DUBAI","2.(ABD)ABU-DHABI-(MB)MUMBAI","3.(DXB)DUBAI-(LDN)LONDON","4.(COK)COCHIN-(SG)SINGAPORE"])
                    w3.pack()
                    
                    def select7():
                        c1=w3.get()
                        c2=e.get()
                        sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123456789',database='airlinedb')
                        if sqlcon.is_connected():
                        
                            messagebox.showinfo('Loading...')
                            crsobj=sqlcon.cursor()
                            if c1=='1.(COK)COCHIN-(DXB)DUBAI':
                                crsobj.execute(f'DELETE FROM FA9725 WHERE PASSENGER="{c2}"')
                                sqlcon.commit()
                                messagebox.showinfo('showinfo','Passenger Details Removed')
                            elif c1=="2.(ABD)ABU-DHABI-(MB)MUMBAI":
                                crsobj.execute(f'DELETE FROM FA2517 WHERE PASSENGER="{c2}"')
                                sqlcon.commit()
                                messagebox.showinfo('showinfo','Passenger Details Removed')
                            elif c1=="3.(DXB)DUBAI-(LDN)LONDON":
                                crsobj.execute(f'DELETE FROM FA2550 WHERE PASSENGER="{c2}"')
                                sqlcon.commit()
                                messagebox.showinfo('showinfo','Passenger Details Removed')
                            elif c1=="4.(COK)COCHIN-(SG)SINGAPORE":
                                crsobj.execute(f'DELETE FROM FA9711 WHERE PASSENGER="{c2}"')
                                sqlcon.commit()
                                messagebox.showinfo('showinfo','Passenger Details Removed')
                        else:
                            messagebox.showerror("showerror",'Error')
                        crsobj.close()
                        sqlcon.close()
                    bs2=Button(root7,text="OK",command=select7).pack()
                    
                
            bs1=Button(root6,text="OK",command=select6).pack()

                        
                            
                        
                    
                
        else:
            messagebox.showinfo("showinfo","Invalid User")
    Bs=Button(root5,text="OK",command=select5).pack()
    root5.mainloop()

'''def staff():
    root5=Tk()
    root5.title("Staff")
    inputtxt = Text(root5,height = 1,width = 20)
    Label(root5,text="USER ID").pack()
    e1= Entry(root5)
    e1.pack()
    e1.focus_set()
    inputtxt2 = Text(root5,height = 1,width = 20)
    Label(root5,text="PASSWORD").pack()
    e2= Entry(root5)
    e2.pack()
    e2.focus_set()
    def select5():
        a=e1.get()
        b=e2.get()
        if a=='admin' and b=='admin123':
            root6=Tk()
            root6.title("staff")
            Label(root6,text="Choose Action").pack()
            w2=ttk.Combobox(root6,height=5,width=50,values=["1.Remove Passenger","2.View"])
            w2.pack()
            c=w2.get()
            if c=="2.View":
                
                root7=Tk()
                root7.title("View")
                
                w3=ttk.Combobox(root7,height=5,width=50,values=["1.(COK)COCHIN-(DXB)DUBAI","2.(ABD)ABU-DHABI-(MB)MUMBAI","3.(DXB)DUBAI-(LDN)LONDON","4.(COK)COCHIN-(SG)SINGAPORE"])
                w3.pack()
                c1=w3.get()
                def select6():
                    sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123456789',database='airlinedb')
                    if sqlcon.is_connected():
                        messagebox.showinfo('Loading...')
                        crsobj=sqlcon.cursor()
                        if c1=='1.(COK)COCHIN-(DXB)DUBAI':
                            crsobj.execute(f'SELECT * FROM FA9725')
                            x=crsobj.fetchall()
                            for i in x:
                                label=Label(root6,text=i).pack()
                        elif c1=="2.(ABD)ABU-DHABI-(MB)MUMBAI":
                            crsobj.execute(f'SELECT * FROM FA2517')
                            x=crsobj.fetchall()
                            for i in x:
                                label=Label(root6,text=i).pack()
                        elif c1=="3.(DXB)DUBAI-(LDN)LONDON":
                            crsobj.execute(f'SELECT * FROM FA2550')
                            x=crsobj.fetchall()
                            for i in x:
                                label=Label(root6,text=i).pack()
                        elif c1=="4.(COK)COCHIN-(SG)SINGAPORE":
                            crsobj.execute(f'SELECT * FROM FA9711')
                            x=crsobj.fetchall()
                            for i in x:
                                label=Label(root7,text=i).pack()
                
                    else:
                        
                        messagebox.showerror("showerror",'Error')
                        crsobj.close()
                        sqlcon.close()
                bs1=Button(root,text="OK",command=select6).pack()
            elif c=='1.Remove Passenger':
                root7=Tk()
                root7.title("View")
                inputtxt = Text(root7,height = 1,width = 20)
                Label(root7,text="Enter Passenger Name").pack()
                e = Entry(root7)
                e.pack()
                e.focus_set()
                w3=ttk.Combobox(root7,height=5,width=50,values=["1.(COK)COCHIN-(DXB)DUBAI","2.(ABD)ABU-DHABI-(MB)MUMBAI","3.(DXB)DUBAI-(LDN)LONDON","4.(COK)COCHIN-(SG)SINGAPORE"])
                w3.pack()
                c1=w3.get()
                c2=e.get()
                def select7():
                    sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123456789',database='airlinedb')
                    if sqlcon.is_connected():
                        messagebox.showinfo('Loading...')
                            crsobj=sqlcon.cursor()
                        if c1=='1.(COK)COCHIN-(DXB)DUBAI':
                            crsobj.execute(f'DELETE FROM FA9725 WHERE PASSENGER="{e}"')
                            sqlcon.commit()
                            messagebox.showinfo('showinfo','Passenger Details Removed')
                        elif c1=="2.(ABD)ABU-DHABI-(MB)MUMBAI":
                            crsobj.execute(f'DELETE FROM FA2517 WHERE PASSENGER="{e}"')
                            sqlcon.commit()
                            messagebox.showinfo('showinfo','Passenger Details Removed')
                        elif c1=="3.(DXB)DUBAI-(LDN)LONDON":
                            crsobj.execute(f'DELETE FROM FA2550 WHERE PASSENGER="{e}"')
                            sqlcon.commit()
                            messagebox.showinfo('showinfo','Passenger Details Removed')
                        elif c1=="4.(COK)COCHIN-(SG)SINGAPORE":
                            crsobj.execute(f'DELETE FROM FA9711 WHERE PASSENGER="{e}"')
                            sqlcon.commit()
                            messagebox.showinfo('showinfo','Passenger Details Removed')
                    else:
                       messagebox.showerror("showerror",'Error')
                       crsobj.close()
                       sqlcon.close()
                bs1=Button(root7,text="OK",command=select7).pack()
                        
                            
                        
                    
                
        else:
            messagebox.showinfo("showinfo","Invalid User")
    Bs=Button(root5,text="OK",command=select5).pack()
    root5.mainloop()'''   


def about():
    
    response=messagebox.askokcancel("Redirect",'Redirecting you to https://github.com/Eapen-Andrews/ARS',default='ok')
    if response is False:
        return "cancel"
    else:
        webbrowser.open('https://github.com/Eapen-Andrews/ARS.git',new=0,autoraise=True)
    
def exit():
    root.destroy()
    


# image object for icon
icon = PhotoImage(file="./plane 2.gif")
root.iconphoto(1, icon)
'''image = Image.open('logo.gif')
image = image.resize((50,50), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = Label(image = my_img)
my_img.pack(side='bottom')'''

img2 = ImageTk.PhotoImage(Image.open("logo.gif"))
panel = Label(root, image = img2,bg='white')
panel.pack(side= "bottom",expand=0)




# dimensions of window
root.geometry('400x400')

# tab navigation
tabs = ttk.Notebook(root)

# screens
Fortitude=Frame(root)
homeSc = Frame(root)
bookSc = Frame(root)
statSc = Frame(root)
viewSc = Frame(root)

staffSc = Frame(root)
AboutSc = Frame(root)
exitSc = Frame(root)


# adding screens to the tab navigation structure
tabs.add(Fortitude,text='Fortitude')
tabs.add(homeSc, text='Home')
tabs.add(bookSc, text='Book Tickets')
tabs.add(statSc,text="Ticket status")
tabs.add(viewSc, text='View ticket')
tabs.add(staffSc, text='Staff Log-in')
tabs.add(AboutSc, text='View')
tabs.add(exitSc, text='Exit')


# hiding temporary tab
tabs.hide(4)

tabs.pack(expand=1, fill=BOTH)


#buttons
button1 = Frame(homeSc)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
button2= Frame(bookSc)
button2.place(relx=0.5, rely=0.5, anchor=CENTER)
button3=Frame(statSc)
button3.place(relx=0.5, rely=0.5, anchor=E)
button4=Frame(statSc)
button4.place(relx=0.5, rely=0.5, anchor=W)
button5=Frame(AboutSc)
button5.place(relx=0.5, rely=0.5, anchor=E)
button6=Frame(staffSc)
button6.place(relx=0.5, rely=0.5, anchor=CENTER)
button7=Frame(AboutSc)
button7.place(relx=0.5, rely=0.5, anchor=W)
button8=Frame(exitSc)
button8.place(relx=0.5, rely=0.5, anchor=CENTER)

#label for home screen
welcome_Label = Label(
    button1, text='Airline Rservation System\n', font='algerian 30')
welcome_Label.pack(pady=10)




#definig buttons


Button(button2, text='Book New Tickets',
       font='helvetica 15', width=25, command=lambda root=root:book()).pack(pady=10)
Button(button3, text='Check-In', font='helvetica 15',
       width=25, command=lambda root=root:check()).pack(pady=10)
Button(button4, text='Cancel Tickets', font='helvetica 15',width=25, command=lambda root=root:cancel()).pack(pady=10)
Button(button5, text='View Ticket', font='helvetica 15',
       width=25, command=lambda root=root:view()).pack(pady=10)
Button(button6, text='Staff login', font='helvetica 15',
       width=25, command=lambda root=root:staff()).pack(pady=10)
Button(button7, text='Project Details', font='helvetica 15',
       width=25, command=lambda root=root:about()).pack(pady=10)
Button(button8, text='Exit', font='helvetica 15',
       width=25, command=lambda root=root:exit()).pack(pady=10)




mainloop()


