#include <iostream>
#include <fstream>

using namespace std;

// Generar numeros aleatorios para una matriz
void Generar_Matriz(int **matriz, int filas, int columnas)
{
    for(int i=0; i<filas; i++)
    {
        for(int j=0; j<columnas; j++)
        {
            matriz[i][j] = rand() % 100;
        }
    }
}

// Guardar una matriz en un archivo de texto
void Guardar_Matriz(int **matriz, int filas, int columnas, char *nombre_archivo)
{
    ofstream archivo;
    archivo.open(nombre_archivo);
    for(int i=0; i<filas; i++)
    {
        for(int j=0; j<columnas; j++)
        {
            archivo << matriz[i][j] << " ";
        }
        archivo << endl;
    }
    archivo.close();
}

// Crear las matrices
void Crear_Matrices(int **matriz1, int **matriz2, int filas, int columnas)
{
    Generar_Matriz(matriz1, filas, columnas);
    Generar_Matriz(matriz2, filas, columnas);
}


int main()
{
    // desactivar la sincronizacion con el flujo de salida estandar

    int filas, columnas;
    char nombre_archivo[100];
    cout << "Ingrese el numero de filas: ";
    cin >> filas;
    cout << "Ingrese el numero de columnas: ";
    cin >> columnas;

    // crear las matrices
    int **matriz1 = new int*[filas];
    int **matriz2 = new int*[filas];
    for(int i=0; i<filas; i++)
    {
        matriz1[i] = new int[columnas];
        matriz2[i] = new int[columnas];
    }

    // crear las matrices
    Crear_Matrices(matriz1, matriz2, filas, columnas);

    // guardar las matrices en archivos de texto
    cout << "Ingrese el nombre del archivo de la matriz 1: ";
    cin >> nombre_archivo;
    Guardar_Matriz(matriz1, filas, columnas, nombre_archivo);

    cout << "Ingrese el nombre del archivo de la matriz 2: ";
    cin >> nombre_archivo;

    Guardar_Matriz(matriz2, filas, columnas, nombre_archivo);

    // liberar la memoria
    for(int i=0; i<filas; i++)
    {
        delete[] matriz1[i];
        delete[] matriz2[i];
    }

    delete[] matriz1;
    delete[] matriz2;

    return 0;
}
