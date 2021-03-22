from datetime import datetime
from tkinter import *
# oyna = Tk()
# oyna.title('Dastur')
# oyna.geometry('300x300')
#
# natija = Label(text="Natija", bg="white")
# natija.place(x=90,y=135,width=120,height=40)
#
# yil=Entry()
# yil.place(x=75,y=50,width=150,height=30)
#
# def farq():
#     bugun = datetime.today()
#     natija.config(text=bugun.year - int(yil.get()))
#
# tugma = Button(text="Hisoblash", command=farq)
# tugma.place(x=90,y=90,width=120,height=40)
#
#
#
# oyna.mainloop()
#

# def farq(yil):
#     bugun = datetime.today()
#     natija = bugun.year - int(yil)
#     return natija
# tugilgan_yil=input('Tug`ilgan yilni kirit: ')
# natija_f=farq(tugilgan_yil)
#
# print('Natija: ', natija_f)
#
# maktab_yil=input('Yilni kiriting: ')
# natija_f = farq(maktab_yil)
# print('Natija=',natija_f)


#mashq
# def popular_list():
#     print('Pupolate')
#
# def add_item():
#     print('Add')
#
# def remove_item():
#     print('Remove')
#
# def update_item():
#     print('Update')
#
# def clear_item():
#     print('Clear Input')
# #Obyekt oynasi yaratish
# app=Tk()
#
# #Part
# part_text=StringVar()
# part_label=Label(app, text='Part Name', font=('bold', '14'), pady=20)
# part_label.grid(row=0, column=0)
# part_entry=Entry(app, textvariable=part_text)
# part_entry.grid(row=0, column=1)
#
# #Customer
# customer_text=StringVar()
# customer_label=Label(app, text='Customer', font=('bold', '14'))
# customer_label.grid(row=0, column=2, sticky=W)
# customer_entry=Entry(app, textvariable=customer_text)
# customer_entry.grid(row=0, column=3)
#
# #Retailer
# retailer_text=StringVar()
# retailer_label=Label(app, text='Retailer', font=('bold', '14'))
# retailer_label.grid(row=1, column=0, sticky=W)
# retailer_entry=Entry(app, textvariable=retailer_text)
# retailer_entry.grid(row=1, column=1)
#
# #Price
# price_text=StringVar()
# price_label=Label(app, text='Price', font=('bold', '14'))
# price_label.grid(row=1, column=2, sticky=W)
# price_entry=Entry(app, textvariable=price_text)
# price_entry.grid(row=1, column=3)
#
# #Parts List (Listbox)
# part_list=Listbox(app, height=8, width=50, border=0)
# part_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#
# #Create Csrolbar
# scrollbar=Scrollbar(app)
# scrollbar.grid(row=3, column=3)
#
# #Set scroll to listbox
# part_list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=part_list.yview)
#
# #Buttons
# add_btn=Button(app, text='Add Part', width=12, command=add_item)
# add_btn.grid(row=2, column=0, pady=20)
#
# remove_btn=Button(app, text='Remove Part', width=12, command=remove_item)
# remove_btn.grid(row=2, column=1)
#
# update_btn=Button(app, text='Update Part', width=12, command=update_item)
# update_btn.grid(row=2, column=2)
#
# clear_btn=Button(app, text='Clear Input', width=12, command=clear_item)
# clear_btn.grid(row=2, column=3)
#
# app.title('Dastur oynasi')
# app.geometry('700x350')
#
# # Populate data
#
#
# # Start program
# app.mainloop()


#mashq3- Oyna parametrlarini sozlash
# from tkinter import  *
#
# root = Tk() #root
# root['bg'] ='#faf852' #fon rangi
# root.title  = "MALUMOT" #Oyna momi
# root.wm_attributes('-alpha',0.8) #oyna yorugliligi
# root.geometry = ('400 x 400') #oyna o'lchami
# root.resizable(width = True, height = True) #oynani kattalashtirish yoki
# # kichiklashtirishni o'chirib ko'yamiz
# root.mainloop()


#mashq-4- Kalkulyator
from tkinter import *
from decimal import *

root = Tk()
root.title('Kalkulyator')

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

activeStr = ''
stack = []
def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

label = Label(root, text='0', width=75)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col],
                command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()