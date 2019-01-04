from tkinter import *
from tkinter import filedialog
import tkinter as ttk
##from nation_grid_electric import National_Electric 
##from nation_grid_gas import National_Gas
import json_update
import json
import ast

root = Tk()
root.title("Applied Jobs")
root.geometry("1300x700")
root.configure(background='powder blue')
root.resizable(width=False, height=False)

Tops = Frame(root, width = 1200, height = 200, bg="powder blue", relief=SUNKEN)
Tops.grid(row=0)

Left = Frame(root,  height = 200, bg="powder blue", relief=SUNKEN)
Left.grid(row=1, sticky='w')

Right = Frame(root, height = 20, bg="powder blue")
Right.grid(row=1,column=1, sticky='e')

RightBottom = Frame(Right, height = 20, bg="powder blue")
RightBottom.grid(row=2,column=0, sticky='e')

Bottom = Frame(root, bg="powder blue")
Bottom.grid(row=3, sticky='s')

typeVar = StringVar(root)
contactVar = StringVar(root)
resultVar = StringVar(root)

dateData = StringVar(root)
nameData = StringVar(root)
personData = StringVar(root)
informationData = StringVar(root)
workData = StringVar(root)

typeChoices = { 'Career Fair','Employer','Employment Agency'}
contactChoices = { 'By Mail','Email','In Person', 'Phone Number', 'Website'}
resultChoices = { 'Follow-up Requessted','No Response','No Work'}

typeVar.set('Employment Agency') # set the default option
contactVar.set('Website')
resultVar.set('No Response')
 

##-----------------------------Title--------------------------------------------
titleLabel = Label(Tops, font=('arial',50,'bold'), bg='white', text="Enter applied jobs.", anchor='center')
titleLabel.pack()
##-----------------------------Enter Fields-------------------------------
dateLabel = Label(Left, font=('arial',20,'bold'), text="Date:",bg='powder blue').grid(row=0,column=0, sticky='NW')
dateEnt = Entry(Left, bd=5, font=('arial',20), width=20, textvariable=dateData)
dateEnt.focus_set()
dateEnt.grid(row=0,column=1, sticky='W')

typeLabel = Label(Left, font=('arial',20,'bold'), text="Type:",bg='powder blue').grid(row=1,column=0, sticky='NW')
typeEnt = OptionMenu(Left, typeVar, *typeChoices)
typeEnt.configure(width=20, font=('arial',15,'bold'))
typeEnt.grid(row=1,column=1)

nameLabel = Label(Left, font=('arial',20,'bold'), text="Name:",bg='powder blue').grid(row=2,column=0,sticky='nw')
nameEnt = Entry(Left, bd=5, font=('arial',20), width=20, textvariable=nameData).grid(row=2,column=1, sticky='W')

personLabel = Label(Left, font=('arial',20,'bold'), text="Person Contact:",bg='powder blue').grid(row=3,column=0,sticky='nw')
personEnt = Entry(Left, font=('arial',20), bd=5, width=20, textvariable=personData).grid(row=3,column=1, sticky='W')

contactLabel = Label(Left, font=('arial',20,'bold'), text="Contact Method:",bg='powder blue').grid(row=4,column=0,sticky='nw')
contactEnt = OptionMenu(Left, contactVar, *contactChoices)
contactEnt.configure(width=20, font=('arial',15,'bold'))
contactEnt.grid(row=4,column=1)

informationLabel = Label(Left, font=('arial',20,'bold'), text="Contact Information:",bg='powder blue').grid(row=5,column=0,sticky='w')
informationEnt = Entry(Left, bd=5, font=('arial',20), width=20, textvariable=informationData).grid(row=5,column=1, sticky='W')

workLabel = Label(Left, font=('arial',20,'bold'), text="Type of work:",bg='powder blue').grid(row=6,column=0,sticky='w')
workEnt = Entry(Left, bd=5, font=('arial',20), width=20, textvariable=workData).grid(row=6,column=1, sticky='W')

resultLabel = Label(Left, font=('arial',20,'bold'), text="Result:",bg='powder blue').grid(row=7,column=0,sticky='w')
resultEnt = OptionMenu(Left, resultVar, *resultChoices)
resultEnt.configure(width=20, font=('arial',15,'bold'))
resultEnt.grid(row=7,column=1)

##-----------------------------Display Data-------------------------------
def get_json_data():
    conn_string = json_update.openFile('job.json')
    if conn_string:
        return conn_string

listbox = Listbox(Right,font=('arial',20),height=5, width=40)
scrollbar = Scrollbar(Right,command=listbox.yview)

listbox.configure(yscrollcommand=scrollbar.set)

if get_json_data():
    for q in get_json_data():
        listbox.insert(END,q)

text = Text(RightBottom,height=10,width=45,font=("Helvetica", 16),state=DISABLED,wrap=NONE)
scrollbarlabel = Scrollbar(RightBottom,command=text.xview,orient = HORIZONTAL)
text.configure(xscrollcommand=scrollbarlabel.set)


label_text = StringVar()
nameLabel1 = Label(RightBottom,textvariable=label_text,bg='white', font=("Helvetica", 16),
                   height=10,width=40,justify=LEFT,relief=SUNKEN,bd=5, anchor=W)


listbox.grid(row=0,column=0,sticky=W)
scrollbar.grid(row=0,column=1,sticky=N+S+W)
##nameLabel1.grid(row=0,column=0,sticky=W)
text.grid(row=0,column=0,sticky=N+S+W+E)
scrollbarlabel.grid(row=1,column=0,sticky=E+W)

def onselect(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print ('You selected item %d: "%s"' % (index, value))
    print(json_update.displayJSON(value))
    label_text.set(json_update.displayJSON(ast.literal_eval(value)).replace('{','').replace('}',''))
    text.configure(state=NORMAL)
    if text.get(1.0,END):
        text.delete(1.0,END)
    text.insert(END,json_update.displayJSON(ast.literal_eval(value)).replace('{','').replace('}','').replace('"','').replace(',',''))
    text.configure(state=DISABLED)

listbox.bind('<<ListboxSelect>>', onselect)

def refresh_data():
    listbox.delete(0,END)
    for q in get_json_data():
        listbox.insert(END,q)

refreshBtn = Button(RightBottom , text = "Refresh", font=('arial',10), command = refresh_data)
refreshBtn.grid(row=2,column=0) 

##-----------------------------Add Data and Exit-------------------------------

def close_window(): 
    root.destroy()

def clear_data(): 
    dateData.set('')
    nameData.set('')
    personData.set('')
    informationData.set('')
    workData.set('') 

def add_data():
    data_set = {}
    data_set['Date'] = dateData.get()
    data_set['Type'] = typeVar.get() 
    data_set['Name'] = nameData.get()
    data_set['Person Contact'] = personData.get()
    data_set['Contact Method'] = contactVar.get()
    data_set['Contact Information'] = informationData.get()
    data_set['Type of Work'] = workData.get()
    data_set['Result'] = resultVar.get()
    if data_set['Date'] != '':
        print(data_set)
        json_update.json_update(data_set)
        clear_data()
    
button = Button(Bottom, font=('arial',10), text = "Good-bye", command = close_window)
submitBtn = Button(Bottom, font=('arial',10), text = "Add", command = add_data)
clearBtn = Button(Bottom, font=('arial',10), text = "Clear Data", command = clear_data)

submitBtn.grid(row=0, column=0, sticky=N+S)
clearBtn.grid(row=1, column=0, sticky=N+S)
button.grid(row=2, column=0, sticky=N+S)


root.mainloop()
