import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
import os

def login():
    root.destroy()  
    os.system("python login.py")

root = tk.Tk()
root.title("Restaurant Website")
root.geometry("1350x650+0+0")


bg_image = Image.open("images/welcome.png")  
bg_image = bg_image.resize((1370, 650), Image.ANTIALIAS) if hasattr(Image, 'ANTIALIAS') else bg_image.resize((1370, 650))
background = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=background)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
welcome_label = tk.Label(root, text="Flavours Fusion", font=('Helvetica', 36, 'bold'),  bg="black", fg="white")
welcome_label.place(relx=0.5, rely=0.45, anchor="center")


login_button = tk.Button(root, text="Login", command=login, font=('Helvetica', 20, 'bold'),  bg="black", fg="white")
login_button.place(x=1150,y= 10,height=40,width=100)

img = ImageTk.PhotoImage(file="images/logo1.png")
root.iconphoto(False,img)
root.mainloop()
