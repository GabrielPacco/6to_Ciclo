#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

// Variables globales
#define NTHREADS 4
#define ARRAYSIZE 100000000
#define ITERATIONS ARRAYSIZE / NTHREADS

// Variables globales
double sum=0.0;  // Variable compartida
double a[ARRAYSIZE];
pthread_mutex_t sum_mutex;  // Mutex para sum

// Funcion que ejecutan las NTHREADS
void *do_work(void *tid)
{
    int i, start, *mytid, end;  
    double mysum=0.0;
    /* Inicializar mi parte de la matriz global y mantener suma local */

    mytid = (int *) tid; // Convertir de void * a int *
    start = (*mytid * ITERATIONS);  // Cada thread calcula su parte de la matriz
    end = start + ITERATIONS;
    printf ("\n[Thread %5d] Doing iterations \t%10d to \t%10d",*mytid,start,end-1);

    // Iterar sobre mi parte de la matriz
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
    int i, start, tids[NTHREADS];
    pthread_t threads[NTHREADS];

    pthread_attr_t attr;
    /* Configuración de Pthreads: inicializar el mutex y crear explícitamente
    crear hilos en un estado de unión (para la portabilidad). Pasar a cada hilo
    su desplazamiento de bucle */
    pthread_mutex_init(&sum_mutex, NULL);
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr,
    PTHREAD_CREATE_JOINABLE);
    for (i=0; i<NTHREADS; i++) {
        tids[i] = i;
        pthread_create(&threads[i], &attr, do_work, (void *)
        &tids[i]);
    }
    /* Esperar a que todos los hilos se completen y luego imprimir la suma global */
    for (i=0; i<NTHREADS; i++) {
        pthread_join(threads[i], NULL);
    }
    printf ("\n[MAIN] Done. Sum= %e", sum);
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