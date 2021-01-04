import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox,ttk
import pymysql

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed by DarkRose")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="#1D1B1B")
        
        #-------Images--------------#
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image=tk.Label(self.root,image=self.phone_image,bd=0)
        self.lbl_phone_image.place(x=200,y=70)
        
        #---------Login tk.Frame-----------#
        login_frame=tk.Frame(self.root,bd=2,relief=tk.RIDGE,bg="#1D1B1B")
        login_frame.place(x=650,y=90,width=350,height=460)
        
        title=tk.Label(login_frame,text="Login System",font=("times new roman",30,"bold"),bg="#1D1B1B",fg='#EC4D37')
        title.place(x=0,y=30,relwidth=1)
        
        lbl_email=tk.Label(login_frame,text="Email Address*",font=("times new roman",15),bg="#1D1B1B",fg='#EC4D37')
        lbl_email.place(x=50,y=100)
        self.email=tk.StringVar()
        
        txt_email=tk.Entry(login_frame,textvariable=self.email,font=("times new roman",15),bg="#1D1B1B",fg="White")
        txt_email.place(x=50,y=140,width=250)
        
        lbl_pass=tk.Label(login_frame,text="Password",font=("times new roman",15),bg="#1D1B1B",fg='#EC4D37')
        lbl_pass.place(x=50,y=200)
        self.password=tk.StringVar()
        
        txt_pass=tk.Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#1D1B1B",fg="White")
        txt_pass.place(x=50,y=240,width=250)
        
        btn_login=tk.Button(login_frame,command=self.login,text="Log In",font=("times new roman",15),bg="#1D1B1B",activebackground="#EC4D37",fg="#EC4D37",activeforeground="#1D1B1B",cursor="hand2")
        btn_login.place(x=50,y=300,width=250,height=35)
        
        hr=tk.Label(login_frame,bg="lightgray")
        hr.place(x=50,y=370,width=250,height=2)
        
        or_=tk.Label(login_frame,text="OR",bg="#1D1B1B",fg="#EC4D37",font=("times new roman",15,"bold"))
        or_.place(x=150,y=355)
        
        btn_forget=tk.Button(login_frame,text="Forget Password?",command=self.forget_password_window,font=("times new roman",13),bg="#1D1B1B",fg="#EC4D37",bd=0,activebackground="#EC4D37",activeforeground="#1D1B1B")
        btn_forget.place(x=100,y=390)
        
        #---------Sign Up? tk.Frame-----------#
        register_frame=tk.Frame(self.root,bd=2,relief=tk.RIDGE,bg="#1D1B1B")
        register_frame.place(x=650,y=570,width=350,height=60)
        
        lbl_reg=tk.Label(register_frame,text="Don't have an account?",font=("times new roman",13),bg="#1D1B1B",fg='#EC4D37')
        lbl_reg.place(x=40,y=20)
        
        btn_signup=tk.Button(register_frame,text="Sign Up",command=self.signup,font=("times new roman",13,"bold"),bg="#1D1B1B",fg="#EC4D37",bd=0,activebackground="#EC4D37",activeforeground="#1D1B1B")
        btn_signup.place(x=215,y=16)
        
        #-------Animation Images------------#
        self.im1=ImageTk.PhotoImage(file="images/animi1.png")
        self.im2=ImageTk.PhotoImage(file="images/animi2.png")
        self.im3=ImageTk.PhotoImage(file="images/animi3.png")
        
        self.lbl_change_image=tk.Label(self.root,bg="White")
        self.lbl_change_image.place(x=328,y=169,width=240,height=428)
        
        self.animate()
        
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,tk.END)
        self.txt_answer.delete(0,tk.END)
        self.email.set('')
        self.password.set('')
        
    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror('Error',"All Fields are required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="1234",database="registration")
                cur=con.cursor()
                cur.execute("select * from regfields where email=%s and question=%s and answer=%s",(self.email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update regfields set password=%s where email=%s",(self.txt_new_pass.get(),self.email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password reset Successfully,Login with New Password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root2)
                
    def forget_password_window(self):
        if self.email.get()=="":
            messagebox.showerror("Error","Please enter valid email address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="1234",database="registration")
                cur=con.cursor()
                cur.execute("select * from regfields where email=%s",self.email.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2=tk.Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="#1D1B1B")
                    self.root2.focus_force()
                    self.root2.grab_set()
                
                    t=tk.Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="#1D1B1B",fg="#EC4D37")
                    t.place(x=0,y=10,relwidth=1)
                    
                    #------------------Forget Password-------------------------------#
                    style = ttk.Style()
                    style.theme_use('alt')
                    style.configure('TCombobox', background = 'gray',foreground="White")
                    style.map('TCombobox', fieldbackground=[('readonly','#1D1B1B')])
                    
                    question=tk.Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="#1D1B1B",fg="#EC4D37")
                    question.place(x=50,y=100)
                    
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=tk.CENTER)
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.current(0)
                
                    answer=tk.Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="#1D1B1B",fg="#EC4D37")
                    answer.place(x=50,y=180)
                    
                    self.txt_answer=tk.Entry(self.root2,font=("times new roman",15),bg="#1D1B1B",fg="White")
                    self.txt_answer.place(x=50,y=210,width=250)
                    
                    new_pass=tk.Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="#1D1B1B",fg="#EC4D37")
                    new_pass.place(x=50,y=260)
                
                    self.txt_new_pass=tk.Entry(self.root2,font=("times new roman",15),bg="#1D1B1B",fg="White")
                    self.txt_new_pass.place(x=50,y=290,width=250)
                    
                    btn_change_password=tk.Button(self.root2,text="Reset Password",command=self.forget_password,bg="#1D1B1B",fg="#EC4D37",activebackground="#EC4D37",activeforeground="#1D1B1B",font=("times new roman",15,"bold"))
                    btn_change_password.place(x=90,y=340)
                
            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root2)
                    
    def signup(self):
        self.root.destroy()
        import registration
    
    def login(self):
        if self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="1234",database="registration")
                cur=con.cursor()
                cur.execute("select * from regfields where email=%s and password=%s",(self.email.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email or Password",parent=self.root)
                    #self.email.set("")
                    self.password.set("")
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import epms
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
root=tk.Tk()
obj=Login_System(root)
root.mainloop()