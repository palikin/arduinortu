# -*- coding: cp1251 -*-
from Tkinter import *


################################ open discret window ###################################################################################

def openDiscret(root,diPath):
     def getLine(e):

         x=listbox.curselection()

         pointName.delete(0,END)
         pointName.insert(0,arrayPointName[int(x[0])+1])

         fig.delete(0,END)
         fig.insert(0,arrayFigName[int(x[0]) + 1])

         pointAddress.delete(0,END)
         pointAddress.insert(0,arrayPointAddress[int(x[0]) + 1])
         startX.delete(0,END)
         startX.insert(0,arrayStartX[int(x[0]) + 1])
         startY.delete(0,END)
         startY.insert(0,arrayStartY[int(x[0]) + 1])
         endX.delete(0,END)
         endX.insert(0,arrayEndX[int(x[0]) + 1])
         endY.delete(0,END)
         endY.insert(0,arrayEndY[int(x[0]) + 1])
         colorOn.delete(0,END)
         colorOn.insert(0,arrayColorOn[int(x[0]) + 1])
         colorOff.delete(0,END)
         colorOff.insert(0,arrayColorOff[int(x[0]) + 1])
         messageOn.delete(0,END)
         messageOn.insert(0,arrayMessageOn[int(x[0]) + 1])
         messageOff.delete(0,END)
         messageOff.insert(0,arrayMessageOff[int(x[0]) + 1])

     def saveArray():
         try:
             if(len(pointAddress.get()) > 0):
                 c=int(pointAddress.get())
                 arrayFigName[c]=fig.get()
                 arrayStartX[c]=startX.get()
                 arrayStartY[c]=startY.get()
                 arrayEndX[c]=endX.get()
                 arrayEndY[c]=endY.get()
                 arrayColorOn[c]=colorOn.get()
                 arrayColorOff[c]=colorOff.get()
                 arrayMessageOn[c]=messageOn.get()
                 arrayMessageOff[c]=messageOff.get()
                 arrayPointAddress[c]=pointAddress.get()
                 arrayPointName[c]=pointName.get()




             else:
                 print "No set adress DI"

         except Exception, e:
             print "Button save di",e

     def addNewPoint():
         try:
             listbox.insert(END,'New Item'+'\n')
         except Exception, e:
             print "Button save di",e




     def saveToFile(diPath):
         saveArray()
         try:
             f = open(diPath,'w')
             for c in range(1,listbox.size()+1):
                 l='di;'+str(arrayFigName[c])+';'+str(arrayPointAddress[c])+';'+str(arrayStartX[c])+';'+ str(arrayStartY[c])+';'+ str(arrayEndX[c])+';'+ str(arrayEndY[c])+';'+str(arrayColorOn[c])+';'+str(arrayColorOff[c])+';'+str(arrayMessageOn[c])+';'+str(arrayMessageOff[c])+';'+str(arrayPointName[c])+';'
                # print l
                 f.write(l+'\n')
             f.close()
             listbox.delete(0, END)
             c=1
             with open(diPath) as f:
                 for line in f:
                     param=line.split(';')
                     if(param[0] == 'di'):
                         listbox.insert(END,param[11]+'\n')

                         arrayFigName[c]=param[1]
                         arrayPointAddress[c]=param[2]
                         arrayStartX[c]=param[3]
                         arrayStartY[c]=param[4]
                         arrayEndX[c]=param[5]
                         arrayEndY[c]=param[6]
                         arrayColorOn[c]=param[7]
                         arrayColorOff[c]=param[8]
                         arrayMessageOn[c]=param[9]
                         arrayMessageOff[c]=param[10]
                         arrayPointName[c]=param[11]

                         c+=1
                         countLines=c
             f.close()







         except Exception, e:
             print "Button save to file di.cfg",e


 #############################################################################

     try:
         win = Toplevel(root)

         win.geometry('600x500+300+200')
         win.title("Discret signals READ_DISCRETE_INPUTS" )
         win["bg"] = "lightgray"
         win.transient(root)
         #win.state('normal')
         win.resizable('n', 'n')

         listbox = Listbox(win,width=40,bg='lightgray')

         listbox.pack(side=LEFT,fill='y')

         listbox.bind('<<ListboxSelect>>', getLine)
         listbox.yview()



         buttonSaveToFile=Button(win,text="Save")
         buttonSaveToFile.bind('<Button-1>', lambda e: saveToFile(diPath))
         buttonSaveToFile.place(x=450,y=350)

         buttonNew=Button(win,text="New",command=addNewPoint)
         buttonNew.place(x=380,y=350)


         X=0
         XX=0
         Y=90
         fig = Entry(win)
         fig.place(x=XX+320,y=Y+10)
         figLabel = Label(win,text='DI Figure',bg='lightgray').place(x=X+250,y=Y+10)

         startX = Entry(win)
         startX.place(x=XX+320,y=Y+30)
         startXLabel = Label(win,text='Start X',bg='lightgray').place(x=X+250,y=Y+30)
         startY = Entry(win)
         startY.place(x=XX+320,y=Y+50)
         startYLabel = Label(win,text='Start Y',bg='lightgray').place(x=X+250,y=Y+50)
         endX = Entry(win)
         endX.place(x=XX+320,y=Y+70)
         endXLabel = Label(win,text='End X',bg='lightgray').place(x=X+250,y=Y+70)

         endY = Entry(win)
         endY.place(x=XX+320,y=Y+90)
         endYLabel = Label(win,text='End Y',bg='lightgray').place(x=X+250,y=Y+90)

         colorOn = Entry(win)
         colorOn.place(x=XX+320,y=Y+130)
         colorOnLabel = Label(win,text='Color On',bg='lightgray').place(x=X+250,y=Y+130)

         colorOff = Entry(win)
         colorOff.place(x=XX+320,y=Y+150)
         colorOffLabel = Label(win,text='Color Off',bg='lightgray').place(x=X+250,y=Y+150)

         messageOn = Entry(win,width=35)
         messageOn.place(x=XX+320,y=Y+180)
         messageOnLabel = Label(win,text='Message On',bg='lightgray').place(x=X+250,y=Y+180)


         messageOff = Entry(win,width=35)
         messageOff.place(x=XX+320,y=Y+200)
         messageOffLabel = Label(win,text='Message Off',bg='lightgray').place(x=X+250,y=Y+200)




         pointName = Entry(win,width=40)
         pointName.place(x=320,y=10)
         pointNameLabel = Label(win,text='DI name',bg='lightgray').place(x=245,y=10)

         pointAddress = Entry(win)
         pointAddress.place(x=320,y=30)
         pointAddressLabel = Label(win,text='DI address',bg='lightgray').place(x=245,y=30)

         arrayFigName=[]
         arrayStartX=[]
         arrayStartY=[]
         arrayEndX=[]
         arrayEndY=[]
         arrayColorOn=[]
         arrayColorOff=[]
         arrayMessageOn=[]
         arrayMessageOff=[]
         arrayPointAddress=[]
         global arrayPointName
         arrayPointName=[]

         for c in range(0,1000):
             arrayFigName.append(c)
             arrayStartX.append(c)
             arrayStartY.append(c)
             arrayEndX.append(c)
             arrayEndY.append(c)
             arrayColorOn.append(c)
             arrayColorOff.append(c)
             arrayMessageOn.append(c)
             arrayMessageOff.append(c)
             arrayPointAddress.append(c)
             arrayPointName.append(c)
             c += 1

         c=1
         with open(diPath) as f:
             for line in f:
                 param=line.split(';')
                 if(param[0] == 'di'):
                     listbox.insert(END,param[11]+'\n')

                     arrayFigName[c]=param[1]
                     arrayPointAddress[c]=param[2]
                     arrayStartX[c]=param[3]
                     arrayStartY[c]=param[4]
                     arrayEndX[c]=param[5]
                     arrayEndY[c]=param[6]
                     arrayColorOn[c]=param[7]
                     arrayColorOff[c]=param[8]
                     arrayMessageOn[c]=param[9]
                     arrayMessageOff[c]=param[10]
                     arrayPointName[c]=param[11]

                     c+=1
                     countLines=c
         f.close()

     except Exception, e:
         print "Failed to edit di",e


def openAnalog(root,aiPath):
     def getLine(e):

         x=listbox.curselection()

         pointName.delete(0,END)
         pointName.insert(0,arrayPointName[int(x[0])+1])


         pointAddress.delete(0,END)
         pointAddress.insert(0,arrayPointAddress[int(x[0]) + 1])
         startX.delete(0,END)
         startX.insert(0,arrayStartX[int(x[0]) + 1])
         startY.delete(0,END)
         startY.insert(0,arrayStartY[int(x[0]) + 1])

         colorAI.delete(0,END)
         colorAI.insert(0,arrayColorAI[int(x[0]) + 1])
         koefAI.delete(0,END)
         koefAI.insert(0,arrayKoefAI[int(x[0]) + 1])
         valueAI.delete(0,END)
         valueAI.insert(0,arrayValueAI[int(x[0]) + 1])
         canvasWidg.delete(0,END)
         canvasWidg.insert(0,arrayCanvasWidg[int(x[0]) + 1])


     def saveArray():
         try:
             if(len(pointAddress.get()) > 0):
                 c=int(pointAddress.get())

                 arrayStartX[c]=startX.get()
                 arrayStartY[c]=startY.get()

                 arrayColorAI[c]=colorAI.get()
                 arrayValueAI[c]=valueAI.get()
                 arrayKoefAI[c]=koefAI.get()

                 arrayPointAddress[c]=pointAddress.get()
                 arrayPointName[c]=pointName.get()
                 arrayCanvasWidg[c]=canvasWidg.get()

             else:
                 print "No set adress AI"

         except Exception, e:
             print "Button save ai",e

     def addNewPoint():
         try:
             listbox.insert(END,'New Item'+'\n')
         except Exception, e:
             print "Button save ai",e


####################################################################

     def saveToFile(aiPath):
         saveArray()
         try:
             f = open(aiPath,'w')
             for c in range(1,listbox.size()+1):
                 l='ai;'+str(arrayPointAddress[c])+';'+str(arrayStartX[c])+';'+ str(arrayStartY[c])+';'+ str(arrayColorAI[c])+';'+ str(arrayKoefAI[c])+';'+str(arrayValueAI[c])+';'+str(arrayPointName[c])+';'+arrayCanvasWidg[c]+';'
                # print l
                 f.write(l+'\n')
             f.close()
             listbox.delete(0, END)
             c=1
             with open(aiPath) as f:
                 for line in f:
                     param=line.split(';')
                     if(param[0] == 'ai'):
                         listbox.insert(END,param[7]+'\n')

                         arrayPointAddress[c]=param[1]
                         arrayStartX[c]=param[2]
                         arrayStartY[c]=param[3]
                         arrayColorAI[c]=param[4]
                         arrayKoefAI[c]=param[5]
                         arrayValueAI[c]=param[6]

                         arrayPointName[c]=param[7]
                         arrayCanvasWidg[c]=param[8]

                         c+=1
                         countLines=c
             f.close()
         except Exception, e:
             print "Button save to file ai.cfg--->",e


 #############################################################################

     try:
         win = Toplevel(root)

         win.geometry('600x500+300+200')
         win.title("Analog signals READ_INPUT_REGISTER " )
         win["bg"] = "lightgray"
         win.transient(root)
         #win.state('normal')
         win.resizable('n', 'n')

         listbox = Listbox(win,width=40,bg='lightgray')

         listbox.pack(side=LEFT,fill='y')

         listbox.bind('<<ListboxSelect>>', getLine)
         listbox.yview()



         buttonSaveToFile=Button(win,text="Save")
         buttonSaveToFile.bind('<Button-1>', lambda e: saveToFile(aiPath))
         buttonSaveToFile.place(x=450,y=350)

         buttonNew=Button(win,text="New",command=addNewPoint)
         buttonNew.place(x=380,y=350)


         X=0
         XX=0
         Y=90


         startX = Entry(win)
         startX.place(x=XX+320,y=Y+30)
         startXLabel = Label(win,text='Place X',bg='lightgray').place(x=X+250,y=Y+30)
         startY = Entry(win)
         startY.place(x=XX+320,y=Y+50)
         startYLabel = Label(win,text='Place Y',bg='lightgray').place(x=X+250,y=Y+50)


         colorAI = Entry(win)
         colorAI.place(x=XX+320,y=Y+130)
         colorAILabel = Label(win,text='Color',bg='lightgray').place(x=X+250,y=Y+130)

         valueAI = Entry(win)
         valueAI.place(x=XX+320,y=Y+150)
         valueAILabel = Label(win,text='Max Value',bg='lightgray').place(x=X+250,y=Y+150)

         koefAI = Entry(win,width=35)
         koefAI.place(x=XX+320,y=Y+180)
         koefAILabel = Label(win,text='Koef',bg='lightgray').place(x=X+250,y=Y+180)

         canvasWidg = Entry(win,width=35)
         canvasWidg.place(x=XX+320,y=Y+210)
         canvasWidgLabel = Label(win,text='Widget',bg='lightgray').place(x=X+250,y=Y+210)




         pointName = Entry(win,width=40)
         pointName.place(x=320,y=10)
         pointNameLabel = Label(win,text='AI name',bg='lightgray').place(x=245,y=10)

         pointAddress = Entry(win)
         pointAddress.place(x=320,y=30)
         pointAddressLabel = Label(win,text='AI address',bg='lightgray').place(x=245,y=30)


         arrayStartX=[]
         arrayStartY=[]

         arrayColorAI=[]
         arrayKoefAI=[]
         arrayValueAI=[]

         arrayPointAddress=[]
         #arrayPointName
         arrayPointName=[]
         arrayCanvasWidg=[]

         for c in range(0,1000):

             arrayStartX.append(c)
             arrayStartY.append(c)

             arrayColorAI.append(c)
             arrayKoefAI.append(c)
             arrayValueAI.append(c)

             arrayPointAddress.append(c)
             arrayPointName.append(c)
             arrayCanvasWidg.append(c)
             c += 1

         c=1
         with open(aiPath) as f:
             for line in f:
                 param=line.split(';')
                 if(param[0] == 'ai'):
                     listbox.insert(END,param[7]+'\n')

                     arrayPointAddress[c]=param[1]
                     arrayStartX[c]=param[2]
                     arrayStartY[c]=param[3]
                     arrayColorAI[c]=param[4]
                     arrayKoefAI[c]=param[5]
                     arrayValueAI[c]=param[6]
                     arrayPointName[c]=param[7]
                     arrayCanvasWidg[c]=param[8]


                     c+=1
                     countLines=c
         f.close()

     except Exception, e:
         print "Failed to edit ai",e



################################ open Coil window ###################################################################################

def openCoil(root,ciPath):
     def getLine(e):

         x=listbox.curselection()

         pointName.delete(0,END)
         pointName.insert(0,arrayPointName[int(x[0])+1])

         fig.delete(0,END)
         fig.insert(0,arrayFigName[int(x[0]) + 1])

         pointAddress.delete(0,END)
         pointAddress.insert(0,arrayPointAddress[int(x[0]) + 1])
         startX.delete(0,END)
         startX.insert(0,arrayStartX[int(x[0]) + 1])
         startY.delete(0,END)
         startY.insert(0,arrayStartY[int(x[0]) + 1])
         endX.delete(0,END)
         endX.insert(0,arrayEndX[int(x[0]) + 1])
         endY.delete(0,END)
         endY.insert(0,arrayEndY[int(x[0]) + 1])
         colorOn.delete(0,END)
         colorOn.insert(0,arrayColorOn[int(x[0]) + 1])
         colorOff.delete(0,END)
         colorOff.insert(0,arrayColorOff[int(x[0]) + 1])
         messageOn.delete(0,END)
         messageOn.insert(0,arrayMessageOn[int(x[0]) + 1])
         messageOff.delete(0,END)
         messageOff.insert(0,arrayMessageOff[int(x[0]) + 1])

     def saveArray():
         try:
             if(len(pointAddress.get()) > 0):
                 c=int(pointAddress.get())
                 arrayFigName[c]=fig.get()
                 arrayStartX[c]=startX.get()
                 arrayStartY[c]=startY.get()
                 arrayEndX[c]=endX.get()
                 arrayEndY[c]=endY.get()
                 arrayColorOn[c]=colorOn.get()
                 arrayColorOff[c]=colorOff.get()
                 arrayMessageOn[c]=messageOn.get()
                 arrayMessageOff[c]=messageOff.get()
                 arrayPointAddress[c]=pointAddress.get()
                 arrayPointName[c]=pointName.get()




             else:
                 print "No set adress CI"

         except Exception, e:
             print "Button save di",e

     def addNewPoint():
         try:
             listbox.insert(END,'New Item'+'\n')
         except Exception, e:
             print "Button save di",e




     def saveToFile(ciPath):
         saveArray()
         try:
             f = open(ciPath,'w')
             for c in range(1,listbox.size()+1):
                 l='ci;'+str(arrayFigName[c])+';'+str(arrayPointAddress[c])+';'+str(arrayStartX[c])+';'+ str(arrayStartY[c])+';'+ str(arrayEndX[c])+';'+ str(arrayEndY[c])+';'+str(arrayColorOn[c])+';'+str(arrayColorOff[c])+';'+str(arrayMessageOn[c])+';'+str(arrayMessageOff[c])+';'+str(arrayPointName[c])+';'
                # print l
                 f.write(l+'\n')
             f.close()
             listbox.delete(0, END)
             c=1
             with open(ciPath) as f:
                 for line in f:
                     param=line.split(';')
                     if(param[0] == 'ci'):
                         listbox.insert(END,param[11]+'\n')

                         arrayFigName[c]=param[1]
                         arrayPointAddress[c]=param[2]
                         arrayStartX[c]=param[3]
                         arrayStartY[c]=param[4]
                         arrayEndX[c]=param[5]
                         arrayEndY[c]=param[6]
                         arrayColorOn[c]=param[7]
                         arrayColorOff[c]=param[8]
                         arrayMessageOn[c]=param[9]
                         arrayMessageOff[c]=param[10]
                         arrayPointName[c]=param[11]

                         c+=1
                         countLines=c
             f.close()







         except Exception, e:
             print "Button save to file di.cfg",e


 #############################################################################

     try:
         win = Toplevel(root)

         win.geometry('600x500+300+200')
         win.title("COILS signals READ_COILS" )
         win["bg"] = "lightgray"
         win.transient(root)
         #win.state('normal')
         win.resizable('n', 'n')

         listbox = Listbox(win,width=40,bg='lightgray')

         listbox.pack(side=LEFT,fill='y')

         listbox.bind('<<ListboxSelect>>', getLine)
         listbox.yview()



         buttonSaveToFile=Button(win,text="Save")
         buttonSaveToFile.bind('<Button-1>', lambda e: saveToFile(ciPath))
         buttonSaveToFile.place(x=450,y=350)

         buttonNew=Button(win,text="New",command=addNewPoint)
         buttonNew.place(x=380,y=350)


         X=0
         XX=0
         Y=90
         fig = Entry(win)
         fig.place(x=XX+320,y=Y+10)
         figLabel = Label(win,text='CI Figure',bg='lightgray').place(x=X+250,y=Y+10)

         startX = Entry(win)
         startX.place(x=XX+320,y=Y+30)
         startXLabel = Label(win,text='Start X',bg='lightgray').place(x=X+250,y=Y+30)
         startY = Entry(win)
         startY.place(x=XX+320,y=Y+50)
         startYLabel = Label(win,text='Start Y',bg='lightgray').place(x=X+250,y=Y+50)
         endX = Entry(win)
         endX.place(x=XX+320,y=Y+70)
         endXLabel = Label(win,text='End X',bg='lightgray').place(x=X+250,y=Y+70)

         endY = Entry(win)
         endY.place(x=XX+320,y=Y+90)
         endYLabel = Label(win,text='End Y',bg='lightgray').place(x=X+250,y=Y+90)

         colorOn = Entry(win)
         colorOn.place(x=XX+320,y=Y+130)
         colorOnLabel = Label(win,text='Color On',bg='lightgray').place(x=X+250,y=Y+130)

         colorOff = Entry(win)
         colorOff.place(x=XX+320,y=Y+150)
         colorOffLabel = Label(win,text='Color Off',bg='lightgray').place(x=X+250,y=Y+150)

         messageOn = Entry(win,width=35)
         messageOn.place(x=XX+320,y=Y+180)
         messageOnLabel = Label(win,text='Message On',bg='lightgray').place(x=X+250,y=Y+180)


         messageOff = Entry(win,width=35)
         messageOff.place(x=XX+320,y=Y+200)
         messageOffLabel = Label(win,text='Message Off',bg='lightgray').place(x=X+250,y=Y+200)




         pointName = Entry(win,width=40)
         pointName.place(x=320,y=10)
         pointNameLabel = Label(win,text='CI name',bg='lightgray').place(x=245,y=10)

         pointAddress = Entry(win)
         pointAddress.place(x=320,y=30)
         pointAddressLabel = Label(win,text='CI address',bg='lightgray').place(x=245,y=30)

         arrayFigName=[]
         arrayStartX=[]
         arrayStartY=[]
         arrayEndX=[]
         arrayEndY=[]
         arrayColorOn=[]
         arrayColorOff=[]
         arrayMessageOn=[]
         arrayMessageOff=[]
         arrayPointAddress=[]
         global arrayPointName
         arrayPointName=[]

         for c in range(0,1000):
             arrayFigName.append(c)
             arrayStartX.append(c)
             arrayStartY.append(c)
             arrayEndX.append(c)
             arrayEndY.append(c)
             arrayColorOn.append(c)
             arrayColorOff.append(c)
             arrayMessageOn.append(c)
             arrayMessageOff.append(c)
             arrayPointAddress.append(c)
             arrayPointName.append(c)
             c += 1

         c=1
         with open(ciPath) as f:
             for line in f:
                 param=line.split(';')
                 if(param[0] == 'ci'):
                     listbox.insert(END,param[11]+'\n')

                     arrayFigName[c]=param[1]
                     arrayPointAddress[c]=param[2]
                     arrayStartX[c]=param[3]
                     arrayStartY[c]=param[4]
                     arrayEndX[c]=param[5]
                     arrayEndY[c]=param[6]
                     arrayColorOn[c]=param[7]
                     arrayColorOff[c]=param[8]
                     arrayMessageOn[c]=param[9]
                     arrayMessageOff[c]=param[10]
                     arrayPointName[c]=param[11]

                     c+=1
                     countLines=c
         f.close()

     except Exception, e:
         print "Failed to edit ci",e


################################ open Button window ###################################################################################

def openButton(root,btPath):
     def getLine(e):

         x=listbox.curselection()

         pointName.delete(0,END)
         pointName.insert(0,arrayPointName[int(x[0])+1])

         regAdrInp.delete(0,END)
         regAdrInp.insert(0,regAdr[int(x[0]) + 1])

         pointAddress.delete(0,END)
         pointAddress.insert(0,arrayPointAddress[int(x[0]) + 1])

         startX.delete(0,END)
         startX.insert(0,arrayStartX[int(x[0]) + 1])

         startY.delete(0,END)
         startY.insert(0,arrayStartY[int(x[0]) + 1])

         pointControlValue.delete(0,END)
         pointControlValue.insert(0,arraySend[int(x[0]) + 1])


     def saveArray():
         try:
             if(len(pointAddress.get()) > 0):
                 c=int(pointAddress.get())
                 arrayStartX[c]=startX.get()
                 arrayStartY[c]=startY.get()
                 regAdr[c]=regAdrInp.get()
                 arrayPointAddress[c]=pointAddress.get()
                 arrayPointName[c]=pointName.get()
                 arraySend[c]=pointControlValue.get()

             else:
                 print "No set adress BT"

         except Exception, e:
             print "Button save bt",e

     def addNewPoint():
         try:
             listbox.insert(END,'New Item'+'\n')
         except Exception, e:
             print "Button save bt",e




     def saveToFile(btPath):
         saveArray()
         try:
             f = open(btPath,'w')
             for c in range(1,listbox.size()+1):
                 l='bt;'+str(arrayPointAddress[c])+';'+str(arrayStartX[c])+';'+ str(arrayStartY[c])+';'+ str(regAdr[c])+';'+ str(arrayPointName[c])+';'+ str(arraySend[c]) + ';'
                                 # print l
                 f.write(l+'\n')
             f.close()
             listbox.delete(0, END)
             c=1
             with open(btPath) as f:
                 for line in f:
                     param=line.split(';')
                     if(param[0] == 'bt'):
                         listbox.insert(END,param[5]+'\n')
                         arrayPointAddress[c]=param[1]
                         arrayStartX[c]=param[2]
                         arrayStartY[c]=param[3]
                         regAdr[c]=param[4]
                         arrayPointName[c]=param[5]
                         arraySend[c]=param[6]
                         c+=1
                         countLines=c
             f.close()

         except Exception, e:
             print "Button save to file bt.cfg -> ",e

     try:
         win = Toplevel(root)

         win.geometry('600x500+300+200')
         win.title("Button control config" )
         win["bg"] = "lightgray"
         win.transient(root)
         #win.state('normal')
         win.resizable('n', 'n')

         listbox = Listbox(win,width=40,bg='lightgray')

         listbox.pack(side=LEFT,fill='y')

         listbox.bind('<<ListboxSelect>>', getLine)
         listbox.yview()



         buttonSaveToFile=Button(win,text="Save")
         buttonSaveToFile.bind('<Button-1>', lambda e: saveToFile(btPath))
         buttonSaveToFile.place(x=450,y=350)

         buttonNew=Button(win,text="New",command=addNewPoint)
         buttonNew.place(x=380,y=350)


         X=0
         XX=0
         Y=90
         regAdrInp = Entry(win)
         regAdrInp.place(x=XX+340,y=Y+10)
         regAdrLabel = Label(win,text='Coil address',bg='lightgray').place(x=X+250,y=Y+10)

         startX = Entry(win)
         startX.place(x=XX+340,y=Y+30)
         startXLabel = Label(win,text='Start X',bg='lightgray').place(x=X+250,y=Y+30)
         startY = Entry(win)
         startY.place(x=XX+340,y=Y+50)
         startYLabel = Label(win,text='Start Y',bg='lightgray').place(x=X+250,y=Y+50)

         pointName = Entry(win,width=40)
         pointName.place(x=340,y=10)
         pointNameLabel = Label(win,text='Button name',bg='lightgray').place(x=245,y=10)

         pointAddress = Entry(win)
         pointAddress.place(x=340,y=30)
         pointAddressLabel = Label(win,text='Button address',bg='lightgray').place(x=245,y=30)

         pointControlValue = Entry(win)
         pointControlValue.place(x=340,y=60)
         ControlValueLabel = Label(win,text='Send value',bg='lightgray').place(x=245,y=60)


         arrayStartX=[]
         arrayStartY=[]
         arrayPointAddress=[]
         regAdr=[]
         arraySend=[]
         global arrayPointName
         arrayPointName=[]

         for c in range(0,1000):
             arrayStartX.append(c)
             arrayStartY.append(c)
             arrayPointAddress.append(c)
             arrayPointName.append(c)
             regAdr.append(c)
             arraySend.append(c)
             c += 1

         c=1
         with open(btPath) as f:
             for line in f:
                 param=line.split(';')
                 if(param[0] == 'bt'):
                     listbox.insert(END,param[5]+'\n')
                     arrayPointAddress[c]=param[1]
                     arrayStartX[c]=param[2]
                     arrayStartY[c]=param[3]
                     regAdr[c]=param[4]
                     arrayPointName[c]=param[5]
                     arraySend[c]=param[6]

                     c+=1
                     countLines=c
         f.close()

     except Exception, e:
         print "Failed to edit bt",e


