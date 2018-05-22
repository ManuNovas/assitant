import mysql.connector

class AsistenteKardpromos:
	conexion = None

	def abre_conexion(self, usuario, password, servidor, base_datos):
		self.conexion = mysql.connector.connect(user = usuario, password = password, host = servidor, database = base_datos)

	def selecciona_todas_tarjetas_usuario(self, usuario):
		archivo_salida = open('SQL/tarjetas_usuario.sql', 'w')
		cursor = self.conexion.cursor( )

		consulta = 'SELECT CVE_TARJETA FROM TBL_TARJETAS WHERE STATUS = 1'
		cursor.execute(consulta)
		tarjetas = cursor.fetchall( )

		for cve_tarjeta in tarjetas:
			clave = cve_tarjeta[0]

			consulta = 'SELECT CVE_REG FROM TBL_REG_TARS WHERE CVE_REG = ' + usuario + ' AND CVE_TARJETA = ' + str(clave)
			cursor.execute(consulta)
			registro = cursor.fetchone( )

			if registro is None:
				consulta = 'INSERT INTO TBL_REG_TARS(CVE_TARJETA, CVE_REG) VALUES(' + str(clave) + ', ' + str(usuario) + ');\n'
				archivo_salida.write(consulta)
				pass
			pass

		archivo_salida.close( )

asistente = AsistenteKardpromos( )

opcion = input('Selecciona una opcion:\n\t1. Asignar todas las tarjetas a usuario\n\t')
	
usuario = input('Escribe el usuario de la base: ')
password = input('Escribe el password de ' + usuario + ': ')
servidor = input('Escribe el servidor de la base: ')
base_datos = input('Escribe el nombre de la base: ')
asistente.abre_conexion(usuario, password, servidor, base_datos)

if asistente.conexion:
	if opcion == '1':
		id_usuario = input('Escribe el id del usuario: ')
		asistente.selecciona_todas_tarjetas_usuario(id_usuario)
		pass
	pass
else:
	print('Error al conectar con la base')