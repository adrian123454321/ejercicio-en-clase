notas = []
resp= "si"
nota=str(input("ingrese una nota "))
notas.append(nota)
resp=input("Desea continuar ")

while resp == "si":
	nota=str(input("ingrese una nota "))
	notas.append(nota)
	resp=input("Desea continuar ")
if resp == "no":
	open("notasguardadas.txt", "w")
	n = open("notasguardadas.txt", "w")
	n.write (nota)

	f= open("notasguardadas.txt" ,"r")
	for i in f:
		print (i)
			


