#include <iostream>
#include <chrono>

struct Timer
{
    std::chrono::system_clock::time_point start;

    Timer()
    {
        start = std::chrono::system_clock::now();
    }

    ~Timer()
    {
        auto end = std::chrono::system_clock::now();
        std::chrono::duration<float, std::milli> duration = end - start;
        std::cout << "\nms transcurridos: " << duration.count() << std::endl;
    }
};

// Generar números aleatorios
void randomize(int* matrix, int size)
{
    for (int i = 0; i < size; i++)
    {
        matrix[i] = rand() % 100;
    }
}

// Multiplicar matrices
void multiply(int* matrix1, int* matrix2, int* result, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            int sum = 0;
            for (int k = 0; k < size; k++)
            {
                sum += matrix1[i * size + k] * matrix2[k * size + j];
            }
            result[i * size + j] = sum;
        }
    }
}

// Sumar matrices
void add(int* matrix1, int* matrix2, int* result, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            result[i * size + j] = matrix1[i * size + j] + matrix2[i * size + j];
        }
    }
}

// Restar matrices
void subtract(int* matrix1, int* matrix2, int* result, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            result[i * size + j] = matrix1[i * size + j] - matrix2[i * size + j];
        }
    }
}

// Crear matrices
void create(int* matrix, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            matrix[i * size + j] = 0;
        }
    }
}

// Imprimir matrices
void print(int* matrix, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            std::cout << matrix[i * size + j] << " ";
        }
        std::cout << std::endl;
    }
}

int main()
{
    // tamaño de la matriz}
    int n;
    std::cin >> n;

    // Crear matrices
    int* matrix1 = new int[n * n];
    int* matrix2 = new int[n * n];
    int* result = new int[n * n];

    // Inicializar matrices
    randomize(matrix1, n * n);
    std::cout << "\nMatrix 1" << std::endl;
    //print(matrix1, n);
    randomize(matrix2, n * n);
    std::cout << "\nMatrix 2" << std::endl;
    //print(matrix2, n);
    create(result, n);

    // Multiplicar matrices
    {
        Timer timer;
        multiply(matrix1, matrix2, result, n);
        add(matrix1, matrix2, result, n);
        subtract(matrix1, matrix2, result, n);
    }

    // Imprimir resultado
    std::cout << "\nResult" << std::endl;
    //print(result, n);

    // Liberar memoria
    delete[] matrix1;
    delete[] matrix2;
    delete[] result;

    return 0;
}