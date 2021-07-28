#这个程序主要是控制树莓派所连接的led灯

import tkinter as tk
import  RPi.GPIO as GPIO

chanel = int(input("chanel? "))#输入第一个led灯的GPIO口(BOARD),乱输可能会使你的树莓派变成一张信用卡大小的废物
chanel2 = int(input("chanel2? "))#输入第二个led灯的GPIO口(BOARD),乱输可能会使你的树莓派变成一张信用卡大小的废物
window = tk.Tk()
window.geometry("600x600")
window.title("RaspberryPi LED Manager")

l = tk.Label(window,text="RaspberryPi LED program",bg="green",width=200,height=2)
l.pack()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(chanel, GPIO.OUT)#设置第chanel号为输出
GPIO.setup(chanel2, GPIO.OUT)#设置第chanel2号为输出

pwm = GPIO.PWM(chanel,100)#实例化对象pwm
pwm.start(0)#点灯，亮度为0
pwm2 = GPIO.PWM(chanel2,100)
pwm2.start(0)

l2 = tk.Label(window,text="",bg="yellow")
l2_2 = tk.Label(window,text="",bg="yellow")
def LEDON():#开灯(chanel)，亮度设置到100
    pwm.ChangeDutyCycle(100)
def LEDOFF():
    pwm.ChangeDutyCycle(0)#关灯(chanel)，亮度设置到0
def PWMLED(dc):#调节亮度(chanel)
    l2.config(text="(chanel) You have setted " + str(dc))
    dc = int(dc)
    pwm.ChangeDutyCycle(dc)

def LED2ON():#开灯(chanel2)，亮度设置到100
    pwm2.ChangeDutyCycle(100)
def LED2OFF():#关灯(chanel2)，亮度设置到0
    pwm2.ChangeDutyCycle(0)
def PWM2LED(dc):#调节亮度(chanel2)
    l2_2.config(text="(chanel2) You have setted " + str(dc))
    dc = int(dc)
    pwm2.ChangeDutyCycle(dc)


def STOPPWM():#清理所有GPIO口(在退出时运行，执行后所有操作将无效)
    GPIO.cleanup()

b1 = tk.Button(window,text="LED ON (chanel1)",bg="yellow",command=LEDON)#生成一个控制chanel的按钮
b1.pack()
b2 = tk.Button(window,text="LED OFF (chanel1)",bg="grey",command=LEDOFF)
b2.pack()

b1_2 = tk.Button(window,text="LED ON (chanel2)",bg="yellow",command=LED2ON)#生成一个控制chanel2的按钮
b1_2.pack()
b2_2 = tk.Button(window,text="LED OFF (chanel2)",bg="grey",command=LED2OFF)
b2_2.pack()


l2.pack()

l2_2.pack()

scale = tk.Scale(window,label="Pull Me (chanel1)",from_=0,to=100,orient=tk.HORIZONTAL,length=1000,showvalue=0,tickinterval=20,resolution=1,command=PWMLED)#生成一个控制chanel的条
scale.pack()
scale = tk.Scale(window,label="Pull Me (chanel2)",from_=0,to=100,orient=tk.HORIZONTAL,length=1000,showvalue=0,tickinterval=20,resolution=1,command=PWM2LED)#生成一个控制chanel2的条
scale.pack()

# b4 = tk.Button(window,text="start",command=STARTPWM)
b3 = tk.Button(window,text="stop",command=STOPPWM)#释放GPIO口
b3.pack()
# b4.pack()
window.mainloop()


# 我相信一定没有人会看到这个程序，注释写得很烂，见谅