from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1050x510+220+130")
        self.root.title("Restaurant Management System")
        self.root.config(bg = "white")
        self.root.focus_force()
        img = ImageTk.PhotoImage(file="images/logo1.png")
        root.iconphoto(False,img)
        #==================================
        #All variables======================
        
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()

        self.var_sup_id=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        self.var_desc = StringVar()

        
        

        #========searchFrame==============#
        #========Options==============#
        lbl_search=Label(self.root,text = "SUP ID",bg = "white",font=("goudy old style",15))
        lbl_search.place(x=700,y=80)
        
        txt_search=Entry(self.root,textvariable=self.var_searchtext,font=("goudy old style",15),bg='lightyellow').place(x=800,y=80, width = 160)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg='#4caf50',fg='white',cursor='hand2').place(x=970,y=79,width=90,height=28)
        #========TITLE==============#

        title=Label(self.root,text="Supplier Details" , font=("goudy old style",20,"bold "),bg='#0f4d7d',fg='white').place(x=50,y=10,height = 40,width=950)


        #=============Content============#
        #=============ROW-1============#

        lbl_supplier_id=Label(self.root,text="SUP ID" , font=("goudy old style",15),bg='white').place(x=50,y=80)
        txt_supplier_id=Entry(self.root,textvariable=self.var_sup_id, font=("goudy old style",15),bg='lightyellow').place(x=180,y=80,width=180)
        
        #=============ROW-2============#
        lbl_name=Label(self.root,text="Name" , font=("goudy old style",15),bg='white').place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style",15),bg='lightyellow').place(x=180,y=120,width=180)

         #=============ROW-3============#
        lbl_contact=Label(self.root,text="Contact" , font=("goudy old style",15),bg='white').place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact, font=("goudy old style",15),bg='lightyellow').place(x=180,y=160,width=180)
       

         #=============ROW-4============#
        lbl_desc=Label(self.root,text="Description" , font=("goudy old style",15),bg='white').place(x=50,y=200)
        self.txt_desc=Text(self.root, font=("goudy old style",15),bg='lightyellow')
        self.txt_desc.place(x=180,y=200,width=470,height=120)
        
        #==========BUTTONS===================
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg='#2196f3',fg='white',cursor='hand2').place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg='#4caf50',fg='white',cursor='hand2').place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg='#f44336',fg='white',cursor='hand2').place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg='#607d8b',fg='white',cursor='hand2').place(x=540,y=370,width=110,height=35)

       #==========Employee Details===================
        
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(emp_frame,columns=("sid","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)


        self.SupplierTable.heading("sid",text="Supplier ID")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Description")
        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("sid",width=80)
        self.SupplierTable.column("name",width=80)
        self.SupplierTable.column("contact",width=80)
        self.SupplierTable.column("desc",width=90)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#=======================ADD====================================================
    def add(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if not self.var_sup_id.get().isdigit() or not self.var_name.get() or not self.var_contact.get() or not self.txt_desc.get('1.0', END).strip():
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            elif not self.var_sup_id.get().isdigit():
                messagebox.showerror("Error", "Supplier ID must be a numeric value", parent=self.root)
            elif not self.var_name.get().isalpha():
                messagebox.showerror("Error", "Name should contain only alphabets", parent=self.root)
            elif not self.var_contact.get().isdigit() or len(self.var_contact.get()) != 10:
                messagebox.showerror("Error", "Contact should contain exactly 10 numeric digits", parent=self.root)
           
            else:
                cur.execute("SELECT * FROM supplier WHERE sid=?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Supplier ID already assigned, try different")
                else:
                    cur.execute("INSERT INTO supplier (sid, name, contact, desc) VALUES (?, ?, ?, ?)",
                                (self.var_sup_id.get(),
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.txt_desc.get('1.0', END)))

                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)

    #=======================SHOW==================================================


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

    #=======================GETDATA=====================================
    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        # print(row)
        self.var_sup_id.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])
        


#===============UPDATE========================================================



    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get()=="":
                messagebox.showerror("Error","Supplier ID must be required",parent=root)
            else:
                cur.execute("Select * from supplier where sid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    cur.execute("Update supplier  set name=?,contact=?,desc=? where sid=?",(
                             self.var_name.get(),
                             self.var_contact.get(),
                             self.txt_desc.get('1.0',END),
                             self.var_sup_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

#===============DELETE==========================================================
    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get()=="":
                messagebox.showerror("Error","Supplier id must be required",parent=root)
            else:
                cur.execute("Select * from supplier where sid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid supplier ID",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where sid=?",(self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

#=============================CLEAR====================================
    def clear(self):
        self.var_sup_id.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtext.set("")
        self.show()

#=================SEARCH========================
    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtext.get()=="":
                messagebox.showerror("Error","Supplier ID should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where sid = ?",(self.var_searchtext.get(),))
                row=cur.fetchone()
                if row != None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")




if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()