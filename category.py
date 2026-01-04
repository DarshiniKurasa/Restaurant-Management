from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1060x510+220+130")
        self.root.title("Restaurant Management System")
        self.root.config(bg = "white")
        self.root.focus_force()
        img = ImageTk.PhotoImage(file="images/logo1.png")
        root.iconphoto(False,img)
        #======Variables====
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
        #====title===
        lbl_title = Label(self.root, text="Manage Category", font = ("goudy old style",30), bg = "#184a45", fg = "white", bd = 3,relief= RIDGE).pack(side=TOP, fill=X, padx = 10,pady = 20)

        lbl_id = Label(self.root, text="Category ID", font = ("goudy old style",15), bg = "white").place(x=50,y = 100)
        txt_id = Entry(self.root, textvariable=self.var_cat_id, font = ("goudy old style",15), bg = "lightyellow").place(x=200,y = 100, width=300)
         
        
        lbl_name = Label(self.root, text="Category Name", font = ("goudy old style",15), bg = "white").place(x=50,y = 135)
        txt_name = Entry(self.root, textvariable=self.var_name, font = ("goudy old style",15), bg = "lightyellow").place(x=200,y = 135, width=300)
         
        btn_add = Button(self.root, text="ADD",command=self.add, font = ("goudy old style",15), bg = "#4acf50", fg = "white", cursor="hand2").place(x=80,y = 180, width=150, height = 30)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font = ("goudy old style",15), bg = "red", fg = "white", cursor="hand2").place(x=300,y = 180, width=150, height = 30)

        #==========Category Details===================
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=600,y=100,width=480,height=380)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)


        self.category_table.heading("cid",text="C ID")
        self.category_table.heading("name",text="Name")
        self.category_table["show"]="headings"

        self.category_table.column("cid",width=90)
        self.category_table.column("name",width=100)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        #===Images===
        self.im1 = Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,250))
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.lbl_im1= Label(self.root, image= self.im1,bd = 2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)
        self.show()

        #=======================ADD====================================================
    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if not self.var_cat_id.get():
                messagebox.showerror("Error","Category id is must", parent=root)
            elif not self.var_cat_id.get().isdigit():
                messagebox.showerror("Error","Category id must be numeric", parent=root)
            elif not self.var_name.get():
                messagebox.showerror("Error","Category name must be required",parent=root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category id already present, try different")
                else:
                    cur.execute("INSERT INTO category ( cid,name) VALUES (?, ?)",
                            (self.var_cat_id.get(),
                                self.var_name.get(),
            
                            ))
                   
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
    #=======================SHOW==================================================


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

    #=======================GETDATA=====================================
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        # print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    #===============DELETE==========================================================
    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please select category from the list",parent=root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()