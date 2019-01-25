# -*- coding: UTF-8 -*-

from sdc.sdc import *
from thread import start_new_thread
import sys

host = "localhost" # aqui la direccion a la cual conectarse
port = 8443

"""
Estos scripts son una demostración del funcionamiento de sdc (Secure Data Connection), para apreciarlo mucho mejor en una aplicación. Si no me crees, conecta a netcat (nc) al servidor y enviale datos a traves de este para que veas todos los datos encriptados que se envian o usa a netcat como servidor y conecta a el cliente para que veas el mismo funcionamiento.
"""

# La contraseña debe tener 32 caracteres y
# Los datos: el host, el puerto, la contraseña, las repeticiones, etc; Tienen que
# ser iguales al otro punto (Servidor).

conexion = Connection(host, port, "12345678901234567890123456789012", repeat=10)

try:

	conexion.client()

except connectError:
	
	sys.exit("Error conectando a la direccion especificada.")
	
def recibiendo_la_conexion():

	global host, port

	while True:
	
		try:

			data = conexion.server_recv()
			
			print "Mensaje recibido de :: {0}:{1}".format(host, str(port))
			print "Mensaje: %s" % (data)
	
		except corruptData:
			
			continue
	
output = start_new_thread(recibiendo_la_conexion, ())

while True:

	try:
	
		try:
		
			debug = raw_input("{0}:{1} >>> ".format(host, str(port)))
		
		except KeyboardInterrupt:
			
			sys.exit()
		
		if not debug:
			continue
			
		print "Enviando mensaje a :: {0}:{1}".format(host, str(port))
			
		conexion.server_interact(debug)
		
	except KeyboardInterrupt:
		
		sys.exit()
		
	except EOFError:
		
		continue
		
	except Exception as error:
		
		print "Exception: %s" % (str(error))
