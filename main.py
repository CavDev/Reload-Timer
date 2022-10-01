import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox as msg
import time
import calendar
import sv_ttk
import threading
import os
import random as rd
from pygame import mixer # 用于播放音乐

'''
# 写后感：用Tkinter写计时器是真几把难受
# 这辈子见过最捞的GUI框架还得是tkinter
'''

isOpenTopMost = 0 # false
isOpenTopMost2 = 1 # fuckingfalse

class Values: # 一些值和变量
    timeClockClick = 0
    showCalendarClick = 0
    s = 0 # 计时器秒数
    fuckThread = False

    # 设置参数变量存放
    talkSentence = ""
    talkTitle = ""
    playVolument = 0.0

    # 设置判断
    isTimeOutTalk = False
    isTimeOutSayGuy = False
    isProtectShutdown = False
    isUseDarkMode = False

class Events: # 事件
    def startCheck(): # 启动检查，并引入配置

        '''
        检查设置，使用文本文件形式存储
        第一行存放时间到时提醒的话语
        第二行存放提醒人或者主标语（好没意义的说）
        第三行是否启用定时关机保护（当时间小于15秒则不能定时关机）yes代表启用 no代表不启用
        时间到时播放的声音文件名：play.mp3，不存在则不播放
        第四行设置播放声音大小（最大值100）
        第五行设定 Dark 模式是否启用 yes代表启用 no代表不启用
        '''

        try: # 看得我头晕
            with open('settings.ret', 'r', encoding='utf-8') as settingsFile:
                readDataList = settingsFile.readlines()

                if readDataList[2].replace("\n", "").lower() == 'yes': # 检查是否开启定时关机保护
                    Values.isProtectShutdown = True
                elif readDataList[2].replace("\n", "").lower() == 'no':
                    Values.isProtectShutdown = False

                if readDataList[4].replace("\n", "").lower() == 'yes': # 检查是否开启dark mode
                    Values.isUseDarkMode = True
                elif readDataList[4].replace("\n", "").lower() == 'no':
                    Values.isUseDarkMode = False

                Values.talkSentence = readDataList[0].replace("\n", "")
                Values.talkTitle = readDataList[1].replace("\n", "")

                if float(readDataList[3].replace("\n", "")) < 0:
                    Values.playVolument = 0.0
                elif float(readDataList[3].replace("\n", "")) > 100:
                    Values.playVolument = 100.0
                else:
                    Values.playVolument = float(readDataList[3].replace("\n", ""))
        except: 
            pass # 报错则不进行配置

    def changeTheme(event):
        global themeValue

        if Values.timeClockClick == 1: # timeclockclick初始为0
            if themeValue == 'light':
                themeValue = 'dark'
            elif themeValue == 'dark':
                themeValue = 'light'

            sv_ttk.set_theme(themeValue) # 更换主题

            Values.timeClockClick = 0
        elif Values.timeClockClick != 2:
            Values.timeClockClick += 1

    def showCalendar(event):
        Values.showCalendarClick += 1
        mouth = time.strftime("%m")
        year = time.strftime("%Y")
        
        if Values.showCalendarClick == 10:
            msg.showinfo("不算彩蛋的彩蛋", "恭喜你发现了这个彩蛋！\n以下是我的一些感言\n\n拿tkinter写计时器是真滴难受，tk属实是我见过最捞的gui了\n这次更新首次加入了设置，至于为什么实现效果这么拉胯，是因为我懒得在tkinter中用json\n我没有记录变量所以你可以重新触发这个捞的一批的彩蛋\n（触发彩蛋的点击次数是10次）\n\n2022.10.1\nBy NSX7\n国庆节长假快乐\n我的个人博客：cavdev.github.io")
            Values.showCalendarClick = 0 # 重新设为零
        else:
            cal = calendar.calendar(int(year), int(mouth)) # 本来应该是 calendar.month的
            msg.showinfo(f"日历 - {year} 年 {mouth} 月", cal)
        
    def staticGetTime():
        while True:
            Timeis.set(time.strftime("%H : %M : %S"))  # 获取当前时间
            time.sleep(1.0)
            
    def goStartTime(event):
        global thread2
        thread2 = threading.Thread(target=Events.overGoStartTime)
        thread2.setDaemon(True)
        thread2.start() # 线程开始，用于计时
    
    def overGoStartTime():   
        Values.fuckThread = False
        
        if isEnable.get() == '开始计时':
            isEnable.set('停止计时')
            
            while True:               
                tempList = TimeClock.get().split(' : ')
                
                tempList1 = int(float(tempList[0]))
                tempList2 = int(float(tempList[1]))
                tempList3 = int(float(tempList[2]))
                
                if tempList3 == 59: # 秒
                    tempList3 = 0
                    tempList2 += 1
                elif tempList2 == 59:
                    tempList2 = 0
                    tempList1 += 1
                else:
                    tempList3 += 1
                    
                overTimeList = str(tempList1) + ' : ' + str(tempList2) + ' : ' + str(tempList3)         
                TimeClock.set(overTimeList)
                
                time.sleep(1.0)
                
                Values.s += 1

                try:
                    if Values.s == int(AlartClock.get()): # 当倒计时结束
                        # 检查字符串是否为空
                        if len(Values.talkSentence) == 0 or len(Values.talkTitle) == 0:
                            roleList = ["NSX7（RETIME By NSX7）", "牛爷爷", "高级特工穿山甲", "刘华强", "摘下眼镜的杰哥", "昏睡中的彬彬", "鸡哥", "正在抽锐刻5的顶针"]
                            whoSay = roleList[rd.randint(0, len(roleList) - 1)]
                            randomTips = rd.randint(1, 20)

                            try:
                                mixer.music.set_volume(Values.playVolument)
                                mixer.music.load('play.mp3') # 播放铃声
                                mixer.music.play()
                            except: pass

                            msg.showwarning(f"{ whoSay } 提醒 您", + randomTips*"时间到了")
                                 
                        elif len(Values.talkSentence) != 0 or len(Values.talkTitle) != 0: 
                            try:
                                mixer.music.set_volume(Values.playVolument)
                                mixer.music.load('play.mp3') # 播放铃声
                                mixer.music.play()
                            except: pass

                            msg.showwarning( Values.talkTitle, Values.talkSentence )

                        break
                    elif AlartClock.get() == '' | AlartClock.get() == ' ': # 当文本框为空
                        pass
                    elif Values.fuckThread == True:
                        break
                except:
                    if Values.fuckThread == True:
                        break
                    else: continue
                    
        elif isEnable.get() == '停止计时':
            Values.s = 0
            
            Values.fuckThread = True
            
            # 当点击停止计时之后，用break结束傻逼线程
            # 操你妈的傻逼python
            
            mixer.music.pause() # 暂停播放

            isEnable.set('开始计时')
            
            TimeClock.set('00 : 00 : 00')
            
    def sayForUse(event):
        msg.askyesno('说明', """不填则不倒计时，反之同样\n倒计时的值同样也会被用于定时关机\n(单位是秒数)""")
        
    def timeToShutdown(event): # 定时关机
        try: # 防止其它操作系统报错
            if isShutdowned.get() == '定时关机':
                tempTime = AlartClock.get()

                if Values.isProtectShutdown == True:
                    if int(tempTime) > 15:
                        os.system("shutdown /s /t %s" % tempTime)

                        isShutdowned.set('撤销关机')
                    else: msg.showerror("操作被取消","定时关机保护已启用\n如果想禁用定时关机保护请进入设置中（当前目录下settings.ret）更改第三行文本为no")
                elif Values.isProtectShutdown == False:
                    os.system("shutdown /s /t %s" % tempTime)

                    isShutdowned.set('撤销关机')

            elif isShutdowned.get() == '撤销关机':
                os.system("shutdown -a ")
                
                isShutdowned.set('定时关机')
        except:
            pass
    
    def topMost(event): # 置于顶层
        try:
            global isOpenTopMost2 # false 拿两个变量来判断是否窗体置顶，cnm真的蛋疼
            global isOpenTopMost
            
            if isOpenTopMost2 == 0:
                isOpenTopMost = 0 # 不设为置顶
                root.MainWindow.wm_attributes('-topmost', isOpenTopMost)
                isOpenTopMost2 = 1
                
                isTopMostText.set('置于顶层 ×')
            elif isOpenTopMost2 == 1: # 成功设为置顶
                isOpenTopMost = 1
                root.MainWindow.wm_attributes('-topmost', isOpenTopMost)
                isOpenTopMost2 = 0
                
                isTopMostText.set('置于顶层 ✓')
        except:
            pass
    
                   
class Root:
    def __init__(self): # 控件实例化
        self.MainWindow = self.creatWindow()
        self.tkBtn_TitleBar = self.__tkBtn_TitleBar()
        self.tkLab_timeClock = self.__tkLab_timeClock()
        self.MainFrame = MainFrame(self.MainWindow)
        
    def creatWindow(self):
        MainWindow = tk.Tk()
        MainWindow.geometry('695x225')
        MainWindow.title('RETIME')
        MainWindow.resizable(width=True, height=False)
        MainWindow.iconbitmap('ico.ico')
       
        return MainWindow
        
    def MainLoop(self):
        self.MainWindow.mainloop()
        
    def __tkBtn_TitleBar(self):
        global Timeis
        Timeis = tk.StringVar()
        btn = Button(self.MainWindow, textvariable=Timeis)
        btn.pack(side='top', fill='x')
        btn.bind("<Button-1>", Events.showCalendar)
        
        return btn
    
    def __tkLab_timeClock(self):
        global TimeClock
        TimeClock = tk.StringVar()
        TimeClock.set('00 : 00 : 00')
        lb = Label(self.MainWindow, textvariable=TimeClock, font=('Consolas', 40, 'bold'), foreground='dimgray')
        lb.pack(side='top', anchor='center', pady=18)
        lb.bind("<Button-1>", Events.changeTheme)
        
        return lb
        
        
class MainFrame:
    def __init__(self,parent):
        self.rootFrame = self.__tkFrm_MainFrame(parent)
        self.tkBtn_goStartTimeBtn = self.__tkBtn_goStartTimeBtn()
        self.tkLab_des = self.__tkLab_des()
        self.tkTBOX_setTimeTbox = self.__tkTBOX_setTimeTbox()
        self.tkBtn_timeToShutdown = self.__tkBtn_timeToShutdown()
        self.tkBtn_topMost = self.__tkBtn_topMost()
        
    def __tkFrm_MainFrame(self, parent):
        frm = Frame(parent, border='0', style="1.TFrame")
        frm.pack(side='top', anchor='center', fill='both',padx=15, pady=0)
        
        return frm
      
    def __tkBtn_goStartTimeBtn(self):
        global isEnable
        isEnable = tk.StringVar()
        isEnable.set('开始计时')
        btn = Button(self.rootFrame, textvariable=isEnable, width=20, style="Accent.TButton")
        btn.pack(side='left', anchor='w', padx=15, pady=18)
        btn.bind("<Button-1>", Events.goStartTime)
        
        return btn
    
    def __tkLab_des(self):
        lb = Label(self.rootFrame,  font=('Microsoft YaHei', 14), foreground='gray', text='倒计时：')
        lb.pack(side='left', anchor='w', padx=10, pady=18)
        lb.bind("<Button-1>", Events.sayForUse)
        
        return lb
        
    def __tkTBOX_setTimeTbox(self):
        global AlartClock
        AlartClock = tk.StringVar()
        AlartClock.set('60')
        tbx = Entry(self.rootFrame, textvariable=AlartClock, width=10)
        tbx.pack(side='left', anchor='w', padx=8, pady=18)
        
        return tbx
    
    def __tkBtn_timeToShutdown(self):
        global isShutdowned
        isShutdowned = tk.StringVar()
        isShutdowned.set('定时关机')
        btn = Button(self.rootFrame, width=12, textvariable=isShutdowned)
        btn.pack(side='right', anchor='e', padx=15, pady=18)
        btn.bind("<Button-1>", Events.timeToShutdown)
        
        return btn
       
    def __tkBtn_topMost(self):
        global isTopMostText
        isTopMostText = tk.StringVar()
        isTopMostText.set('置于顶层 ×')
        btn = Button(self.rootFrame, textvariable=isTopMostText, width=12)
        btn.pack(side='right', anchor='e', padx=1, pady=18)
        btn.bind("<Button-1>", Events.topMost)
        
        return btn
         
if __name__ == '__main__':    
    Events.startCheck() # 启动检查

    if Values.isUseDarkMode == True:
        themeValue = 'dark' # 主题颜色 light dark
    elif Values.isUseDarkMode == False:
        themeValue = 'light'
    
    root = Root() # 初始化函数
    mixer.init() # 初始化mixer用于播放

    sv_ttk.set_theme(themeValue)
    
    thread = threading.Thread(target=Events.staticGetTime) # 启动线程，同步系统时间
    thread.setDaemon(True)
    thread.start()

    root.MainLoop()