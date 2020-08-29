from tkinter import *
import time
import datetime
import random
from tkinter import messagebox
import tkinter.messagebox
#import py_mysql_connector
import pymysql
import mysql.connector
root =Tk()
root.geometry("1330x650+0+0")
root.title("WE DELIVER")
root.configure(background='white')

Tops = Frame(root,bg='white',bd=2,pady=5,relief=RIDGE)
Tops.pack(side=TOP)
second_page = Frame(root)


lblTitle=Label(Tops,font=('arial',60,'bold'),text='WE DELIVER',bd=0,bg='white',
               fg='black',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='white',bd=1,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='white',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='white',bd=1,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='white',bd=1,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='white',bd=1,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='white',bd=1)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='white',bd=1)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='white',bd=1,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='white',bd=1,relief=RIDGE)
Food_F.pack(side=RIGHT)
###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Milk = StringVar()
E_Tea = StringVar()
E_Toor = StringVar()
E_Urad = StringVar()
E_Wheat = StringVar()
E_Sevai = StringVar()
E_Turmeric= StringVar()
E_Sabudana = StringVar()

E_Maida = StringVar()
E_Salt = StringVar()
E_Peanut = StringVar()
E_Poha = StringVar()
E_Rava = StringVar()
E_Rice = StringVar()
E_Sugar = StringVar()
E_oil = StringVar()

E_Milk.set("0")
E_Tea.set("0")
E_Toor.set("0")
E_Urad.set("0")
E_Wheat.set("0")
E_Sevai.set("0")
E_Turmeric.set("0")
E_Sabudana.set("0")

E_Maida.set("0")
E_Salt.set("0")
E_Peanut.set("0")
E_Poha.set("0")
E_Rava.set("0")
E_Rice.set("0")
E_Sugar.set("0")
E_oil.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit  System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Milk.set("0")
    E_Tea.set("0")
    E_Toor.set("0")
    E_Urad.set("0")
    E_Wheat.set("0")
    E_Sevai.set("0")
    E_Turmeric.set("0")
    E_Sabudana.set("0")

    E_Maida.set("0")
    E_Salt.set("0")
    E_Peanut.set("0")
    E_Poha.set("0")
    E_Rava.set("0")
    E_Rice.set("0")
    E_Sugar.set("0")
    E_oil.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtMilk.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtToor.configure(state=DISABLED)
    txtUrad.configure(state=DISABLED)
    txtWheat.configure(state=DISABLED)
    txtSevai.configure(state=DISABLED)
    txtTurmeric.configure(state=DISABLED)
    txtSabudana.configure(state=DISABLED)
    txtMaida.configure(state=DISABLED)
    txtSalt.configure(state=DISABLED)
    txtPeanut.configure(state=DISABLED)
    txtPoha.configure(state=DISABLED)
    txtRava.configure(state=DISABLED)
    txtRice.configure(state=DISABLED)
    txtSugar.configure(state=DISABLED)
    txtoil.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Milk.get())
    Item2=float(E_Tea.get())
    Item3=float(E_Toor.get())
    Item4=float(E_Urad.get())
    Item5=float(E_Wheat.get())
    Item6=float(E_Sevai.get())
    Item7=float(E_Turmeric.get())
    Item8=float(E_Sabudana.get())

    Item9=float(E_Maida.get())
    Item10=float(E_Salt.get())
    Item11=float(E_Peanut.get())
    Item12=float(E_Poha.get())
    Item13=float(E_Rava.get())
    Item14=float(E_Rice.get())
    Item15=float(E_Sugar.get())
    Item16=float(E_oil.get())

    PriceofDrinks =(Item1 * 26) + (Item2 * 235) + (Item3 * 95) + (Item4 * 135) + (Item5 * 35) + (Item6 * 33) + (Item7 * 34) + (Item8 * 78)

    PriceofFood =(Item9 * 29) + (Item10 * 9.6) + (Item11 * 99) + (Item12 * 38) + (Item13 * 39) + (Item14 * 39) + (Item15 * 37) + (Item16 * 104)



    DrinksPrice = "Rs",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "Rs",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rs",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs",str('%.2f'%((PriceofDrinks + PriceofFood + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 1.59) * 0.15)
    TC="Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59 + TT))
    TotalCost.set(TC)


def chkMilk():
    if(var1.get() == 1):
        txtMilk.configure(state = NORMAL)
        txtMilk.focus()
        txtMilk.delete('0',END)
        E_Milk.set("")
    elif(var1.get() == 0):
        txtMilk.configure(state = DISABLED)
        E_Milk.set("0")

def chkTea():
    if(var2.get() == 1):
        txtTea.configure(state = NORMAL)
        txtTea.focus()
        txtTea.delete('0',END)
        E_Tea.set("")
    elif(var2.get() == 0):
        txtTea.configure(state = DISABLED)
        E_Tea.set("0")

def chk_Toor():
    if(var3.get() == 1):
        txtToor.configure(state = NORMAL)
        txtToor.delete('0',END)
        txtToor.focus()
    elif(var3.get() == 0):
        txtToor.configure(state = DISABLED)
        E_Toor.set("0")

def chk_Urad():
    if(var4.get() == 1):
        txtUrad.configure(state = NORMAL)
        txtUrad.delete('0',END)
        txtUrad.focus()
    elif(var4.get() == 0):
        txtUrad.configure(state = DISABLED)
        E_Urad.set("0")

def chk_Wheat():
    if(var5.get() == 1):
        txtWheat.configure(state = NORMAL)
        txtWheat.delete('0',END)
        txtWheat.focus()
    elif(var5.get() == 0):
        txtWheat.configure(state = DISABLED)
        E_Wheat.set("0")

def chk_Sevai():
    if(var6.get() == 1):
        txtSevai.configure(state = NORMAL)
        txtSevai.delete('0',END)
        txtSevai.focus()
    elif(var6.get() == 0):
        txtSevai.configure(state = DISABLED)
        E_Sevai.set("0")

def chk_Turmeric():
    if(var7.get() == 1):
        txtTurmeric.configure(state = NORMAL)
        txtTurmeric.delete('0',END)
        txtTurmeric.focus()
    elif(var7.get() == 0):
        txtTurmeric.configure(state = DISABLED)
        E_Turmeric.set("0")

def chk_Sabudana():
    if(var8.get() == 1):
        txtSabudana.configure(state = NORMAL)
        txtSabudana.delete('0',END)
        txtSabudana.focus()
    elif(var8.get() == 0):
        txtSabudana.configure(state = DISABLED)
        E_Sabudana.set("0")

def chk_Maida():
    if(var9.get() == 1):
        txtMaida.configure(state = NORMAL)
        txtMaida.delete('0',END)
        txtMaida.focus()
    elif(var9.get() == 0):
        txtMaida.configure(state = DISABLED)
        E_Maida.set("0")

def chk_Salt():
    if(var10.get() == 1):
        txtSalt.configure(state = NORMAL)
        txtSalt.delete('0',END)
        txtSalt.focus()
    elif(var10.get() == 0):
        txtSalt.configure(state = DISABLED)
        E_Salt.set("0")

def chk_Peanut():
    if(var11.get() == 1):
        txtPeanut.configure(state = NORMAL)
        txtPeanut.delete('0',END)
        txtPeanut.focus()
    elif(var11.get() == 0):
        txtPeanut.configure(state = DISABLED)
        E_Peanut.set("0")

def chk_Poha():
    if(var12.get() == 1):
        txtPoha.configure(state = NORMAL)
        txtPoha.delete('0',END)
        txtPoha.focus()
    elif(var12.get() == 0):
        txtPoha.configure(state = DISABLED)
        E_Poha.set("0")

def chk_Rava():
    if(var13.get() == 1):
        txtRava.configure(state = NORMAL)
        txtRava.delete('0',END)
        txtRava.focus()
    elif(var13.get() == 0):
        txtRava.configure(state = DISABLED)
        E_Rava.set("0")

def chk_Rice():
    if(var14.get() == 1):
        txtRice.configure(state = NORMAL)
        txtRice.delete('0',END)
        txtRice.focus()
    elif(var14.get() == 0):
        txtRice.configure(state = DISABLED)
        E_Rice.set("0")

def chk_Sugar():
    if(var15.get() == 1):
        txtSugar.configure(state = NORMAL)
        txtSugar.delete('0',END)
        txtSugar.focus()
    elif(var15.get() == 0):
        txtSugar.configure(state = DISABLED)
        E_Sugar.set("0")

def chk_oil():
    if(var16.get() == 1):
        txtoil.configure(state = NORMAL)
        txtoil.delete('0',END)
        txtoil.focus()
    elif(var16.get() == 0):
        txtoil.configure(state = DISABLED)
        E_oil.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)




    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Milk-500ml:\t\t\t\t' + E_Milk.get() +'\n')
    txtReceipt.insert(END,'Tea-powder-1kg:\t\t\t\t\t'+ E_Tea.get()+'\n')
    txtReceipt.insert(END,'Toordal-1kg:\t\t\t\t\t'+ E_Toor.get()+'\n')
    txtReceipt.insert(END,'Uraddal-1kg:\t\t\t\t\t'+ E_Urad.get()+'\n')
    txtReceipt.insert(END,'Wheatflour-1kg:\t\t\t\t\t'+ E_Wheat.get()+'\n')
    txtReceipt.insert(END,'Sevai-500gms:\t\t\t\t\t'+ E_Sevai.get()+'\n')
    txtReceipt.insert(END,'Turmeric-250gms:\t\t\t\t\t'+ E_Turmeric.get()+'\n')
    txtReceipt.insert(END,'Sabudana-1kg:\t\t\t\t\t'+ E_Sabudana.get()+'\n')
    txtReceipt.insert(END,'Maida-1Kg:\t\t\t\t\t'+ E_Maida.get()+'\n')
    txtReceipt.insert(END,'Salt-1kg:\t\t\t\t\t'+ E_Salt.get()+'\n')
    txtReceipt.insert(END,'Peanut-1kg:\t\t\t\t\t'+ E_Peanut.get()+'\n')
    txtReceipt.insert(END,'Poha-1kg:\t\t\t\t\t'+ E_Poha.get()+'\n')
    txtReceipt.insert(END,'Rava(s)-1kg:\t\t\t\t\t'+ E_Rava.get()+'\n')
    txtReceipt.insert(END,'Rice-1kg:\t\t\t\t\t'+ E_Rice.get()+'\n')
    txtReceipt.insert(END,'Sugar-1kg:\t\t\t\t\t'+ E_Sugar.get()+'\n')
    txtReceipt.insert(END,'Sunflowe oil-1l:\t\t\t\t\t'+ E_oil.get()+'\n')
    txtReceipt.insert(END,'Cost of Items:\t\t\t\t\t'+ CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")
    
Milk=Checkbutton(Drinks_F,text='Milk',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chkMilk).grid(row=0,sticky=W)
Tea=Checkbutton(Drinks_F,text='Tea-powder-1kg',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chkTea).grid(row=1,sticky=W)
Toor=Checkbutton(Drinks_F,text='Toordal-1kg',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Toor).grid(row=2,sticky=W)
Urad=Checkbutton(Drinks_F,text='Uraddal-1kg ',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Urad).grid(row=3,sticky=W)
Wheat=Checkbutton(Drinks_F,text='Wheatflour-1kg',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Wheat).grid(row=4,sticky=W)
Sevai=Checkbutton(Drinks_F,text='Sevai-500gms',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Sevai).grid(row=5,sticky=W)
Turmeric=Checkbutton(Drinks_F,text='Turmeric-250gms',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Turmeric).grid(row=6,sticky=W)
Sabudana=Checkbutton(Drinks_F,text='Sabudana',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Sabudana).grid(row=7,sticky=W)



#########################################Drinks####################################################################
Milk=Checkbutton(Drinks_F,text='Milk',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chkMilk).grid(row=0,sticky=W)
Tea=Checkbutton(Drinks_F,text='Tea-powder-1kg',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chkTea).grid(row=1,sticky=W)
Toor=Checkbutton(Drinks_F,text='Toordal-1kg',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Toor).grid(row=2,sticky=W)
Urad=Checkbutton(Drinks_F,text='Uraddal-1kg ',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Urad).grid(row=3,sticky=W)
Wheat=Checkbutton(Drinks_F,text='Wheatflour-1kg',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Wheat).grid(row=4,sticky=W)
Sevai=Checkbutton(Drinks_F,text='Sevai-500gms',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Sevai).grid(row=5,sticky=W)
Turmeric=Checkbutton(Drinks_F,text='Turmeric-250gms',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Turmeric).grid(row=6,sticky=W)
Sabudana=Checkbutton(Drinks_F,text='Sabudana',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='white',command=chk_Sabudana).grid(row=7,sticky=W)
##############################################Drink Entry###############################################################

txtMilk = Entry(Drinks_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Milk)
txtMilk.grid(row=0,column=1)

txtTea = Entry(Drinks_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Tea)
txtTea.grid(row=1,column=1)

txtToor = Entry(Drinks_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Toor)
txtToor.grid(row=2,column=1)

txtUrad= Entry(Drinks_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Urad)
txtUrad.grid(row=3,column=1)

txtWheat = Entry(Drinks_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Wheat)
txtWheat.grid(row=4,column=1)

txtSevai = Entry(Drinks_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Sevai)
txtSevai.grid(row=5,column=1)

txtTurmeric = Entry(Drinks_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Turmeric)
txtTurmeric.grid(row=6,column=1)

txtSabudana = Entry(Drinks_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Sabudana)
txtSabudana.grid(row=7,column=1)
#############################################Foods######################################################################

Maida = Checkbutton(Food_F,text="Maida-1Kg ",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='white',command=chk_Maida).grid(row=0,sticky=W)
Salt = Checkbutton(Food_F,text="Salt",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='white',command=chk_Salt).grid(row=1,sticky=W)
Peanut = Checkbutton(Food_F,text="Peanut-1kg ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='white',command=chk_Peanut).grid(row=2,sticky=W)
Poha = Checkbutton(Food_F,text="Poha-1kg ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='white',command=chk_Poha).grid(row=3,sticky=W)
Rava= Checkbutton(Food_F,text="Rava(s) ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='white',command=chk_Rava).grid(row=4,sticky=W)
Fires = Checkbutton(Food_F,text="Rice-1kg ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='white',command=chk_Rice).grid(row=5,sticky=W)
Sugar = Checkbutton(Food_F,text="Sugar-1kg ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='white',command=chk_Sugar).grid(row=6,sticky=W)
oil = Checkbutton(Food_F,text="Sunflower oil-1l ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='white',command=chk_oil).grid(row=7,sticky=W)
################################################Entry Box For Cake##########################################################
txtMaida=Entry(Food_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Maida)
txtMaida.grid(row=0,column=1)

txtSalt=Entry(Food_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Salt)
txtSalt.grid(row=1,column=1)

txtPeanut=Entry(Food_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Peanut)
txtPeanut.grid(row=2,column=1)

txtPoha=Entry(Food_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Poha)
txtPoha.grid(row=3,column=1)

txtRava=Entry(Food_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Rava)
txtRava.grid(row=4,column=1)

txtRice=Entry(Food_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Rice)
txtRice.grid(row=5,column=1)

txtSugar=Entry(Food_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Sugar)
txtSugar.grid(row=6,column=1)

txtoil=Entry(Food_F,font=('arial',16,'bold'),bd=1,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_oil)
txtoil.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='white',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods  ',bg='white',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='white',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=1,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='white',bd=1,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=1,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='white',bd=1,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=1,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='white',bd=1,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=1,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=1,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)



###########################################BUTTONS################################################################################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=1,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='orange',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=1,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='orange',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=1,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='orange',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=1,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='orange',command=iExit).grid(row=0,column=3)


###################################Calculator Display################################################################################




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




#############################################Calculator###############################################################################
txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='orange',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='orange',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='orange',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='orange',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='orange',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='orange',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='orange',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='orange',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='orange',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='orange',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='orange',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='orange',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='orange',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='orange',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='orange',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='orange',command=lambda:btnClick('/')).grid(row=5,column=3)




def items_list():
    #forget all frames
    Tops.pack_forget()
    ReceiptCal_F .pack_forget()
    Cal_F.pack_forget()
    Buttons_F.pack_forget()
    MenuFrame.pack_forget()
    Cost_F.pack_forget()
    #Food_F.pack_forget()
    #Drinks_F.pack_forget()
    #connect to database
    


    second_page.config(background="lavender")
    second_page.pack()

button_2 = Button(Buttons_F, text="Items", width=30, height=2, command=items_list, font=('times new roman', 10)).grid(row=0,column=4)
    

root.mainloop()
