def es_palindromo(palabra):
	mi_cola=deque([])
	mi_pila =[]
	for i in palabra:
		print(i)
	mi_cola.append(i)
	mi_pila.append(i)	

	while (mi_cola.popleft()) == (mi_pila.pop()):
		print(true)


