#File: vizardWar.py
import viz
import vizshape
import vizcam


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
		
		self.smallShack = viz.add('models//smallShack.dae')
		m = viz.Matrix()
		m.postTrans(10, 0, 10)
		self.smallShack.setMatrix(m)
		
		self.avatar = viz.add('vcc_female.cfg')
		
		#Reads in the file to create the terrain
		inputFile = open('vizardWar.asc','r')
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
		
	def onKeyDown(self,key):
		pass
		
	def onTimer(self,num):
		pass
		
	