#author: Gregory Guditus
import csv
from tkinter import*
from tkinter import ttk
from scipy.stats.distributions import binom

#code to store z-scores in a dictionary filled with lists (similar to a 2D array) from a .csv file
zScore={}
i=-34
with open('zScore.csv') as f:
    reader=csv.reader(f, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        zScore[i/10]=row
        i+=1

#CODE FOR GUI
#code for home page
root = Tk()
root.title("Probability Calculator")
root.geometry('600x450')

tab_control=ttk.Notebook(root)
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)

tab_control.add(tab1, text='Home')
tab_control.add(tab2, text='Calculate')
tab_control.add(tab3, text='Quit')

lbl1=Label(tab1, text='Hello')
lbl1.grid(row=0, padx=210, pady=15)
lblA=Label(tab1, text='Welcome to the Probability Calculator!')
lblA.grid(row=1, padx=160, pady=15)
lblB=Label(tab1, text='Enjoy!')
lblB.grid(row=2, padx=160, pady=15)
lblC=Label(tab1, text='Created by Greg Guditus')
lblC.grid(row=3, padx=210, pady=15)

#code for calculate page
frm=Frame(tab2,bd=5, relief=GROOVE)
frm.grid()
lblG=Label(frm, text='Enter the relevant information to \nfind the probability', font=("Arial Bold", 10))
lblG.pack()

frm1=Frame(tab2,bd=5, relief=GROOVE)
frm1.grid(column=1, row=0)
lblH=Label(frm1, text='Normal Approximation', font=("Arial Bold", 10))
lblH.grid(column=0, row=0)
lblm=Label(frm1, text='Mean =')
lblm.grid(column=0, row=1)
boxm=Entry(frm1, width=3)
boxm.grid(column=1, row=1)
lblstdev=Label(frm1, text='St. Dev. =')
lblstdev.grid(column=0, row=2)
boxstdev=Entry(frm1, width=3)
boxstdev.grid(column=1, row=2)
lblxval=Label(frm1, text="X Value =")
lblxval.grid(column=0, row=3)
boxxval=Entry(frm1, width=3)
boxxval.grid(column=1, row=3)
lblresult=Label(frm1)

def clickedna():
    mean=int(boxm.get())
    stdev=int(boxstdev.get())
    xval=int(boxxval.get())
    z=(xval-mean)/stdev
    z1 = (z * 100) % 10
    z2 = ((z * 100) - z1) / 100
    if z<0:
        z1=9-z1
    lblresult.configure(text="Result: " + zScore[z2][int(z1)])

buttonna=Button(frm1, text="Calculate",command=clickedna,)
buttonna.grid(column=2, row=4)
lblresult.grid(column=0, row=4)

frm2=Frame(tab2,bd=5, relief=GROOVE)
frm2.grid(row=1)
lblI=Label(frm2, text='Statistical Information', font=("Arial Bold", 10))
lblI.grid(column=0, row=0)
lblp=Label(frm2, text='P: ')
lblp.grid(column=0, row=1)
boxp=Entry(frm2, width=3)
boxp.grid(column=1, row=1)
lblN=Label(frm2, text="N: ")
lblN.grid(column=0, row=2)
boxN=Entry(frm2, width=3)
boxN.grid(column=1, row=2)
lblX=Label(frm2, text="X: ")
lblX.grid(column=0, row=3)
boxX=Entry(frm2, width=3)
boxX.grid(column=1, row=3)
selected=IntVar()
lblress=Label(frm2)

def LEG():
    p=float(boxp.get())
    n=int(boxN.get())
    x=int(boxX.get())
    q=1-p
    varLEG=selected.get()
    if(varLEG<0):
        lblress.configure(text="Result: " + str(binom.cdf(x-1, n, p, loc=0)))
    elif(varLEG>0):
        lblress.configure(text="Result: " + str(binom.sf(x-1, n, p, loc=0)))
    else:
        lblress.configure(text="Result: " +str(binom.pmf(x, n, p, loc=0)))

radl=Radiobutton(frm2, text='Less Than', value=-1, variable=selected)
radl.grid(column=2, row=1)
rade=Radiobutton(frm2, text='Exactly', value=0, variable=selected)
rade.grid(column=2, row=2)
radg=Radiobutton(frm2, text='Greater Than', value=1, variable=selected)
radg.grid(column=2, row=3)
butns=Button(frm2, text="Calculate", command=LEG)
butns.grid(column=2, row=4)
lblress.grid(column=0, row=4)

frm3=Frame(tab2,bd=5, relief=GROOVE)
frm3.grid(column=1, row=1)
lblJ=Label(frm3, text='Z-Score Probability', font=("Arial Bold", 10))
lblJ.grid(column=0, row=0)
lblz=Label(frm3, text="Enter Z-Score to\n2 decimal places")
lblz.grid(column=0, row=1)
boxz=Entry(frm3, width=5)
boxz.grid(column=1, row=1)
lblresz=Label(frm3)

def clickedz():
    z=float(boxz.get())
    z1=(z*100)%10
    z2=((z*100)-z1)/100
    lblresz.configure(text="Result: "+ zScore[z2][int(z1)])
    
butnz=Button(frm3, text="Calculate", command=clickedz)
butnz.grid(column=2, row=1)
lblresz.grid(column=0, row=2)

frm4=Frame(tab2,bd=5, relief=GROOVE)
frm4.grid(row=2)
lblK=Label(frm4, text='Flip a Coin', font=("Arial Bold", 10))
lblK.grid(column=0, row=0)
lblfc=Label(frm4, text='How many flips? ')
lblfc.grid(column=0, row=1)
boxfc=Entry(frm4, width=3)
boxfc.grid(column=1, row=1)
lblresfc=Label(frm4)

def clickedfc():
    x=int(boxfc.get())
    lblresfc.configure(text="Heads: "+str(int((x+1)/2))+"\nTails: "+str(int((x)/2)))
    
butnfc=Button(frm4, text="Calculate", command=clickedfc)
butnfc.grid(column=2, row=1)
lblresfc.grid(column=0, row=2)

frm5=Frame(tab2,bd=5, relief=GROOVE)
frm5.grid(column=1, row=2)
lblL=Label(frm5, text='Roll a Die', font=("Arial Bold", 10))
lblL.grid(column=0, row=0)
lblrd=Label(frm5, text='Number of sides')
lblrd.grid(column=0, row=1)
lblrd2=Label(frm5, text='How many values are\nyou looking for?')
lblrd2.grid(column=0,row=2)
boxrd=Entry(frm5, width=3)
boxrd.grid(column=1, row=1)
boxrd2=Entry(frm5, width=3)
boxrd2.grid(column=1, row=2)
lblresultd=Label(frm5)

def clickedrd():
    lblresultd.configure(text="Result: "+str((float(boxrd2.get())/float(boxrd.get())))+" chance")
    
buttonrd=Button(frm5, text="Calculate",command=clickedrd)
buttonrd.grid(column=2, row=4)
lblresultd.grid(column=0, row=4)

# code for quit page
lbl2=Label(tab3, text='Thank you for using this GUI!')
lbl2.grid(row=0, padx=175, pady=25)
lbl3=Label(tab3, text='Have a great day!')
lbl3.grid(row=1, padx=175, pady=25)

def clicked1():
    exit()
    
button1=Button(tab3, text="Quit",command=clicked1)
button1.grid(row=2, padx=275, pady=30)

tab_control.pack(expand=1, fill='both')

root.mainloop()
