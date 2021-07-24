from tkinter import *
from math import *
import tkinter.messagebox as msg

def theme():
    if var1.get()==1:
        calc.configure(bg="black")
        frame.configure(bg="black")
        for i in range(40):
            buttons[i].configure(fg="black",bg="grey")
            buttons[i].update()
            enter.configure(fg="red",disabledforeground="black")
    else:
        calc.configure(bg="white")
        frame.configure(bg="white")
        enter.configure(fg="blue2",disabledforeground="blue2")
        for i in range(40):
            buttons[i].configure(fg="blue2",bg="white")
            buttons[i].update()
def toggle():
    if buttons[19].cget('text')=="SC":
        calc.geometry("949x570")
        calc.resizable(height=False,width=False)
        buttons[19].configure(text="ST")
    else:
        calc.geometry("480x570")
        calc.resizable(height=False,width=False)
        buttons[19].configure(text="SC")


ct=0
def showvalue(co):
    global ct
    if ct==0:
        entryvar.set("")
        ct=1
    entryvar.set(entryvar.get()+co)


def click(event):
    global ct
    if event.widget in buttons:
        text=event.widget.cget('text')
    else:
        if str(event.char) in ['1','2','3','4','5','6','7','8','9','0','+','-','*','/','=','.']:
            text=str(event.char)
        else:
            pass
    
    if text=="=":
        try:
            value=eval(entryvar.get())
            entryvar.set(value)
        except:
            entryvar.set("Error")
    elif text=="C":
        entryvar.set("0")
        ct=0
    elif text=="<=":
        expr=entryvar.get()
        entryvar.set(expr.replace(expr[len(expr)-1],""))
        if entryvar.get()=="":
            ct=0
            entryvar.set("0")
    elif text=="π":
        showvalue("pi")
    
    elif text=="cos":
        showvalue("cos(")
    elif text=="sin":
        showvalue("sin(")
    elif text=="tan":
        showvalue("tan(")
    elif text=="√":
        showvalue("sqrt(")
    elif text=="!":
        showvalue("factorial(")
    elif text=="x^y":
        showvalue("**")
    elif text=="cosh":
        showvalue("cosh(")
    elif text=="sinh":
        showvalue("sinh(")
    elif text=="tanh":
        showvalue("tanh(")
    elif text=="Deg":
        entryvar.set(str(degrees(float(entryvar.get()))))
    elif text=="sin-1":
        showvalue("asin(")
    elif text=="cos-1":
        showvalue("acos(")
    elif text=="tan-1":
        showvalue("atan(")
    elif text=="1/x":
        showvalue("**(-1)")
    elif text=="ln":
        showvalue("log(")
    elif text=="lg":
        showvalue("log10(")
    else:
        showvalue(text)

def history():
    pass

calc=Tk()
calc.geometry("480x570")
calc.resizable(height=False,width=False)
photo=PhotoImage(file="Calculator.png")
calc.iconphoto(False,photo)
calc.title("Calculator")

#******************************************************************************************************
var1=IntVar()
mainmenu=Menu(calc)

m1=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="Theme",menu=m1)
m1.add_checkbutton(label="Dark Theme",activebackground="black",activeforeground="red",command=theme,variable=var1)
mainmenu.add_checkbutton(label="Show History",command=history)
calc.config(menu=mainmenu)

#**************************************************************************************************************

frame=Frame(calc)
frame.grid()

entryvar=StringVar()
entryvar.set("0")
enter=Entry(frame,width=28,font="arial 20 bold",justify=RIGHT,bd=30,bg="lightgrey",fg="blue2",textvariable=entryvar,state=DISABLED,disabledforeground="blue2")
enter.grid(row=0,column=0,columnspan=4,pady=1)

buttons=[]
button1_9="789456123"
i=0
for j in range(2,5):
    for k in range(3):
        buttons.append(Button(frame,height=2,width=6,text=button1_9[i],font="arial 20 bold",bd=4,fg="blue2"))
        buttons[i].grid(row=j,column=k,pady=1)
        i+=1

buttons.append(Button(frame,height=2,width=6,text="C",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="%",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="<=",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="+",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="-",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="*",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="/",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="=",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text=".",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="0",font="arial 20 bold",bd=4,fg="blue2"))
buttons.append(Button(frame,height=2,width=6,text="SC",font="arial 20 bold",bd=4,fg="blue2",command=toggle))

buttons[9].grid(row=1,column=0,pady=1)
buttons[10].grid(row=1,column=1,pady=1)
buttons[11].grid(row=1,column=2,pady=1)
buttons[12].grid(row=1,column=3,pady=1)
buttons[13].grid(row=2,column=3,pady=1)
buttons[14].grid(row=3,column=3,pady=1)
buttons[15].grid(row=4,column=3,pady=1)
buttons[16].grid(row=5,column=3,pady=1)
buttons[17].grid(row=5,column=2,pady=1)
buttons[18].grid(row=5,column=1,pady=1)
buttons[19].grid(row=5,column=0,pady=1)

# *****************************************************************************************************

# Additional buttons

label=Label(frame,text="Scientific Calculator",font="arial 20 bold")
label.grid(row=0,column=4,columnspan=4,pady=1)

buttons.append(Button(frame,height=2,width=6,text="π",font="arial 20 bold",bd=4,fg="blue2"))
buttons[20].grid(row=1,column=4,pady=1)

buttons.append(Button(frame,height=2,width=6,text="cos",font="arial 20 bold",bd=4,fg="blue2"))
buttons[21].grid(row=1,column=5,pady=1)

buttons.append(Button(frame,height=2,width=6,text="tan",font="arial 20 bold",bd=4,fg="blue2"))
buttons[22].grid(row=1,column=6,pady=1)

buttons.append(Button(frame,height=2,width=6,text="sin",font="arial 20 bold",bd=4,fg="blue2"))
buttons[23].grid(row=1,column=7,pady=1)

buttons.append(Button(frame,height=2,width=6,text="e",font="arial 20 bold",bd=4,fg="blue2"))
buttons[24].grid(row=2,column=4,pady=1)

buttons.append(Button(frame,height=2,width=6,text="cosh",font="arial 20 bold",bd=4,fg="blue2"))
buttons[25].grid(row=3,column=4,pady=1)

buttons.append(Button(frame,height=2,width=6,text="sinh",font="arial 20 bold",bd=4,fg="blue2"))
buttons[26].grid(row=3,column=5,pady=1)

buttons.append(Button(frame,height=2,width=6,text="tanh",font="arial 20 bold",bd=4,fg="blue2"))
buttons[27].grid(row=3,column=6,pady=1)

buttons.append(Button(frame,height=2,width=6,text="√",font="arial 20 bold",bd=4,fg="blue2"))
buttons[28].grid(row=2,column=5,pady=1)

buttons.append(Button(frame,height=2,width=6,text="Deg",font="arial 20 bold",bd=4,fg="blue2"))
buttons[29].grid(row=3,column=7,pady=1)

buttons.append(Button(frame,height=2,width=6,text="!",font="arial 20 bold",bd=4,fg="blue2"))
buttons[30].grid(row=2,column=6,pady=1)

buttons.append(Button(frame,height=2,width=6,text="x^y",font="arial 20 bold",bd=4,fg="blue2"))
buttons[31].grid(row=2,column=7,pady=1)

buttons.append(Button(frame,height=2,width=6,text="sin-1",font="arial 20 bold",bd=4,fg="blue2"))
buttons[32].grid(row=4,column=4,pady=1)

buttons.append(Button(frame,height=2,width=6,text="cos-1",font="arial 20 bold",bd=4,fg="blue2"))
buttons[33].grid(row=4,column=5,pady=1)

buttons.append(Button(frame,height=2,width=6,text="tan-1",font="arial 20 bold",bd=4,fg="blue2"))
buttons[34].grid(row=4,column=6,pady=1)

buttons.append(Button(frame,height=2,width=6,text="ln",font="arial 20 bold",bd=4,fg="blue2"))
buttons[35].grid(row=5,column=6,pady=1)

buttons.append(Button(frame,height=2,width=6,text="(",font="arial 20 bold",bd=4,fg="blue2"))
buttons[36].grid(row=5,column=4,pady=1)

buttons.append(Button(frame,height=2,width=6,text=")",font="arial 20 bold",bd=4,fg="blue2"))
buttons[37].grid(row=5,column=5,pady=1)

buttons.append(Button(frame,height=2,width=6,text="lg",font="arial 20 bold",bd=4,fg="blue2"))
buttons[38].grid(row=5,column=7,pady=1)

buttons.append(Button(frame,height=2,width=6,text="1/x",font="arial 20 bold",bd=4,fg="blue2"))
buttons[39].grid(row=4,column=7,pady=1)

calc.bind("<Key>",click)

for i in range(40):
    if i==19:
        continue
    buttons[i].bind("<Button-1>",click)
    buttons[i].bind("<Key>",click)

calc.mainloop()