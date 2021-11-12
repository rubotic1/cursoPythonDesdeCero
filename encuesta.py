respuestas = {}

# Activamos un FLAG si la encuesta está activa
encuesta_activa = True

while encuesta_activa:
	# Esperamos introduzan nombre y respuesta
	nombre = input("\n¿Cual es tu nombre? ")
	respuesta = input("¿Que marca de coche tienes? ")

	# Guardamos respuestas en diccionario.
	respuestas[nombre] = respuesta

	# Preguntamos si alguien más hace la encuesta.
	repetir = input("¿Alguien más contestará la encuesta? (si/ no) ")
	if repetir == 'no':
		encuesta_activa = False

# Encuesta terminada. Veamos los resultados.
print("\n--- Resultados de la encuesta ---")
for nombre, respuesta in respuestas.items():
	print(f"{nombre.title()} conduce un {respuesta.title()}.")