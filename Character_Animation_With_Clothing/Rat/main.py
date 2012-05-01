from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import TransparencyAttrib
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import *

class MyApp(ShowBase):
 
	def __init__(self):
		ShowBase.__init__(self)

		# Turn Auto Shaders and Antialiasing
		self.render.setShaderAuto()
		self.render.setAntialias(AntialiasAttrib.MAuto)


		# Setup Bloom and Blur Filters
		self.filters = CommonFilters(base.win, base.cam)
		self.filters.setBloom(blend=(1,0,0,1), desat=-0.5, intensity=6.0, size=2)
		#self.filters.setBlurSharpen(amount=0.5)

		# Create Ambient Lighting
		alight = AmbientLight('alight')
		alight.setColor(VBase4(1, 1, 1, 1))
		alnp = render.attachNewNode(alight)
		self.render.setLight(alnp)

		# Load Model and Add it to Scene
		self.environ = self.loader.loadModel("untitled.egg")
		self.environ.reparentTo(self.render)
		self.environ.setTransparency(TransparencyAttrib.MAlpha)

app = MyApp()
app.run()


