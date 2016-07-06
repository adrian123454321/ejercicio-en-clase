

lista=[
["a" , "b" , "c"],
["d" , "e" , "f"],
["g" , "h" , "i"] 
]

print(lista[0])
print(lista[1])
print(lista[2])

play1=input("Elija una casilla: ")
if play1=="a":
	lista[0][0]="x"
print(lista[0])
print(lista[1])
print(lista[2])

if play1=="b":
	lista[0][1]="x"
	