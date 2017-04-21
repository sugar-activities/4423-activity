from gettext import gettext as _

import sys
sys.path.insert(0, "lib")

import gtk

from sugar.graphics.toolbutton import ToolButton
from sugar.activity import activity
import sugargame.canvas

import logging
import time
import Procesador

class hMouse(activity.Activity):
	def __init__(self, handle):
		activity.Activity.__init__(self, handle)

		self.mCamara = False #si se esta mostrando la camara
		self.pAyuda = 1 #paso de la ayuda

		self._logger = logging.getLogger('hMouse-activity')

		toolbox = activity.ActivityToolbox(self)

		#activity toolbar
		self.activity_tb = toolbox.get_activity_toolbar()
		self.activity_tb.keep.props.visible = False
		self.activity_tb.share.props.visible = False

		#########toolbar hMouse############
		self.hMouseTB = gtk.Toolbar()

		TI = gtk.ToolItem()
		#etiqueta estado
		self.estado = gtk.Label(_("Presione Iniciar!"))
		self.estado.set_width_chars(40)
		
		TI.add(self.estado)
		self.estado.show()

		self.hMouseTB.insert(TI, -1)
		TI.show()
		

		#boton calibrar ArrIzq-AbjDer
		self.calibrar0_bt = ToolButton('calibrar0')
		self.calibrar0_bt.set_tooltip(_('Calibrar ArrIzq-AbjDer'))
		self.hMouseTB.insert(self.calibrar0_bt, -1)
		self.calibrar0_bt.connect('clicked', self.calibrar0)
		self.calibrar0_bt.show()


		#boton calibrar Izq-Der-Arr-Abj
		self.calibrar1_bt = ToolButton('calibrar1')
		self.calibrar1_bt.set_tooltip(_('Calibrar 1'))
		self.hMouseTB.insert(self.calibrar1_bt, -1)
		self.calibrar1_bt.connect('clicked', self.calibrar1)
		self.calibrar1_bt.show()


		#boton calibrar Centro
		self.calibrar2_bt = ToolButton('calibrar2')
		self.calibrar2_bt.set_tooltip(_('Calibrar 2'))
		self.hMouseTB.insert(self.calibrar2_bt, -1)
		self.calibrar2_bt.connect('clicked', self.calibrar2)
		self.calibrar2_bt.show()

		#boton iniciar
		self.iniciar_bt = ToolButton('iniciar')
		self.iniciar_bt.set_tooltip(_('Iniciar'))
		self.hMouseTB.insert(self.iniciar_bt, -1)
		self.iniciar_bt.connect('clicked', self.start)
		self.iniciar_bt.show()

		#boton camara
		self.camara_bt = ToolButton('camara')
		self.camara_bt.set_tooltip(_('Ver camara'))
		self.hMouseTB.insert(self.camara_bt, -1)
		self.camara_bt.connect('clicked', self.camara)
		self.camara_bt.show()

		#boton ayuda
		self.ayuda_bt = ToolButton('ayuda')
		self.ayuda_bt.set_tooltip(_('Ayuda'))
		self.hMouseTB.insert(self.ayuda_bt, -1)
		self.ayuda_bt.connect('clicked', self.ayuda)
		self.ayuda_bt.show()

		#boton acerca
		self.acerca_bt = ToolButton('acerca')
		self.acerca_bt.set_tooltip(_('Acerca de...'))
		self.hMouseTB.insert(self.acerca_bt, -1)
		self.acerca_bt.connect('clicked', self.acerca)
		self.acerca_bt.show()

		##############toolbar velocidad################
		self.velTB = gtk.Toolbar()
		
		#boton 1hz
		self.uno_bt = ToolButton('1hz')
		self.uno_bt.set_tooltip(_('Velocidad 1'))
		self.velTB.insert(self.uno_bt, -1)
		self.uno_bt.connect('clicked', self.uno)
		self.uno_bt.show()
		
		#boton 2hz
		self.dos_bt = ToolButton('2hz')
		self.dos_bt.set_tooltip(_('Velocidad 2'))
		self.velTB.insert(self.dos_bt, -1)
		self.dos_bt.connect('clicked', self.dos)
		self.dos_bt.show()
		
		#boton 3hz
		self.tres_bt = ToolButton('3hz')
		self.tres_bt.set_tooltip(_('Velocidad 3'))
		self.velTB.insert(self.tres_bt, -1)
		self.tres_bt.connect('clicked', self.tres)
		self.tres_bt.show()
		
		#boton 4hz
		self.cuatro_bt = ToolButton('4hz')
		self.cuatro_bt.set_tooltip(_('Velocidad 4'))
		self.velTB.insert(self.cuatro_bt, -1)
		self.cuatro_bt.connect('clicked', self.cuatro)
		self.cuatro_bt.show()


		#toolbox
		toolbox.add_toolbar(_("hMouse"), self.hMouseTB)
		toolbox.show_all()

		#toolbox
		toolbox.add_toolbar(_("Velocidad"), self.velTB)
		toolbox.show_all()
		
		toolbox.set_current_toolbar(1)
		self.set_toolbox(toolbox)
		toolbox.show()

		#canvas
		self.canv = sugargame.canvas.PygameCanvas(self)
		self.set_canvas(self.canv)

		self.proc = Procesador.Procesador(self.estado)
		time.sleep(2)
		self.canv.run_pygame(self.proc.iniciar)	


	def start(self, boton):
		self.proc.cont = not self.proc.cont
		if self.proc.cont:
			#self.iniciar_bt.set_icon("detener")
			self.iniciar_bt.set_tooltip(_('Detener'))
			self.proc.funcionando()
		else:
			self.iniciar_bt.set_icon("iniciar")
			self.iniciar_bt.set_tooltip(_('Iniciar'))


	def sensibilidad(self, boton, dx, dy):
		self.proc.calibrar2SetSensib(dx, dy)

	def calibrar0(self, boton):
		self.proc.iniciarCalibrado(0)

	def calibrar1(self, boton):
		self.proc.iniciarCalibrado(1)

	def calibrar2(self, boton):
		self.proc.iniciarCalibrado(2)

	def camara(self, boton):
		self.mCamara = not self.mCamara
		if self.mCamara:
			self.proc.mostrarVideo((0,0))
			i=0
			while self.mCamara:
				i+=1
				if i > 60:
					self.proc.updGTK()
					i=0
		else:
			self.proc.dejarDeMostrar()

	def ayuda(self, boton):
		self.ayuda_bt.set_tooltip(_('Siguiente'))
		self.ayuda_bt.set_icon('siguiente')

		self.proc.updFondo()
		self.proc.tutorial(3, self.pAyuda)
		self.pAyuda +=1
		if self.pAyuda >4:
			self.pAyuda = 1
			self.ayuda_bt.set_tooltip(_('Ayuda'))
			self.ayuda_bt.set_icon('ayuda')
			self.proc.updFondo()


	def acerca(self, boton):
		self.proc.updFondo()
		self.proc.tutorial(4, 1)

	def uno (self, boton):
		self.proc.setVel(1)

	def dos (self, boton):
		self.proc.setVel(2)

	def tres (self, boton):
		self.proc.setVel(3)

	def cuatro (self, boton):
		self.proc.setVel(4)

if __name__=='__main__':
	sys.path.insert(0, "lib")
	from Procesador import Procesador
	estado = gtk.Label("Presione Iniciar!")
	procesador = Procesador(estado)
	procesador.iniciar()
	procesador.iniciarCalibrado(0)
