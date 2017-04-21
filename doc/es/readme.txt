hMouse v.1.0

===Introducción===

hMouse permite el moviemiento del puntero del mouse de la XO con la cabeza u otra parte del cuerpo. Esto se logra siguiendo con la cámara un puntero LED.
La h de hMouse viene de la palabra inglesa 'head', que significa cabeza. 'h' debe pronunciarse en español y 'Mouse' como en inglés.


===Modo de uso===

El LED debe apuntar directamente a la cámara y puede, por ejemplo, estar montado en la sien derecha del usuario mediante una vincha.
Para lograr un funcionamiento óptimo el LED debe ser de alta potencia (ej. 4.5 V), el usuario debe encontrarse en un sitio oscuro, con un fondo uniforme y opaco, o en su defecto, ponerle un filtro translúcido a la cámara.
El clic debe efectuarse mediante otro método, ya que el programa no soporta aún esta acción.
El programa dispone de una pequeña ayuda que explica brevemente los pasos a seguir y luego, cada uno de estos pasos tiene sus instrucciones que guían al usuario a través del proceso. Además dispone de la opción "Ver cámara" que permite visualizar lo que está captando la cámara, útil para comprobar que el LED está correctamente apuntado y el usuario se encuentra en una posición favorable.

Primero que nada el usuario debe calibrar el programa. Esto se debe hacer ya que la distancia y la posición del usuario frente a la cámara variará en cada uso, por lo que es necesario reconfigurar el área de la imagen en la que se buscará el puntero LED y además se reconfigura cuáles son los movimientos límite del usuario que representarán los bordes de la pantalla.
Actualmente se dispone de tres métdos de calbiración equivalentes, de los que se debe escoger uno, según las capacidades y preferencias del usuario:

	==Arriba a la Izquierda - Abajo a la Derecha==
	
	Este método es de precisión óptima y simplifica la calibración a solo dos movimientos. El usuario debe mover la cabeza en primera instancia hacia arriba a la izquierda y luego hacerlo hacia abajo a la derecha.
	
	==Izquierda - Derecha - Arriba - Abajo==
	
	Este método también es de precisión óptima pero duplica la cantidad de movimientos requeridos, siendo estos los expresados en el nombre. El objetivo de este método es disminuir la complejidad de los movimientos requeridos para la calibración.
	
	==Centro==
	
	El usuario debe acomodarse o acomodar la XO para que el LED coincida con el centro de la imagen. Luego de esto se toma como centro la posición actual del LED y los límites están predeterminados. Este es el método menos preciso, pero no requiere movimiento del usuario.

Luego de haber calibrado el usuario ya está en condiciones de presionar el botón "Iniciar", con lo que se dará paso al control del cursor con la cabeza.
Antes de presionar el botón Iniciar el usuario puede elegir recalibrar con el mismo u otro método, siempre siendo la última calibración hecha la que será utilizada.
El usuario deberá ocultar manualmente la actividad para poder comenzar a utilizar otras.
Para detener el control del mouse debe presionarse nuevamente el botón Iniciar.

===Detalles técnicos===

El movimiento registrado del LED es suavizado por un Filtro de Butterworth para un movimiento más suave del cursor.
El movimiento del cursor se realiza mediante la utilización de la biblioteca libX11.
El manejo de la cámara y las imágenes que la misma captura se realiza mediante Pygame y Numpy.
El proyecto fue desarrollado con NetBeans para Python. Los archivos de proyecto NetBeans están incluidos.

===Licencia===

Este programa es software libre: usted puede redistribuirlo y/o modificarlo conforme a los términos de la Licencia Pública General de GNU publicada por la Fundación para el Software Libre, ya sea la versión 3 de esta Licencia o (a su elección) cualquier versión posterior.
Este programa se distribuye con el deseo de que le resulte útil, pero SIN GARANTÍAS DE NINGÚN TIPO; ni siquiera con las garantías implícitas de COMERCIABILIDAD o APTITUD PARA UN PROPÓSITO DETERMINADO.  Para más información, consulte la Licencia Pública General de GNU.
Junto con este programa, se debería incluir una copia de la Licencia Pública General de GNU. De no ser así, ingrese en <http://www.gnu.org/licenses/>.
Este progama fue desarrollado por el Departamento de Ingeniería de la Fundación Teletón Uruguay. No remover las menciones a la misma.
