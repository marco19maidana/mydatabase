# configured mariadb with utf8
import mysql.connector
import tkinter as tk
from tkinter import ttk
import mysql.connector

# database connection to lampedusa_airlines_db
mydb = mysql.connector.connect(host='localhost', port=3306, user="root", password='unbekannt',
                               database='lampedusa_airlines_db')
cursor = mydb.cursor()
# data output of a wished table
'SELECT f.FlugNr, s.Stadtname, f.StartAbflug, zo.Stadtname, f.ZielAnkunft FROM flug f INNER JOIN Ort so ON f.StartOrtId = so.OrtId'
'INNER JOIN Ort zo ON f.ZielOrtId = zo.OrtId' \
'ORDER BY f.StartAbflug'
# sql = "SELECT * FROM Flug"
# ort table is the same but is treated as two different
sql = 'SELECT f.FlugNr, so.Stadtname, f.StartAbflug, zo.Stadtname, f.ZielAnkunft FROM flug f INNER JOIN Ort so ON f.StartOrtId = so.OrtId INNER JOIN Ort zo ON f.ZielOrtId = zo.OrtId ORDER BY f.StartAbflug'
cursor.execute(sql)
rows = cursor.fetchall()
total = cursor.rowcount
print('Total data entries: '+str(total))

win = tk.Tk()
frm = tk.Frame(win)
frm.pack(side=tk.LEFT, padx=20)

tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6), show='headings', height='5')
tv.pack()
tv.heading(1, text='FlugNr')
tv.heading(2, text='StartOrt')
tv.heading(3, text='StartAbflug')
tv.heading(4, text='ZielOrt')
tv.heading(5, text='ZielAnkunft')
tv.heading(6, text='Sitzkapazität')

for i in rows:
    tv.insert('', 'end', values=i)
win.title('Our Project')
win.geometry('500x500')
win.mainloop()





'''
    FlugId.delete(0, END)
    FlugId_label.delete(0, END)

# create text boxes
FlugId = Entry(gui, width=30)
FlugId.grid(row=0, column=0, padx=20)

# create textbox labels
FlugId_label = Label(gui, text='flug')
FlugId_label.grid(row=0, column=0)

# create Submit Button
submit_btn = Button(gui, text='Add record to db', command=submit())
submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
'''
