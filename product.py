
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1060x510+220+130")
        self.root.title("Restaurant Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        img = ImageTk.PhotoImage(file="images/logo1.png")
        root.iconphoto(False,img)
        self.var_searchby = StringVar()
        self.var_searchtext = StringVar()
        self.var_productID = StringVar()
        self.var_cat = StringVar()
        self.cat_list = []
        self.fetch_cat_sup()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        product_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_Frame.place(x=10, y=10, width=450, height=480)

        title = Label(product_Frame, text=" Manage Dishes", font=("goudy old style", 18), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        lbl_productID = Label(product_Frame, text="Product ID", font=("goudy old style", 18), bg="white").place(x=30, y=60)
        lbl_category = Label(product_Frame, text="Category", font=("goudy old style", 18), bg="white").place(x=30, y=110)
        lbl_product_name = Label(product_Frame, text="Name", font=("goudy old style", 18), bg="white").place(x=30, y=160)
        lbl_price = Label(product_Frame, text="Price", font=("goudy old style", 18), bg="white").place(x=30, y=210)
        lbl_quantity = Label(product_Frame, text="Quantity", font=("goudy old style", 18), bg="white").place(x=30, y=260)
        lbl_status = Label(product_Frame, text="Status", font=("goudy old style", 18), bg="white").place(x=30, y=310)

        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER, font=("goudy old style,", 15))
        cmb_cat.place(x=150, y=110, width=200)
        cmb_cat.current(0)

        txt_productID = Entry(product_Frame, textvariable=self.var_productID, font=("goudy old style,", 15), bg='lightyellow').place(x=150, y=60, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style,", 15), bg='lightyellow').place(x=150, y=160, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style,", 15), bg='lightyellow').place(x=150, y=210, width=200)
        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style,", 15), bg='lightyellow').place(x=150, y=260, width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("goudy old style,", 15))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

        btn_add = Button(product_Frame, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor='hand2').place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor='hand2').place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor='hand2').place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor='hand2').place(x=340, y=400, width=100, height=40)

        SearchFrame = LabelFrame(self.root, text="Search Dishes", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg='white')
        SearchFrame.place(x=480, y=10, width=600, height=80)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Category", "Name"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtext, font=("goudy old style", 15), bg='lightyellow').place(x=200, y=10)
        btn_search = Button(SearchFrame, text="search", command=self.search, font=("goudy old style", 15), bg='#4caf50', fg='white', cursor='hand2').place(x=420, y=8, width=150, height=30)

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame, columns=("pid", "Category", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="P ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Qty")
        self.product_table.heading("status", text="Status")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("Category", width=100)
        self.product_table.column("name", width=150)
        self.product_table.column("price", width=70)
        self.product_table.column("qty", width=70)
        self.product_table.column("status", width=90)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    
    def add(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if not self.var_cat.get() or not self.var_name.get() or not self.var_price.get() or not self.var_qty.get() or not self.var_productID.get():
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            elif not (self.var_productID.get().isdigit() and self.var_price.get().isdigit() and self.var_qty.get().isdigit()):
                messagebox.showerror("Error", "Product ID, Price, and Quantity should be numeric", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Dish already exists, try different", parent=self.root)
                else:
                    cur.execute("INSERT INTO product (pid, Category, name, price, qty, status) VALUES (?, ?, ?, ?, ?, ?)", (
                        self.var_productID.get(),
                        self.var_cat.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


    def show(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT pid, Category, name, price, qty, status FROM product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                # Check if the category is None, if so, replace it with an empty string
                category = row[1] if row[1] is not None else ""
                self.product_table.insert('', END, values=(row[0], category, row[2], row[3], row[4], row[5]))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.var_productID.set(row[0])
        self.var_cat.set(row[1])
        self.var_name.set(row[2])
        self.var_price.set(row[3])
        self.var_qty.set(row[4])
        self.var_status.set(row[5])

    def update(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_productID.get() == "":
                messagebox.showerror("Error", "Please select dish from list", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_productID.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid dish ", parent=self.root)
                else:
                    cur.execute("UPDATE product SET Category=?, name=?, price=?, qty=?, status=? WHERE pid=?", (
                        self.var_cat.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_productID.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def delete(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_productID.get() == "":
                messagebox.showerror("Error", "Select product from the list", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_productID.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid product", parent=self.root)
                else:
                    op = messagebox.askyesno("confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM product WHERE pid=?", (self.var_productID.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def clear(self):
        self.var_cat.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_productID.set("")
        self.var_searchtext.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By option", parent=self.root)
            elif self.var_searchtext.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE " + self.var_searchby.get() + " LIKE '%" + self.var_searchtext.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        reordered_row = (row[0], row[1], row[2], row[3], row[4], row[5])  
                        self.product_table.insert('', END, values=reordered_row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
