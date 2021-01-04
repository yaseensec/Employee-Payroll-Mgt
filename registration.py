import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk,ImageDraw
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="#161B21")
        
        ###Bg Image####
        self.bg=ImageTk.PhotoImage(file="images/bg.jpg")
        bg=tk.Label(self.root,image=self.bg)
        bg.place(x=250,y=0,relwidth=1,relheight=1)
        
        ###Left Image####
        self.left=ImageTk.PhotoImage(file="images/side.jpg")
        left=tk.Label(self.root,image=self.left)
        left.place(x=80,y=100,width=400,height=500)
        
        ##Register tk.Frame###
        frame1=tk.Frame(self.root,bg="#161B21")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=tk.Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="#161B21",fg="#F4A950")
        title.place(x=50,y=30)
        
        #----------------ROW 1--------------------------#
        f_name=tk.Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="#161B21",fg="#F4A950")
        f_name.place(x=50,y=100)
        
        self.txt_fname=tk.Entry(frame1,font=("times new roman",15),bg="#161B21",fg="White")
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name=tk.Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="#161B21",fg="#F4A950")
        l_name.place(x=370,y=100)
        
        self.txt_lname=tk.Entry(frame1,font=("times new roman",15),bg="#161B21",fg="White")
        self.txt_lname.place(x=370,y=130,width=250)
        
        #--------------------ROW 2-----------------------------#
        contact=tk.Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="#161B21",fg="#F4A950")
        contact.place(x=50,y=170)
        
        self.txt_contact=tk.Entry(frame1,font=("times new roman",15),bg="#161B21",fg="White")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=tk.Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="#161B21",fg="#F4A950")
        email.place(x=370,y=170)
        
        self.txt_email=tk.Entry(frame1,font=("times new roman",15),bg="#161B21",fg="White")
        self.txt_email.place(x=370,y=200,width=250)
        
        #------------------ROW 3-------------------------------#
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TCombobox', background = 'gray',foreground="White")
        style.map('TCombobox', fieldbackground=[('readonly','#161B21')])
        
        question=tk.Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="#161B21",fg="#F4A950")
        question.place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=tk.CENTER)
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.current(0)
        
        answer=tk.Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="#161B21",fg="#F4A950")
        answer.place(x=370,y=240)
        
        self.txt_answer=tk.Entry(frame1,font=("times new roman",15),bg="#161B21",fg="White")
        self.txt_answer.place(x=370,y=270,width=250)
        
        #--------------------ROW 4-----------------------------#
        passwd=tk.Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="#161B21",fg="#F4A950")
        passwd.place(x=50,y=310)
        
        self.txt_passwd=tk.Entry(frame1,font=("times new roman",15),bg="#161B21",fg="White")
        self.txt_passwd.place(x=50,y=340,width=250)
        
        cpasswd=tk.Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="#161B21",fg="#F4A950")
        cpasswd.place(x=370,y=310)
        
        self.txt_cpasswd=tk.Entry(frame1,font=("times new roman",15),bg="#161B21",fg="White")
        self.txt_cpasswd.place(x=370,y=340,width=250)
        
        #--------Terms & Conditions---------#
        self.var_chk=tk.IntVar()
        chk=tk.Checkbutton(frame1,text="Agree to Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="#161B21",fg="#F4A950",activebackground="#F4A950",activeforeground="#161B21",font=("times new roman",12))
        chk.place(x=50,y=385)
        
        #--------Register & Signin Buttons------------#
        btn_register=tk.Button(frame1,text="Register Now",font=("times new roman",13),bg="#161B21",fg="#F4A950",activebackground="#F4A950",activeforeground="#161B21",bd=0,cursor="hand2",command=self.register_data)
        btn_register.place(x=50,y=430)
        
        btn_login=tk.Button(self.root,text="Sign In",font=("times new roman",13),bg="#161B21",fg="#F4A950",activebackground="#F4A950",activeforeground="#161B21",bd=0,cursor="hand2",command=self.signin)
        btn_login.place(x=870,y=530,width=120)
        
    def signin(self):
        self.root.destroy()
        import login
        
    def clear(self):
        self.txt_fname.delete(0,tk.END)
        self.txt_lname.delete(0,tk.END)
        self.txt_contact.delete(0,tk.END)
        self.txt_email.delete(0,tk.END)
        self.txt_passwd.delete(0,tk.END)
        self.txt_cpasswd.delete(0,tk.END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,tk.END)
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_passwd.get()=="" or self.txt_cpasswd.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_passwd.get()!=self.txt_cpasswd.get() :
            messagebox.showerror("Error","Passwords are not matched",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Terms & Conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="1234",database="registration")
                cur=con.cursor()
                cur.execute("select * from regfields where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exists with same email address,Register with another Email address",parent=self.root)
                else:
                    cur.execute("insert into regfields (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),self.txt_passwd.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Sucessful",parent=self.root)  
                    self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
              
root=tk.Tk()
obj=Register(root)
root.mainloop()