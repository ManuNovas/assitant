import mysql.connector
import string
import codecs

class AsistenteCocaICE:
	conexion = None

	def conectaBaseMYSQL(self, usuario, password, hostMysql, database):
		self.conexion = mysql.connector.connect(user = usuario, password = password, host = hostMysql, database = database)

	def my_strtr(self, cadena, reemplazo):    
	    """Reemplazo multiple de cadenas en Python."""
	    import re
	    regex = re.compile("(%s)" % "|".join(map(re.escape, reemplazo.keys())))
	    return regex.sub(lambda x: str(reemplazo[x.string[x.start() :x.end()]]), cadena)

	def verifica_existencia(self, nombre, cursor, id_tabla, tabla, archivo_salida = None):
		consulta = "SELECT " + id_tabla + " FROM " + tabla + " WHERE NOMBRE = '" + nombre + "'"
		cursor.execute(consulta)
		identificador = cursor.fetchone( )
		if identificador is None:
			#consulta = "INSERT INTO " + tabla + " (NOMBRE) VALUES ('" + nombre + "')"
			#cursor.execute(consulta)
			#self.conexion.commit( )
			#if archivo_salida != None:
				#archivo_salida.write(consulta + ';\n')
				#pass
			print("Falta el registro " + nombre)
			#identificador = cursor.lastrowid
			identificador = 0
		else:
			identificador = identificador[0]
		return identificador

	def inserta_tiendas(self, nombre_archivo):
		archivo_entrada = codecs.open(nombre_archivo, "r", "latin-1")
		cursor = self.conexion.cursor(buffered = True)
		i = 0
		for linea in archivo_entrada.readlines( ):
			if i != 0:
				campos = linea.split(',')

				tienda_id = campos[0]
				nombre_tienda = campos[1]
				status_tienda = campos[2]
				formato = campos[6]
				region = campos[8]
				franquicia = campos[9]
				direccion = campos[13] + ", " + campos[14]
				zona_sombra = campos[33]

				formato_id = self.verifica_existencia(formato, cursor, "FORMATO_TIENDA_ID", "FORMATO_TIENDA")
				region_id = self.verifica_existencia(region, cursor, "REGION_ID", "REGION")
				franquicia_id = self.verifica_existencia(franquicia, cursor, "FRANQUICIA_ID", "FRANQUICIA")
				zona_sombra_id = self.verifica_existencia(zona_sombra, cursor, "ZONA_SOMBRA_MULTIPACK_ID", "ZONA_SOMBRA_MULTIPACK")

				if formato_id > 0 and franquicia_id > 0 and zona_sombra_id > 0:
					consulta = "SELECT TIENDA_ID FROM TIENDA WHERE NOMBRE = '" + nombre_tienda + "'"
					cursor.execute(consulta)
					identificador = cursor.fetchone( )
					if identificador is None:
						consulta = "INSERT INTO TIENDA(REGION_FK, FRANQUICIA_FK, ZONA_SOMBRA_MULTIPACK_FK, NOMBRE, DIRECCION, FORMATO_TIENDA_FK, STATUS) VALUES(" + str(region_id) + ", " + str(franquicia_id) + ", " + str(zona_sombra_id) + ", '" + nombre_tienda + "', '" + direccion + "', " + str(formato_id) + ", " + status_tienda + ")"
						cursor.execute(consulta)
						self.conexion.commit( )
						print("Se inserto la tienda: " + nombre_tienda)
			i += 1
		archivo_entrada.close( )

	def cierra_conexion(self):
		self.conexion.close( )

asistente = AsistenteCocaICE( )

opcion = input('Selecciona una opcion:\n\t1. Subir tiendas\n\t')
	
usuario = input('Escribe el usuario de la base: ')
password = input('Escribe el password de ' + usuario + ': ')
servidor = input('Escribe el servidor de la base: ')
base_datos = input('Escribe el nombre de la base: ')
asistente.conectaBaseMYSQL(usuario, password, servidor, base_datos)

if asistente.conexion:
	if opcion == '1':
		archivo_entrada = input('Escribe el nombre del archivo de entrada: ')
		asistente.inserta_tiendas(archivo_entrada)
		pass
	pass
else:
	print('Error al conectar con la base')