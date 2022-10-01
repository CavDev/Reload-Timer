# RETIME.tkinter
一个使用Python Tkinter开发的简单倒计时软件

![](./app.png)
![](./app-dark.png)

说真的，用tkinter来做这种软件真的很痛苦
为了避免tkinter的丑逼界面，我使用了一个挺牛逼的控件库：https://github.com/rdbende/Sun-Valley-ttk-theme :)


A Easy App to Countdown
It was developed with tkinter

Seriously, tkinter to do this kind of software is really painful
To avoid tkinter's ugly interface, I used a nice library of controls: https://github.com/rdbende/Sun-Valley-ttk-theme :)

# HELP.txt（已更新）
注意*
**RETIME 现已支持自定义设置，请使用记事本或其它文本编辑器打开程序主目录下文件 settings.ret 查看如何配置**

1、双击计时显示区（00 : 00 : 00）即可切换主题（深色和浅色）
2、点击上方显示的系统时间（精确到秒）即可查看当前年份的日历
3、倒计时要求填入的值单位是秒
4、倒计时可被填也可不填，如果填“0”或是不填则视为直接计时（无倒计时）
5、请不要在倒计时中填入字符，由于我没写异常处理，所以填入字符之后点击计时可能会出现一些BUG，点击停止计时后重新输入数字再开始计时即可恢复正常
6、你可以计时之后把原来倒计时输入的值删去，然后输入你这次计时的行动名称，便于自己查看，原来的计时会照常显示
7、定时关机的时间是你自己设定的倒计时的值，单位一样是秒，你当然可以不开始计时就定时关机
6、定时关机可被随时撤销
7、置于顶层可以让 RETIME 优先显示于你正在工作的软件上面，所以你可以边使用其它软件边工作边查看 RETIME 来管理时间
8、RETIME 窗体宽度可被改变，但高度不能，但也可以最大化，同时你可以看看只有宽度最大化的最大化是什么样（狗头）
9、请不要作死把倒计时设为1后点击定时关机，造成的数据损失本人概不负责（现在有定时关机保护机制了）

开发总结（新）
这辈子也不用python做GUI了

开发总结（旧）
暑假没有学校那些破事舒服多了
好不容易生地会考考完也该 奖励 下自己
闲的没事就做搞个GUI软件玩玩
人不在老家但这里也有台电脑，但配置不行，VS和Qt打开项目或是编译一次得花好久时间
折腾半天最后选择用Python的亲儿子GUI Tkinter来做
（Tkinter做软件是真的蛋疼啊woc）

By NSX7
2022.10.01
