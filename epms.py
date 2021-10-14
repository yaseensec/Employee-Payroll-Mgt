import tkinter as tk
import pymysql,time,os,sys,subprocess,tempfile
from tkinter import messagebox,ttk

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System | Developed By DarkRose")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="#292826")
        title=tk.Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#292826",fg="white",anchor="w",padx=10)
        title.place(x=0,y=0,relwidth=1)
        button_emp=tk.Button(self.root,text="All Employees",command=self.employee_frame,font=("times new roman",13),bg="#292826",fg="white",activebackground="#F9D342")
        button_emp.place(x=1050,y=10,height=30,width=140)
        button_logout=tk.Button(self.root,text="Log Out",command=self.logout,font=("times new roman",13),bg="#292826",fg="white",activebackground="#F9D342")
        button_logout.place(x=1200,y=10,height=30,width=140)
        
        ##-----------TTK Styling----------------##
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TCombobox', background = 'gray',foreground="White")
        style.map('TCombobox', fieldbackground=[('readonly','#292826')])
        style.configure("Treeview",background="#292826",foreground="White",fieldbackground="#292826")
        style.map('Treeview',background=[('selected',"#292826")],foreground=[('selected','#F9D342')])
        
        ##------------------------------------Frame 1-------------#-----------------#
        #--------------Variables-----------------#
        self.var_emp_code=tk.StringVar()
        self.var_designation=tk.StringVar()
        self.var_name=tk.StringVar()
        self.var_experience=tk.StringVar()
        self.var_age=tk.StringVar()
        self.var_gender=tk.StringVar()
        self.var_email=tk.StringVar()
        self.var_hr_location=tk.StringVar()
        self.var_dob=tk.StringVar()
        self.var_doj=tk.StringVar()
        self.var_proofid=tk.StringVar()
        self.var_contact=tk.StringVar()
        self.var_status=tk.StringVar()
        
        Frame1=tk.Frame(self.root,bd=3,relief=tk.RIDGE,bg="#292826")
        Frame1.place(x=10,y=70,width=750,height=650)
        
        title2=tk.Label(Frame1,text="Employee Details",font=("times new roman",20),bg="#292826",fg="#F9D342",anchor="w",padx=10)
        title2.place(x=0,y=0,relwidth=1)
        
        lbl_code=tk.Label(Frame1,text="Employee Code*",font=("times new roman",20),bg="#292826",fg="#F9D342")
        lbl_code.place(x=10,y=70)
        self.txt_code=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_emp_code,bg="#292826",fg="White")
        self.txt_code.place(x=250,y=74,width=200)
        button_search=tk.Button(Frame1,text="Search",command=self.search,font=("times new roman",18),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        button_search.place(x=480,y=72,height=30)
        
        #--------Row 1--------#
        lbl_designation=tk.Label(Frame1,text="Designation",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_designation.place(x=10,y=120)
        txt_designation=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_designation,bg="#292826",fg="White")
        txt_designation.place(x=170,y=120,width=200)
        
        lbl_dob=tk.Label(Frame1,text="D.O.B",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_dob.place(x=410,y=120)
        txt_dob=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_dob,bg="#292826",fg="White")
        txt_dob.place(x=520,y=120,width=200)
        
        #--------Row 2----------#
        lbl_name=tk.Label(Frame1,text="Name*",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_name.place(x=10,y=170)
        txt_name=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_name,bg="#292826",fg="White")
        txt_name.place(x=170,y=170,width=200)
        
        lbl_doj=tk.Label(Frame1,text="D.O.J",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_doj.place(x=410,y=170)
        txt_doj=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_doj,bg="#292826",fg="White")
        txt_doj.place(x=520,y=170,width=200)
        
        #---------Row 3-----------#
        lbl_experience=tk.Label(Frame1,text="Experience",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_experience.place(x=10,y=220)
        txt_experience=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_experience,bg="#292826",fg="White")
        txt_experience.place(x=170,y=220,width=200)
        
        lbl_age=tk.Label(Frame1,text="Age",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_age.place(x=410,y=220)
        txt_age=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_age,bg="#292826",fg="White")
        txt_age.place(x=520,y=220,width=200)
        
        #---------Row 4--------------#
        lbl_proofid=tk.Label(Frame1,text="Proof I.D",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_proofid.place(x=10,y=270)
        txt_proofid=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_proofid,bg="#292826",fg="White")
        txt_proofid.place(x=170,y=270,width=200)
        
        lbl_gender=tk.Label(Frame1,text="Gender",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_gender.place(x=410,y=270)
        
        combo_gender=ttk.Combobox(Frame1,textvariable=self.var_gender,font=('times new roman',13,'bold'),state="readonly")
        combo_gender['values']=("Select","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.place(x=520,y=270,width=200)
        
        #----------Row 5-------------#
        lbl_email=tk.Label(Frame1,text="Email*",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_email.place(x=10,y=320)
        txt_email=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_email,bg="#292826",fg="White")
        txt_email.place(x=170,y=320,width=200)
        
        lbl_contact=tk.Label(Frame1,text="Contact",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_contact.place(x=410,y=320)
        txt_contact=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_contact,bg="#292826",fg="White")
        txt_contact.place(x=520,y=320,width=200)
        
        #----------Row 6----------------#
        lbl_hired=tk.Label(Frame1,text="Hired Location",font=("times new roman",15),bg="#292826",fg="#F9D342")
        lbl_hired.place(x=10,y=370)
        txt_hired=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_hr_location,bg="#292826",fg="White")
        txt_hired.place(x=170,y=370,width=200)
        
        lbl_status=tk.Label(Frame1,text="Status",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_status.place(x=410,y=370)
        txt_status=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_status,bg="#292826",fg="White")
        txt_status.place(x=520,y=370,width=200)
        
        #--------Row 7------------#
        lbl_address=tk.Label(Frame1,text="Address",font=("times new roman",20),bg="#292826",fg="#F9D342")
        lbl_address.place(x=10,y=480)
        self.txt_address=tk.Text(Frame1,font=("times  new roman",13),bg="#292826",fg="White")
        self.txt_address.place(x=170,y=420,width=550,height=150)
        
        ##------------------------------Frame2---------------------------##
        #---------------Variables------------#
        self.var_month=tk.StringVar()
        self.var_year=tk.StringVar()
        self.var_absents=tk.StringVar()
        self.var_t_days=tk.StringVar()
        self.var_b_salary=tk.StringVar()
        self.var_medical=tk.StringVar()
        self.var_pf=tk.StringVar()
        self.var_conveyance=tk.StringVar()
        self.var_n_salary=tk.StringVar()
        
        Frame2=tk.Frame(self.root,bd=3,relief=tk.RIDGE,bg="#292826")
        Frame2.place(x=770,y=70,width=580,height=330)
        
        title3=tk.Label(Frame2,text="Employee Salary Details",font=("times new roman",20),bg="#292826",fg="#F9D342",anchor="w",padx=10)
        title3.place(x=0,y=0,relwidth=1)
        
        lbl_month=tk.Label(Frame2,text="Month",font=("times new roman",17),bg="#292826",fg="#F9D342")
        lbl_month.place(x=10,y=60)
        txt_month=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_month,bg="#292826",fg="White")
        txt_month.place(x=95,y=64,width=100)
        
        lbl_year=tk.Label(Frame2,text="Year",font=("times new roman",17),bg="#292826",fg="#F9D342")
        lbl_year.place(x=205,y=60)
        txt_year=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_year,bg="#292826",fg="White")
        txt_year.place(x=270,y=64,width=100)
        
        lbl_absents=tk.Label(Frame2,text="Absents",font=("times new roman",17),bg="#292826",fg="#F9D342")
        lbl_absents.place(x=375,y=60)
        txt_absents=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_absents,bg="#292826",fg="White")
        txt_absents.place(x=470,y=64,width=100)
        
        #---------------Row 1-------------#
        lbl_days=tk.Label(Frame2,text="Total Days",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_days.place(x=10,y=120)
        txt_days=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_t_days,bg="#292826",fg="White")
        txt_days.place(x=160,y=125,width=100)
        
        lbl_salary=tk.Label(Frame2,text="Basic Salary",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_salary.place(x=280,y=120)
        txt_salary=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_b_salary,bg="#292826",fg="White")
        txt_salary.place(x=440,y=125,width=120)
        
        #---------------Row 2--------------#
        lbl_medical=tk.Label(Frame2,text="Medical",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_medical.place(x=10,y=180)
        txt_medical=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_medical,bg="#292826",fg="White")
        txt_medical.place(x=160,y=185,width=100)
        
        lbl_pf=tk.Label(Frame2,text="P.F",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_pf.place(x=280,y=180)
        txt_pf=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_pf,bg="#292826",fg="White")
        txt_pf.place(x=440,y=185,width=100)
        
        #---------------Row 3--------------#
        lbl_conveyance=tk.Label(Frame2,text="Conveyance",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_conveyance.place(x=10,y=220)
        txt_conveyance=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_conveyance,bg="#292826",fg="White")
        txt_conveyance.place(x=160,y=225,width=100)
        
        lbl_netsalary=tk.Label(Frame2,text="Net Salary*",font=("times new roman",18),bg="#292826",fg="#F9D342")
        lbl_netsalary.place(x=280,y=220)
        txt_netsalary=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_n_salary,bg="#292826",fg="White")
        txt_netsalary.place(x=440,y=225,width=120)
        
        ##--------Buttons----------##
        button_calculate=tk.Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",18),bg="#292826",fg="White",activebackground="#F9D342")
        button_calculate.place(x=100,y=275,height=30,width=120)
        
        self.button_save=tk.Button(Frame2,text="Save",command=self.add,font=("times new roman",18),bg="#292826",fg="white",activebackground="#F9D342")
        self.button_save.place(x=230,y=255,height=30,width=120)
        
        button_clear=tk.Button(Frame2,text="Clear",command=self.clear,font=("times new roman",18),bg="#292826",fg="White",activebackground="#F9D342")
        button_clear.place(x=360,y=255,height=30,width=120)
        
        self.button_update=tk.Button(Frame2,text="Update",state=tk.DISABLED,command=self.update,font=("times new roman",18),bg="#292826",fg="white",activebackground="#F9D342")
        self.button_update.place(x=230,y=295,height=30,width=120)
        
        self.button_delete=tk.Button(Frame2,text="Delete",state=tk.DISABLED,command=self.delete,font=("times new roman",18),bg="#292826",fg="White",activebackground="#F9D342")
        self.button_delete.place(x=360,y=295,height=30,width=120)
        
        ##----------------------------Frame3---------------------------------##  
        Frame3=tk.Frame(self.root,bd=3,relief=tk.RIDGE,bg="#292826")
        Frame3.place(x=770,y=410,width=580,height=310)
        
        #------------------Calculator Frame------------------------#
        self.var_txt=tk.StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
            
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
            
        def clear_calc():
            self.var_txt.set('')
            self.var_operator=''
        
        cal_frame=tk.Frame(Frame3,bg="#292826",bd=2,relief=tk.RIDGE)
        cal_frame.place(x=5,y=5,width=247,height=295)
        
        txt_result=tk.Entry(cal_frame,bg='#292826',fg="White",textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=tk.RIGHT)
        txt_result.place(x=0,y=0,relwidth=1,height=50)
        
        #-----------------------Row 1-------------------#
        btn_7=tk.Button(cal_frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_7.place(x=0,y=52,w=60,h=60)
        btn_8=tk.Button(cal_frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_8.place(x=61,y=52,w=60,h=60)
        btn_9=tk.Button(cal_frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_9.place(x=122,y=52,w=60,h=60)
        btn_divide=tk.Button(cal_frame,text='/',command=lambda:btn_click("/"),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_divide.place(x=183,y=52,w=60,h=60)
        
        #-----------------------Row 2-------------------#
        btn_4=tk.Button(cal_frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_4.place(x=0,y=112,w=60,h=60)
        btn_5=tk.Button(cal_frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_5.place(x=61,y=112,w=60,h=60)
        btn_6=tk.Button(cal_frame,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_6.place(x=122,y=112,w=60,h=60)
        btn_multiply=tk.Button(cal_frame,text='*',command=lambda:btn_click("*"),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_multiply.place(x=183,y=112,w=60,h=60)
        
        #-----------------------Row 3-------------------#
        btn_1=tk.Button(cal_frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_1.place(x=0,y=172,w=60,h=60)
        btn_2=tk.Button(cal_frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_2.place(x=61,y=172,w=60,h=60)
        btn_3=tk.Button(cal_frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_3.place(x=122,y=172,w=60,h=60)
        btn_minus=tk.Button(cal_frame,text='-',command=lambda:btn_click("-"),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_minus.place(x=183,y=172,w=60,h=60)
        
        #-----------------------Row 4-------------------#
        btn_0=tk.Button(cal_frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_0.place(x=0,y=233,w=60,h=60)
        btn_clear=tk.Button(cal_frame,text='C',command=clear_calc,font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_clear.place(x=61,y=233,w=60,h=60)
        btn_plus=tk.Button(cal_frame,text='+',command=lambda:btn_click("+"),font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_plus.place(x=122,y=233,w=60,h=60)
        btn_equalto=tk.Button(cal_frame,text='=',command=result,font=("times new roman",15,"bold"),bg="#292826",fg="#F9D342",activebackground="#F9D342")
        btn_equalto.place(x=183,y=233,w=60,h=60)
        
        ##---------------------Salary Frame---------------------##
        sal_frame=tk.Frame(Frame3,bg="#292826",bd=2,relief=tk.RIDGE)
        sal_frame.place(x=260,y=5,width=310,height=295)

        title_sal=tk.Label(sal_frame,text="Salary Receipt",font=("times new roman",20),bg="#292826",fg="#F9D342",anchor="w",padx=10)
        title_sal.place(x=0,y=0,relwidth=1)
        
        sal_frame2=tk.Frame(sal_frame,bg="#292826",bd=2,relief=tk.RIDGE)
        sal_frame2.place(x=0,y=30,relwidth=1,height=230)
        self.sample=f'''Company Name: Darkrose INC\nAddress: A.P,India
--------------------------------------------------------
 Employee ID\t\t:  
 Salary of\t\t:  Mon-YYYY
 Generated on\t\t:  DD-MM-YYYY
--------------------------------------------------------
 Total Days\t\t:  DD
 Total Present\t\t:  DD
 Total Absent\t\t:  DD
 Conveyance\t\t:  Rs.-----
 Medical\t\t:  Rs.-----
 PF\t\t:  Rs.-----
 Gross Payment\t\t:  Rs.-----
 Net Salary\t\t: Rs.-----
-------------------------------------------------------
This is Computer Generated slip,\tSignature not required
'''
        scroll_y=tk.Scrollbar(sal_frame2,orient=tk.VERTICAL)
        scroll_y.pack(fill=tk.Y,side=tk.RIGHT)
        
        self.txt_salary_receipt=tk.Text(sal_frame2,font=("times new roman",11),bg="#292826",fg="White",yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=tk.BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(tk.END,self.sample)
        
        self.button_print=tk.Button(sal_frame,text="Print",command=self.print,state=tk.DISABLED,font=("times new roman",18),bg="#292826",fg="White",activebackground="#F9D342")
        self.button_print.place(x=180,y=262,height=30,width=110)
        
        self.check_connection()
    
    ##------------Functions----------##
    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Employee ID,Please try with another ID",parent=self.root)
            else:
                self.var_emp_code.set(row[0]) 
                self.var_designation.set(row[1]) 
                self.var_name.set(row[2]) 
                self.var_age.set(row[3]) 
                self.var_gender.set(row[4]) 
                self.var_email.set(row[5]) 
                self.var_hr_location.set(row[6]) 
                self.var_dob.set(row[7]) 
                self.var_doj.set(row[8]) 
                self.var_experience.set(row[9]) 
                self.var_proofid.set(row[10]) 
                self.var_contact.set(row[11]) 
                self.var_status.set(row[12]) 
                self.txt_address.delete('1.0',tk.END) 
                self.txt_address.insert(tk.END,row[13]) 
                self.var_month.set(row[14]) 
                self.var_year.set(row[15]) 
                self.var_b_salary.set(row[16]) 
                self.var_t_days.set(row[17]) 
                self.var_absents.set(row[18]) 
                self.var_medical.set(row[19]) 
                self.var_pf.set(row[20]) 
                self.var_conveyance.set(row[21]) 
                self.var_n_salary.set(row[22])
                file=open('receipts/'+str(row[23]),'r')
                self.txt_salary_receipt.delete('1.0',tk.END)
                for i in file:
                    self.txt_salary_receipt.insert(tk.END,i)
                file.close
                self.button_save.config(state=tk.DISABLED)
                self.button_update.config(state=tk.NORMAL)
                self.button_delete.config(state=tk.NORMAL)
                self.txt_code.config(state='readonly')
                self.button_print.config(state=tk.NORMAL)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')
            
    def clear(self):
        self.button_save.config(state=tk.NORMAL)
        self.button_update.config(state=tk.DISABLED)
        self.button_delete.config(state=tk.DISABLED)
        self.button_print.config(state=tk.DISABLED)
        self.txt_code.config(state=tk.NORMAL)
        
        self.var_emp_code.set('') 
        self.var_designation.set('') 
        self.var_name.set('') 
        self.var_age.set('') 
        self.var_gender.set('Select') 
        self.var_email.set('') 
        self.var_hr_location.set('') 
        self.var_dob.set('') 
        self.var_doj.set('') 
        self.var_experience.set('') 
        self.var_proofid.set('') 
        self.var_contact.set('') 
        self.var_status.set('') 
        self.txt_address.delete('1.0',tk.END) 
        self.var_month.set('') 
        self.var_year.set('') 
        self.var_b_salary.set('') 
        self.var_t_days.set('') 
        self.var_absents.set('') 
        self.var_medical.set('') 
        self.var_pf.set('') 
        self.var_conveyance.set('') 
        self.var_n_salary.set('')
        self.txt_salary_receipt.delete('1.0',tk.END)
        self.txt_salary_receipt.insert(tk.END,self.sample)
        
    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee ID is required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='1234',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID,Please try with another ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you want to Delete??")
                    if op==True:
                        cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.clear()
                    pass
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
        
    def add(self):
        if self.var_emp_code.get()=='' or self.var_email.get()=='' or self.var_name.get()=='' or self.var_n_salary.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='1234',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This employee id is already available in our record,try again with another id",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_emp_code.get(),self.var_designation.get(),self.var_name.get(),self.var_age.get(),self.var_gender.get(),self.var_email.get(),self.var_hr_location.get(),self.var_dob.get(),self.var_doj.get(),self.var_experience.get(),self.var_proofid.get(),self.var_contact.get(),self.var_status.get(),self.txt_address.get('1.0',tk.END),self.var_month.get(),self.var_year.get(),self.var_b_salary.get(),self.var_t_days.get(),self.var_absents.get(),self.var_medical.get(),self.var_pf.get(),self.var_conveyance.get(),self.var_n_salary.get(),self.var_emp_code.get()+".txt"))
                    con.commit()
                    con.close()
                    file=open('receipts/'+str(self.var_emp_code.get())+".txt",'w')
                    file.write(self.txt_salary_receipt.get('1.0',tk.END))
                    file.close
                    messagebox.showinfo("Success","Record Added Successfully")
                    self.button_print.config(state=tk.NORMAL)
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
                
    def update(self):
        if self.var_emp_code.get()=='' or self.var_n_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='1234',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This employee id is invalid,try again with valid id",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`dob`=%s,`doj`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t-days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`conveyance`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",(self.var_designation.get(),self.var_name.get(),self.var_age.get(),self.var_gender.get(),self.var_email.get(),self.var_hr_location.get(),self.var_dob.get(),self.var_doj.get(),self.var_experience.get(),self.var_proofid.get(),self.var_contact.get(),self.var_status.get(),self.txt_address.get('1.0',tk.END),self.var_month.get(),self.var_year.get(),self.var_b_salary.get(),self.var_t_days.get(),self.var_absents.get(),self.var_medical.get(),self.var_pf.get(),self.var_conveyance.get(),self.var_n_salary.get(),self.var_emp_code.get()+".txt",self.var_emp_code.get()))
                    con.commit()
                    con.close()
                    file=open('receipts/'+str(self.var_emp_code.get())+".txt",'w')
                    file.write(self.txt_salary_receipt.get('1.0',tk.END))
                    file.close
                    messagebox.showinfo("Success","Record Updated Successfully")
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
            
    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_b_salary.get()=='' or self.var_absents.get()=='' or self.var_t_days.get()=='' or self.var_medical.get()=='' or self.var_pf.get()=='' or self.var_conveyance.get()=='':
            messagebox.showerror('Error','All Fields are required')
        else:
            per_day=int(self.var_b_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absents.get())
            e_sal=per_day*work_day###Effective Salary
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_conveyance.get())
            n_sal=e_sal-deduct+addition
            self.var_n_salary.set(str(round(n_sal,2)))
            #####Update Receipt####
            new_sample=f'''Company Name: Darkrose INC\nAddress: A.P,India
--------------------------------------------------------
 Employee ID\t\t:  {self.var_emp_code.get()}
 Salary of\t\t:  {self.var_month.get()}-{self.var_year.get()}
 Generated on\t\t:  {str(time.strftime("%d-%m-%Y"))}
--------------------------------------------------------
 Total Days\t\t:  {self.var_t_days.get()}
 Total Present\t\t:  {str(int(self.var_t_days.get())-int(self.var_absents.get()))}
 Total Absent\t\t:  {self.var_absents.get()}
 Conveyance\t\t:  Rs.{self.var_conveyance.get()}
 Medical\t\t:  Rs.{self.var_medical.get()}
 PF\t\t:  Rs.{self.var_pf.get()}
 Gross Payment\t\t:  Rs{self.var_b_salary.get()}
 Net Salary\t\t: Rs.{self.var_n_salary.get()}
-------------------------------------------------------
This is Computer Generated slip,\tSignature not required
'''         
            self.txt_salary_receipt.delete('1.0',tk.END)
            self.txt_salary_receipt.insert(tk.END,new_sample)
    
    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            self.row=cur.fetchall()
            #print(self.row)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')
            
    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            row=cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for x in row:
                self.employee_tree.insert('',tk.END,values=x)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')
            
    def logout(self):
        messagebox.showinfo("Success","Loged Out Successfully",parent=self.root)
        self.root.destroy()
        import login
    
    ##---------------------------All Employees Frame-------------------##
    def employee_frame(self):
        self.root2=tk.Toplevel(self.root)
        self.root2.title("All Employee Details")
        self.root2.geometry("950x550+130+100")
        self.root2.config(bg="#292826")
        title=tk.Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold"),bg="#292826",fg="#F9D342",anchor="w",padx=10)
        title.pack(side=tk.TOP,fill=tk.X)
        self.root2.focus_force()
        
        scrolly=tk.Scrollbar(self.root2,orient=tk.VERTICAL,bg="#292826")
        scrollx=tk.Scrollbar(self.root2,orient=tk.HORIZONTAL,bg="#292826")
        scrollx.pack(side=tk.BOTTOM,fill=tk.X)
        scrolly.pack(side=tk.RIGHT,fill=tk.Y)
        
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'dob', 'doj', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 't-days', 'absent_days', 'medical', 'pf', 'conveyance', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='Hr Location')
        self.employee_tree.heading('dob',text='DOB')
        self.employee_tree.heading('doj',text='DOJ')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof ID')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('t-days',text='T.Days')
        self.employee_tree.heading('absent_days',text='Absents')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('conveyance',text='Conveyance')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('salary_receipt',text='Salary Receipt')
        self.employee_tree['show']='headings'
        
        self.employee_tree.column('e_id',width=50)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=50)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=200)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('t-days',width=70)
        self.employee_tree.column('absent_days',width=70)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('conveyance',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=200)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=tk.BOTH,expand=1)
        self.show()
    
        self.root2.mainloop()
        
    def print(self):
        file=tempfile.mktemp(".txt")
        open(file,'w').write(self.txt_salary_receipt.get('1.0',tk.END))
        # os.startfile(file_,'print')
        # if sys.platform == "win32":
        #     os.startfile(file,'print')
        # else:
        #     opener = "open" if sys.platform == "darwin" else "xdg-open"
        #     subprocess.call([opener, file])
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, file])
        
root=tk.Tk()
obj=EmployeeSystem(root)
root.mainloop()