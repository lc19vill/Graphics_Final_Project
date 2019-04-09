#File: vizardWar.py
import viz
import vizshape
import vizcam
import math
from weapon import *


#create each individual class
class vizardWarTerrain(viz.EventClass):
	def __init__(self):
		
		# base class constructor 
		viz.EventClass.__init__(self)
		
		# set up keyboard and timer callback methods
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		self.callback(viz.MOUSEDOWN_EVENT,self.onMouseDown)
		self.callback(viz.TIMER_EVENT,self.onTimer)
		self.starttimer(1, 1/20.0, viz.FOREVER)
		
		#Create the cordinates for the main avatar
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		self.firstPerson = False
		self.forwardMovement = False
		
		self.smallShack = viz.add('models//smallShack.dae')
		m = viz.Matrix()
		m.postTrans(10, 0, 10)
		self.smallShack.setMatrix(m)
		
		self.smallShack2 = viz.add('models//smallShack.dae')
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 45)
		m.postTrans(10, 0, 30)
		self.smallShack2.setMatrix(m)
		
		self.smallShack3 = viz.add('models//smallShack.dae')
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 180)
		m.postTrans(35, 0, 15)
		self.smallShack3.setMatrix(m)
		
		self.smallShack4 = viz.add('models//smallShack.dae')
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 360)
		m.postTrans(49, 0, 22)
		self.smallShack4.setMatrix(m)
		
		self.smallShack5 = viz.add('models//smallShack.dae')
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 70)
		m.postTrans(60, 0, 45)
		self.smallShack5.setMatrix(m)
		
		self.smallShack6 = viz.add('models//smallShack.dae')
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 15)
		m.postTrans(50, 0, 60)
		self.smallShack6.setMatrix(m)
		
		self.smallShack7 = viz.add('models//smallShack.dae')
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 70)
		m.postTrans(46, 0, 50)
		self.smallShack7.setMatrix(m)
		
#		self.gun = viz.add('models//colt3//model.dae')
#		m = viz.Matrix()
#		m.postScale(.05,.05,.05)
#		m.postAxisAngle(0,0,1,270)
#		m.postTrans(.1,2,.30)
#		self.gun.setMatrix(m)

		self.gun = buildWeapon()
		
		self.avatar = viz.add('vcc_female.cfg')
		
		#Reads in the file to create the terrain
		inputFile = open('vizardWarTerrain.asc','r')
		line = inputFile.readline()
		tokens = str.split(line)
		col = int(tokens[1])
		line = inputFile.next()
		tokens = str.split(line)
		row = int(tokens[1])

		line = inputFile.next()
		line = inputFile.next()
		line = inputFile.next()
		line = inputFile.next()
		
		ter = [[0]*col]*row
		for r in range(0, row):
			line = inputFile.next()
			tokens = str.split(line)
			ter[r] = tokens

		
		viz.startLayer(viz.TRIANGLES)
		for r in range(0,row - 1):
			viz.vertexcolor(0.13,0.54,0.13)
			for c in range(0, col - 1):
				height1t1 = float(ter[r][c])
				if height1t1 > 3:
					viz.vertexcolor(0.13,0.54,0.13)
				elif height1t1 > 2:
					viz.vertexcolor(0.18,0.59,0.18)
				elif height1t1 > 0:
					viz.vertexcolor(0.23,0.64,0.23)
				else:
					viz.vertexcolor(0.28,0.69,0.28)
					
				if (c + 1) > (col):
					height2t1 = height1t1
				else:
					height2t1 = float(ter[r][c + 1])
				
				if (r + 1) > (row):
					height3t1 = height1t1
				else:
					height3t1 = float(ter[r + 1][c])
					
				viz.vertex(c, height1t1, r)
				viz.vertex(c + 1, height2t1, r)
				viz.vertex(c, height3t1, r + 1)
				
				height1t2 = float(ter[r][c + 1])
				if (c + 1) > (col):
					height2t2 = height1t2
				else:
					height2t2 = float(ter[r + 1][c + 1])
				
				if (r + 1) > (row):
					height3t2 = height1t2
				else:
					height3t2 = float(ter[r + 1][c])
				
				viz.vertex(c + 1, height1t2, r)
				viz.vertex(c + 1, height2t2, r + 1)
				viz.vertex(c, height3t2, r + 1)
		triangle = viz.endLayer()
	
	def onMouseDown(self,button):
		pass
		
	# Key pressed down event code.
	def onKeyDown(self,key):
		if (key == viz.KEY_LEFT):
			self.theta -= 2
		elif (key == viz.KEY_RIGHT):
			self.theta += 2
		elif (key == viz.KEY_UP):
			dx = 0.2*math.sin( math.radians( self.theta ) )
			dz = 0.2*math.cos( math.radians( self.theta ) )
			self.x = self.x + dx
			self.z = self.z + dz	
			self.forwardMovement = True
			
		elif (key == viz.KEY_DOWN):
			dx = 0.2*math.sin( math.radians( self.theta ) )
			dz = 0.2*math.cos( math.radians( self.theta ) )
			self.x = self.x - dx
			self.z = self.z - dz
			
		elif (key == "1"):
			view = viz.MainView
			m = viz.Matrix()
			m.postAxisAngle(1,0,0,90)
			m.postTrans(0,20,0)
			view.setMatrix(m)
			self.firstPerson = False
			
		elif (key == "2"):
			view = viz.MainView
			m = viz.Matrix()
			m.postAxisAngle(1,0,0,45)
			m.postAxisAngle(0,1,0,-90)
			m.postTrans(20,15,5)
			view.setMatrix(m)
			self.firstPerson = False
		view = viz.MainView
		
		if (key == "3"):
			dx =  0.1*math.sin( math.radians( self.theta ) )
			dz =  0.1*math.cos( math.radians( self.theta ) )
			m = viz.Matrix()
			m.postAxisAngle(0,2,0,self.theta)
			m.postTrans(self.x+dx,.8,self.z+dz)
			view.setMatrix(m)
			
			m = viz.Matrix()
			m.postScale(.05,.05,.05)
			m.postAxisAngle(0,0,1,270)
			m.postTrans(self.x+dx+.15,2,self.z+dz+.25)
			self.gun.setMatrix(m)
			
			self.firstPerson = True
			
		if self.firstPerson:
			m = viz.Matrix()
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,0,self.z);
			self.avatar.setMatrix(m)
			m.postTrans(0, 2, 0)
			view.setMatrix(m)
			m = viz.Matrix()
			m.postScale(.05,.05,.05)
			m.postAxisAngle(0,0,1,270)
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x + .15, 2, self.z + .18)
			self.gun.setMatrix(m)
			
		else:
			m = viz.Matrix()
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,0,self.z);
			self.avatar.setMatrix(m)
			m = viz.Matrix()
			m.postScale(.05,.05,.05)
			m.postAxisAngle(0,0,1,270)
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x + .1, 2, self.z + .18)
			self.gun.setMatrix(m)
			
	def setLocation(self,x,y,z):
		m = viz.Matrix()
		m.postTrans(x,y,z)
		self.avatar.setMatrix(m)
		
	def onTimer(self,num):
		if self.forwardMovement:
			m = viz.Matrix()
			m.postTrans(self.x, self.y + .1, self.z)
			self.avatar.setMatrix(m)