import backEnd as backend
import mysql.connector
from tkinter import ttk
from tkinter import *
def main():
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Fitness Tracker")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='skyblue2')
        self.frame = Frame(self.master, bg='skyblue2')
        self.frame.pack()
        # self.userName = StringVar()
        # self.pw = StringVar()
        #
        self.label_Title = Label(self.frame, text='Fitness Tracker Login', font=('arial', 50, 'bold'), bg='skyblue2',
                                 fg='black')
        self.label_Title.grid(row=0, column=0, columnspan=2, pady=40)
        #####################Frames
        self.frame2 = LabelFrame(self.frame, width=1350, height=600, font=('arial', 20, 'bold'), relief='ridge',
                                 bg='skyblue2', bd=20)
        self.frame2.grid(row=1, column=0, pady=20, padx=8)
        #####Labels and Entry boxes (user and pw)
        self.userNameLabel = Label(self.frame2, text='Username', font=('arial', 20, 'bold'), bg='skyblue2')
        self.userNameLabel.grid(row=0, column=0, pady=20, padx=20)
        self.textuserName = Entry(self.frame2, font=('arial', 20, 'bold'), bg='LightSteelBlue2')
        self.textuserName.grid(row=0, column=1, pady=20, padx=20)
        self.passwordLabel = Label(self.frame2, text='Password', font=('arial', 20, 'bold'), bg='skyblue2')
        self.passwordLabel.grid(row=1, column=0, pady=20, padx=20)
        self.textpassword = Entry(self.frame2, font=('arial', 20, 'bold'), bg='LightSteelBlue2')
        self.textpassword.grid(row=1, column=1, pady=20, padx=20)
        ####Buttons
        self.Loginbtn = Button(self.frame2, text='Login', width=10, bg='skyblue2', command=self.toMainWindow)
        self.Loginbtn.grid(row=3, column=3, pady=20, padx=20)
        self.Exitbtn = Button(self.frame2, text='Exit', width=10, bg='skyblue2', command=self.appExit)
        self.Exitbtn.grid(row=3, column=0, pady=20, padx=20)
    def toMainWindow(self):
        self.toMainWindow = Toplevel(self.master)
        self.app = MainWindow(self.toMainWindow)
    def appExit(self):
        self.master.destroy()
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("User Records System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='skyblue2')
        self.frame = Frame(self.master, bg='skyblue2')
        self.frame.pack()
        self.frame2 = LabelFrame(self.frame, width=1350, height=600, font=('arial', 20, 'bold'), relief='ridge',
                                 bg='skyblue2', bd=20)
        self.frame2.grid(row=20, column=0, pady=10, padx=10)
        #
        # Define four labels
        self.fnL = Label(self.frame2, text="First Name", bg='skyblue2')
        self.fnL.grid(row=3, column=0)
        #
        self.lastnL = Label(self.frame2, text="Last Name", bg='skyblue2')
        self.lastnL.grid(row=3, column=2)
        #
        self.goal_label = Label(self.frame2, text="Fitness Goal", bg='skyblue2')
        self.goal_label.grid(row=4, column=0)
        self.weight_label = Label(self.frame2, text="Weight", bg='skyblue2')
        self.weight_label.grid(row=4, column=2)
        # Define Entries
        self.fname_entry = StringVar()
        self.e1 = Entry(self.frame2, textvariable=self.fname_entry)
        self.e1.grid(row=3, column=1)
        self.lastname_entry = StringVar()
        self.e2 = Entry(self.frame2, textvariable=self.lastname_entry)
        self.e2.grid(row=3, column=3)
        self.goal_entry = StringVar()
        self.e3 = Entry(self.frame2, textvariable=self.goal_entry)
        self.e3.grid(row=4, column=1)
        #
        self.weight_entry = StringVar()
        self.e4 = Entry(self.frame2, textvariable=self.weight_entry)
        self.e4.grid(row=4, column=3, pady=5, padx=5)
        #
        #
        self.searchBtn = Button(self.frame2, text="Search Record", width=15, command=self.toSearchWindow)
        self.searchBtn.grid(row=11, column=0, pady=20, padx=20)
        self.addBtn = Button(self.frame2, text="Add Record", width=15,
                             command=lambda: [self.text.delete(1.0, END), self.text.insert(END,
                                                                                           backend.newUser(
                                                                                               self.fname_entry.get(),
                                                                                               self.lastname_entry.get(),
                                                                                               self.goal_entry.get())), self.clearEntries()])
        self.addBtn.grid(row=5, column=0, pady=10, padx=10)
        # lambda: self.text.insert(END,
        self.updateBtn = Button(self.frame2, text='Update', width=15,
                                command=lambda: [self.text.delete(1.0, END), self.text.insert(END,
                                                                                              backend.userUpdate(
                                                                                                  self.fname_entry.get(),
                                                                                                  self.lastname_entry.get(),
                                                                                                  self.goal_entry.get())), self.clearEntries()])
        self.updateBtn.grid(row=5, column=3, pady=10, padx=10)
        #
        self.deleteBtn = Button(self.frame2, text="Delete", width=15, command=lambda: [self.text.delete(1.0, END), self.text.insert(END,
                                                                                              backend.userDelete(
                                                                                                  self.fname_entry.get(),
                                                                                                  self.lastname_entry.get(),)), self.clearEntries()])
        self.deleteBtn.grid(row=6, column=3, pady=10, padx=10)
        self.viewBtn = Button(self.frame2, text="View All Users", width=15, command=self.toViewAllRecords)
        self.viewBtn.grid(row=6, column=0, pady=10, padx=10)
        self.text = Text(self.frame2, height=5, width=100, bg='skyblue2')
        self.text.grid(row=7, columnspan=7, padx=5, pady=5)
        self.closeBtn = Button(self.frame2, text="Close", width=15, command=self.appExit)
        self.closeBtn.grid(row=11, column=3, pady=10, padx=10)
    def displayData(self):
        self.records.delete(0, END)
        for row in lambda: backend.showData():
            self.records.insert(END, row, str(""))
    def clearEntries(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
    def toSearchWindow(self):
        self.toSearchWindow = Toplevel(self.master)
        self.app = searchRecordWindow(self.toSearchWindow)
    def toViewAllRecords(self):
        self.toViewAllRecords = Toplevel(self.master)
        self.app = viewAllRecords(self.toViewAllRecords)
    def appExit(self):
        self.master.destroy()
class searchRecordWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("User Records System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='skyblue2')
        self.frame = Frame(self.master, bg='skyblue2')
        self.frame.pack()
        self.label_Title = Label(self.frame, text='Search User', font=('arial', 50, 'bold'), bg='skyblue2',
                                 fg='black')
        self.label_Title.grid(row=0, column=0, columnspan=2, pady=40)
        self.frame2 = LabelFrame(self.frame, width=1350, height=600, font=('arial', 20, 'bold'), relief='ridge',
                                 bg='skyblue2', bd=20)
        self.frame2.grid(row=20, column=0, pady=20, padx=20)
        #
        # Define four labels
        self.fnL = Label(self.frame2, text="First Name", bg='skyblue2')
        self.fnL.grid(row=3, column=0, pady=20, padx=20)
        #
        self.lastnL = Label(self.frame2, text="Last Name", bg='skyblue2')
        self.lastnL.grid(row=3, column=2, pady=20, padx=20)
        # Define Entries
        self.fname_entry = StringVar()
        self.e1 = Entry(self.frame2, textvariable=self.fname_entry)
        self.e1.grid(row=3, column=1, pady=20, padx=20)
        self.lastname_entry = StringVar()
        self.e2 = Entry(self.frame2, textvariable=self.lastname_entry)
        self.e2.grid(row=3, column=3, pady=20, padx=20)
        self.text = Text(self.frame2, height=15, width=60)
        self.text.grid(row=4, columnspan=4, padx=20, pady=20)
        self.searchBtn = Button(self.frame2, text="Search Record", width=12, bg='skyblue2',
                                command=lambda: self.text.insert(END, backend.searchData(self.fname_entry.get(),
                                                                                         self.lastname_entry.get())))
        self.searchBtn.grid(row=5, column=2, padx=20, pady=20)
        self.exitBtn = Button(self.frame2, text="Exit", width=12, bg='skyblue2', command=self.appExit)
        self.exitBtn.grid(row=6, column=2, padx=30, pady=20)
    def appExit(self):
        self.master.destroy()
class viewAllRecords:
    def __init__(self, master):
        self.master = master
        self.master.title("All Records")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='skyblue2')
        self.frame = Frame(self.master, bg='skyblue2')
        self.frame.pack()
        self.label_Title = Label(self.frame, text='Records', font=('arial', 50, 'bold'), bg='skyblue2',
                                 fg='black')
        self.label_Title.grid(row=0, column=0, columnspan=2, pady=40)
        self.frame2 = LabelFrame(self.frame, width=1350, height=600, font=('arial', 20, 'bold'), relief='ridge',
                                 bg='skyblue2', bd=20)
        self.frame2.grid(row=20, column=0)
        self.exitBtn = Button(self.frame2, text="Exit", width=12, bg='skyblue2', command=self.appExit)
        self.exitBtn.grid(row=8, column=2, padx=20, pady=20)
        self.text = Text(self.frame2, height=15, width=60)
        self.text.grid(row=4, columnspan=3, padx=20, pady=20)
        self.showRecBtn = Button(self.frame2, text="Display Records", width=12, bg='skyblue2',
                                 command=lambda: self.text.insert(END, backend.showData()))
        self.showRecBtn.grid(row=8, column=1, padx=20, pady=20)
        self.exportCSVBtn = Button(self.frame2, text="Export", width=12, bg='skyblue2',
                                   command=lambda: backend.exportCSV())
        self.exportCSVBtn.grid(row=8, column=3, padx=20, pady=20)
    def appExit(self):
        self.master.destroy()
if __name__ == '__main__':
    main()