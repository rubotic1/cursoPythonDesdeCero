prompt = "Puedes ejecutar comandos en esta consola:"
prompt += "\nPara salir escribe 'exit'"
message = ""
print (prompt)
while message != 'exit':
	message = input("console >>> ")
	if message == 'help':
		print ("Lista de comandos:")
		print ("\n help:   muestra una ayuda")
		print ("\n exit:   salida de la aplicación")
	
print ("Hemos terminado!")