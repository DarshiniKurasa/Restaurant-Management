from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillClass
import sqlite3
from tkinter import messagebox
import os
import time
class RMS:

    def __init__ (self, root):
        self.root = root
        self.root.geometry("1350x650+0+0")
        self.root.title("Restaurant Management System")
        self.root.config(bg = "white")

        #===Title====
        self.original_image = Image.open("images/logo1.png")
        self.icon_title = ImageTk.PhotoImage(self.original_image.resize((60, 60)))
        title = Label(self.root,text="Restaurant Management System",image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        btn_logout=Button(self.root, text="Logout", command=self.logout, font=("times new roman",15,"bold"), bg = "yellow", cursor="hand2").place(x=1150,y= 10,height=50,width=100)

    
        
        self.lbl_clock= Label(self.root,text="Welcome to Flavour Fusion\t\t date:DD-MM-YYYY\t\t Time:HH:MM:SS",font=("times new roman", 15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====Left Menu===
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo.resize((200, 180)))
       
        LeftMenu = Frame(self.root, bd = 2, relief=RIDGE, bg = "white")
        LeftMenu.place(x = 0, y = 102, width = 200, height = 565)

        lbl_menuLogo = Label(LeftMenu, image = self.MenuLogo)
        lbl_menuLogo.pack(side="top", fill=X)

        original_image = Image.open("images/side.png")
        resized_image = original_image.resize((25, 25))
        self.icon_side = ImageTk.PhotoImage(resized_image)
  
        lbl_menu= Label(LeftMenu, text="Menu", font=("times new roman",20,), bg = "#009688").pack(side="top",fill=X)
        btm_employee= Button(LeftMenu, text="Employee",command=self.employee, image=self.icon_side,compound=LEFT,padx=10, anchor="w", font=("times new roman",20,"bold"), bg = "white", bd = 3, cursor="hand2",height=37).pack(side="top",fill=X)
        btm_supplier= Button(LeftMenu, text="Supplier",command=self.supplier, image=self.icon_side,compound=LEFT,padx=10, anchor="w",font=("times new roman",20,"bold"), bg = "white", bd = 3, cursor="hand2",height=37).pack(side="top",fill=X)
        btm_category= Button(LeftMenu, text="Category",command = self.category, image=self.icon_side,compound=LEFT,padx=10, anchor="w", font=("times new roman",20,"bold"), bg = "white", bd = 3, cursor="hand2",height=37).pack(side="top",fill=X)
        btm_product= Button(LeftMenu, text="Dishes", command=self.product,image=self.icon_side,compound=LEFT,padx=10, anchor="w",font=("times new roman",20,"bold"), bg = "white", bd = 3, cursor="hand2",height=37).pack(side="top",fill=X)
        btm_bill= Button(LeftMenu, text="Billing",command=self.billing, image=self.icon_side,compound=LEFT,padx=10, anchor="w",font=("times new roman",20,"bold"), bg = "white", bd = 3, cursor="hand2",height=37).pack(side="top",fill=X)
        btm_sales= Button(LeftMenu, text="All Bills",command=self.sales, image=self.icon_side,compound=LEFT,padx=10, anchor="w",font=("times new roman",20,"bold"), bg = "white", bd = 3, cursor="hand2",height=37).pack(side="top",fill=X)
        btm_exit= Button(LeftMenu, text="Exit",command=self.exit, image=self.icon_side,compound=LEFT,padx=10, anchor="w",font=("times new roman",20,"bold"), bg = "white", bd = 3, cursor="hand2",height=37).pack(side="top",fill=X)
        
        #====content=====
        self.lbl_employee= Label(self.root, text = "Total Employee\n[ 0 ]",bd=5, relief=RIDGE ,bg="#33bbf9", fg="white", font = ("gouday old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150, width= 300)

        self.lbl_supplier= Label(self.root, text = "Total Supplier\n[ 0 ]",bd=5, relief=RIDGE ,bg="#ff5722", fg="white", font = ("gouday old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150, width= 300)

        self.lbl_category= Label(self.root, text = "Total Category\n[ 0 ]",bd=5, relief=RIDGE ,bg="#009688", fg="white", font = ("gouday old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150, width= 270)

        self.lbl_product= Label(self.root, text = "Total Product\n[ 0 ]",bd=5, relief=RIDGE ,bg="#607d8b", fg="white", font = ("gouday old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150, width= 300)

        self.lbl_sales= Label(self.root, text = "Total Sales\n[ 0 ]",bd=5, relief=RIDGE ,bg="#ffc107", fg="white", font = ("gouday old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150, width= 300)
        #===footer====
        lbl_footer= Label(self.root,text="RMS-Restaurant Management System\n For any Technical Issue Contact : 8274527233",font=("times new roman", 12),bg="#4d636d",fg="white")
        self.update_content()
        #===========================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Dishes\n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Bills\n[{str(bill)}]')
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m:%Y")
            self.lbl_clock.config(text=f"Welcome to Flavour Fusion\t\t Date:{str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

    def logout(self):
        self.root.destroy()  
        os.system("python welcome.py")
    
    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    img = ImageTk.PhotoImage(file="images/logo1.png")
    root.iconphoto(False,img)
    root.mainloop()