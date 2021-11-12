# Inicializamos usuarios que han de ser confirmados,
# y creamos una lista vacia para introducirlos luego
usuarios_no_confirmados = ['juan', 'ana', 'pedro', 'lucia']
usuarios_confirmados = []
# Verificar usuarios hasta que no haya mas no confirmados
# Mover cada usuario a la lista de confirmados
while usuarios_no_confirmados:
	usuario_actual = usuarios_no_confirmados.pop()
	print(f"Verificando usuario: {usuario_actual.title()}")
	usuarios_confirmados.append(usuario_actual)

# Mostrar todos los confirmados.
print("\nLos siguientes usuarios han sido confirmados:")
for confirmado in usuarios_confirmados:
	print(confirmado.title())