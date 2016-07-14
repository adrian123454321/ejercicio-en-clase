totito=[
["a","b","c"],
["d","e","f"],
["g","h","i"]
]

print(totito[0])
print(totito[1])
print(totito[2])

turno1=input("elija una casilla ")
tirovalor=ord(turno1)-65
tirofila=(tirovalor %  3)
tirocolumna=(tirovalor // 3)
for i in range(3):
	for j in range(3):
		cl=totito[i][j]
		if cl==1:
			resultado="X"

		elif cl==-1:
			resultado="O"
		else:
			resultado=chr(3*i+j+65)	

			

print("turno2")
print(totito[0])
print(totito[1])
print(totito[2])

turno2=input("elija una casilla ")
tirovalor=ord(turno2)-65
tirofila=(tirovalor % 3)
tirocolumna=(tirovalor//3)



