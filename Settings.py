import sv_ttk
import webbrowser
import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox as msg

class Values: # 一些值和变量
    # 设置参数变量存放
    # musicFileLocation = "" # 铃声文件位置
    talkSentence = "" #提醒文字
    talkTitle = "" # 提醒标题
    playVolument = 0.0
    tranValueWindow = 0.0 # 窗体透明度

    # 设置判断
    isProtectShutdown = False
    isUseDarkMode = False

class onLoad:
    def readToStart(): # 读取文本文件写入设置
        try:

            with open('settings.ret', 'r', encoding='utf-8') as settingsFile:
                readDataList = settingsFile.readlines()

                Values.talkSentence = readDataList[0].replace("\n", "")
                Values.talkTitle = readDataList[1].replace("\n", "")

                if readDataList[2].replace("\n", "").lower() == 'yes': # 检查是否开启定时关机保护
                    Values.isProtectShutdown = True
                elif readDataList[2].replace("\n", "").lower() == 'no':
                    Values.isProtectShutdown = False

                if float(readDataList[3].replace("\n", "")) < 0:
                    Values.playVolument = 0.0
                elif float(readDataList[3].replace("\n", "")) > 100:
                    Values.playVolument = 100.0
                else:
                    Values.playVolument = float(readDataList[3].replace("\n", ""))
                    
                if readDataList[4].replace("\n", "").lower() == 'yes': # 检查是否开启dark mode
                    Values.isUseDarkMode = True
                elif readDataList[4].replace("\n", "").lower() == 'no':
                    Values.isUseDarkMode = False

                if float(readDataList[5].replace("\n", "")) <= 0: # 窗体透明度
                    Values.tranValueWindow = 0.35
                elif float(readDataList[5].replace("\n", "")) > 1:
                    Values.tranValueWindow = 1.0
                else:
                    Values.tranValueWindow = float(readDataList[5].replace("\n", ""))

        
        except: 
            pass # 报错则不进行配置
    
    def setToControls(): # 将设置文本内容同步到控件
        volumentValue.set(str(Values.playVolument))
        tipTitleValue.set(str(Values.talkTitle))
        TipsSayValue.set(str(Values.talkSentence))
        ofProtectShutdown.set(int(Values.isProtectShutdown))
        ofAutoEnableDarkMode.set(int(Values.isUseDarkMode))
        tranValue.set(str(Values.tranValueWindow))


class Events:
    def Github(event): 
        webbrowser.open('github.com/CavDev/Reload-Timer')

    def Bilibili(event): 
        x = msg.showwarning('Question', "Open?")
        if x == 'OK'.lower:
            webbrowser.open('space.bilibili.com/396631212')
        

    def pickFileDialog(event): # 帮助
        # filetypes = [('MP3', '.mp3')]
        # Values.musicFileLocation = filedialog.askopenfilename(filetypes=filetypes, initialdir="Select Music File")
        strTemp = """
        铃声文件默认存放在程序的所在目录下，文件名为 music.mp3\n 
        如果想使用自定义铃声，请将你的铃声文件命名为 music.mp3 并替换掉程序目录下的默认铃声文件\n
        注意格式是否为mp3，若不是请转换格式，否则可能无法正常播放铃声
        \n
        \n
        默认铃声是 Kordhell 的 Live Another Day\n
        推荐去听他和疤王合作出的 PSYCHX 专辑 (*/ω＼*)
        """

        msg.askyesno("帮助", strTemp)

    def ProtectShutdown(event): 
        if Values.isProtectShutdown == True:
            Values.isProtectShutdown = False
        elif Values.isProtectShutdown == False:
            Values.isProtectShutdown = True

    def AutoEnableDarkMode(event):
        if Values.isUseDarkMode == True:
            Values.isUseDarkMode = False
        elif Values.isUseDarkMode == False:
            Values.isUseDarkMode = True

    def Save(event):
        global writeSetting
        global temp1
        global temp2

        temp1 = ''
        temp2 = ''

        if Values.isProtectShutdown == True:
            temp1 = 'YES'
        else: temp1 = 'NO'
        if Values.isUseDarkMode == True:
            temp2 = 'YES'
        else: temp2 = 'NO'

        writeSetting = [TipsSayValue.get(), tipTitleValue.get(), temp1, volumentValue.get(), temp2, tranValue.get()]
        
        with open('settings.ret', 'w', encoding='utf-8') as settingsFileForSave:
            settingsFileForSave.close()

            for n in writeSetting:
                with open('settings.ret', 'w', encoding='utf-8') as settingsFileForSave:
                    settingsFileForSave.write('\n'.join(writeSetting))
            
    def boolToStr(value : bool):
        if value == True : return 'YES' 
        elif value == False : return 'NO'



class WinGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__win()

        self.tk_label_frame_musicSettings = Frame_musicSettings(self)
        self.tk_label_frame_lb0pziyb = Frame_lb0pziyb(self)
        self.tk_label_frame_lb0rqzia = Frame_lb0rqzia(self)
        self.tk_label_frame_lb0rxcu1 = Frame_lb0rxcu1(self)
        self.tk_button_Github = self.__tk_button_Github()
        self.tk_button_myBilibili = self.__tk_button_myBilibili()
        self.tk_button_Save = self.__tk_button_Save()
        self.tk_label_lb230u4c = self.__tk_label_lb230u4c()
        self.tk_label_lb22zaeb = self.__tk_label_lb22zaeb()

    def __win(self):
        self.title("计时器 设置")
        # 设置窗口大小、居中
        width = 410
        height = 510
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.iconbitmap('Settings.ico')
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_button_Github(self):
        btn = Button(self, text="Github")
        btn.place(x=10, y=460, width=82, height=30)
        btn.bind("<Button-1>", Events.Github)
        return btn

    def __tk_button_myBilibili(self):
        btn = Button(self, text="作者B站")
        btn.place(x=110, y=460, width=91, height=30)
        btn.bind("<Button-1>", Events.Bilibili)
        return btn

    def __tk_button_Save(self):
        btn = Button(self, text="保存", style="Accent.TButton")
        btn.place(x=12, y=410, width=189, height=39)
        btn.bind('<Button-1>', Events.Save)
        return btn

    def __tk_label_lb22zaeb(self):
        label = Label(self,text="sukuw0 Create in 2022/11/29", foreground='gray')
        label.place(x=230, y=450, width=200, height=24)
        return label

    def __tk_label_lb230u4c(self):
        label = Label(self,text="v2.1")
        label.place(x=340, y=470, width=84, height=24)
        return label
    

class Frame_musicSettings(LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_lb0pwttl = self.__tk_label_lb0pwttl()
        self.tk_button_pickFile = self.__tk_button_pickFile()
        self.tk_input_Volument = self.__tk_input_Volument()
        self.tk_label_lb0pypd7 = self.__tk_label_lb0pypd7()
    def __frame(self):
        self.configure(text="铃声")
        self.place(x=10, y=10, width=190, height=133)

    def __tk_label_lb0pwttl(self):
        label = Label(self,text="位置")
        label.place(x=10, y=0, width=50, height=28)
        return label

    def __tk_button_pickFile(self):
        btn = Button(self, text="帮助")
        btn.place(x=80, y=0, width=91, height=33)
        btn.bind("<Button-1>", Events.pickFileDialog)
        return btn

    def __tk_input_Volument(self): # 设置音量
        global volumentValue
        volumentValue = tk.StringVar()
        ipt = Entry(self, textvariable=volumentValue)       
        ipt.place(x=80, y=50, width=90, height=31)
        return ipt

    def __tk_label_lb0pypd7(self):
        label = Label(self,text="音量")
        label.place(x=10, y=50, width=50, height=32)
        return label

class Frame_lb0pziyb(LabelFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_lb0pzxh7 = self.__tk_label_lb0pzxh7()
        self.tk_input_TipsTitle = self.__tk_input_TipsTitle()
        self.tk_label_lb0rmx6u = self.__tk_label_lb0rmx6u()
        self.tk_text_TipsSay = self.__tk_text_TipsSay()      

    def __frame(self):
        self.configure(text="计时结束提醒")
        self.place(x=210, y=10, width=187, height=238)

    def __tk_label_lb0pzxh7(self):
        label = Label(self,text="标题")
        label.place(x=10, y=10, width=55, height=28)
        return label

    def __tk_input_TipsTitle(self):
        global tipTitleValue
        tipTitleValue = tk.StringVar()
        ipt = Entry(self, textvariable=tipTitleValue)
        ipt.place(x=80, y=10, width=92, height=29)
        return ipt

    def __tk_label_lb0rmx6u(self):
        label = Label(self,text="内容")
        label.place(x=10, y=50, width=55, height=30)
        return label

    def __tk_text_TipsSay(self):
        global TipsSayValue
        TipsSayValue = tk.StringVar()
        text = Entry(self, textvariable=TipsSayValue)
        text.place(x=10, y=90, width=164, height=100)
        return text

class Frame_lb0rqzia(LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_lb0rrdc3 = self.__tk_label_lb0rrdc3()
        self.tk_check_button_AutoEnableDarkMode = self.__tk_check_button_AutoEnableDarkMode()
        self.tk_label_lb0rs8d5 = self.__tk_label_lb0rs8d5()
        self.tk_check_button_ProtectShutdown = self.__tk_check_button_ProtectShutdown()
    def __frame(self):
        self.configure(text="其它设置")
        self.place(x=10, y=160, width=190, height=231)

    def __tk_label_lb0rrdc3(self):
        label = Label(self,text="默认启用 Dark 模式")
        label.place(x=10, y=10, width=119, height=29)
        return label

    def __tk_check_button_AutoEnableDarkMode(self):
        global ofAutoEnableDarkMode
        ofAutoEnableDarkMode = tk.IntVar()
        cb = Checkbutton(self,text="", style="Switch.TCheckbutton", variable=ofAutoEnableDarkMode)
        cb.place(x=10, y=50, width=80, height=31)
        cb.bind("<Button-1>", Events.AutoEnableDarkMode)
        return cb

    def __tk_label_lb0rs8d5(self):
        label = Label(self,text="定时关机保护")
        label.place(x=10, y=100, width=86, height=29)
        return label

    def __tk_check_button_ProtectShutdown(self):
        global ofProtectShutdown
        ofProtectShutdown = tk.IntVar()
        cb = Checkbutton(self,text="", style="Switch.TCheckbutton", variable=ofProtectShutdown)
        cb.place(x=10, y=150, width=80, height=36)
        cb.bind("<Button-1>", Events.ProtectShutdown)
        return cb

class Frame_lb0rxcu1(LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_lb0rxzp5 = self.__tk_label_lb0rxzp5()
        self.tk_input_TranValue = self.__tk_input_TranValue()
    def __frame(self):
        self.configure(text="窗体透明度")
        self.place(x=210, y=260, width=189, height=175)

    def __tk_label_lb0rxzp5(self):
        label = Label(self,text="最大 1.0 (不透明) 最小 0.35")
        label.place(x=10, y=10, width=159, height=48)
        return label

    def __tk_input_TranValue(self):
        global tranValue
        tranValue = tk.StringVar()
        ipt = Entry(self, textvariable=tranValue)
        ipt.place(x=10, y=80, width=161, height=26)
        return ipt

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass
        
if __name__ == "__main__":
    win = Win()

    onLoad.readToStart()
    onLoad.setToControls()

    if Values.isUseDarkMode == True:
        sv_ttk.set_theme('dark')
    else:
        sv_ttk.set_theme('light')

    win.mainloop()
