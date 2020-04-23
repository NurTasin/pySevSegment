from graphics import *
import time
A=0x001
B=0x002
C=0x003
D=0x004
E=0x005
F=0x006
G=0x007
DP=0x008
dictionary={
	0:[A,B,C,D,E,F],
	1:[B,C],
	2:[A,B,G,E,D],
	3:[A,B,G,C,D],
	4:[F,G,B,C],
	5:[A,F,G,C,D],
	6:[A,F,G,C,D,E],
	7:[A,B,C],
	8:[A,B,C,D,E,F,G],
	9:[G,F,A,B,C,D]
}
switchMan={
#basic format preDig:{0:[energize],[deenergize]}
	0:{
		0:[[],[]],
		1:[[],[A,D,E,F,G]],
		2:[[G],[F,C]],
		3:[[G],[E,F]],
		4:[[G],[A,E,D]],
		5:[[G],[B,E]],
		6:[[G],[B]],
		7:[[],[F,E,D]],
		8:[[G],[]],
		9:[[G],[E]]
	},
	1:{
		0:[[A,F,G,E,D],[]],
		1:[[],[]],
		2:[[A,G,E,D],[C]],
		3:[[A,G,D],[]],
		4:[[F,G],[]],
		5:[[A,F,G,D],[B]],
		6:[[A,F,G,D,E],[B]],
		7:[[A],[]],
		8:[[A,F,G,D,E],[]],
		9:[[A,F,G,D],[]]
	},
	2:{
		0:[[F,C],[G]],
		1:[[C],[A,G,E,D]],
		2:[[],[]],
		3:[[C],[E]],
		4:[[F,C],[A,E,D]],
		5:[[F,C],[B,E]],
		6:[[F,C],[B]],
		7:[[C],[G,E,D]],
		8:[[F,C],[]],
		9:[[F,C],[E]]
	},
	3:{
		0:[[F,E],[G]],
		1:[[],[A,G,D]],
		2:[[E],[C]],
		3:[[],[]],
		4:[[F],[A,D]],
		5:[[F],[B]],
		6:[[F,E],[B]],
		7:[[],[G,D]],
		8:[[F,E],[]],
		9:[[F],[]]
	},
	4:{
		0:[[A,E,D],[G]],
		1:[[],[F,G]],
		2:[[A,D,E],[F,C]],
		3:[[A,D],[F]],
		4:[[],[]],
		5:[[A,D],[B]],
		6:[[A,E,D],[B]],
		7:[[A],[F,G]],
		8:[[A,E,D],[]],
		9:[[A,D],[]]
	},
	5:{
		0:[[B,E],[G]],
		1:[[B],[A,F,G,D]],
		2:[[B,E],[F,C]],
		3:[[B],[F]],
		4:[[B],[A,D]],
		5:[[],[]],
		6:[[E],[]],
		7:[[B],[F,G,D]],
		8:[[B,E],[]],
		9:[[B],[]]
	},
	6:{
		0:[[B],[G]],
		1:[[B],[A,F,G,E,D]],
		2:[[B],[F,C]],
		3:[[B],[F,E]],
		4:[[B],[A,E,D]],
		5:[[],[E]],
		6:[[],[]],
		7:[[B],[F,G,E,D]],
		8:[[B],[]],
		9:[[B],[E]]
	},
	7:{
		0:[[F,E,D],[]],
		1:[[],[A]],
		2:[[G,E,D],[C]],
		3:[[G,D],[]],
		4:[[F,G],[A]],
		5:[[F,G,D],[B]],
		6:[[F,G,E,D],[B]],
		7:[[],[]],
		8:[[F,G,E,D],[]],
		9:[[F,G,E,D],[E]]
	},
	8:{
		0:[[],[G]],
		1:[[],[A,D,E,F,G]],
		2:[[],[F,C]],
		3:[[],[F,E]],
		4:[[],[A,E,D]],
		5:[[],[B,E]],
		6:[[],[B]],
		7:[[],[F,G,E,D]],
		8:[[],[]],
		9:[[],[E]]
	},
	9:{
		0:[[E],[G]],
		1:[[],[A,F,G,D]],
		2:[[E],[F,C]],
		3:[[],[F]],
		4:[[],[A,D]],
		5:[[],[B]],
		6:[[E],[B]],
		7:[[],[F,G,D]],
		8:[[E],[]],
		9:[[],[]]
	}
}
def uncommon(a,b):
	inter=[]
	for i in a:
		if i not in b:
			inter.append(i)
	return inter

def common(a,b):
	inter=[]
	for i in a :
		if i in b:
			inter.append(i)
	return inter
class ssDisplay:
	def __init__(self,window,x,y):
		self.window=window
		self.cordinate=(x,y)
		#Drawing the blank segments
		self.a=Rectangle(Point(x+20,y+20), Point(x+110,y+30))
		self.a.setFill(color_rgb(255,255,255))
		self.b=Rectangle(Point(x+120,y+20), Point(x+130,y+120))
		self.b.setFill(color_rgb(255,255,255))
		self.c=Rectangle(Point(x+120,y+130),Point(x+130,y+230))
		self.c.setFill(color_rgb(255,255,255))
		self.d=Rectangle(Point(x+20,y+220), Point(x+110,y+230))
		self.d.setFill(color_rgb(255,255,255))
		self.f=Rectangle(Point(x,y+20),Point(x+10,y+120))
		self.f.setFill(color_rgb(255,255,255))
		self.g=Rectangle(Point(x+20,y+120), Point(x+110,y+130))
		self.g.setFill(color_rgb(255,255,255))
		self.e=Rectangle(Point(x,y+130), Point(x+10,y+230))
		self.e.setFill(color_rgb(255,255,255))
		self.dp=Circle(Point(x+140,y+220), 5)
		self.dp.setFill(color_rgb(255,255,255))
		self.a.draw(self.window)
		self.b.draw(self.window)
		self.c.draw(self.window)
		self.d.draw(self.window)
		self.f.draw(self.window)
		self.g.draw(self.window)
		self.e.draw(self.window)
		self.dp.draw(self.window)
		self.isDpEnergized=False
		self.previousNum=None
	def energize(self,*arg):
		if A in arg:
			self.a.setFill(color_rgb(255,0,0))
		if B in arg:
			self.b.setFill(color_rgb(255,0,0))
		if C in arg:
			self.c.setFill(color_rgb(255,0,0))
		if D in arg:
			self.d.setFill(color_rgb(255,0,0))
		if E in arg:
			self.e.setFill(color_rgb(255,0,0))
		if F in arg:
			self.f.setFill(color_rgb(255,0,0))
		if G in arg:
			self.g.setFill(color_rgb(255,0,0))
		if DP in arg:
			self.dp.setFill(color_rgb(255,0,0))
		if self.isDpEnergized:
			self.dp.setFill(color_rgb(255,0,0))

	def enableDP(self):
		self.isDpEnergized=True
	def disableDP(self):
		self.isDpEnergized=False
	def showDig(self,number):
		number=int(number)
		if number>9 and number<0:
			raise ValueError("Can't display a number which is less than 0 or grater than 9")
		else:
			if number==0:
				self.energize(A,B,C,D,E,F)
			elif number==1:
				self.energize(B,C)
			elif number==2:
				self.energize(A,B,G,E,D)
			elif number==3:
				self.energize(A,B,G,C,D)
			elif number==4:
				self.energize(F,G,B,C)
			elif number==5:
				self.energize(A,F,G,C,D)
			elif number==6:
				self.energize(A,F,G,C,D,E)
			elif number==7:
				self.energize(A,B,C)
			elif number==8:
				self.energize(A,B,C,D,E,F,G)
			elif number==9:
				self.energize(A,F,G,B,C,D)
		self.previousNum=number
	def clear(self):
		self.a.setFill(color_rgb(255,255,255))
		self.b.setFill(color_rgb(255,255,255))
		self.c.setFill(color_rgb(255,255,255))
		self.d.setFill(color_rgb(255,255,255))
		self.e.setFill(color_rgb(255,255,255))
		self.f.setFill(color_rgb(255,255,255))
		self.g.setFill(color_rgb(255,255,255))
		self.dp.setFill(color_rgb(255,255,255))
	def showNum(self,number,delay):
		if type(number)==type(""):
			raise ValueError("An integer is required!")
		number=str(number)
		for i in range(len(number)):
			self.showDig(int(number[i]))
			time.sleep(delay)
			self.clear()
	def deenergize(self,*arg):
		if A in arg:
			self.a.setFill(color_rgb(255,255,255))
		if B in arg:
			self.b.setFill(color_rgb(255,255,255))
		if C in arg:
			self.c.setFill(color_rgb(255,255,255))
		if D in arg:
			self.d.setFill(color_rgb(255,255,255))
		if E in arg:
			self.e.setFill(color_rgb(255,255,255))
		if F in arg:
			self.f.setFill(color_rgb(255,255,255))
		if G in arg:
			self.g.setFill(color_rgb(255,255,255))

	def switchDig(self,new):
		for i in switchMan[self.previousNum][int(new)][0]:
			self.energize(i)
		for i in switchMan[self.previousNum][int(new)][1]:
			self.deenergize(i)
		self.previousNum=int(new)
		
if __name__=='__main__':
	win=GraphWin("Test",500,300)
	i=ssDisplay(win, 50, 50)
	j=ssDisplay(win, 220, 50)
	j.showDig(0)
	for i in range(10):
		time.sleep(1)
		j.switchDig(i)