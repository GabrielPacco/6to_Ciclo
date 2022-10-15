import random
import multiprocessing

NUM_PROC = 2  # Se declara la cantidad de procesos que se van a utilizar

# Función agrega a una losta los numeros aleatorios generados
def append_to_list(lst, num_items):
	"""
	Appends num_items integers within the range [0-20000000) to the input lst
	"""
	for n in random.sample(range(20000000), num_items):
		lst.append(n)

if __name__ == "__main__":
	jobs = [] # Se crea una lista para almacenar los procesos

    # Se iteran la cantidad de procesos que se van a utilizar
	for i in range(NUM_PROC):
		process = multiprocessing.Process(  # Se crea el proceso
			target=append_to_list,   # Se le pasa la función que se va a ejecutar en cada proceso
		    args=([], 10000000)  # Se le pasan los argumentos que recibe la función
		)
		jobs.append(process) # Se agrega el proceso a la lista de procesos

	for j in jobs: # Se itera sobre la lista de procesos 
		j.start()

	for j in jobs: 
		j.join()