#File: weapon.py
import viz
import vizshape
import vizcam
import math
from bullet import *

class buildWeapon(viz.EventClass):
	def __init__(self):
		
		viz.EventClass.__init__(self)
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		
		self.pistol = viz.add('models//colt3//model.dae')
		m = viz.Matrix()
		m.postScale(.05,.05,.05)
		m.postAxisAngle(0,0,1,270)
		m.postTrans(.1,1.5,.30)
		self.pistol.setMatrix(m)
		
		self.x = 0
		self.y = 0
		self.z = 0
		self.theta = 0
		
		self.bulletList = []
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getZ(self):
		return self.z
		
	def getTheta(self):
		return self.theta
		
	def setXYZ(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		m = viz.Matrix()
		m.postTrans(self.x,self.y,self.z)
		self.pistol.setMatrix(m)

	def setTheta(self, theta):
		self.theta = theta
		
	def setScale(self,amount):
		m = viz.Matrix()
		m.postScale(amount,amount,amount)
		self.pistol.setMatrix(m)
		
	def rotateOnX(self,theta):
		m = viz.Matrix()
		m.postAxisAngle(1,0,0,theta)
		self.pistol.setMatrix(m)
		
	def rotateOnY(self,theta):
		m = viz.Matrix()
		m.postAxisAngle(0,1,0,theta)
		self.pistol.setMatrix(m)
		
	def rotateOnZ(self,theta):
		m = viz.Matrix()
		m.postAxisAngle(0,0,1,theta)
		self.pistol.setMatrix(m)
		
	def onKeyDown(self, key): 
		if key == " ":
			self.bulletList.append(bullet(self.getX(), self.getY(), self.getZ(), self.getTheta()))