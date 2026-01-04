from tkinter import*
from PIL import ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg="light blue")
        #================Images===========
        
        #==================Login_Frame====================
        self.employee_id=StringVar()
        self.password=StringVar()
        self.var_utype=StringVar()

        login_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=470,y=80,width=400,height=500)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=280)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass = Entry(login_frame, textvariable=self.password, show='•', font=("times new roman", 15), bg="#ECECEC")
        txt_pass.place(x=50, y=240, width=280)
        
        lbl_utype=Label(login_frame,text="User Type" , font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=300)
        cmb_utype = ttk.Combobox(login_frame, textvariable=self.var_utype, values=("Select","Admin", "Employee"), state='readonly', justify=CENTER, font=("times new roman",15))
        cmb_utype.place(x=50,y=340,width=280)
        cmb_utype.current(0)


        
        
        btn_login=Button(login_frame,text="Log In", command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=60,y=400,width=250,height=35)
        
      
    def login(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "" or not self.var_utype.get():
                messagebox.showerror('Error', "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.employee_id.get(),))
                user = cur.fetchone()
                if user is None:
                    messagebox.showerror('Error', "Invalid username/password", parent=self.root)
                else:
                    if user[7] == self.password.get():  
                        if user[8] == self.var_utype.get(): 
                            if self.var_utype.get() == "Employee":
                                self.root.destroy()
                                os.system("python empDashboard.py")
                            elif self.var_utype.get() == "Admin":
                                self.root.destroy()
                                os.system("python adminDashboard.py")
                        else:
                            messagebox.showerror('Error', "Incorrect user type", parent=self.root)
                    else:
                       
                        messagebox.showerror('Error', "Incorrect password", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")




if __name__ == "__main__":
    root=Tk()
    obj=Login_system(root)
    img = ImageTk.PhotoImage(file="images/logo1.png")
    root.iconphoto(False,img)
    root.mainloop()
