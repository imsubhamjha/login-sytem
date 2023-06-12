from tkinter import *
from tkinter import ttk
import ast
from PIL import Image, ImageTk
from tkinter import messagebox as tmsg


root = Tk()

root.title("Login")
root.geometry("1020x630")
root.wm_iconbitmap("csym.ico")
root.config(bg="#930bbd")

def forgot_pass():
    forgot = Toplevel(root)
    forgot.geometry("860x455")
    forgot.title("Forgot Password")
    forgot.config(bg="lightgrey")

    def submit():
        username = userna.get()
        newpassword = newpass.get()

        f = open("datesheet.txt", 'r')
        d = f.read()
        r = ast.literal_eval(d)
        f.close()

        if username in r.keys() and len(newpassword) >= 6:
            f = open("datesheet.txt","+r")
            d = f.read()
            r = ast.literal_eval(d)


            dict1 = {username:newpassword}
            r.update(dict1)
            f.truncate(0)
            f.close()

            f = open("datesheet.txt",'w')
            w = f.write(str(r))
                
            forgot.destroy()
            tmsg.showinfo('Success',"Successfully created new password")

        elif len(newpassword) < 6:
            tmsg.showwarning("Warning", "Please enter 6 character or more in password ")

        else:
            tmsg.showwarning("Error","Username not found")

    userna = StringVar()
    newpass = StringVar()
    
    frame = Frame(forgot, bg="#fafcfb", width=815 , height= 400)
    frame.place(x=20, y=30)

    login_lab = Label(frame,text="New Password", fg="black", bg="#ffffff", font="Ubuntu 18 bold")
    login_lab.place(x = 20, y =20)
    

    frameunder1 = Frame(frame, width= 367, height=2, bg="#aa1bde")
    frameunder1.place(x = 20, y=153)
        
    user_lab = Label(frame, text="Enter Username for which you want to password", fg="black", bg="#ffffff", font=("@Malgun Gothic" , 10, "bold"))
    user_lab.place(x = 20, y = 98)

    user_entry1 = Entry(frame,border=0, textvariable=userna, width=30,foreground="#969096", font=("Candara" , 16))
    user_entry1.place(x = 20, y = 124)
    #################################################################################################################
    def on_enter(e):
        pass_entry.delete(0,'end')

    def on_leave(e):
        name = pass_entry.get()
        if name == '':
            pass_entry.insert(0,"Enter 6 character or more")


    pass_lab = Label(frame, text="Create new Password", fg="black", bg="#ffffff", font=("@Malgun Gothic" , 10, "bold"))
    pass_lab.place(x = 20, y = 186)

    pass_entry = Entry(frame,border=0,textvariable=newpass,width=30,foreground="#969096", font=("Candara" , 16))
    pass_entry.place(x = 20, y = 214 )
    pass_entry.insert(0,"Enter 6 character or more")
    pass_entry.bind("<FocusIn>", on_enter)
    pass_entry.bind("<FocusOut>", on_leave)

    ########################################################################################################################

    frameunder2 = Frame(frame, width= 367, height=2, bg="#aa1bde")
    frameunder2.place(x = 20, y=244)

    login_button = Button(frame, command=submit,width="36",text="SUBMIT",cursor="hand2",border=0,fg="white", bg="#570da6", font=("@Malgun Gothic" , 12, "bold")  )
    login_button.place(x=20, y=320)


def signin():
    username = user_signin.get()
    password = passw_signin.get()
    check = checkitem.get() 
    try:
        f = open("datesheet.txt", 'r')
        d = f.read()
        r = ast.literal_eval(d)
        f.close()
    except:
        f = open('datesheet.txt','w')
        pp = str({'Username':'password'})
        f.write(pp)
        f.close()


    f = open("datesheet.txt", 'r')
    d = f.read()
    r = ast.literal_eval(d)
    f.close()
    

    if username in r.keys() and password == r[username] and check == "yes":
        screen = Toplevel(root)
        screen.geometry("498x312")
        screen.title("registration form")
        screen.configure(bg='lightgreen')

        def get_val(): 
            print("The name of the student: ",nameval.get())
            print("The course of the student: ",courseval.get())
            print("The semester of the student: ",semval.get())
            print("The form number of the student: ",formval.get())
            print("The contact number of the student: ",contactval.get())
            print("The email id of the student: ",emailval.get())
            print("The address of the student: ",addval.get())


        main_head = Label(screen,text="Form", bg="lightgreen")
        main_head.grid(row=1, column=1)

        # Creating lableing for form
        name = Label(screen,text="Name", bg="lightgreen")
        course = Label(screen,text="Course", bg="lightgreen")
        sem = Label(screen,text="Semester", bg="lightgreen")
        form_no = Label(screen,text="Form No.", bg="lightgreen")
        contact = Label(screen,text="Contact No.", bg="lightgreen")
        email = Label(screen,text="Email id", bg="lightgreen")
        add = Label(screen,text="Address", bg="lightgreen")

        name.grid(row=2)
        course.grid(row=3)
        sem.grid(row=4)
        form_no.grid(row=5)
        contact.grid(row=6)
        email.grid(row=7)
        add.grid(row=8)

        # Creating varibles and its types
        nameval = StringVar()
        courseval = StringVar()
        semval = StringVar()
        formval = StringVar()
        contactval = StringVar()
        emailval = StringVar()
        addval = StringVar()

        #  Creating entry boxs
        nameentry = Entry(screen, textvariable=nameval, width=50)
        courseentry = Entry(screen, textvariable=courseval, width=50)
        sementry = Entry(screen, textvariable=semval, width=50)
        formentry = Entry(screen, textvariable=formval, width=50)
        contactentry = Entry(screen, textvariable=contactval, width=50)
        emailentry = Entry(screen, textvariable=emailval, width=50)
        addentry = Entry(screen, textvariable=addval, width=50)

        # Packing boxes in grid
        nameentry.grid(row=2, column=1)
        courseentry.grid(row=3, column=1)
        sementry.grid(row=4, column=1)
        formentry.grid(row=5, column=1)
        contactentry.grid(row=6, column=1)
        emailentry.grid(row=7, column=1)
        addentry.grid(row=8, column=1)

        # Creating a button
        sub_but = Button(screen, text="Submit",bg="red", command=get_val).grid(column=1)

        screen.title("registration form")
        screen.mainloop()


##################################################################################################################################
###############################################################################################################################33

    elif check != "yes":
        tmsg.showwarning("Warning", "Please Accept the terms and conditions")

    else:
        tmsg.showerror("Error","Invalid username or password" )



def signupwindow():
    signup = Toplevel(root)
    signup.title("Signup")
    signup.wm_iconbitmap("csym.ico")
    signup.geometry("1020x630")
    signup.config(bg="#d711fa")

    def sign():
        signup.destroy()

    def signup_function():
        username = user.get()
        password = passw.get()
        confirm_password = confirm_pass.get()
        try:
            f = open("datesheet.txt", 'r')
            d = f.read()
            r = ast.literal_eval(d)
            f.close()
        except:
            f = open('datesheet.txt','w')
            pp = str({'Username':'password'})
            f.write(pp)
            f.close()

        f = open("datesheet.txt", 'r')
        d = f.read()
        r = ast.literal_eval(d)
        f.close()

        if username in r.keys():
            tmsg.showerror("Error","Username already taken")

        elif len(password) >= 6 and password == confirm_password:
            
            try :
                f = open("datesheet.txt","+r")
                d = f.read()
                r = ast.literal_eval(d)


                dict1 = {username:password}
                r.update(dict1)
                f.truncate(0)
                f.close()

                f = open("datesheet.txt",'w')
                w = f.write(str(r))
                signup.destroy()
                tmsg.showinfo('SignUp',"Successfully sign up")
                
            except:
                f = open('datesheet.txt','w')
                pp = str({'Username':'password'})
                f.write(pp)
                f.close()


        elif len(password) < 6:
            tmsg.showwarning("Warning", "Please enter 6 character or more in password ")
        
        else:
            tmsg.showwarning('Invalid',"Both Password should match")

    frame = Frame(signup, bg="#fafcfb", width=980 , height= 570)
    frame.place(x=20, y=30)
    ########################=====

    user = StringVar()
    passw = StringVar()
    confirm_pass = StringVar()
    ##################==========

    image2 = Image.open("side_imagelogin.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    photo2add = Label(frame, image=photo2, bg="#fafcfb")
    photo2add.place(x = 530, y = 30 )

    in_frame = Frame(frame, bg="#ffffff", width=445, height=510)
    in_frame.place(x=60,y=30)


    login_lab = Label(in_frame,text="SignUp", fg="black", bg="#ffffff", font="Ubuntu 18 bold")
    login_lab.place(x = 20, y =20)



    user_lab = Label(in_frame, text="Username", fg="black", bg="#ffffff", font=("@Malgun Gothic" , 10, "bold"))
    user_lab.place(x = 20, y = 68)

    ##################################--------------

    def on_enter(e):
        user_entry.delete(0,'end')

    def on_leave(e):
        name = user_entry.get()
        if name == '':
            user_entry.insert(0,"Example231")

    user_entry = ttk.Entry(in_frame,textvariable=user, width=30,foreground="#969096", font=("Candara" , 16))
    user_entry.place(x = 20, y = 94)
    user_entry.insert(0,"Example231")
    user_entry.bind("<FocusIn>", on_enter)
    user_entry.bind("<FocusOut>", on_leave)

    ######################################--------------

    pass_lab = Label(in_frame, text="Password", fg="black", bg="#ffffff", font=("@Malgun Gothic" , 10, "bold"))
    pass_lab.place(x = 20, y = 146)


    ############################################-----------
    def on_enter(e):
        pass_entry.delete(0,'end')

    def on_leave(e):
        name = pass_entry.get()
        if name == '':
            pass_entry.insert(0,"Enter 6 character or more")

    pass_entry = ttk.Entry(in_frame, textvariable=passw,width=30,foreground="#969096", font=("Candara" , 16))
    pass_entry.place(x = 20, y = 171)
    pass_entry.insert(0,"Enter 6 character or more")
    pass_entry.bind("<FocusIn>", on_enter)
    pass_entry.bind("<FocusOut>", on_leave)


    #################################-----------------

    confirmpass_lab = Label(in_frame, text="Confirm Password", fg="black", bg="#ffffff", font=("@Malgun Gothic" , 10, "bold"))
    confirmpass_lab.place(x = 20, y = 223)


    ############################################-----------
    def on_enter(e):
        confirmpass_entry.delete(0,'end')

    def on_leave(e):
        name = confirmpass_entry.get()
        if name == '':
            confirmpass_entry.insert(0,"Enter 6 character or more")

    confirmpass_entry = ttk.Entry(in_frame,textvariable=confirm_pass, width=30,foreground="#969096", font=("Candara" , 16))
    confirmpass_entry.place(x = 20, y = 250)
    confirmpass_entry.insert(0,"Enter 6 character or more")
    confirmpass_entry.bind("<FocusIn>", on_enter)
    confirmpass_entry.bind("<FocusOut>", on_leave)

    #############################################--------------

    ##########################-----------------

    login_button = Button(in_frame,command=signup_function, width="35", text="SignUp",cursor="hand2",border=0,fg="white", bg="#570da6", font=("@Malgun Gothic" , 12, "bold")  )
    login_button.place(x=20, y=320)

    ###################################_-----------------------
    label2 = Label(in_frame, text="Already signed up?",fg="#969096", bg="#ffffff", font=("Cascadia Code Semilight" , 10))
    label2.place(x = 20, y = 367)

    signup_button = Button(in_frame,cursor="hand2", command=sign, text="Sign In", bg="#ffffff",fg="#aa1bde",border=0,font=("Cascadia Code Semilight" , 10, "bold"))
    signup_button.place(x=170, y=367)

    #########################################----------------
    frame_div = Frame(in_frame, width= 367, height=2, bg="#c9c9c1")
    frame_div.place(x=20, y=420)

    label_div = Label(in_frame, text=" or continue with", fg="#c9c9c1", bg="#ffffff", font=("Candara" , 10))
    label_div.place(x=160, y = 410)

    #################################_----------------------

    photo = PhotoImage(file = "googlesym.png")
    

    photoimage = photo.subsample(3, 3)
    photoadd = Button(in_frame,background="white",border=0,padx=25,font=("@Malgun Gothic" , 12, "bold") , fg="red",text = 'Google', image = photoimage,compound = LEFT)
    photoadd.place(x=20, y=450)



    ###########################_------------------------

    photo1 = PhotoImage(file = "facebooksym.png")
    

    photo1image = photo1.subsample(3, 3)
    photoadd1 = Button(in_frame,background="white",border=0,padx=19,font=("@Malgun Gothic" , 12, "bold") , fg="blue",text = 'Facebook', image = photo1image,compound = LEFT)
    photoadd1.place(x=220, y=450)

    goo_frame1 = Frame(in_frame, width= 164, height=2, bg="#aa1bde")
    goo_frame1.place(x = 20, y=450)

    goo_frame2 = Frame(in_frame, width= 164, height=2, bg="#aa1bde")
    goo_frame2.place(x = 20, y=485)

    goo_frame3 = Frame(in_frame, width= 2, height=35, bg="#aa1bde")
    goo_frame3.place(x = 20, y=450)

    goo_frame4 = Frame(in_frame, width= 2, height=37, bg="#aa1bde")
    goo_frame4.place(x = 184, y=450)


    ##########################_---------------------------------

    face_frame1 = Frame(in_frame, width= 164, height=2, bg="blue")
    face_frame1.place(x = 220, y=450)


    face_frame2 = Frame(in_frame, width= 164, height=2, bg="blue")
    face_frame2.place(x = 220, y=485)

    face_frame3 = Frame(in_frame, width= 2, height=35, bg="blue")
    face_frame3.place(x = 220, y=450)

    face_frame3 = Frame(in_frame, width= 2, height=37, bg="blue")
    face_frame3.place(x = 384, y=450)


    signup.mainloop()
    
#############################################################################################################################
############################################################################################################################
#####################################################################################

user_signin = StringVar()
passw_signin = StringVar()

frame = Frame(root, bg="#fafcfb", width=980 , height= 570)
frame.place(x=20, y=30)


image2 = Image.open("side_imagelogin.jpg")
photo2 = ImageTk.PhotoImage(image2)
photo2add = Label(frame, image=photo2, bg="#fafcfb")
photo2add.place(x = 500, y = 30 )

in_frame = Frame(frame, bg="#ffffff", width=445, height=510)
in_frame.place(x=60,y=30)


login_lab = Label(in_frame,text="Login", fg="black", bg="#ffffff", font="Ubuntu 18 bold")
login_lab.place(x = 20, y =20)

label2 = Label(in_frame, text="Doesn't have an account yet?",fg="#969096", bg="#ffffff", font=("Cascadia Code Semilight" , 10))
label2.place(x = 20, y = 55)

signup_button = Button(in_frame,cursor="hand2", text="Sign Up", bg="#ffffff",fg="#aa1bde",border=0,font=("Cascadia Code Semilight" , 10, "bold"), command=signupwindow)
signup_button.place(x=247, y=55)

user_lab = Label(in_frame, text="Username", fg="black", bg="#ffffff", font=("@Malgun Gothic" , 10, "bold"))
user_lab.place(x = 20, y = 98)

##################################--------------
def on_enter(e):
    user_entry.delete(0,'end')

def on_leave(e):
    name = user_entry.get()
    if name == '':
        user_entry.insert(0,"Example231")

user_entry = Entry(in_frame,border=0,textvariable=user_signin, width=30,foreground="#969096", font=("Candara" , 16))
user_entry.place(x = 20, y = 124)
user_entry.insert(0,"Example231")
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)

frameunder1 = Frame(in_frame, width= 367, height=2, bg="#aa1bde")
frameunder1.place(x = 20, y=153)
######################################--------------

pass_lab = Label(in_frame, text="Password", fg="black", bg="#ffffff", font=("@Malgun Gothic" , 10, "bold"))
pass_lab.place(x = 20, y = 186)


############################################-----------
def on_enter(e):
    pass_entry.delete(0,'end')

def on_leave(e):
    name = pass_entry.get()
    if name == '':
        pass_entry.insert(0,"Password",)

pass_entry = Entry(in_frame ,textvariable=passw_signin,border=0,width=30,foreground="#969096", font=("Candara" , 16))
pass_entry.place(x = 20, y = 214 )
pass_entry.insert(0,"Password")
pass_entry.bind("<FocusIn>", on_enter)
pass_entry.bind("<FocusOut>", on_leave)

frameunder2 = Frame(in_frame, width= 367, height=2, bg="#aa1bde")
frameunder2.place(x = 20, y=244)

#################################-----------------
forgot_button = Button(in_frame, command=forgot_pass,text="Forgot Password?", border=0, fg="#aa1bde", bg="#ffffff",cursor="hand2", font=("@Malgun Gothic" , 10, "bold"))
forgot_button.place(x=247, y=186)

#############################################--------------
checkitem = StringVar()
checkitem.set("nutral")

check = Checkbutton(in_frame, cursor="hand2",text="Accept terms & condition",variable=checkitem, onvalue="yes", offvalue="no" , fg="#4d4f4d", bg="#ffffff", font=("Candara" , 10))
check.place(x=20, y=265)

##########################-----------------

login_button = Button(in_frame, width="36",command=signin, text="LOGIN",cursor="hand2",border=0,fg="white", bg="#570da6", font=("@Malgun Gothic" , 12, "bold")  )
login_button.place(x=20, y=320)

#########################_---------------------------

frame_div = Frame(in_frame, width= 367, height=2, bg="#c9c9c1")
frame_div.place(x=20, y=400)

label_div = Label(in_frame, text=" or login with", fg="#c9c9c1", bg="#ffffff", font=("Candara" , 10))
label_div.place(x=173, y = 390)

#################################_----------------------

photo = PhotoImage(file = "googlesym.png")
  

photoimage = photo.subsample(3, 3)
photoadd = Button(in_frame,background="white",border=0,padx=25,font=("@Malgun Gothic" , 12, "bold") , fg="red",text = 'Google', image = photoimage,compound = LEFT)
photoadd.place(x=20, y=450)



###########################_------------------------

photo1 = PhotoImage(file = "facebooksym.png")
  

photo1image = photo1.subsample(3, 3)
photoadd1 = Button(in_frame,background="white",border=0,padx=19,font=("@Malgun Gothic" , 12, "bold") , fg="blue",text = 'Facebook', image = photo1image,compound = LEFT)
photoadd1.place(x=220, y=450)

goo_frame1 = Frame(in_frame, width= 164, height=2, bg="#aa1bde")
goo_frame1.place(x = 20, y=450)

goo_frame2 = Frame(in_frame, width= 164, height=2, bg="#aa1bde")
goo_frame2.place(x = 20, y=485)

goo_frame3 = Frame(in_frame, width= 2, height=35, bg="#aa1bde")
goo_frame3.place(x = 20, y=450)

goo_frame4 = Frame(in_frame, width= 2, height=37, bg="#aa1bde")
goo_frame4.place(x = 184, y=450)


##########################_---------------------------------

face_frame1 = Frame(in_frame, width= 164, height=2, bg="blue")
face_frame1.place(x = 220, y=450)


face_frame2 = Frame(in_frame, width= 164, height=2, bg="blue")
face_frame2.place(x = 220, y=485)

face_frame3 = Frame(in_frame, width= 2, height=35, bg="blue")
face_frame3.place(x = 220, y=450)

face_frame3 = Frame(in_frame, width= 2, height=37, bg="blue")
face_frame3.place(x = 384, y=450)

root.mainloop()