#Copyright Brian S. Haney 2020

mydict = {'good':0.75, 'acceptable':0.5, 'outstanding': 1, 'unacceptable': 0, 'marginal': .25}

# Widgets:
from tkinter import *
from tkinter.messagebox import *

master = Tk()
label1 = Label(master, text = 'Proposal', relief = 'groove', width = 19)
label2 = Label(master, text = 'Price', relief = 'groove', width = 19)
label3 = Label(master, text = 'Past Performance', relief = 'groove', width = 19)
label4 = Label(master, text = 'Technical Quality', relief = 'groove', width = 19)
label5 = Label(master, text = 'Management', relief = 'groove', width = 19)
label6 = Label(master, text = 'Compliance', relief = 'groove', width = 19)
label7 = Label(master, text = 'Innovation', relief = 'groove', width = 19)
label8 = Label(master, text = 'A' , relief = 'groove', width = 12)
label9 = Label(master, text = 'B', relief = 'groove', width = 12)
label10 = Label(master, text = 'C' , relief = 'groove', width = 12)
label11 = Label(master, text = 'Proposal Score', relief = 'groove', width = 19)
entry1 = Entry(master, relief = 'groove', width = 12)
entry2 = Entry(master, relief = 'groove', width = 12)
entry3 = Entry(master, relief = 'groove', width = 12)
entry4 = Entry(master, relief = 'groove', width = 12)
entry5 = Entry(master, relief = 'groove', width = 12)
entry6 = Entry(master, relief = 'groove', width = 12)
entry7 = Entry(master, relief = 'groove', width = 12)
entry8 = Entry(master, relief = 'groove', width = 12)
entry9 = Entry(master, relief = 'groove', width = 12)
entry10 = Entry(master, relief = 'groove', width = 12)
entry11 = Entry(master, relief = 'groove', width = 12)
entry12 = Entry(master, relief = 'groove', width = 12)
entry13 = Entry(master, relief = 'groove', width = 12)
entry14 = Entry(master, relief = 'groove', width = 12)
entry15 = Entry(master, relief = 'groove', width = 12)
entry16 = Entry(master, relief = 'groove', width = 12)
entry17 = Entry(master, relief = 'groove', width = 12)
entry18 = Entry(master, relief = 'groove', width = 12)
blank1 = Entry(master, relief = 'groove', width = 12)
blank2 = Entry(master, relief = 'groove', width = 12)
blank3 = Entry(master, relief = 'groove', width = 12)


def show_answer():
    b = 1/9
    Ans1 = float(1) * float(1) * float( mydict[entry2.get()]) *float( mydict[entry3.get()]) * float( mydict[entry4.get()]) *float( mydict[entry5.get()]) *float( mydict[entry5.get()]) *float( mydict[entry6.get()])
    Ans11 = Ans1**b
    blank1.insert(0, Ans11)
    Ans2 = float(.91) * float(.91) * float( mydict[entry8.get()]) *float( mydict[entry9.get()]) * float( mydict[entry10.get()]) *float( mydict[entry11.get()]) *float( mydict[entry11.get()]) *float( mydict[entry12.get()])
    Ans22 = Ans2**b
    blank2.insert(0, Ans22)
    Ans3 = float(.95) * float(.95) * float( mydict[entry14.get()]) *float( mydict[entry15.get()]) * float( mydict[entry16.get()]) *float( mydict[entry17.get()]) *float( mydict[entry17.get()]) *float( mydict[entry18.get()])
    Ans33 = Ans3**b
    blank3.insert(0, Ans33)
 
button1 = Button(master, text = 'Calculate Bid Scores', relief = 'groove', width = 20, command =show_answer)


#Geometry
label1.grid( row = 1, column = 1, padx = 10 )
label2.grid( row = 1, column = 2, padx = 10 )
label3.grid( row = 1, column = 3, padx = 10 )
label4.grid( row = 1, column = 4, padx = 10 )
label5.grid( row = 1, column = 5, padx = 10 )
label6.grid( row = 1, column = 6, padx = 10 )
label7.grid( row = 1, column = 7, padx = 10 )
label8.grid( row = 2, column = 1, padx = 10 )
label9.grid( row = 3, column = 1, padx = 10 )
label10.grid( row = 4, column = 1, padx = 10 )
label11.grid( row = 1, column = 8, padx = 10 )
entry1.grid( row = 2, column = 2, padx = 10 )
entry2.grid( row = 2, column = 3, padx = 10 )
entry3.grid( row = 2, column = 4, padx = 10 )
entry4.grid( row = 2, column = 5, padx = 10 )
entry5.grid( row = 2, column = 6, padx = 10 )
entry6.grid( row = 2, column = 7, padx = 10 )
entry7.grid( row = 3, column = 2, padx = 10 )
entry8.grid( row = 3, column = 3, padx = 10 )
entry9.grid( row = 3, column = 4, padx = 10 )
entry10.grid( row = 3, column = 5, padx = 10 )
entry11.grid( row = 3, column = 6, padx = 10 )
entry12.grid( row = 3, column = 7, padx = 10 )
entry13.grid( row = 4, column = 2, padx = 10 )
entry14.grid( row = 4, column = 3, padx = 10 )
entry15.grid( row = 4, column = 4, padx = 10 )
entry16.grid( row = 4, column = 5, padx = 10 )
entry17.grid( row = 4, column = 6, padx = 10 )
entry18.grid( row = 4, column = 7, padx = 10 )
blank1.grid( row = 2, column = 8, padx = 10 )
blank2.grid( row = 3, column = 8, padx = 10 )
blank3.grid( row = 4, column = 8, padx = 10 )
button1.grid( row = 6, column = 4, columnspan = 2)

#Static Properties
master.title('Bid Score Calculator')
