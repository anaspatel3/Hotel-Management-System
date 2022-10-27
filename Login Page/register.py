from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, win):
        self.win = win
        self.win.title("Register")
        self.win.geometry("1600x900+0+0")
        #====================Variables==========================
        self.f_name = StringVar()
        self.l_name = StringVar()
        self.contact = StringVar()
        self.v_email = StringVar()
        self.securityQ = StringVar()
        self.securityA = StringVar()
        self.v_pass = StringVar()
        self.v_c_pass = StringVar()
        self.v_check = IntVar()

        # ==============Background Image================
        self.back_ground = ImageTk.PhotoImage(file=r"background.jpg");
        back_lbl = Label(self.win,image=self.back_ground)
        back_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        # ==============Left Image================
        self.back_ground1 = ImageTk.PhotoImage(file=r"background.jpg");
        left_lbl = Label(self.win, image=self.back_ground1)
        left_lbl.place(x=50, y=100, height=550, width=470)

        # ==============Frame================
        my_frame = Frame(self.win,bg="white")
        my_frame.place(x=520,y=100,height=550,width=800)

        reg_lbl = Label(my_frame, text="REGISTER HERE",font=("times new roman",23,"bold"),fg="black",bg="white")
        reg_lbl.place(x=20,y=20)

        fname = Label(my_frame, text="First Name", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        fname.place(x=50, y=100)
        self.f_input = ttk.Entry(my_frame, textvariable=self.f_name, font=("times new roman", 19, "bold"))
        self.f_input.place(x=50, y=130,width=250)

        contact = Label(my_frame, text="Contact Number", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        contact.place(x=50, y=175)
        self.f_cont = ttk.Entry(my_frame, textvariable=self.contact,font=("times new roman", 19, "bold"))
        self.f_cont.place(x=50, y=205,width=250)

        sec_que = Label(my_frame, text="Select Security Question", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        sec_que.place(x=50, y=250)

        self.combo_sec=ttk.Combobox(my_frame, textvariable=self.securityQ, font=("times new roman", 19, "bold"),state="readonly")
        self.combo_sec["values"]=("Select","Your mother name","Your grandfather name")
        self.combo_sec.place(x=50,y=282,width=250)
        self.combo_sec.current(0)

        passwrd = Label(my_frame,  text="Password", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        passwrd.place(x=50, y=330)
        self.f_pass = ttk.Entry(my_frame, textvariable=self.v_pass, font=("times new roman", 19, "bold"))
        self.f_pass.place(x=50, y=360,width=250)

        Lname = Label(my_frame, text="Last Name", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        Lname.place(x=400, y=100)
        self.f_l_name = ttk.Entry(my_frame,  textvariable=self.l_name, font=("times new roman", 19, "bold"))
        self.f_l_name.place(x=400, y=130,width=250)

        email = Label(my_frame, text="Email", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        email.place(x=400, y=175)
        self.f_email = ttk.Entry(my_frame, textvariable=self.v_email,font=("times new roman", 19, "bold"))
        self.f_email.place(x=400, y=205,width=250)

        sec_ans = Label(my_frame,  text="Security Answer", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        sec_ans.place(x=400, y=250)
        self.f_input = ttk.Entry(my_frame, textvariable=self.securityA,font=("times new roman", 19, "bold"))
        self.f_input.place(x=400, y=280,width=250)

        c_pass = Label(my_frame,  text="Confirm Password", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        c_pass.place(x=400, y=330)
        self.f_c_pass = ttk.Entry(my_frame, textvariable=self.v_c_pass, font=("times new roman", 19, "bold"))
        self.f_c_pass.place(x=400, y=360,width=250)


        # ******************* Check Button **************************
        chek_btn = Checkbutton(my_frame, variable=self.v_check, text="I Agree Terms And Conditions",font=("times new roman", 19, "bold"),onvalue=1,offvalue=0,fg="gray",bg="white")
        chek_btn.place(x=50,y=410)

        #******************** Buttons *********************************
        ig1 = Image.open("Nature.jpeg")
        ig1=ig1.resize((200,50),Image.ANTIALIAS)
        self.phoig=ImageTk.PhotoImage(ig1)
        b1=Button(my_frame,image=self.phoig, command=self.register_data, borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=450,width=200)

        ig2 = Image.open("Nature.jpeg")
        ig2 = ig2.resize((200, 50), Image.ANTIALIAS)
        self.phoig1 = ImageTk.PhotoImage(ig2)
        b2 = Button(my_frame, image=self.phoig1, borderwidth=0, cursor="hand2", bg="white")
        b2.place(x=400, y=450, width=200)

        #********************* Function *******************************
    def register_data(self):
        if self.f_name.get()=="" or self.v_email.get()=="" or self.securityQ.get=="Select":
            messagebox.showerror("Error", "All fields required")
        elif self.v_pass.get()!= self.v_c_pass.get():
            messagebox.showerror("Error","Passwords are incorrect")
        elif self.v_check.get()==0:
            messagebox.showerror("Error","Agree terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="sys")
            cur = conn.cursor()
            query = "select * from register where email=%s"
            value = self.v_email.get()
            cur.execute(query,value)
            data = cur.fetchone()
            if data != NONE:
                messagebox.showerror("Error", "User already exist")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.f_name.get(),
                                                                                 self.l_name.get(),
                                                                                 self.contact.get(),
                                                                                 self.v_email.get(),
                                                                                 self.securityQ.get(),
                                                                                 self.securityA.get(),
                                                                                 self.v_pass.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succes","Successfull")





if __name__ == "__main__":

    win = Tk()
    app=Register(win)
    win.mainloop()