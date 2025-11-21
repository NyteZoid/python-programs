#start



from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector as sqlconn


myconn = sqlconn.connect(
    host = "localhost",
    user = "root",
    password = "****")

cur = myconn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS SDBMS;")
cur.execute("USE SDBMS;")
cur.execute("CREATE TABLE IF NOT EXISTS DATA(roll INT PRIMARY KEY, name VARCHAR(30), class INT, section CHAR(1), house VARCHAR(7));")



def Main():
    global start
    start = Tk()
    start.geometry('700x600')
    start.configure(bg = 'cornflower blue')
    start.title('STUDENT MANAGEMENT SYSTEM')
    start.resizable(False, False)

    start.protocol("WM_DELETE_WINDOW", lambda: (start.destroy()))

    Label(start, text = 'DELHI PUBLIC SCHOOL PRAYAGRAJ', fg = 'black', bg = "cornflower blue", font = ('Times New Roman', 20)).place(x=120, y=50)
    Label(start, text = 'STUDENT MANAGEMENT SYSTEM', fg = 'black', bg = "cornflower blue", font = ('Bahnschrift bold', 30)).place(x=50, y=120)
    Label(start, text = 'By :- Abhiraj Mandal', fg = 'black', bg = "cornflower blue", font = ('Bahnschrift bold', 20)).place(x=225, y=400)

    def LOGIN():
        start.withdraw()
        LoginForm()
    Button(start, text = "Start", command = LOGIN, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=300, y=500)

    start.mainloop()



def LoginForm():
    Myform = Toplevel()
    Myform.geometry('400x300')
    Myform.configure(bg = 'cornflower blue')
    Myform.title('STUDENT MANAGEMENT SYSTEM')
    Myform.resizable(False, False)

    Myform.protocol("WM_DELETE_WINDOW", lambda: (Myform.destroy(), start.destroy()))

    Label(Myform, text = 'LOGIN', fg = 'black', bg = "cornflower blue", font = ('Bahnschrift bold', 30)).place(x=145, y=20)
    Label(Myform, text = 'User Name', fg = 'black', bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=52, y=98)
    Label(Myform, text = 'Password', fg = 'black', bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=52, y=148)

    v1 = StringVar()
    v2 = StringVar()
    T1 = Entry(Myform, fg = "black", bg = "white", textvariable = v1, font = ('bahnschrift semibold', 10)).place(x=202, y=110)
    T2 = Entry(Myform, fg = "black", bg = "white", textvariable = v2, show = "*",font = ('bahnschrift semibold', 10)).place(x=202, y=160)

    def BACK():
        Myform.destroy()
        start.deiconify()
    Button(Myform, text = "Back", command = BACK, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=42, y=220)

    def CLEAR():
        v1.set('')
        v2.set('')
    Button(Myform, text = "Clear", command = CLEAR, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=152, y=220)

    def VALIDATE():
        if v1.get() == "abhiraj" and v2.get() == "1809":
            Myform.destroy()
            MenuForm()
        else:
            messagebox.showinfo("Access Denied", "Invalid Username or Password")
    Button(Myform, text = "Login", command = VALIDATE, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=262, y=220)



def MenuForm():
    Menu = Toplevel()
    Menu.geometry('400x300')
    Menu.configure(bg = 'cornflower blue')
    Menu.title('STUDENT MANAGEMENT SYSTEM')
    Menu.resizable(False, False)

    Menu.protocol("WM_DELETE_WINDOW", lambda: (Menu.destroy(), start.destroy()))

    Label(Menu, text = 'MENU', fg = 'black', bg = "cornflower blue", font = ('Bahnschrift bold', 30)).place(x=145, y=20)

    def SMENU():
        Menu.destroy()
        StudentMenuForm()
    Button(Menu, text = "Manage Students", command = SMENU, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=100, y=115)
    
    def EMENU():
        messagebox.showinfo("Info", "Exam Menu is under construction.")
    Button(Menu, text = "Manage Marks", command = EMENU, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 26).place(x=100, y=200)



def StudentMenuForm():
    SMenu = Toplevel()
    SMenu.geometry('500x500')
    SMenu.configure(bg = 'cornflower blue')
    SMenu.title('STUDENT MANAGEMENT SYSTEM')
    SMenu.resizable(False,False)

    SMenu.protocol("WM_DELETE_WINDOW", lambda: (SMenu.destroy(), start.destroy()))

    Label(SMenu, text = 'STUDENT MENU', fg = 'black', bg = "cornflower blue", font = ('bahnschrift bold', 30)).place(x=130, y=50)

    def New():
        SMenu.destroy()
        NewForm()
    def Display():
        SMenu.destroy()
        DisplayForm()
    def Update():
        SMenu.destroy()
        UpdateForm()
    def Delete():
        SMenu.destroy()
        DeleteForm()
    def Search():
        SMenu.destroy()
        SearchForm()
    def Exit():
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            SMenu.destroy()
            start.destroy()

    Button(SMenu, text = "NEW", command = New, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 30).place(x=90, y=180)
    Button(SMenu, text = "DISPLAY", command = Display, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=290, y=180)
    Button(SMenu, text = "UPDATE", command = Update, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=90, y=280)
    Button(SMenu, text = "DELETE", command = Delete, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 18).place(x=290, y=280)
    Button(SMenu, text = "SEARCH", command = Search, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=90, y=380)
    Button(SMenu, text = "EXIT", command = Exit, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 35).place(x=290, y=380)



def NewForm():
    New = Toplevel()
    New.geometry('500x500')
    New.configure(bg = 'cornflower blue')
    New.title('STUDENT MANAGEMENT SYSTEM')
    New.resizable(False,False)

    New.protocol("WM_DELETE_WINDOW", lambda: (New.destroy(), start.destroy()))

    Label(New, text = 'NEW RECORD', fg = 'black', bg = 'cornflower blue', font = ('bahnschrift bold', 30)).place(x=120, y=20)
    cur.execute("SELECT MAX(roll) FROM DATA")
    result = cur.fetchone()
    if result[0] is None:
        nextroll = 101
    else:
        nextroll = result[0] + 1

    rn = StringVar(value = str(nextroll))
    nm = StringVar()
    cl = StringVar()
    sc = StringVar()
    hs = StringVar()

    Label(New, text='Roll Number', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=60,y=120)
    T1 = Entry(New, fg = "white", bg = "gray26", textvariable = rn, state = "readonly", font = ('bahnschrift semibold', 9)).place(x=300, y=130)
    Label(New, text='Name', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=60,y=170)
    T2 = Entry(New, fg = "black", bg = "white", textvariable = nm, font = ('bahnschrift semibold', 9)).place(x=300, y=180)
    Label(New, text = 'Class', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=60,y=220)
    T3 = ttk.Combobox(New, state = "readonly", textvariable = cl, values = [1,2,3,4,5,6,7,8,9,10,11,12], width = 17, font = ('bahnschrift semibold', 9)).place(x=300,y=230)
    Label(New, text = 'Section', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=60,y=270)
    T4 = ttk.Combobox(New, state = "readonly", textvariable = sc, values = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"], width = 17, font = ('bahnschrift semibold', 9)).place(x=300,y=280)
    Label(New, text = 'House', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=60,y=320)
    T5 = ttk.Combobox(New, state = "readonly", textvariable = hs, values = ["RED","GREEN","BLUE","YELLOW"], width = 17, font = ('bahnschrift semibold', 9)).place(x=300,y=330)

    def BACK():
        New.destroy()
        MenuForm()
    Button(New, text = "Back", command = BACK, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=60, y=420)

    def CLEAR():
        nm.set('')
        cl.set('')
        sc.set('')
        hs.set('')
    Button(New, text = "Clear", command = CLEAR, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=192.5, y=420)

    def VALIDATE():
        if rn.get() == "" or nm.get() == "" or cl.get() == "" or sc.get() == "" or hs.get() == "":
            messagebox.showinfo("Failed", "Please try again")
        else:
            roll = int(rn.get())
            name =  nm.get()
            clas = int(cl.get())
            sect = sc.get()
            house = hs.get()
            sql = "INSERT INTO DATA VALUES (%s,%s,%s,%s,%s);"
            data = (roll,name,clas,sect,house)
            cur.execute(sql,data)
            myconn.commit()
            messagebox.showinfo("Success","Record added")
            New.destroy()
            MenuForm()
    Button(New, text = "Enter", command = VALIDATE, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=325, y=420)



def DeleteForm():
    Del = Toplevel()
    Del.geometry('500x300')
    Del.configure(bg = 'cornflower blue')
    Del.title('STUDENT MANAGEMENT SYSTEM')
    Del.resizable(False,False)

    Del.protocol("WM_DELETE_WINDOW", lambda: (Del.destroy(), start.destroy()))

    Label(Del, text = 'DELETE RECORD', fg = 'black', bg = 'cornflower blue', font = ('bahnschrift bold', 30)).place(x=100, y=20)
    Label(Del, text = 'Roll Number', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=80,y=120)
    n = StringVar()
    T = Entry(Del, fg = "black", bg = "white", textvariable = n, width = 10, font = ('bahnschrift semibold', 9)).place(x=320, y=133)

    def BACK():
        Del.destroy()
        MenuForm()
    Button(Del, text = "Back", command = BACK, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=60, y=220)

    def CLEAR():
        n.set('')
    Button(Del, text = "Clear", command = CLEAR, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=192.5, y=220)

    def VALIDATE():
        cur.execute("SELECT roll FROM DATA;")
        L = cur.fetchall()
        H = []
        for x in L:
            H.append(str(x[0]))
        if n.get() in H:
            confirm = messagebox.askyesno("Confirm Delete", f"Delete record with Roll No {n.get()}?")
            if confirm:
                cur.execute(f"DELETE FROM DATA WHERE roll = {n.get()};")
                myconn.commit()
                messagebox.showinfo("Success", "Record Deleted")
                Del.destroy()
                MenuForm()
        else:
            messagebox.showinfo("Failed", "Invalid Roll Number")
    Button(Del, text = "Enter", command = VALIDATE, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=325, y=220)



def DisplayForm():
    Dis = Toplevel()
    Dis.geometry('700x500')
    Dis.configure(bg = 'cornflower blue')
    Dis.title('STUDENT MANAGEMENT SYSTEM')
    Dis.resizable(False, False)

    Dis.protocol("WM_DELETE_WINDOW", lambda: (Dis.destroy(), start.destroy()))

    Label(Dis, text = 'DISPLAY RECORDS', fg = 'black', bg = 'cornflower blue', font = ('bahnschrift bold', 30)).place(x=180, y=20)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview", background = "white", foreground = "black", rowheight = 25, fieldbackground = "white")
    style.map('Treeview', background = [('selected', 'cornflower blue')])

    tree = ttk.Treeview(Dis, columns = ("roll", "name", "class", "section", "house"), show = 'headings', height = 12)

    tree.heading("roll", text = "Roll No")
    tree.heading("name", text = "Name")
    tree.heading("class", text = "Class")
    tree.heading("section", text = "Section")
    tree.heading("house", text = "House")

    tree.column("roll", anchor = CENTER, width = 80)
    tree.column("name", anchor = W, width = 180)
    tree.column("class", anchor = CENTER, width = 80)
    tree.column("section", anchor = CENTER, width = 80)
    tree.column("house", anchor = CENTER, width = 120)

    cur.execute("SELECT * FROM DATA;")
    data = cur.fetchall()
    for row in data:
        tree.insert('', 'end', values = row)

    scroll = ttk.Scrollbar(Dis, orient = "vertical", command = tree.yview)
    tree.configure(yscrollcommand = scroll.set)
    scroll.place(x=660, y=80, height = 331)

    tree.place(x=75, y=80)

    def BACK():
        Dis.destroy()
        MenuForm()

    Button(Dis, text = "Back", command = BACK, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=300, y=430)



def UpdateForm():
    Upd = Toplevel()
    Upd.geometry('500x400')
    Upd.configure(bg = 'cornflower blue')
    Upd.title('STUDENT MANAGEMENT SYSTEM')
    Upd.resizable(False, False)

    Upd.protocol("WM_DELETE_WINDOW", lambda: (Upd.destroy(), start.destroy()))

    Label(Upd, text = 'UPDATE RECORD', fg = 'black', bg = 'cornflower blue', font = ('bahnschrift bold', 30)).place(x=95, y=20)

    Label(Upd, text = 'Roll Number', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=80, y=120)
    n = StringVar()
    T1 = Entry(Upd, fg = "black", bg = "white", textvariable = n, width = 14, font = ('bahnschrift semibold', 9)).place(x=320, y=133)

    Label(Upd, text = 'Column', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=80, y=180)
    col = StringVar()
    T2 = ttk.Combobox(Upd, state = "readonly", textvariable = col, values = ['Name', 'Class', 'Section', 'House'], width = 11, font = ('bahnschrift semibold', 9)).place(x=320, y=193)

    Label(Upd, text = 'New Value', fg = 'black',bg = "cornflower blue", font = ('bahnschrift semibold', 20)).place(x=80, y=240)
    uv = StringVar()
    T3 = Entry(Upd, fg = "black", bg = "white", textvariable = uv, width = 14, font = ('bahnschrift semibold', 9)).place(x=320, y=253)

    def BACK():
        Upd.destroy()
        MenuForm()
    Button(Upd, text = "Back", command = BACK, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=60, y=320)

    def CLEAR():
        n.set('')
        col.set('')
        uv.set('')
    Button(Upd, text = "Clear", command = CLEAR, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=192.5, y=320)

    def VALIDATE():
        cur.execute("SELECT roll FROM DATA;")
        L = cur.fetchall()
        H = []
        for x in L:
            H.append(str(x[0]))
        if n.get() in H:
            if col.get().lower() in ['name','section','house']:
                cur.execute(f"UPDATE DATA SET {col.get()} = '{(uv.get())}' WHERE roll = {n.get()};")
            else:
                cur.execute(f"UPDATE DATA SET {col.get()} = {(uv.get())} WHERE roll = {n.get()};")
            myconn.commit()
            messagebox.showinfo("Success", "Record Updated")
            Upd.destroy()
            MenuForm()
        else:
            messagebox.showinfo("Failed", "Invalid Roll Number")
    Button(Upd, text = "Enter", command = VALIDATE, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=325, y=320)



def SearchForm():
    Ser = Toplevel()
    Ser.geometry('700x500')
    Ser.configure(bg = 'cornflower blue')
    Ser.title('STUDENT MANAGEMENT SYSTEM')
    Ser.resizable(False, False)

    Ser.protocol("WM_DELETE_WINDOW", lambda: (Ser.destroy(), start.destroy()))

    Label(Ser, text = 'SEARCH RECORDS', fg = 'black', bg = 'cornflower blue', font = ('bahnschrift bold', 30)).place(x=180, y=20)

    c = StringVar()
    n = StringVar()
    T1 = ttk.Combobox(Ser, state = "readonly", textvariable = c, values = ['Roll No', 'Name', 'Class', 'Section', 'House'], width = 11, font = ('bahnschrift semibold', 15)).place(x=165, y=100)
    T2 = Entry(Ser, fg = "black", bg = "white", textvariable = n, width = 10, font = ('bahnschrift semibold', 15)).place(x=425, y=100)

    def VALIDATE():
        if not c.get():
            messagebox.showinfo("Error", "Please select a search field.")
            return
        elif not n.get():
            messagebox.showinfo("Error", "Please enter a value to search.")
            return
        
        if c.get() == "Roll No":
            z = "roll"
        elif c.get() == "Name":
            z = "name"
        elif c.get() == "Class":
            z = "class"
        elif c.get() == "Section":
            z = "section"
        else:
            z = "house"
    
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background = "white", foreground = "black", rowheight = 25, fieldbackground = "white")
        style.map('Treeview', background = [('selected', 'cornflower blue')])

        tree = ttk.Treeview(Ser, columns = ("roll", "name", "class", "section", "house"), show = 'headings', height = 8)

        tree.heading("roll", text = "Roll No")
        tree.heading("name", text = "Name")
        tree.heading("class", text = "Class")
        tree.heading("section", text = "Section")
        tree.heading("house", text = "House")

        tree.column("roll", anchor = CENTER, width = 80)
        tree.column("name", anchor = W, width = 180)
        tree.column("class", anchor = CENTER, width = 80)
        tree.column("section", anchor = CENTER, width = 80)
        tree.column("house", anchor = CENTER, width = 120)

        if z in ['section','house']:
            if n.get().isalpha() == False:
                messagebox.showinfo("Error", f"{c.get()} must be a word.")
                return
            cur.execute(f"SELECT * FROM DATA WHERE {z} = '{n.get().upper()}';")
        elif z in ['name']:
            if n.get().replace(" ","").isalpha() == False:
                messagebox.showinfo("Error", f"{c.get()} must be a word.")
                return
            cur.execute(f"SELECT * FROM DATA WHERE {z} LIKE '%{n.get()}%';")
        else:
            if n.get().isdigit() == False:
                messagebox.showinfo("Error", f"{c.get()} must be a number.")
                return
            cur.execute(f"SELECT * FROM DATA WHERE {z} = {n.get()};")
        
        values = cur.fetchall()
        for row in values:
            tree.insert('', 'end', values = row)

        scroll = ttk.Scrollbar(Ser, orient = "vertical", command = tree.yview)
        tree.configure(yscrollcommand = scroll.set)
        scroll.place(x=660, y=160, height = 231)

        tree.place(x=75, y=160)

    Button(Ser, text = "Enter", command = VALIDATE, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=300, y=430)

    def BACK():
        Ser.destroy()
        MenuForm()
    Button(Ser, text = "Back", command = BACK, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=190, y=430)

    def CLEAR():
        n.set('')
        c.set('')
    Button(Ser, text = "Clear", command = CLEAR, border = 3, font = ("bahnschrift semibold", 15), bg = "gray67", fg = "black", padx = 15).place(x=410, y=430)



Main()
myconn.close()



#end
