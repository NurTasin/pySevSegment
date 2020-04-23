from datetime import datetime
import time
from sevSeg import *
mainWin=GraphWin("DigitalClockV1.0",1100,300)
hour=(ssDisplay(mainWin,20,20),ssDisplay(mainWin,170,20))
minute=(ssDisplay(mainWin,370,20),ssDisplay(mainWin,520,20))
second=(ssDisplay(mainWin,720,20),ssDisplay(mainWin,870,20))
while mainWin.isOpen():
	properTime=str(datetime.today().time())[0:8]
	properTime=properTime.replace(':','')
	hour[0].showDig(int(properTime[0]))
	hour[1].showDig(int(properTime[1]))
	minute[0].showDig(int(properTime[2]))
	minute[1].showDig(int(properTime[3]))
	second[0].showDig(int(properTime[4]))
	second[1].showDig(int(properTime[5]))
	time.sleep(1)
	hour[0].clear()
	hour[1].clear()
	minute[0].clear()
	minute[1].clear()
	second[0].clear()
	second[1].clear()
print("quit")