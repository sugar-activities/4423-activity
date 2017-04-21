from ctypes import cdll

class Mouse():
	def __init__(self, supIzq, infDer):
		self.resol = (1152, 864)
		self.supIzq = supIzq
		self.infDer = infDer


	def __convertir(self, punto):
		x = punto[0]*self.resol[0]/(self.infDer[0]-self.supIzq[0]) * 1.1 - self.resol[0] * 0.1 / 2
		y = punto[1]*self.resol[1]/(self.infDer[1]-self.supIzq[1])* 1.1 - self.resol[1] * 0.1 / 2
		return (x,y)

	def setPos(self, punto):
		#nuevoPto = self.convertir(punto)
		#print nuevoPto
		#pygame.mouse.set_pos(nuevoPto)
		nuevoPto = self.__convertir(punto)
		#print nuevoPto
		dll = cdll.LoadLibrary('/usr/lib/libX11.so.6')
		d = dll.XOpenDisplay(None)
		root = dll.XDefaultRootWindow(d)
		dll.XWarpPointer(d, None, root, 0, 0, 0, 0, int(nuevoPto[0]), int(nuevoPto[1]))
		dll.XCloseDisplay(d)

