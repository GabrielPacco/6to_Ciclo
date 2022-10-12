#include <stdio.h>
#include <sys/types.h>
#define MAX_COUNT 200
/* El programa crea un proceso hijo que ejecuta el bucle for. El proceso padre ejecuta el bucle for.
Ambos procesos comparten la variable count. El proceso padre espera a que el proceso hijo termine
su ejecución antes de terminar su ejecución. */

void ChildProcess(void); /* child process prototype */
void ParentProcess(void); /* parent process prototype */

void main(void)
{
    pid_t pid; // Inicializa la variable pid que representa el ID del proceso
    pid = fork(); // Crea un nuevo proceso que se convierte en hijo del proceso padre
    if (pid == 0) // Si el proceso es hijo
        ChildProcess(); // Llama a la función ChildProcess
    else // Si el proceso es padre
        ParentProcess(); // Llama a la función ParentProcess
}
// Función que se ejecuta en el proceso hijo
void ChildProcess(void)
{
    int i; // Variable de control del ciclo for
    for (i = 1; i <= MAX_COUNT; i++)
    printf(" This line is from child, value = %d\n", i);
    printf(" *** Child process is done ***\n");
}
// Función que se ejecuta en el proceso padre
void ParentProcess(void)
{
    int i; // Variable de control del ciclo for
    for (i = 1; i <= MAX_COUNT; i++)
    printf("This line is from parent, value = %d\n", i);
    printf("*** Parent is done ***\n");
}