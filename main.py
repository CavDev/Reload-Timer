from multiprocessing import Value
import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox as msg
import time
import calendar
import sv_ttk
import threading
import os
import random as rd

'''
# 写后感：用Tkinter写计时器是真几把难受
# 这辈子见过最捞的GUI框架还得是tkinter
'''

isOpenTopMost = 0 # false
isOpenTopMost2 = 1 # fuckingfalse
themeValue = 'light' # 主题颜色 light dark

class Values: # 一些值和变量
    timeClockClick = 0
    showCalendarClick = 0
    s = 0 # 计时器秒数
    fuckThread = False
    
class Events: # 事件
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
        
        if Values.showCalendarClick == int(mouth):
            msg.showinfo("不算彩蛋的彩蛋", "恭喜你发现了这个彩蛋！\n虽说这个彩蛋是有些牛马\n\n拿tkinter写计时器是真滴难受，tk属实是我见过最捞的gui了\n就写到这里吧\n我没有记录变量所以你可以重新触发这个捞的一批的彩蛋\n（顺便一提你应该发现触发彩蛋的点击次数刚好是你的所在月吧）\n\n2022.8.22\n能不能别jb开学\nBy NSX7\n我的个人博客：cavdev.github.io")
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
                        roleList = ["NSX7（RETIME By NSX7）", "精通人性的女讲师", "牛爷爷", "高级特工穿山甲", "刚偷完狗的嘎子", "刚恰完W的潘叔", "Cheems", "帮忙劈瓜的刘华强", "摘下眼镜的杰哥", "昏睡中的彬彬", "刚被篮球打完的鸡哥", "正在抽锐刻5的顶针"]
                        whoSay = roleList[rd.randint(0, len(roleList) - 1)]
                        randomTips = rd.randint(1, 20)
                        msg.showwarning(f"{ whoSay } 提醒 您", + randomTips*"时间到了")
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
            # 操你妈的python结束线程怎么这么难
            
            isEnable.set('开始计时')
            
            TimeClock.set('00 : 00 : 00')
            
    def sayForUse(event):
        msg.askyesno('说明', """不填则不倒计时，反之同样\n倒计时的值同样也会被用于定时关机\n(单位是秒数)""")
        
    def timeToShutdown(event): # 定时关机
        try: # 防止其它操作系统报错
            if isShutdowned.get() == '定时关机':
                tempTime = AlartClock.get()
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
        MainWindow.geometry('680x225')
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
        lb = Label(self.MainWindow, textvariable=TimeClock, font=('Consolas', 40), foreground='dimgray')
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
    root = Root() # 初始化函数
    sv_ttk.set_theme(themeValue)
    
    thread = threading.Thread(target=Events.staticGetTime)
    thread.setDaemon(True)
    thread.start()

    root.MainLoop()