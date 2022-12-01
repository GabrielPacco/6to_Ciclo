#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
// Libreria para medir el tiempo de ejecucion
#include <time.h>
#include <sys/time.h>
#include <unistd.h>

// Mutex es un bloqueo de exclusión mutua. Solo un hilo puede mantener la cerradura.

// Variables globales
#define NTHREADS 4
#define ARRAYSIZE 100000000
#define ITERATIONS ARRAYSIZE / NTHREADS

// Variables globales
double sum=0.0;  // Variable compartida
double a[ARRAYSIZE];
pthread_mutex_t sum_mutex;  // ID del mutex

// Función para calcular el tiempo de ejecución en milisegundos
void timeval_subtract (struct timeval *result, struct timeval *x, struct timeval *y)
{
  /* Perform the carry for the later subtraction by updating y. */
  if (x->tv_usec < y->tv_usec) {
    int nsec = (y->tv_usec - x->tv_usec) / 1000 + 1;
    y->tv_usec -= 1000 * nsec;
    y->tv_sec += nsec;
  }
  if (x->tv_usec - y->tv_usec > 1000) {
    int nsec = (x->tv_usec - y->tv_usec) / 1000;
    y->tv_usec += 1000 * nsec;
    y->tv_sec -= nsec;
  }

  /* Compute the time remaining to wait.
     tv_usec is certainly positive. */
  result->tv_sec = x->tv_sec - y->tv_sec;
  result->tv_usec = x->tv_usec - y->tv_usec;
}

// Función que ejecutan los hilos
void *do_work(void *tid)
{
    int i, start, *mytid, end;  
    double mysum=0.0;
    /* Inicializar mi parte de la matriz global y mantener suma local */

    mytid = (int *) tid; // Convertir de void * a int *
    start = (*mytid * ITERATIONS);  // Cada thread calcula su parte de la matriz
    end = start + ITERATIONS;
    printf ("\n[Thread %5d] Doing iterations \t%10d to \t%10d",*mytid,start,end-1);

    // Iterar sobre mi parte del array y calcular la suma local de cada thread 
    for (i=start; i < end ; i++) {
        a[i] = i * 1.0;
        mysum = mysum + a[i];
    }

    /* Bloquear el mutex y actualizar la suma global, luego salir */
    pthread_mutex_lock (&sum_mutex);
    sum = sum + mysum;
    pthread_mutex_unlock (&sum_mutex);
    pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
    // Variables para medir el tiempo de ejecucion
    struct timeval t_ini, t_fin;
    double msecs;


    // Empezar a medir el tiempo de ejecucion
    gettimeofday(&t_ini, NULL);
    
    // Identificadores de los threads
    int i, start, tids[NTHREADS];
    pthread_t threads[NTHREADS];

    pthread_attr_t attr; // Atributos de los threads

    /* Configuración de Pthreads: inicializar el mutex y crear explícitamente
    crear hilos en un estado de unión (para la portabilidad). Pasar a cada hilo
    su desplazamiento de bucle */
    pthread_mutex_init(&sum_mutex, NULL);   // Inicializar el mutex
    pthread_attr_init(&attr);               // Inicializar los atributos
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);  // Configurar los atributos
    for (i=0; i<NTHREADS; i++) {
        tids[i] = i;   // Cada thread calcula su parte de la matriz
        pthread_create(&threads[i], &attr, do_work, (void *)&tids[i]);  // Crear los threads con los atributos y la funcion a ejecutar por cada thread
    }
    /* Esperar a que todos los hilos se completen y luego imprimir la suma global */
    for (i=0; i<NTHREADS; i++) {
        pthread_join(threads[i], NULL);   // Esperar a que todos los threads terminen
    }
    printf ("\n[MAIN] Done. Sum= %e", sum);
    printf ("\n");

    // Terminar de medir el tiempo de ejecucion
    gettimeofday(&t_fin, NULL);

    // Tiempo de ejecucion
    timeval_subtract(&t_fin, &t_fin, &t_ini);
    msecs = (double) t_fin.tv_sec + (double) t_fin.tv_usec / 1000.0;
    printf("Tiempo de ejecucion: %f milisegundos: \t", msecs);
    printf ("\n");

    sum=0.0;
    /* for (i=0;i<ARRAYSIZE;i++){
    a[i] = i*1.0;
    sum = sum + a[i]; }
    printf("\n[MAIN] Check Sum= %e",sum);
    */
    /* Clean up and exit */
    pthread_attr_destroy(&attr);
    pthread_mutex_destroy(&sum_mutex);
    pthread_exit (NULL);    
}