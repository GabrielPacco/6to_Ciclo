#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
// Libreria para medir el tiempo de ejecucion
#include <time.h>
#include <sys/time.h>
#include <unistd.h>

// Mutex es un bloqueo de exclusión mutua. Solo un hilo puede mantener la cerradura.

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



double do_work2(void *tid, double a[], double sum, double sum_mutex, int NTHREADS, int ARRAYSIZE, int ITERATIONS)
{
    int i, start, end;  
    double mysum=0.0;
    /* Inicializar mi parte de la matriz global y mantener suma local */

    start = (0 * ITERATIONS);  // Cada thread calcula su parte de la matriz
    end = start + ITERATIONS;
    printf ("\n[Thread %5d] Doing iterations \t%10d to \t%10d",0,start,end-1);

    // Iterar sobre mi parte del array y calcular la suma local de cada thread 
    for (i=start; i < end ; i++) {
        a[i] = i * 1.0;
        mysum = mysum + a[i];
    }

    /* Bloquear el mutex y actualizar la suma global, luego salir */
    pthread_mutex_lock(&sum_mutex);
    sum = sum + mysum;
    pthread_mutex_unlock(&sum_mutex);
    return sum;
}

int main(int argc, char *argv[])
{
    int NTHREADS = 4; // Número de threads
    int ARRAYSIZE = 100000000; // Tamaño del array
    int ITERATIONS = ARRAYSIZE/NTHREADS; // Iteraciones por thread
    
    // Declarar variables
    double sum=0.0;
    double a[ARRAYSIZE];
    pthread_mutex_t sum_mutex;
    
    // Inicializar variables
    int i, start, tid[NTHREADS];
    pthread_t threads[NTHREADS];

    pthread_attr_t attr;

    // Inicializar el mutex
    pthread_mutex_init(&sum_mutex, NULL);
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    // Inicializar el array
    for (i=0; i<NTHREADS; i++) {
        tid[i] = i;
        // Crear los threads
        pthread_create(&threads[i], &attr, do_work2, (void *) &tid[i]);
    }

    // Unir los threads
    for (i=0; i<NTHREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    // Imprimir el resultado
    printf("Sum = %f \n", sum);
    
    /* for (i=0;i<ARRAYSIZE;i++){
    a[i] = i*1.0;
    sum = sum + a[i]; }
    printf("\n[MAIN] Check Sum= %e",sum);
    */
    // Clean up and exit 
    pthread_attr_destroy(&attr);
    //pthread_mutex_destroy(&sum_mutex);
    pthread_exit (NULL);    
    
}