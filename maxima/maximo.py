def maxima (lista):
	if len(lista) == 1:
		return (lista)

	sublista = lista[1:]
	submaxima = maxima(sublista)
	
	if lista[0] > submaxima:
		return lista[0]

	return submaxima