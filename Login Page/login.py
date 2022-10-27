from msilib.schema import File
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

def main():
    winn = Tk()
    app = Login_Window(winn)
    winn.mainloop()


class Login_Window:
    def __init__(self, win):
        self.win = win
        self.win.title("Login")
        self.win.geometry("1550x800+0+0")

        img1 = Image.open(r"background.jpg")
        img1 = img1.resize((1600, 1000), Image.ANTIALIAS)
        self.Img11 = ImageTk.PhotoImage(img1)

        label_bi = Label(self.win,image=self.Img11)
        label_bi.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.win,bg="black")
        frame.place(x=600,y=170,width=350,height=450)

        img = Image.open(r"riya.png")
        img = img.resize((100,100),Image.ANTIALIAS)
        self.phoImg = ImageTk.PhotoImage(img)

        lblimg1 = Label(image=self.phoImg,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        lbl1 = Label(frame,text="Get Started", font=("Times New Roman",20,"bold"),fg="gray",bg="black")
        lbl1.place(x=110,y=100)

        #Label
        user = lbl = Label(frame,text="Username", font=("Times New Roman",15,"bold"),fg="gray",bg="black")
        user.place(x=90,y=145)

        self.txtuser = ttk.Entry(frame,font=("Times New Roman", 10, "bold"))
        self.txtuser.place(x=60,y=170,width=250)

        password = lbl = Label(frame, text="Password", font=("Times New Roman", 15, "bold"), fg="gray", bg="black")
        password.place(x=90, y=210)

        self.txtpass=ttk.Entry(frame, show='*',font=("Times New Roman",10,"bold"))
        self.txtpass.place(x=60,y=237,width=250)

        #
        img1 = Image.open(r"user_icon.png")
        img1 = img1.resize((25,25),Image.ANTIALIAS)
        self.phoImg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(image=self.phoImg1,bg="black",borderwidth=0)
        lblimg1.place(x=663,y=315,width=25,height=25)

        img2 = Image.open(r"password_icon.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.phoImg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(image=self.phoImg2, bg="black", borderwidth=0)
        lblimg2.place(x=663, y=382, width=25, height=25)

        #Button

        logbtn = Button(frame,command=self.login,text="Login",font=("Times New Roman",10,"bold"),bd=2,relief=RIDGE,fg="white",bg="red")
        logbtn.place(x=120,y=280,width=100,height=30)

        usrbtn = Button(frame, text="New User", command=self.register_window, font=("Times New Roman", 10, "bold"), bd=2, relief=RIDGE, borderwidth=0, fg="white",bg="black",activeforeground="white",activebackground="black")
        usrbtn.place(x=35, y=320, width=100, height=30)




    def register_window(self):
        self.new_window = Toplevel(self.win)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get()=="":
            messagebox.showerror("Error", "Enter Username and Password")
        elif self.txtuser.get()=="Anas" and self.txtpass.get()=="anas":
            messagebox.showinfo("Successful","Correct")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="sys")
            cur = conn.cursor()
            cur.execute("select * from register where email=%s ans password=%s",(
                                                                                self.v_email.get(),
                                                                                self.v_pass.get()
                                                                        ))

            row = cur.fetchone()
            if row == NONE:
                messagebox.showerror("Error","Invalid Username ans Password")
            else:
                open_main=messagebox.askyesno("YesNo","Acces to only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.new_window)
                    #self.app = Hotel(self.new_window)
                else:
                    if not open_main:
                        return



            conn.commit()
            conn.close()
class Register:
    def __init__(self, win):
        self.win = win
        self.win.title("Register")
        self.win.geometry("1600x900+0+0")
        # ====================Variables==========================
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
        img11 = Image.open(r"background.jpg")
        img11 = img11.resize((1600, 1000), Image.ANTIALIAS)
        self.back_ground = ImageTk.PhotoImage(img11)
        back_lbl = Label(self.win, image=self.back_ground)
        back_lbl.place(x=0, y=0, relheight=1, relwidth=1)


        # ==============Left Image================
        self.back_ground1 = ImageTk.PhotoImage(file=r"register.jpg");
        left_lbl = Label(self.win, image=self.back_ground1)
        left_lbl.place(x=50, y=100, height=550, width=470)

        # ==============Frame================
        my_frame = Frame(self.win, bg="white")
        my_frame.place(x=520, y=100, height=550, width=800)

        reg_lbl = Label(my_frame, text="REGISTER HERE", font=("times new roman", 23, "bold"), fg="black", bg="white")
        reg_lbl.place(x=20, y=20)

        fname = Label(my_frame, text="First Name", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        fname.place(x=50, y=100)
        self.f_input = ttk.Entry(my_frame, textvariable=self.f_name, font=("times new roman", 19, "bold"))
        self.f_input.place(x=50, y=130, width=250)

        contact = Label(my_frame, text="Contact Number", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        contact.place(x=50, y=175)
        self.f_cont = ttk.Entry(my_frame, textvariable=self.contact, font=("times new roman", 19, "bold"))
        self.f_cont.place(x=50, y=205, width=250)

        sec_que = Label(my_frame, text="Select Security Question", font=("times new roman", 19, "bold"), fg="gray",
                        bg="white")
        sec_que.place(x=50, y=250)

        self.combo_sec = ttk.Combobox(my_frame, textvariable=self.securityQ, font=("times new roman", 19, "bold"),
                                      state="readonly")
        self.combo_sec["values"] = ("Select", "Your mother name", "Your grandfather name")
        self.combo_sec.place(x=50, y=282, width=250)
        self.combo_sec.current(0)

        passwrd = Label(my_frame, text="Password", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        passwrd.place(x=50, y=330)
        self.f_pass = ttk.Entry(my_frame, textvariable=self.v_pass, font=("times new roman", 19, "bold"))
        self.f_pass.place(x=50, y=360, width=250)

        Lname = Label(my_frame, text="Last Name", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        Lname.place(x=400, y=100)
        self.f_l_name = ttk.Entry(my_frame, textvariable=self.l_name, font=("times new roman", 19, "bold"))
        self.f_l_name.place(x=400, y=130, width=250)

        email = Label(my_frame, text="Email", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        email.place(x=400, y=175)
        self.f_email = ttk.Entry(my_frame, textvariable=self.v_email, font=("times new roman", 19, "bold"))
        self.f_email.place(x=400, y=205, width=250)

        sec_ans = Label(my_frame, text="Security Answer", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        sec_ans.place(x=400, y=250)
        self.f_input = ttk.Entry(my_frame, textvariable=self.securityA, font=("times new roman", 19, "bold"))
        self.f_input.place(x=400, y=280, width=250)

        c_pass = Label(my_frame, text="Confirm Password", font=("times new roman", 19, "bold"), fg="gray", bg="white")
        c_pass.place(x=400, y=330)
        self.f_c_pass = ttk.Entry(my_frame, textvariable=self.v_c_pass, font=("times new roman", 19, "bold"))
        self.f_c_pass.place(x=400, y=360, width=250)

        # ******************* Check Button **************************
        chek_btn = Checkbutton(my_frame, variable=self.v_check, text="I Agree Terms And Conditions",
                               font=("times new roman", 19, "bold"), onvalue=1, offvalue=0, fg="gray", bg="white")
        chek_btn.place(x=50, y=410)

        # ******************** Buttons *********************************
        ig1 = Image.open("register_now.jpg")
        ig1 = ig1.resize((200, 80), Image.ANTIALIAS)
        self.phoig = ImageTk.PhotoImage(ig1)
        b1 = Button(my_frame, image=self.phoig, command=self.register_data, borderwidth=0, cursor="hand2", bg="white")
        b1.place(x=10, y=460, width=200)

        ig2 = Image.open("ligonnow.jpg")
        ig2 = ig2.resize((200, 50), Image.ANTIALIAS)
        self.phoig1 = ImageTk.PhotoImage(ig2)
        b2 = Button(my_frame, image=self.phoig1, borderwidth=0, cursor="hand2", bg="white")
        b2.place(x=400, y=470, width=200)

        # ********************* Function *******************************

    def register_data(self):
        if self.f_name.get() == "" or self.v_email.get() == "" or self.securityQ.get == "Select":
            messagebox.showerror("Error", "All fields required")
        elif self.v_pass.get() != self.v_c_pass.get():
            messagebox.showerror("Error", "Passwords are incorrect")
        elif self.v_check.get() == 0:
            messagebox.showerror("Error", "Agree terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="sys")
            cur = conn.cursor()
            query = "select * from register where email=%s"
            value = self.v_email.get()
            cur.execute(query, value)
            data = cur.fetchone()
            if data != NONE:
                messagebox.showerror("Error", "User already exist")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (self.f_name.get(),
                                                                                  self.l_name.get(),
                                                                                  self.contact.get(),
                                                                                  self.v_email.get(),
                                                                                  self.securityQ.get(),
                                                                                  self.securityA.get(),
                                                                                  self.v_pass.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Succes", "Successfull")

if __name__ == "__main__":
      main()
