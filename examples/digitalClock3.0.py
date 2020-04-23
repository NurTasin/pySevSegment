"""
Change_Log:
used self.switchDig() methode instead of self.showDig()
for that reason the animation has been smoothest. (Comapared to Ver1.0 or Ver2.0).
"""
from datetime import datetime
import time
from sevSeg import *
properTime=str(datetime.today().time())[0:8]
properTime=properTime.replace(':','')
previousHour=properTime[0]+properTime[1]
previousMinute=properTime[2]+properTime[3]
previousSecond=properTime[4]+properTime[5]
mainWin=GraphWin("DigitalClockV3.0 by NurTasin",1100,300)
dots1=Circle(Point(330,100), 10)
dots1.setFill(color_rgb(255,00,00))
dots1.draw(mainWin)
dots2=Circle(Point(330,200), 10)
dots2.setFill(color_rgb(255,00,00))
dots2.draw(mainWin)
dots3=Circle(Point(680,100), 10)
dots3.setFill(color_rgb(255,00,00))
dots3.draw(mainWin)
dots4=Circle(Point(680,200), 10)
dots4.setFill(color_rgb(255,00,00))
dots4.draw(mainWin)
hour=(ssDisplay(mainWin,20,20),ssDisplay(mainWin,170,20))
minute=(ssDisplay(mainWin,370,20),ssDisplay(mainWin,520,20))
second=(ssDisplay(mainWin,720,20),ssDisplay(mainWin,870,20))
hour[0].showDig(previousHour[0])
hour[1].showDig(previousHour[1])
minute[0].showDig(previousMinute[0])
minute[1].showDig(previousMinute[1])
second[0].showDig(previousSecond[0])
second[1].showDig(previousSecond[1])
i=1
while mainWin.isOpen():
	properTime=str(datetime.today().time())[0:8]
	properTime=properTime.replace(':','')
	presentHour=properTime[0]+properTime[1]
	presentMinute=properTime[2]+properTime[3]
	presentSecond=properTime[4]+properTime[5]
	if i==1:
		dots1.setFill(color_rgb(255,0,0))
		dots2.setFill(color_rgb(255,0,0))
		dots3.setFill(color_rgb(255,0,0))
		dots4.setFill(color_rgb(255,0,0))
		i=2
	elif i==2:
		dots1.setFill(color_rgb(255,255,255))
		dots2.setFill(color_rgb(255,255,255))
		dots3.setFill(color_rgb(255,255,255))
		dots4.setFill(color_rgb(255,255,255))
		i=1
	if presentHour[0]!=previousHour[0]:
		hour[0].switchDig(presentHour[0])
	if presentHour[1]!=previousHour[1]:
		hour[1].switchDig(presentHour[1])
	if presentMinute[0]!=previousMinute[0]:
		minute[0].switchDig(presentMinute[0])
	if presentMinute[1]!=previousMinute[1]:
		minute[1].switchDig(presentMinute[1])
	if presentSecond[0]!=previousSecond[0]:
		second[0].switchDig(presentSecond[0])
	if presentSecond[1]!=previousSecond[1]:
		second[1].switchDig(presentSecond[1])
	time.sleep(1)
	previousSecond=presentSecond
	previousHour=presentHour
	previousMinute=presentMinute
print("Closed digitalClock3.0")