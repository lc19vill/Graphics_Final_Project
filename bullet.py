#File: bullet.py
import viz
import vizshape
import vizcam
import math

class bullet(viz.EventClass):
	def __init__(self, x, y ,z ,theta):
		
		viz.EventClass.__init__(self)
		self.callback(viz.TIMER_EVENT,self.onTimerBullet)
		self.starttimer(1, 1/20.0, viz.FOREVER)
		
		self.bullet = viz.add('models//bullet//model.dae')
		self.bullet.setMatrix(m)
		
		self.x = x
		self.y = y
		self.z = z
		self.theta = theta
		
#		self.setXYZ(x,y,z)
#		self.setTheta(theta)
		
	def setXYZ(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		m = viz.Matrix()
		m.postTrans(self.x,self.y,self.z)
		self.bullet.setMatrix(m)

	def setTheta(self, theta):
		self.theta = theta
		
	def getBulletX(self):
		return self.bulletX
		
	def getBulletY(self):
		return self.bulletY
		
	def getBulletZ(self):
		return self.bulletZ
		
	def onTimerBullet(self, num):
		newX = self.getBulletX() + math.sin( math.radians (self.bulletTheta))
		newZ = self.getBulletZ() + math.cos( math.radians (self.bulletTheta))
		self.setXY(newX, self.gety(), newZ)