#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "Rodrigo"
__date__ = "$26-nov-2010 11:31:34$"

if __name__ == "__main__":
	smooth = 15

	b = (0.000038926174683, 0.000272483222782, 0.000817449668345, 0.001362416113908, 0.001362416113908, 0.000817449668345, 0.000272483222782, 0.000038926174683)
	a = (-4.548677605587151, 9.169313662615249, -10.541407463246442, 7.431411774523795, -3.202508041697642, 0.779304796989226, -0.082454573237603)

	#b = (0.0012, 0.0047, 0.0071, 0.0047, 0.0012)
	#a = ( -2.9090, 3.2840, -1.6876, 0.3315)


	bb = [0, 0]
	aa = [0, 0]
	"""en los a pares van  los fotografiados!!!"""
	puntosFoto = [(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(150,300),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
	puntosSuav = [(151.3666274047909, 302.73325480958181),(160.44202408543524, 320.88404817087047),(168.98300472737614, 337.96600945475228),(174.15262525152565, 348.3052505030513),(173.2871292387731, 346.57425847754621),(164.62676386383572, 329.25352772767144),(147.8866636866077, 295.77332737321541),(124.46680383003634, 248.93360766007268),(97.191210863258831, 194.38242172651766),(69.614703331674278, 139.22940666334856),(45.09541036002372, 90.190820720047441),(25.940523831605674, 51.881047663211348),(12.932232772620639, 25.864465545241277),(5.4046814176582574, 10.809362835316515),(1.8060969870863155, 3.612193974172631),(0.44907517244122386, 0.89815034488244772),(0.073270802477510347, 0.14654160495502069),(0.0058389262024499998, 0.0116778524049),(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
	"""Butterworth"""
	for i in xrange(int(smooth / 2) + 1):
		"""fotografiados"""
		bb[0] += b[i] * puntosFoto[i][0]
		bb[1] += b[i] * puntosFoto[i][1]

	

	for i in xrange(int(smooth / 2)):
		"""suavizados"""
		aa[0] += a[i] * puntosSuav[i][0]
		aa[1] += a[i] * puntosSuav[i][1]
	
	x = bb[0]-aa[0]
	y = bb[1]-aa[1]

	print (x, y)

#	bb[0] = b[0]* puntos[0][0] + b[1]* puntos[2][0] + b[2]* puntos[4][0] + b[3]* puntos[6][0]+ b[4]* puntos[8][0] + b[5]* puntos[10][0]+ b[6]* puntos[12][0]+ b[7]* puntos[14][0]
#	aa[0] = a[0]* puntos[1][0] + a[1]* puntos[3][0] + a[2]* puntos[5][0] + a[3]* puntos[7][0] + a[4]* puntos[9][0]+ a[5]* puntos[11][0]+ a[6]* puntos[13][0]

	print bb[0]-aa[0]