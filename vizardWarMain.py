#File: vizardWarMain.py
import viz
import vizcam
from vizardWar import *

#create the window and set the color
window = viz.MainWindow
viz.window.setSize( 640, 480 )
viz.window.setName( "Vizard War" )
window.clearcolor(0,0,0)
viz.MainView.eyeheight(0)

pivotNav = vizcam.PivotNavigate()

t = vizardWarTerrain()

viz.go()
