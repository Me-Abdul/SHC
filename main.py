from tkinter import *
from tkinter.ttk import Combobox

win = Tk()

#GlobalVaribales

message = ['b1','b2','b3','b4']
p = ['p']
shc = ['d7','d6','d5','p4','d3','p2','p1']
binary = {'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
msg1 = Message(win, text = '', width = 400, relief = 'ridge', bd = 3, font = ('Helvetica',  12))

# writes validation command
def validation(entryVal):
    if len(entryVal)<2 and entryVal in '01':
        return True
    return False
# register a validation command
isValid = win.register(validation)

def formats(q):
    q = q.replace('[','').replace("\'", '').replace(']','').replace(',','')
    return q


#//////////////////////////////\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\\/////////////////////////////////////////////////////////////////////////////////////////////////
class HammingCode:
    def __init__(self,_main_):
        mainF = Frame(_main_, bg ='#eee', width = '720', height = '800')
        self.frame = mainF
        global isValid


        def generateSHC():
            def paritize(db1,db2,db3,parity):
                #      s = db1+db2+db3
                s = int(db1)+int(db2)+int(db3)
                #        print('im in paritize with parit',parity,'s=',s, 'db1',type(db1))
                if s%2 == 0:
                    if parity[0] == 'e':
                        return '0'
                    elif parity[0] == 'o':
                        return '1'
                elif s%2 == 1:
                    if parity[0] == 'e':
                        return '1'
                    elif parity[0] == 'o':
                        return '0'
            def CalculateSHC():
                global message
                print(message)
                message[0] = bit1.get()
                message[1] = bit2.get()
                message[2] = bit3.get()
                message[3] = bit4.get()
                global p
                q = com.get().lower()
                if q == 'even parity':
                    p[0] = 'e'
                elif q == 'odd parity':
                    p[0] = 'o'
                global shc
                print(p)
                shc[0] = message[0]
                shc[1] = message[1]
                shc[2] = message[2]
                shc[4] = message[3]
                print(shc)
                shc[6] = paritize(shc[4],shc[2],shc[0],p)
                shc[5] = paritize(shc[4],shc[1],shc[0],p)
                shc[3] = paritize(shc[2],shc[1],shc[0],p)
                print(shc)
                #   ['1', '1', '0', '0', '1', '1', '0']

            CalculateSHC()
            re = 'Generated Hammming Code:    '

            global msg1
            msg1['text'] = re+formats(str(shc))
            msg1.pack(side = BOTTOM, pady = 100)

        def reset():
            global msg1
            bit1.delete(0)
            bit2.delete(0)
            bit3.delete(0)
            bit4.delete(0)
            com.delete(0,11)
            msg1.pack_forget()

            
        # Top Title of the software
        title=Label(_main_, text="7-bit Hamming Code Generator", fg='#127898', font=("Agency FB", 28, "bold","underline"))
        title.place(x=300, y=50)
        ver=Label(_main_, text="Version v1.1", fg='gray', font=("Courier", 8,"underline"))
        ver.place(x=450, y=100)


        # caption for message
        msg=Label(_main_, text="Enter 4-bit Message(e.g. 1010):", fg='black', font=("Helvetica", 12))
        msg.place(x=200, y=150)

        # Input Entry For 4 bits
        bit1=Entry(_main_,validate='all', validatecommand=(isValid,'%P'), text="bit1", exportselect = 0, bd = 3, width = 4)
        bit1.place(x=450, y=155)    
        bit1.focus()
        #
        bit1.tk_focusFollowsMouse()#
        #
        bit2=Entry(_main_, validate='all', validatecommand=(isValid,'%P'), text="bit2", exportselect = 0, bd = 3, width = 4)
        bit2.place(x=500, y=155)
        bit2.tk_focusNext()
        bit3=Entry(_main_, validate='all', validatecommand=(isValid,'%P'), text="bit3", exportselect = 0, bd = 3, width = 4)
        bit3.place(x=550, y=155)

        bit4=Entry(_main_,validate='all', validatecommand=(isValid,'%P'), text="bit4", exportselect = 0, bd = 3, width = 4)
        bit4.place(x=600, y=155)


        # caption for parity
        parity=Label(_main_, text="Select Parity Scheme:", fg='black', font=("Helvetica", 12))
        parity.place(x=250, y=200)

        #Combobox
        data = ('Even Parity','Odd Parity')
        com = Combobox(_main_, values = data, width = '27')
        com.place(x=450, y=205)

        genbtn = Button(_main_, text = "Generate", relief = "ridge", bd = 3, height = '1', width = '10', command = generateSHC)
        genbtn.place(x=350, y=250)


        resetbtn = Button(_main_, text = "Reset", relief = "ridge", bd = 3, height = '1', width = '10', command = reset)
        resetbtn.place(x=450, y=250)

        mainF.place()

#//////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class ErrHandle:
    
    def __init__(self, mainWindow):
        self.frame = Frame(mainWindow, bg ='#eee', width = '720', height = '800')

        _main_ = self.frame;
        msgED = Message(_main_, text = '', width = 400, relief = 'ridge', bd = 3, font = ('Helvetica',  12))
                

        def detect():
            def Check(db1,db2,db3,p,parity):
            #      s = db1+db2+db3
                s = int(db1)+int(db2)+int(db3)+int(p)
            #        print('im in paritize with parit',parity,'s=',s, 'db1',type(db1))
                if s%2 == 0:
                    if parity[0] == 'e':
                        return '0'
                    elif parity[0] == 'o':
                        return '1'
                elif s%2 == 1:
                    if parity[0] == 'e':
                        return '1'
                    elif parity[0] == 'o':
                        return '0'
        


            def reconfig():

                global p,binary
                q = com.get().lower()
                if q == 'even parity':
                    p[0] = 'e'
                elif q == 'odd parity':
                    p[0] = 'o'
                
                print(p)
                sh = ['p1','p2','p4']
                print(sh)
                sh[2] = Check(shc[4],shc[2],shc[0],shc[6],p)
                sh[1] = Check(shc[4],shc[1],shc[0],shc[5],p)
                sh[0] = Check(shc[2],shc[1],shc[0],shc[3],p)
                

                pa = ''

                print(sh,formats(str(sh)),shc,sep=' ')
                for i in sh:
                    pa += str(i)
                print(pa)
                for x in binary:
                   if pa == x:
                       return(binary[x])
                

            global shc
            shc[0] = d7.get()
            shc[1] = d6.get()
            shc[2] = d5.get()
            shc[3] = p4.get()
            shc[4] = d3.get()
            shc[5] = p2.get()
            shc[6] = p1.get()
            print('SHC_GET: ',shc)

            detC = reconfig()
            def correct():
                global shc
                for i in range(0,7):
                    if shc[7-detC] == '0':
                        shc[7-detC] = '1'
                    elif shc[7-detC] == '1':
                        shc[7-detC] = '0'
            re = '    Error detected in given Hammming Code at bit-' + str(detC) + ' from Right side'
            print(shc,'AFTERWARD!!')

        

            if detC != 0:
                correct()
                msgED['text'] = re + '\n Corrected Hamming Code is: ' + formats(str(shc))
                msgED.pack(side = BOTTOM, pady = 100)
            else:
                msgED['text'] = 'No Error Detected'
                msgED.pack(side = BOTTOM, pady = 100)


        def reset():
            global msg1
            p1.delete(0)
            p2.delete(0)
            d3.delete(0)
            p4.delete(0)
            d5.delete(0)
            d6.delete(0)
            d7.delete(0)
            com.delete(0,11)
            msgED.pack_forget()

           
                # Top Title of the software
        titleF=Label(_main_, text="Hamming Code Error Handler", fg='#127898', font=("Agency FB", 29, "bold","underline"))
        titleF.place(x=300, y=50)
        verF=Label(_main_, text="Version v1.1", fg='gray', font=("Courier", 8,"underline"))
        verF.place(x=450, y=100)


        # caption for message
        msgF=Label(_main_, text="Enter 7-bit Received SHC:", fg='black', font=("Helvetica", 12))
        msgF.place(x=60, y=150)

        # Input Entry For 7 bits
        d7=Entry(_main_,validate='key', validatecommand=(isValid,'%P'),  exportselect = 0, bd = 3, width = 4)
        d7.place(x=280, y=153)    
        #
        d7.tk_focusFollowsMouse()#
        #

        d6=Entry(_main_, validate='key', validatecommand=(isValid,'%P'), exportselect = 0, bd = 3, width = 4)
        d6.place(x=330, y=153)

        d5=Entry(_main_, validate='key', validatecommand=(isValid,'%P'),  exportselect = 0, bd = 3, width = 4)
        d5.place(x=380, y=153)

        p4=Entry(_main_,validate='key',  validatecommand=(isValid,'%P'),  exportselect = 0, bd = 3, width = 4)
        p4.place(x=430, y=153)

        d3=Entry(_main_,validate='key', validatecommand=(isValid,'%P'), exportselect = 0, bd = 3, width = 4)
        d3.place(x=480, y=153)

        p2=Entry(_main_,validate='key', validatecommand=(isValid,'%P'),exportselect = 0, bd = 3, width = 4)
        p2.place(x=530, y=153)

        p1=Entry(_main_,validate='key', validatecommand=(isValid,'%P'), exportselect = 0, bd = 3, width = 4)
        p1.place(x=580, y=153)

        # caption for parity
        parityF=Label(_main_, text="Select Used Parity Scheme:", fg='black', font=("Helvetica", 12))
        parityF.place(x=60, y=200)

        #Combobox
        data = ('Even Parity','Odd Parity')
        com = Combobox(_main_, values = data, width = '27')
        com.place(x=280, y=205)

        detbtn = Button(_main_, text = "Detect & Correct", relief = "ridge", bd = 3, height = '1', width = '15', command = detect)
        detbtn.place(x=350, y=250)


        rebtn = Button(_main_, text = "Reset", relief = "ridge", bd = 3, height = '1', width = '10', command = reset)
        rebtn.place(x=490, y=250)


    

class MENU:
    def __init__(self,_main_, mainFrame):
        self.mainFrame = mainFrame;
        self.errorFrame = None;
        global isValid
        def about():
            top = Toplevel(_main_)
            top.geometry("700x300+150+150")
            top.resizable(width = False, height = False)
            title = Label(top, fg = '#127898', text="7-bit Hamming Code Generator", font =('Agnecy FB',16,'bold','underline'))
            title.place(x = 200, y= 50)
            top.title("About - 7-bit Hamming Code Generator")

            ver=Label(top, text="Version v1.1", fg='#124699', font=("Courier", 8,"underline"))
            ver.place(x=300,y=80)

            dev=Label(top, text="Developed by: Abdul Mateen", fg='#127898', font=("Courier", 12,'bold'))
            dev.place(x = 100, y= 120)
            con=Label(top, text="Contact: mateen9194@gmail.com", fg='#127898', font=("Courier", 12,'italic'))
            con.place(x = 100, y= 140)
            credit=Label(top, text="Credits: Special Thanks to Matti Ullah Sahab (GC1 DIKHAN)", fg='#127898', font=("Courier", 12))
            credit.place(x = 100, y= 160)
            copyr=Label(top, text="Copyrights: 2022(c) All rights Reserved.", fg='gray', font=("Courier", 8))
            copyr.place(x = 200, y= 270)

        def helps():
            def openFile():
                tf = r'./docs/hammingCode.txt'
                tf = open(tf)  # or tf = open(tf, 'r')
                content = tf.read()
                data.insert(END,content)
                tf.close()
                data['state'] = 'disabled'
            top = Toplevel(_main_)
            top.geometry("900x500+150+150")
            top.resizable(width = False, height = False)

            scrollbar = Scrollbar(top)
            scrollbar.pack( side = RIGHT, fill = Y )
            title = Label(top, fg = '#127898', text="Help Index", font =('Agnecy FB',16,'bold','underline'))
            title.place(x = 100, y= 20)
            top.title("Help- 7-bit Hamming Code Generator")
           
            data=Text(top, yscrollcommand = scrollbar.set, wrap = WORD, width = 100, bg = top['bg'], fg='black', font=("Consolas", 9))
            data.place(x = 100, y= 80)
            readmore = Button(top, text="Show Content...", command = openFile ).place(x=400, y= 430)
            
            scrollbar.config( command = data.yview )

                    
        def ErrHandl():
            #del HC
            self.mainFrame.forget();
            Err = ErrHandle(win)
            Err.frame.pack(expand=1, fill='both')
            self.errorFrame = Err.frame;



        def HC():
            #del Err
            self.errorFrame.forget();
            HC = HammingCode(win)
            HC.frame.pack(expand=1, fill="both")
            self.mainFrame = HC.frame;
            
        
        menubar = Menu(_main_)

        file = Menu(menubar, tearoff=0)
        file.add_command(label="Exit (Alt+F4)", command=_main_.destroy)
        menubar.add_cascade(label="File", menu=file)
        
        modemenu = Menu(menubar, tearoff=0)
        modemenu.add_command(label="Hamming Code", command=HC)
        modemenu.add_command(label="Error Handling", command=ErrHandl)
        menubar.add_cascade(label="Modes", menu=modemenu)

        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=helps)
        helpmenu.add_command(label="About...", command=about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
       
        _main_.config(menu=menubar)


# -----------------------------------------------> __main__ <----------------------------------------------------------------------- #
hc = HammingCode(win)

mbar = MENU(win, hc.frame)



win.title('7-bit Hamming Code')
win.geometry("900x480")
win.iconbitmap('.//docs//hc.ico')
win.resizable(width = False, height = False)
win.mainloop()
