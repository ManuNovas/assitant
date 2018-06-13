import mysql.connector
import io

class AsistenteYama:
	conexion = None

	def abre_conexion(self, usuario, password, servidor, base_datos):
		self.conexion = mysql.connector.connect(user = usuario, password = password, host = servidor, database = base_datos)

	def genera_imagenes_galeria(self, entrada, micrositio_id):
		#entrada = open('C:\\Users\\Franco\\Documents\\Documentación\\Yama\\' + archivo_entrada, 'r', encoding = 'UTF-8')
		#salida = open('C:\\Users\\Franco\\Documents\\Documentación\\Yama\\imagenes_yama.sql', "w", encoding = 'UTF-8')
		entrada = open('/home/mane/Documentos/Codice/Yama/' + archivo_entrada, 'r', encoding = 'UTF-8')
		salida = open('/home/mane/Documentos/Codice/Yama/imagenes_yama.sql', "w", encoding = 'UTF-8')
		cursor = self.conexion.cursor( )

		i = 0
		for linea in entrada.readlines( ):
			if i != 0:
				campos = linea.split(',')
				anio = str(campos[1])
				mes = campos[2]
				imagen = campos[3]

				meses = {
					'Enero': 1,
					'Febrero': 1,
					'Marzo': 1,
					'Abril': 2,
					'Mayo': 2,
					'Junio': 2,
					'Julio': 3,
					'Agosto': 3,
					'Septiembre': 3,
					'Octubre': 4,
					'Noviembre': 4,
					'Diciembre': 4
				}

				periodos = {
					1: 'ENERO - MARZO',
					2: 'ABRIL - JUNIO',
					3: 'JULIO - SEPTIEMBRE',
					4: 'OCTUBRE - DICIEMBRE'

				}

				consulta = "SELECT GALERIA_AVANCE_ID FROM GALERIA_AVANCE WHERE MICROSITIO_FK = " + str(micrositio_id) + " AND PERIODO_TRIMESTRAL_FK = " + str(meses[mes]) + ' AND AÑO = ' + anio
				cursor.execute(consulta)
				galeria_avance_id = cursor.fetchone( )
				if galeria_avance_id is None:
					print('No existe la galeria de ' + mes +  '/' + anio + ' en base')
					pass
				else:
					galeria_avance_id = galeria_avance_id[0]
					consulta = "INSERT INTO IMAGEN_GALERIA(GALERIA_AVANCE_FK, ENLACE, STATUS) VALUES(" + str(galeria_avance_id) + ", '" + anio + "/" + str(periodos[meses[mes]]) + "/" + mes.upper( ) + "/" +  imagen + "', 1);\n"
					salida.write(consulta)
					pass

				pass
			pass
			i += 1
		pass

		entrada.close( )
		salida.close( )

asistente = AsistenteYama( )

opcion = input('Selecciona una opcion:\n\t1. Exportar imagenes\n\t')
	
usuario = input('Escribe el usuario de la base: ')
password = input('Escribe el password de ' + usuario + ': ')
servidor = input('Escribe el servidor de la base: ')
base_datos = input('Escribe el nombre de la base: ')
asistente.abre_conexion(usuario, password, servidor, base_datos)

if asistente.conexion:
	if opcion == '1':
		archivo_entrada = input('Escribe el nombre del archivo de entrada: ')
		micrositio_id = input('Escribe el id del micrositio: ')
		asistente.genera_imagenes_galeria(archivo_entrada, micrositio_id)
		pass
	pass
else:
	print('Error al conectar con la base')