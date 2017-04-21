import time

from Camara import Camara
import Mouse
from gettext import gettext as _
import gtk
import numpy
import pygame
import pygame.display
import pygame.draw
import pygame.event
from pygame.locals import *
import threading


class Procesador():
	def __init__(self, estado):
		#estado es una etiqueta de gtk
		self.puntosSuav = []
		self.puntosFoto = []
		
		self.estado = estado
		

		self.dx = 50
		self.dy = 50

		self.muestro = False
		self.color = 220 #solo la luminancia!

		self.cont = False

		self.smooth = 7

		#2.5hz
		#self.b =(3.00434403052718e-005, 0.000210304082136903, 0.000630912246410709, 0.00105152041068451, 0.00105152041068451, 0.000630912246410709, 0.000210304082136903, 3.00434403052718e-005)
		#self.a =(-4.65052274821162, 9.5509242910573, -11.1601445267082, 7.98218512356193, -3.48494150611555, 0.858128505362491, -0.0917835785872751)

		#5 3hz
		self.b = [0.0180989330075144, 0.0542967990225433, 0.0542967990225433, 0.0180989330075144]
		self.a = [-1.76004188034317, 1.18289326203783, -0.278059917634546]
		
	def iniciar(self):
		"""Hace todas las importaciones y pinta la pantalla de blanco"""

		pygame.display.init()

		self.cam = Camara()
		self.supIzq = (0, 0)
		self.infDer = self.cam.tam

		self.updFondo()
		self.cam.iniciar()

	def updGTK(self):
		while gtk.events_pending():
			gtk.main_iteration()

	def updFondo(self):
		#pinto todo de blanco
		self.display = pygame.display.set_mode()
		surf = pygame.display.get_surface()
		surf.fill((255, 255, 255))
		#cargo el logo de teleton
		teleton = pygame.image.load("activity/teleton.gif")
		surf.blit(teleton, (790, 460))
		pygame.display.flip()

	def tutorial(self, id, p):
		"""Muestra el paso p del tutorial de id id
		id=0 -> Calibrar0 | id=1 -> Calibrar1 | id=2 -> Calibrar2 | id3-> General | id4-> About
		"""
		surf = pygame.display.get_surface()
		if id == 3:
			if p == 1:
				img = pygame.image.load("help/camara.png")
			elif p == 2:
				img = pygame.image.load("help/calibrar.png")
			elif p == 3:
				img = pygame.image.load("help/iniciar.png")
		elif id == 4:
			if p == 1:
				img = pygame.image.load("help/about.png")


		surf.blit(img, (5, 20))
		pygame.display.flip()


		
	############################################################################################
	#######################MUESTRO VIDEO EN PANTALLA############################################
	############################################################################################		
		
		
	def mostrarVideo(self, pos, robo=False, cruz=(-1, -1)):
		"""Muestra lo que esta recibiendo la camara en la posicion pos.
		Si robo es True, roba la imagen de lo que se esta procesando, si es False, saca fotos por si solo"""
		self.thrVideo = threading.Thread(target=self.__video, args=(pos, robo, cruz))
		self.mostrando = True
		self.thrVideo.start()
		
		
	def __video(self, pos, robo, cruz):
		while self.mostrando:
			if robo:
				surf = self.cam.image
			else:
				surf = self.cam.fotoXO()

			if cruz != (-1, -1):
				pygame.draw.rect(surf, 50, (cruz[0], cruz[1], 2, 2), 15)

			self.display.blit(surf, pos)
			#pygame.display.update((pos[0], pos[1], self.cam.tam[0]-pos[0],self.cam.tam[1]-pos[1]))
			pygame.display.flip()
			


		
	def dejarDeMostrar(self):
		"""Detiene la reproduccion de video"""
		self.mostrando = False
		del self.thrVideo



	############################################################################################
	#######################FUNCIONES PARA SUAVIZADO DEL PUNTO###################################
	############################################################################################
	def setSmooth(self, valor):
		self.smooth = valor

	def __agregarPunto(self, punto, buffer):
		"""buffer es una lista"""
		if punto != (-1, -1):
			buffer.insert(0, punto)
		else:
			#si no es un punto no visto
			buffer.insert(0, buffer[0])

		#remuevo el ultimo
		if len(buffer) > self.smooth:
			buffer.remove(buffer[len(buffer)-1])
		#print punto
		#print self.puntos

	def __getPuntoSuav0(self):
		"""Calcula el punto suavizado con promedio comun y lo devuelve"""
		suma = reduce(lambda x, y: (x[0] + y[0], y[1] + x[1]), self.puntos)
		return (suma[0] / len(self.puntos), (suma[1] / len(self.puntos)))

	def setVel(self, vel):
		if vel==1:
			#1hz
			self.b = (8.84051895022608e-008, 6.18836326515826e-007, 1.85650897954748e-006, 3.09418163257913e-006, 3.09418163257913e-006, 1.85650897954748e-006, 6.18836326515826e-007, 8.84051895022608e-008)
			self.a = (-6.05902795876839, 15.7895452743402, -22.9350937191999, 20.0506792924615, -10.5481378415148, 3.09133558602081, -0.389289317475187)
		elif vel==2:
			#2hz
			self.b = (7.57990411578979e-006, 5.30593288105286e-005, 0.000159177986431586, 0.000265296644052643, 0.000265296644052643, 0.000159177986431586, 5.30593288105286e-005, 7.57990411578979e-006)
			self.a = (-5.11943838550082, 11.4269078178929, -14.37764320968, 10.9927741508905, -5.09989077245218, 1.32777543054669, -0.149514803970293)
		elif vel==3:
			#3hz
			self.b = (9.03489625198178e-005, 0.000632442737638725, 0.00189732821291617, 0.00316221368819362, 0.00316221368819362, 0.00189732821291617, 0.000632442737638725, 9.03489625198178e-005)
			self.a = (-4.18233008932062, 7.87171920221281, -8.53094212929846, 5.70994480788949, -2.34924722805244, 0.548264774778682, -0.0558446710069275)
		elif vel==4:
			#4hz
			self.b = (0.000489912553213789, 0.00342938787249653, 0.0102881636174896, 0.0171469393624826, 0.0171469393624826, 0.0102881636174896, 0.00342938787249653, 0.000489912553213789)
			self.a = (-3.24831900842921, 5.08417214957582, -4.72383271597112, 2.77362001111002, -1.01754042816489, 0.214564545649469, -0.0199557469587319)





	def __getPuntoSuav1(self):
		
		bb = [0, 0]
		aa = [0, 0]

		for i in xrange(int(self.smooth / 2) + 1):
			"""fotografiados"""
			bb[0] += self.b[i] * self.puntosFoto[i][0]
			bb[1] += self.b[i] * self.puntosFoto[i][1]



		for i in xrange(int(self.smooth / 2)):
			"""suavizados"""
			aa[0] += self.a[i] * self.puntosSuav[i][0]
			aa[1] += self.a[i] * self.puntosSuav[i][1]

		x = bb[0]-aa[0]
		y = bb[1]-aa[1]
		
		return (x, y)


	############################################################################################
	#############################ANALIZO LA IMAGEN##########################################
	############################################################################################

	#Analizo la imagen
	def analizar(self):
		"""Captura una imagen y devuelve el centro del circulo
		En self.terminado deja la imagen en blanco y negro
		Devuelve una tupla de la siguiente forma:
		(x centro, y centro)
		todo es True si analizo toda la imagen o False si solo lo calibrado
		"""
		image = self.cam.fotoXO()
		Arr3D = pygame.surfarray.pixels3d(image)

		blancos = numpy.nonzero(Arr3D[self.supIzq[0]:self.infDer[0], self.supIzq[1]:self.infDer[1], 0] >= self.color) #analizo solo la luminancia


		prom = numpy.mean(blancos, axis=1)

		if not numpy.isnan(prom[0]):
			return (prom[0], prom[1])
		else:
			return (-1, -1)



	############################################################################################
	#############################CALIBRACION DEL MOUSE##########################################
	############################################################################################
	def __calibrar0(self, paso):
		"""Calibracion modo ArrIzq-AbjDer"""
		if paso == 0:
			self.mostrarVideo((0, 0))
			self.estado.set_text(_("Mueva la cabeza arriba a la izquierda"))			
		elif paso == 1:
			time.sleep(3)
			self.dejarDeMostrar()
			centro = self.analizar()
			self.cam.detener()
			self.supIzq = (int(centro[0]), int(centro[1]))
			self.estado.set_text(_("Mueva la cabeza abajo a la derecha"))
		elif paso == 2:
			self.cam.iniciar()
			self.mostrarVideo((self.cam.tam[0], 0))					
		elif paso == 3:
			time.sleep(3)
			self.dejarDeMostrar()
			centro = self.analizar()
			self.infDer = (int(centro[0]) + self.supIzq[0], int(centro[1]) + self.supIzq[1])

	def __calibrar1(self, paso):
		"""Calibracion modo Izq-Der-Arr-Abj"""
		if paso == 0:
			self.mostrarVideo((0, 0))
			self.estado.set_text(_("Mueva la cabeza a la izquierda"))					
		elif paso == 1:
			time.sleep(3)
			self.dejarDeMostrar()
			centro = self.analizar()
			self.cam.detener()
			self.izq = int(centro[0])
			self.estado.set_text(_("Mueva la cabeza a la derecha"))
		elif paso == 2:
			self.cam.iniciar()
			self.mostrarVideo((self.cam.tam[0], 0))
		elif paso == 3:
			time.sleep(3)
			self.dejarDeMostrar()
			centro = self.analizar()
			self.cam.detener()
			self.der = int(centro[0])
			self.estado.set_text(_("Mueva la cabeza arriba"))
		elif paso == 4:
			self.cam.iniciar()
			self.mostrarVideo((self.cam.tam[0], 0))
		elif paso == 5:
			self.dejarDeMostrar()
			centro = self.analizar()
			self.cam.detener()
			self.arriba = int(centro[1])
			self.estado.set_text(_("Mueva la cabeza abajo"))
		elif paso == 6:
			self.cam.iniciar()
			self.mostrarVideo((self.cam.tam[0], 0))
		elif paso == 7:
			self.dejarDeMostrar()
			centro = self.analizar()
			self.abajo = int(centro[1])
			self.supIzq = (self.izq, self.arriba)
			self.infDer = (self.der, self.abajo)

		

	def __calibrar2(self):		
		self.estado.set_text(_("Coloquese lo mas cerca del centro posible."))
		self.updGTK()
		self.mostrarVideo((0, 0), cruz=(self.cam.tam[0] / 2, self.cam.tam[1] / 2))
		time.sleep(5)
		self.dejarDeMostrar()		
		centro = self.analizar()
		self.supIzq = (centro[0]-self.dx, centro[1] - self.dy)
		self.infDer = (centro[0] + self.dx, centro[1] + self.dy)

	def calibrar2SetSensib(self, dx, dy):
		self.supIzq -= (self.dx, self.dy)
		self.infDer += (self.dx, self.dy)

	def iniciarCalibrado(self, tipo):
		if tipo == 0:
			for i in xrange(4):
				self.updGTK()
				self.__calibrar0(i)
				self.updGTK()
			self.estado.set_text(_("Fin de la calibracion."))
			time.sleep(2)
		elif tipo == 1:
			for i in xrange(8):
				self.updGTK()
				self.__calibrar1(i)
				self.updGTK()
			self.estado.set_text(_("Fin de la calibracion."))
			time.sleep(2)
		elif tipo == 2:
			self.updGTK()
			self.__calibrar2()
			self.estado.set_text(_("Fin de la calibracion."))
			self.updGTK()
			time.sleep(2)

		print self.supIzq
		print self.infDer
	

	def funcionando(self):
		self.updFondo()
		
		self.m = Mouse.Mouse(self.supIzq, self.infDer)
		#inicializo todos para que no haya errores
		for i in xrange(int(self.smooth / 2) + 1):
			centro = (0, 0)
			self.__agregarPunto(centro, self.puntosFoto)
			self.__agregarPunto(centro, self.puntosSuav)

		self.centroSuav = (0, 0)

		i = 0
		print time.clock()
		while self.cont:
			i += 1
			centro = self.analizar()

			self.__agregarPunto(centro, self.puntosFoto)
			#para el butter
			

			self.centroSuav = self.__getPuntoSuav1()
			
			self.__agregarPunto(self.centroSuav, self.puntosSuav)

			self.m.setPos(self.centroSuav)

			if i > 60:
				self.updGTK()
				i = 0
				print time.clock()

