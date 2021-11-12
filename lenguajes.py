lenguajes = ['basic', 'cplus', 'javascript', 'python']
lenguajes.append('csharp')
lenguajes[2] = 'java'
lenguajes.insert(2,'visualbasic')
del lenguajes[3]
lenguajes.sort(reverse=True)
primer_lenguaje = lenguajes.pop()

print (lenguajes)
print ("Pero mi primer lenguaje fue " + primer_lenguaje)

nuevos_lenguajes = lenguajes[:]
print (nuevos_lenguajes)

