# -*- coding: cp1251 -*-

import sys
import os
import time
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import datetime
import gc
from Tkinter import *
import scadaWidgets
import scadaWin

def logFile(messageText):
     f=open(appPath + time.strftime('%d_%m_%Y')+'.log','a')
     f.write(messageText+'\n')
     f.close()

################################ init Discret Input ###################################################################################
def initDiscretInput():


     global diNameUnit
     global diArray
     global diArrayColorOn
     global diArrayColorOff
     global diArrayAlarmOn
     global diArrayAlarmOff
     global diX
     global diY


     diArray = []
     diArrayColorOn=[]
     diArrayColorOff=[]
     diArrayAlarmOn = []
     diArrayAlarmOff = []

     for counter in range(0,500):
         diArray.append(counter)
         diArrayColorOn.append(counter)
         diArrayColorOff.append(counter)
         diArrayAlarmOn.append(counter)
         diArrayAlarmOff.append(counter)
         diArray[counter]=0
     try:
         counter=1
         with open(diPath) as f:
             for line in f:
                 param=line.split(';')
                 if(param[0] == 'di'):
                     if(param[1] == 'rectangle'):
                         diFig=canv.create_rectangle(int(param[3]),int(param[4]),int(param[5]),int(param[6]),fill='gray',outline='black')
                     if(param[1] == 'circle'):
                         diFig=canv.create_oval(int(param[3]),int(param[4]),int(param[5]),int(param[6]),fill='grey',outline='black')

                     diArrayColorOn[counter] = param[7]
                     diArrayColorOff[counter] = param[8]
                     diArrayAlarmOn[counter] = param[9]
                     diArrayAlarmOff[counter] = param[10]


                     diArray[counter] = diFig
                     counter += 1
         diArray[0] =  counter - 1
         f.close()
     except IOError as e:
         print "I/O error({0}): {1}".format(e.errno, e.strerror)
     return diArray






################################ init Coil Input ###################################################################################
def initCoilInput():


     global ciNameUnit
     global ciArray
     global ciArrayColorOn
     global ciArrayColorOff
     global ciArrayAlarmOn
     global ciArrayAlarmOff
     global ciX
     global ciY


     ciArray = []
     ciArrayColorOn=[]
     ciArrayColorOff=[]
     ciArrayAlarmOn = []
     ciArrayAlarmOff = []

     for counter in range(0,500):
         ciArray.append(counter)
         ciArrayColorOn.append(counter)
         ciArrayColorOff.append(counter)
         ciArrayAlarmOn.append(counter)
         ciArrayAlarmOff.append(counter)
         ciArray[counter]=0
     try:
         counter=1
         with open(ciPath) as f:
             for line in f:
                 param=line.split(';')
                 if(param[0] == 'ci'):
                     if(param[1] == 'rectangle'):
                         ciFig=canv.create_rectangle(int(param[3]),int(param[4]),int(param[5]),int(param[6]),fill='gray',outline='black')
                     if(param[1] == 'circle'):
                         ciFig=canv.create_oval(int(param[3]),int(param[4]),int(param[5]),int(param[6]),fill='grey',outline='black')

                     ciArrayColorOn[counter] = param[7]
                     ciArrayColorOff[counter] = param[8]
                     ciArrayAlarmOn[counter] = param[9]
                     ciArrayAlarmOff[counter] = param[10]


                     ciArray[counter] = ciFig
                     counter += 1
         ciArray[0] =  counter - 1
         f.close()
     except IOError as e:
         print "I/O error({0}): {1}".format(e.errno, e.strerror)
     return ciArray






################################ init button tu ###################################################################################
def initButton():

     global btArray
     global btAddress
     global btNameUnit
     global controlValue

     btArray = []
     btAddress=[]
     btNameUnit=[]
     controlValue=[]

     for counter in range(0,500):
         btArray.append(counter)
         btAddress.append(counter)
         btNameUnit.append(counter)
         controlValue.append(counter)
         btArray[counter]=(1,' ')
         counter += 1
     try:
         counter=1
         with open(btPath) as f:
             for line in f:
                 param=line.split(';')
                 if(param[0] == 'bt'):
                     controlValue[counter] = param[6]
                     btFig = Button(root,text=param[5],width=10,height=1,bg="white",fg="black" )
                     btFig.place(x=int(param[2]),y=int(param[3]))
                     btFig.config(command=lambda widget=btFig,coilNum=param[4],coilState=param[6]: sendControl(widget,coilNum,coilState) )
                     btAddress[counter]=param[1]
                     btNameUnit[counter] = param[5]
                     btArray[counter] = btFig
                     counter += 1
         btArray[0] =  counter - 1
         f.close()
     except IOError as e:
         print "I/O error({0}): {1}".format(e.errno, e.strerror)
     return btArray

def sendControl(widget,coilNum,coilState):
     master.execute(1, cst.WRITE_SINGLE_COIL, int(coilNum), output_value=int(coilState) )
     logFile(time.strftime('%H:%M:%S') +  " Send command - Coil - " + coilNum +' State - '+ coilState )




################################ init Analog Input ###################################################################################
def initAnalogInput():

     global aiArray
     global aiArrayKoef
     global aiNameUnit
     global aiArrayColor

     aiArray = []
     aiArrayKoef=[]
     aiNameUnit=[]
     aiArrayColor=[]

     for counter in range(0,500):
         aiArray.append(counter)
         aiArrayKoef.append(counter)
         aiNameUnit.append(counter)
         aiArrayColor.append(counter)
         aiArray[counter]=(1,' ')
         counter += 1
     try:
         counter=1
         with open(aiPath) as f:
             for line in f:
                 param=line.split(';')
                 if(param[0] == 'ai'):
                     if(param[8] == 'text'):
                         aiFig=[canv.create_text(int(param[2]),int(param[3]),text=param[6],font="Verdana 12",anchor="w",justify=CENTER,fill=param[4])," "]
                     if(param[8] == 'hmeter'):
                         aiFig=elements.hMeterC(100,int(param[2]),int(param[3]),300,20,int(param[6]),param[4],param[7],root)
                     if(param[8] == 'vmeter'):
                         aiFig=elements.vMeterC(100,int(param[2]),int(param[3]),30,300,int(param[6]),param[4],param[7],root)
                     if(param[8] == 'ameter'):
                         aiFig=elements.aMeterC(100,int(param[2]),int(param[3]),150,150,int(param[6]),param[4],param[7],root)
                     aiArrayKoef[counter] = param[5]
                     aiNameUnit[counter] = param[7]

                     aiArray[counter] = aiFig
                     counter += 1
         aiArray[0] =  counter - 1
         f.close()
     except IOError as e:
         print "I/O error({0}): {1}".format(e.errno, e.strerror)
     return aiArray

########################### request ###########################


def createText(canvas,x,y,txt):
    rect=canvas.create_text(x,y,text=txt,font="Verdana 12",anchor="w",justify=CENTER,fill="white")
    return rect


def configDI(canvas,DI,color):
    canvas.itemconfig(DI,fill=color)
def configCI(canvas,DI,color):
    canvas.itemconfig(DI,fill=color)



######################################request for DIGITAL INPUT #################################
def jobDi():
         global getDI
         global master
         try:

             try:
                 if(diArray[0] > 0):
                     getDI = master.execute(1, cst.READ_DISCRETE_INPUTS, 0,diArray[0])
                     if(time.strftime('%S')=='00'):
                         logFile(time.strftime('%H:%M:%S') + " Get answer Discret - " +str(getDI) )
                     if(debugValue == 'True'): textB.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Get answer Discret - " +str(getDI)+"\n")


                 ################## to log file


             except:
                 print 'getDI Except DI'
                 if(debugValue == 'True'): textB.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Not answer Discret \n")
                 logFile(time.strftime('%H:%M:%S') + " Not answer Discret" )
                 getDI=' Error connect'
                 master = modbus_tcp.TcpMaster(host=slaveIP, port=int(slavePort))
                 master.set_timeout(5.0)


             for count in range(0,diArray[0]):
                 newDi[count+1] = getDI[count]

                 if(getDI[count] == 1 ):
                     configDI(canv,diArray[count+1],diArrayColorOn[count+1])
                 else:
                     configDI(canv,diArray[count+1],diArrayColorOff[count+1])

                 if(oldDi[count+1]!= newDi[count+1] and getDI[count] == 1):
                     #print time.strftime('%d-%m-%Y %H:%M:%S') + " Message - " + diArrayAlarmOn[count+1]
                     textA.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Message - " + diArrayAlarmOn[count+1] +"\n")
                     logFile(time.strftime('%H:%M:%S') +  " Message DI - " + diArrayAlarmOn[count+1] )

                 if(oldDi[count+1]!= newDi[count+1] and getDI[count] == 0):
                     #print time.strftime('%d-%m-%Y %H:%M:%S') + " Message - " + diArrayAlarmOff[count+1]
                     textA.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Message - " + diArrayAlarmOff[count+1] +"\n")
                     logFile(time.strftime('%H:%M:%S') +  " Message DI - " + diArrayAlarmOff[count+1] )

                 oldDi[count+1] = getDI[count]
                 count+=1

             root.update()
         except Exception, e:
             print 'jobDI Error connect to master DI',e








######################################request for DIGITAL INPUT #################################
def jobCi():
         global getCI
         global master
         try:

             try:
                 if(ciArray[0] > 0):
                     getCI = master.execute(1, cst.READ_COILS, 0,ciArray[0])
                     if(debugValue == 'True'): textB.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Get answer Coil - " +str(getCI)+"\n")
                     if(time.strftime('%S')=='00'):
                         logFile(time.strftime('%H:%M:%S') + " Get answer Coil - " +str(getCI) )

             except:
                 print 'getCI Except CI'
                 if(debugValue == 'True'): textB.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Not answer Coil \n")
                 logFile(time.strftime('%H:%M:%S') + " Not answer Coil" )
                 getCI=' Error connect'
                 master = modbus_tcp.TcpMaster(host=slaveIP, port=int(slavePort))
                 master.set_timeout(5.0)


             for count in range(0,ciArray[0]):
                 newCi[count+1] = getCI[count]

                 if(getCI[count] == 1 ):
                     configCI(canv,ciArray[count+1],ciArrayColorOn[count+1])
                 else:
                     configCI(canv,ciArray[count+1],ciArrayColorOff[count+1])

                 if(oldCi[count+1]!= newCi[count+1] and getCI[count] == 1):

                     textA.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Message Coil - " + ciArrayAlarmOn[count+1] +"\n")
                     logFile(time.strftime('%H:%M:%S') +  " Message CI - " + ciArrayAlarmOn[count+1] )

                 if(oldCi[count+1]!= newCi[count+1] and getCI[count] == 0):

                     textA.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Message Coil - " + ciArrayAlarmOff[count+1] +"\n")
                     logFile(time.strftime('%H:%M:%S') +  " Message CI - " + ciArrayAlarmOff[count+1] )

                 oldCi[count+1] = getCI[count]
                 count+=1

             root.update()
         except Exception, e:
             print 'jobCI Error connect to master CI',e








######################################request for ANALOG INPUT #################################
def jobAi():
         global getAI
         global master
         try:

             try:
                 if(aiArray[0] > 0):
                     getAI  = master.execute(1, cst.READ_INPUT_REGISTERS, 0,aiArray[0])
                     if(debugValue == 'True'): textB.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Get answer Analog - " +str(getAI)+"\n")
                 #    varError = False
                 ################### to log file
                     if(time.strftime('%S')=='00'):
                         logFile(time.strftime('%H:%M:%S') + " Get answer Analog - " +str(getAI) )
                         if(debugValue == 'True'):  textB.delete('1.0', END)
                         gc.collect()
                 varError = False
             except:
                 print 'getAI except '
                 if(debugValue == 'True'): textB.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S') + " Not answer Analog \n")
                 logFile(time.strftime('%H:%M:%S') + ' Not answer Analog ' )
                 getAI=' Error connect'
                 varError = True
                 master = modbus_tcp.TcpMaster(host=slaveIP, port=int(slavePort))
                 master.set_timeout(5.0)

             if(varError == False):

                 for count in range(0,aiArray[0]):
                     if(aiArray[count+1][1]=='hmeter'):
                         aiArray[count+1][0].delete("all")
                         elements.hMeter([ aiArray[count+1][0],getAI[count]*float(aiArrayKoef[count+1]),aiArray[count+1][2],aiArray[count+1][3],aiArray[count+1][4],aiArray[count+1][5],aiArray[count+1][6],aiArray[count+1][7],aiArray[count+1][8] ])
                     elif(aiArray[count+1][1]=='vmeter'):
                         aiArray[count+1][0].delete("all")
                         elements.vMeter([ aiArray[count+1][0],getAI[count]*float(aiArrayKoef[count+1]),aiArray[count+1][2],aiArray[count+1][3],aiArray[count+1][4],aiArray[count+1][5],aiArray[count+1][6],aiArray[count+1][7],aiArray[count+1][8] ])
                     elif(aiArray[count+1][1]=='ameter'):
                         aiArray[count+1][0].delete("all")
                         elements.aMeter([ aiArray[count+1][0],getAI[count]*float(aiArrayKoef[count+1]),aiArray[count+1][2],aiArray[count+1][3],aiArray[count+1][4],aiArray[count+1][5],aiArray[count+1][6],aiArray[count+1][7],aiArray[count+1][8]])



                     else:
                         canv.itemconfig(aiArray[count+1][0],text=str(getAI[count] * float(aiArrayKoef[count+1]) ) )

                     count+=1
             root.update()
             gc.collect()
         except Exception, e:

             print 'iobAI Error connect to master AI', e


def jobModbusTCP():
             global master
             if hendl:


                 timeNow.delete('1.0', END)
                 timeNow.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S'))




                 try:
                     jobCi()

                 except:
                     print 'jobModbusTCP CI No  connection'

                     master = modbus_tcp.TcpMaster(host=slaveIP, port=int(slavePort))
                     master.set_timeout(5.0)




                 try:
                     jobDi()

                 except:
                     print 'jobModbusTCP DI No  connection'

                     master = modbus_tcp.TcpMaster(host=slaveIP, port=int(slavePort))
                     master.set_timeout(5.0)



                 try:

                     jobAi()

                 except Exception, e:
                     print 'jobModbusTCP AI No  connection',e
                     master = modbus_tcp.TcpMaster(host=slaveIP, port=int(slavePort))
                     master.set_timeout(5.0)




                 root.update()
             root.after(int(delayTime), jobModbusTCP)



def startWorking():
     global hendl
     global diArray
     global diArrayColorOn
     global diArrayColorOff
     global diArrayAlarmOn
     global diArrayAlarmOff

     global ciArray
     global ciArrayColorOn
     global ciArrayColorOff
     global ciArrayAlarmOn
     global ciArrayAlarmOff

     global btArray
     global btAddress
     global btNameUnit


     global aiArray
     global aiArrayKoef

     global master
     hendl=True
     canv.delete("all")
     canv.create_image(1, 1,anchor=NW, image=im)
     diArray=initDiscretInput()
     ciArray=initCoilInput()
     btArray=initButton()

     aiArray=initAnalogInput()

     logFile(time.strftime('%H:%M:%S') + " Run programm" )

def stopWorking():
     global hendl
     if(debugValue == 'True'):  textB.delete('1.0', END)
     hendl = False
     for c in range(1,aiArray[0]):
         canv.delete(aiArray[c][0])
     logFile(time.strftime('%H:%M:%S') + " Stop Running programm" )




def exitWin(Event):
     global hendl
     hendl=False
     #root.close_all()
     logFile(time.strftime('%H:%M:%S') + " Exit programm" )
     root.quit()



def openTrend():
     def getLine(e):
         global trendName
         global tr1
         global hendlTrend
         global getAiTrend
         global mesureValue

         hendlTrend=False
         mesureValue=None
         mesureValue=[]

         x=listbox.curselection()
         trendName=arrayPointName[int(x[0])+1]
         tr1=hTrendC(250,5,1030,400,int(arrayValueAI[int(x[0]) + 1]),arrayColorAI[int(x[0])+1],arrayPointName[int(x[0])+1], arrayKoefAI[int(x[0])+1])
         getAiTrend=int(x[0])
         hendlTrend=True

     def hTrendC(x,y,widgLen,widgHigh,maxValue,outerColor,nameValue,trendKoef):
         c = Canvas(win,width=widgLen+50,height=widgHigh+40,bg="black",bd=0, highlightthickness=0, relief='ridge')
         c.place(x=x, y=y)
         return (c,'htrend',x,y,widgLen,widgHigh,maxValue,outerColor,nameValue,trendKoef)

     def hTrend(arrayData,arrayValue,devValue):
         c,markErr,x,y,widgLen,widgHigh,maxValue,outerColor,nameValue,trendKoef=arrayData
         c.create_rectangle(1,1,widgLen,widgHigh,fill='black',outline=outerColor)
         c.create_line(50,widgHigh/2,widgLen-5,widgHigh/2,width=0.1,fill='white',dash=(4, 2))
         c.create_line(50,widgHigh/4,widgLen-5,widgHigh/4,width=0.1,fill='white',dash=(4, 2))
         c.create_line(50,widgHigh - widgHigh/4,widgLen-5,widgHigh -widgHigh/4,width=0.2,fill='white',dash=(4, 2))
         c.create_text(10,widgHigh-10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text=0)
         c.create_text(10,12,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text=str(maxValue))
         c.create_text(10,widgHigh/2,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text=str(int(maxValue/2)))
         c.create_text(10,widgHigh/4,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text=str(int(maxValue-maxValue/4)))
         c.create_text(10,widgHigh - widgHigh/4 ,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text=str(int(maxValue/4)))
         c.create_text(1,widgHigh+25,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text=nameValue)
         c.create_text(widgLen/10,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='1')
         c.create_text((widgLen/10)*2,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='2')
         c.create_text((widgLen/10)*3,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='3')
         c.create_text((widgLen/10)*4,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='4')
         c.create_text((widgLen/10)*5,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='5')
         c.create_text((widgLen/10)*6,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='6')
         c.create_text((widgLen/10)*7,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='7')
         c.create_text((widgLen/10)*8,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='8')
         c.create_text((widgLen/10)*9,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='9')
         c.create_text(widgLen-10,widgHigh+10,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text='100')

         oldy=widgHigh - float(widgHigh)/float(maxValue) * arrayValue[0] * float(trendKoef)
         oldx=5
         xval=0

         for counter in range(0,len(arrayValue)):

             val=arrayValue[counter]
             yval=widgHigh - float(widgHigh)/float(maxValue) * val * float(trendKoef)
             xval+=devValue
             c.create_line(oldx,oldy,xval,yval,width=1.5,fill='green')

             oldy=yval
             oldx=xval
         mesureValue = arrayValue[len(arrayValue)-1 ] * float(trendKoef)
         c.create_line(xval,widgHigh-10,xval,0,width=0.5,fill='white')
         c.create_text(xval+devValue,yval,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text=str(mesureValue))
         c.create_text(xval+devValue,yval+20,font="Verdana 10",anchor="w",justify=CENTER,fill='white',text=time.strftime('%H:%M:%S'))

     def jobTrend():
         global master
         global mesureValue
         global hendlTrend
         global getAiTrend

         devValue = 5

         if hendlTrend:
             lenVal = len(mesureValue)+1
             mesureValue.append(lenVal)
             mesureValue[lenVal-1] = getAI[getAiTrend]
             tr1[0].delete("all")
             hTrend(tr1,mesureValue,devValue)

             if(len(mesureValue) == 1000/devValue):
                 mesureValue=None
                 mesureValue=[]

         root.update()
         root.after(timeDelay, jobTrend)

     def startTrend():
         global hendlTrend
         hendlTrend=True
     def stopTrend():
         global hendlTrend
         hendlTrend=False
     def p(event):
         global hendlTrend
         hendlTrend=False
         win.destroy()
         #print 'exit'

 #############################################################################


     win = Toplevel(root)

     win.geometry('1300x500+300+200')
     win.title("Trend" )
     win["bg"] = "black"
     win.transient(root)
     win.resizable('n', 'n')


     listbox = Listbox(win,width=40,bg='black',foreground='white')
     listbox.pack(side=LEFT,fill='y')
     listbox.bind('<<ListboxSelect>>', getLine)
     listbox.yview()

     buttonStart=Button(win,width=10,text="Start",command=startTrend)
     buttonStart.place(x=250,y=450)

     buttonStop=Button(win,width=10,text="Stop",command=stopTrend)
     buttonStop.place(x=350,y=450)

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
     global mesureValue
     global hendlTrend
     global tr1
     hendlTrend=False
     mesureValue=[]
     tr1=[]
     win.attributes('-alpha', 0.8)
     timeDelay=100
     win.bind('<Destroy>',p)
     win.after(1, jobTrend)







#######################open log
def openLogWin():
     global stringLines
     global getAI
     def logJob():
         global stringLines
         if(stringLines == 30):
             textLog.delete('1.0', END)
             stringLines=0
         stringLines+=1
         if 'getAI' in globals():
             textLog.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S')+' get AI '+str(getAI)+'\n')
         if 'getDI' in globals():
             textLog.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S')+' get DI '+str(getDI)+'\n')
         if 'getCI' in globals():
             textLog.insert(1.0,time.strftime('%d-%m-%Y %H:%M:%S')+' get CI '+str(getCI)+'\n')


         win.after(1000, logJob)

     def p(event):
         win.destroy()


     stringLines=0
     win = Toplevel(root)
     win.geometry('600x600+50+200')
     win.title("Connection log" )
     win["bg"] = "black"
     win.transient(root)
     win.resizable('y', 'y')
     textLog=Text(win,font='Arial 12',width=500,height=50,wrap=WORD, bg='black',bd=0,fg='white')
     textLog.place(x=1,y=1)
     win.attributes('-alpha', 0.65)
     win.bind('<Destroy>',p)
    # win.overrideredirect(1)
     win.after(1, logJob)





##########################  start
if __name__ == "__main__":


##########################  params
     global stringLinesLog
     stringLinesLog=0

     if(os.name=='nt'):
         appPath=os.path.dirname(sys.argv[0]) + '\\'
         if(appPath=='\\'):
             appPath='.\\'
     else:
         appPath=os.path.dirname(sys.argv[0]) + '/'
         if(appPath=='/'):
             appPath='./'






     with open(appPath+'settings.cfg') as f:
             for line in f:
                 param=line.split('=')
                 if(param[0] == 'slaveIP'):    slaveIP=param[1].strip()
                 if(param[0] == 'slavePort'):  slavePort=param[1].strip()
                 if(param[0] == 'discretCfg'): discretCfg=param[1].strip()
                 if(param[0] == 'coilCfg'):    coilCfg=param[1].strip()
                 if(param[0] == 'buttonCfg'):    buttonCfg=param[1].strip()

                 if(param[0] == 'analogCfg'):  analogCfg=param[1].strip()
                 if(param[0] == 'bgimage'):    bgimage=param[1].strip()
                 if(param[0] == 'delayTime'):  delayTime=param[1].strip()
                 if(param[0] == 'debug'):      debugValue=param[1].strip()

     f.close()
    # global aiPath
     picturePath=appPath+'picture.cfg'
     backGroundPath=appPath+bgimage
     diPath=appPath+discretCfg
     ciPath=appPath+coilCfg
     aiPath=appPath+analogCfg
     btPath=appPath+buttonCfg


     master = modbus_tcp.TcpMaster(host=slaveIP, port=int(slavePort))
     master.set_timeout(1.0)



     root = Tk()
   #  root.overrideredirect(1)
     root.title("ScadaPy modbusTCP v2.20")
     if(os.name=='nt'): root.state("zoomed")
     else:  root.state("normal")
     root["bg"] = "black"
############ create menu ###########################
     elements=scadaWidgets.elements()

############ create buttons ###########################

     runButton = Button(root,text="Start",width=5,height=1,bg="white",fg="black",command=startWorking)
     runButton.place(x=1,y=1)

     stopButton = Button(root,text="Stop",width=5,height=1,bg="white",fg="black",command=stopWorking)
     stopButton.place(x=50,y=1)



     aiButton = Button(root,text="TI",width=5,height=1,bg="white",fg="black")
     aiButton.bind('<Button-1>', lambda e:   scadaWin.openAnalog(root,aiPath) )
     aiButton.place(x=100,y=1)

     ciButton = Button(root,text="TCc",width=5,height=1,bg="white",fg="black")
     ciButton.bind('<Button-1>', lambda e:   scadaWin.openCoil(root,ciPath) )
     ciButton.place(x=150,y=1)

     diButton = Button(root,text="TCd",width=5,height=1,bg="white",fg="black")
     diButton.bind('<Button-1>', lambda e:   scadaWin.openDiscret(root,diPath) )
     diButton.place(x=200,y=1)


     btButton = Button(root,text="TU",width=5,height=1,bg="white",fg="black")
     btButton.bind('<Button-1>', lambda e:   scadaWin.openButton(root,btPath) )
     btButton.place(x=250,y=1)



     trButton = Button(root,text="Trend",width=7,height=1,bg="white",fg="black",command=openTrend)

     trButton.place(x=300,y=1)


     logButton = Button(root,text="Log",width=10,height=1,bg="white",fg="black",command=openLogWin)
     logButton.place(x=380,y=1)


     im = PhotoImage(file=backGroundPath)
     canv = Canvas(root,width=1900,height=950,bg="black",bd=0, highlightthickness=0, relief='ridge')

     canv.place(x=0, y=25)
     canv.create_image(1, 1,anchor=NW, image=im)


########################## time
     timeNow=Text(root,height=1,width=20,font='Arial 12',wrap=WORD, bg='black',bd=0,fg='white')
     timeNow.place(x=500,y=2)
########################## log TC
     textA=Text(root,height=7,width=50,font='Arial 12',wrap=WORD, bg='black',bd=0,fg='white')
     textA.place(x=10,y=800)
     ###################################### log network
     if(debugValue == 'True'):
         textB=Text(root,height=7,width=145,font='Arial 12',wrap=WORD, bg='black',bd=0,fg='white')
         textB.place(x=900,y=800)



     oldDi=[]
     newDi=[]
     oldCi=[]
     newCi=[]

     for c in range(0,1000):
         oldDi.append(c)
         oldDi[c]=0
         newDi.append(c)
         newDi[c]=0

         oldCi.append(c)
         oldCi[c]=0
         newCi.append(c)
         newCi[c]=0


         c += 1


     print "Programm start"
     logFile(time.strftime('%H:%M:%S') + " Load program" )
     global hendl
     hendl=False
     root.bind('<Destroy>',exitWin)
     root.after(1, jobModbusTCP)
     root.mainloop()
















