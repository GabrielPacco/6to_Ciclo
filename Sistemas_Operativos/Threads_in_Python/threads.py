import requests
from queue import Queue
from threading import Thread

NUM_THREADS = 5  # Se declara la cantidad de hilos que se van a utilizar
q = Queue() 

# Se crea la función que descarga la imagen
def download_img():
	"""
	Download image from img_url in curent directory
	"""
	global q  # q almacenará las urls de las imágenes

	while True:
		img_url = q.get()

		res = requests.get(img_url, stream=True)
		filename = f"{img_url.split('/')[-1]}.jpg"

		with open(filename, 'wb') as f:
			for block in res.iter_content(1024):
				f.write(block)
		q.task_done()

if __name__ == '__main__':
    images = [
    	'https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7',
    	'https://images.unsplash.com/photo-1587620962725-abab7fe55159',
    	'https://images.unsplash.com/photo-1493119508027-2b584f234d6c',
    	'https://images.unsplash.com/photo-1482062364825-616fd23b8fc1',
    	'https://images.unsplash.com/photo-1521185496955-15097b20c5fe',
    	'https://images.unsplash.com/photo-1510915228340-29c85a43dcfe',
    ]
    
    # Se itera sobre el array que contiene los links de las imágenes
    for img_url in images * 5:
        q.put(img_url)

    # Se itera la cantidad de hilos que se van a utilizar
    for t in range(NUM_THREADS):

        # Se crea el hilo
        worker = Thread(target=download_img) # Se le pasa la función que se va a ejecutar en cada hilo
        worker.daemon = True # Se declara que el hilo es un daemon
        worker.start()  # Se inicia el hilo

    q.join() 