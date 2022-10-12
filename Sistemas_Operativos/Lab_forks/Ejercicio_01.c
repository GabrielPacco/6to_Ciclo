#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

pid_t wait(int *status);
int main(){

    int status;

    pid_t fork_return; // Variable que almacena el ID del proceso

    fork_return = fork(); // Crea un nuevo proceso que se convierte en hijo del proceso padre

    if(fork_return == 0) /* child process */
    {
        printf("\n I'm the child!");
        exit(0); // Cuando el hijo termina su proceso o se detiene el padre recibe una señal
        /*
        La función exit interrumpe la ejecución del programa en forma inmediata y retorna un entero
        al proceso que llamó al programa (normalmente este valor devuelto lo recibe el sistema operativo)
        El valor devuelto por convención es un cero si el programa finaliza en forma correcta o un valor
        distinto a cero indicando distintos códigos de error que los puede interpretar quien ejecutó el programa.
        */
    }
    else if(fork_return > 0) /* parent process */
    {
        wait(&status); // Suspende la ejecución del proceso de llamada hasta que finaliza uno de sus hijos
        printf("\n I'm the parent!");

        if (WIFEXITED(status)) // Es una llamada al sistema para conocer el estado de su hijo, si retorna true
            printf("\n Child returned: %d\n", WEXITSTATUS(status)); // Imprime el estado de salida del proceso hijo
        }
    
    else /* fork() returned an error */
    {
        perror("fork");  // Imprime el mensaje de error
        exit(1);
    }
    return 0;
}