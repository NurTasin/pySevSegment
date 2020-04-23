"""
Change_Log:
Only updates the segment which value is changed.
For this the animation has been smoother than before (V1.0)
"""
from datetime import datetime
import time
from sevSeg import *
properTime=str(datetime.today().time())[0:8]
properTime=properTime.replace(':','')
previousHour=properTime[0]+properTime[1]
previousMinute=properTime[2]+properTime[3]
previousSecond=properTime[4]+properTime[5]
mainWin=GraphWin("DigitalClockV2.0",1100,300)
hour=(ssDisplay(mainWin,20,20),ssDisplay(mainWin,170,20))
minute=(ssDisplay(mainWin,370,20),ssDisplay(mainWin,520,20))
second=(ssDisplay(mainWin,720,20),ssDisplay(mainWin,870,20))
hour[0].showDig(previousHour[0])
hour[1].showDig(previousHour[1])
minute[0].showDig(previousMinute[0])
minute[1].showDig(previousMinute[1])
second[0].showDig(previousSecond[0])
second[1].showDig(previousSecond[1])
while mainWin.isOpen():
	properTime=str(datetime.today().time())[0:8]
	properTime=properTime.replace(':','')
	presentHour=properTime[0]+properTime[1]
	presentMinute=properTime[2]+properTime[3]
	presentSecond=properTime[4]+properTime[5]
	if presentHour[0]!=previousHour[0]:
		hour[0].clear()
		hour[0].showDig(presentHour[0])
	if presentHour[1]!=previousHour[1]:
		hour[1].clear()
		hour[1].showDig(presentHour[1])
	if presentMinute[0]!=previousMinute[0]:
		minute[0].clear()
		minute[0].showDig(presentMinute[0])
	if presentMinute[1]!=previousMinute[1]:
		minute[1].clear()
		minute[1].showDig(presentMinute[1])
	if presentSecond[0]!=previousSecond[0]:
		second[0].clear()
		second[0].showDig(presentSecond[0])
	if presentSecond[1]!=previousSecond[1]:
		second[1].clear()
		second[1].showDig(presentSecond[1])
	previousSecond=presentSecond
	previousHour=presentHour
	previousMinute=presentMinute
print("Closed digitalClock2.0")