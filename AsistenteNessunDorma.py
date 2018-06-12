from random import uniform
from random import randint
import io

class AsistenteNessunDorma:
	def genera_consulta_estados(self, entrada):
		archivo_entrada = open(entrada, 'r')
		archivo_salida = open('../sql/estados_nd.sql', 'w')

		for linea in archivo_entrada.readlines( ):
			linea = linea.rstrip(',')
			linea = linea.replace('[', '')
			linea = linea.replace("'", '')
			linea = linea.replace(']', '')
			linea = linea.replace(' ', '')
			campo = linea.split(',')
			consulta = "INSERT INTO ESTADO(CLAVE, NOMBRE, VENTA_M2, INCREMENTO, ZONA_FK) VALUES('" + campo[0] + "', '', " + str(uniform(0, 167327)) + ", " + campo[1] + ", );"
			archivo_salida.write(consulta + '\n')
			pass
		print('Consulta generada')

		archivo_entrada.close( )
		archivo_salida.close( )
	def genera_consulta_municipios(self, entrada):
		archivo_entrada = io.open(entrada, mode = 'r', encoding = 'UTF-8')
		archivo_salida = io.open('../sql/municipios_nd.sql', mode = 'w', encoding = 'UTF-8')

		for linea in archivo_entrada.readlines( ):
			linea = linea.rstrip(',')
			linea = linea.replace('{', '')
			linea = linea.replace('"', '')
			linea = linea.replace('}', '')
			linea = linea.replace(' ', '')
			campo = linea.split('|')

			consulta = "INSERT INTO MUNICIPIO(ZONA_FK, PATH, NOMBRE, VENTA_M2, INCREMENTO) VALUES(5, '" + campo[2] + "', '" + campo[0] + "', " + str(uniform(0, 167327)) + ", " + campo[1] + ");"
			archivo_salida.write(consulta + '\n')
			pass

		archivo_salida.close( );

	def simula_centro_comercial_estados(self):
		archivo_salida = open('../sql/centros_comerciales_nd.sql', 'w')

		for x in xrange(1, 165):
			consulta = 'UPDATE CENTROS_COMERCIALES SET ESTADO_FK = ' + str(randint(1, 32)) + ', VENTA_M2 = ' + str(uniform(0, 167327)) + ', INCREMENTO = ' + str(randint(-20, 20)) + ', ASOCIADOS = ' + str(randint(1, 16)) + ' WHERE CENTRO_COMERCIAL_ID = ' + str(x) + ';'
			archivo_salida.write(consulta + '\n')
			pass

		print('Consulta generada')
		archivo_salida.close( )

	def genera_consulta_centros(self, nombre):
		archivo_entrada = open(nombre, 'r')
		archivo_salida = open('SQL/centros_comerciales_nd.sql', 'w')

		for linea in archivo_entrada.readlines( ):
			campos = linea.split('|')
			consulta = campos[0]
			consulta = consulta.replace("}EFK{", campos[2])
			consulta = consulta.replace("}MFK{", campos[3])
			consulta = consulta.replace("}VM2{", campos[5])
			consulta = consulta.replace("}INC{", campos[6])
			consulta = consulta.replace("}ASO{", campos[7])
			consulta = consulta.replace("}NOM{", campos[4])
			archivo_salida.write(consulta + ';\n')
			pass

		print("consulta generada");

		archivo_entrada.close( )
		archivo_salida.close( )

	def actualiza_municipios(self):
		archivo_entrada = open('SQL/incidencia_municipios.sql', 'r')
		archivo_salida = open('SQL/actualiza_municipios_nd.sql', 'w')

		for linea in archivo_entrada.readlines( ):	
			campos = linea.split('|')
			consulta = campos[0]
			consulta = consulta.replace("}ID{", campos[1])
			consulta = consulta.replace("}ZFK{", campos[2])
			consulta = consulta.replace("}VM2{", campos[5])
			consulta = consulta.replace("}INC{", campos[6])
			consulta = consulta.replace("}NOM{", campos[4])
			archivo_salida.write(consulta + ';\n')
			pass

		archivo_entrada.close( )
		archivo_salida.close( )

	def actualiza_estados(self):
		archivo_entrada = open('SQL/incidencia_estados.sql', 'r')
		archivo_salida = open('SQL/actualiza_estados_nd.sql', 'w')

		for linea in archivo_entrada.readlines( ):	
			campos = linea.split('|')
			consulta = campos[0]
			consulta = consulta.replace("}VM2{", campos[3])
			consulta = consulta.replace("}INC{", campos[4])
			consulta = consulta.replace("}NOC{", campos[5])
			consulta = consulta.replace("}ZFK{", campos[6])
			consulta = consulta.replace("}NOM{", campos[2])
			archivo_salida.write(consulta + ';\n')
			pass

		archivo_entrada.close( )
		archivo_salida.close( )

asistente = AsistenteNessunDorma( )

opcion = input('Selecciona una opcion:\n\t1. Generar consulta de estados\n\t2. Generar consulta de municipios\n\t3. Generar consulta para simular centros comerciales\n\t4. Obtener consulta para actualizar centros comerciales\n\t5. Actualiza municipios\n\t6. Actualiza estados')
opcion = int(opcion)

if opcion == 1:
	nombre = raw_input('Escribe el nombre del archivo de entrada: ')
	asistente.genera_consulta_estados(nombre)
	pass
elif opcion == 2:
	nombre = raw_input('Escribe el nombre del archivo de entrada: ')
	asistente.genera_consulta_municipios(nombre)
	pass
elif opcion == 3:
	asistente.simula_centro_comercial_estados( )
	pass
elif opcion == 4:
	nombre = input('Escribe el nombre del archivo de entrada: ')
	asistente.genera_consulta_centros(nombre)
	pass
elif opcion == 5:
	asistente.actualiza_municipios( )
	pass
elif opcion == 6:
	asistente.actualiza_estados( )
	pass