from tkinter import*
import sqlite3

root=Tk()
root.title('My Kyutie SAm Project')
root.geometry("500x500")

conn=sqlite3.connect('mydata.db')

c = conn.cursor()
'''
c.execute ("""CREATE TABLE "mydata" (
	"f_name"	TEXT,
	"l_name"	TEXT,
	"age"	INTEGER,
	"address"	TEXT,
	"email"	TEXT

)""")
'''

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)
conn.commit()
conn.close()

submit_btn=Button(root,text="Add Record to Database", command=submit)

submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

root.mainloop()
