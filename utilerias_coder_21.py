import sys
global nombre_del_guion, funcion_solicitada
nombre_del_guion = sys.argv[0]
try:
	funcion_solicitada = sys.argv[1]
except:
	funcion_solicitada = None
class Imprime:
		def __init__(self,var=str):        	
			print(var)


if __name__ == "__main__":
	if funcion_solicitada is None:
		print("-->Este es es el guión: " + nombre_del_guion + ", bienvenido.")
		print("-->para utilizar una función simplemente ejecuta:")
		print("-->python3 + nombre_del_archivo + funcion_deseada")
	else:
		print("-->Bienvenido, solicitaste la función: "+ nombre_del_guion)
		if "imprimir" in funcion_solicitada:
			p = Imprime
			p("--<Felicidades, esta es la funcion imprimir")
		else:
			print("--xEsa no es una función :'( ")
		
		
	
		
