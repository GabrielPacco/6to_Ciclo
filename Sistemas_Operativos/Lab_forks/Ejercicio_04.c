#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/wait.h>

int main(void) {
    pid_t pid = 0; // Incializa la variable pid que representa el ID del proceso con 0
    int status;

    pid = fork(); // Crea un nuevo proceso que se convierte en hijo del proceso padre
    if (pid == 0) {
        printf("I am the child. \n");
        execl("/bin/ls", "ls", "-l", "/tmp/kris", (char *) 0);
        /*
        execl() ejecuta el programa especificado por filename, que debe ser una cadena de caracteres que

        contiene el nombre de un archivo ejecutable.

        */
        perror("In exec(): "); // Imprime el mensaje de error
    }
    if (pid > 0) { // Comprueba si el proceso es padre
        printf("I am the parent, and the child is %d. \n", pid);
        pid = wait(&status); // Suspende la ejecución del proceso de llamada hasta que finaliza uno de sus hijos

        printf("End of process %d: ", pid);
    if (WIFEXITED(status)) { // Es una llamada al sistema para conocer el estado de su hijo, si retorna true

        printf("The process ended with exit(%d). \n", WEXITSTATUS(status)); // Imprime el estado de salida del proceso hijo
    }
    if (WIFSIGNALED(status)) { // Consulta el estado de finalización del proceso hijo, si retorna true
        printf("The process ended with kill -%d. \n", WTERMSIG(status)); // Imprime número de la señal que causó la terminación del proceso hijo

    }
    }
    if (pid < 0) { // Comprueba si el proceso no se ha creado
        perror("In fork():"); // Imprime el mensaje de error
    }
    exit(0); // Ejecución exitosa del programa
}