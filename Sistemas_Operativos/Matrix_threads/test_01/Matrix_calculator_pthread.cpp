#include <iostream>
#include <fstream>
#include <pthread.h>
#include <sys/sysinfo.h>
#include <semaphore.h>
#include <sys/shm.h>
#include <chrono>

using namespace std;

struct Matrix{

	int** firstMatrix;
	int** secondMatrix;
	int** result;
	int index;
	int firstMatrixM;
	int firstMatrixN;
	int secondMatrixM;
	int secondMatrixN;
	int threadNumber[100];
	int noOfProcesses;
};

sem_t semaphore1;


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

// Genera una matriz de tamaño m x n
int** generateMatrix(int m, int n){
	int** matrix = new int*[m];
	for(int i = 0; i < m; i++){
		matrix[i] = new int[n];
	}
	return matrix;
}

// Llena una matriz de tamaño m x n con valores aleatorios
void fillMatrix(int** matrix, int m, int n){
	for(int i = 0; i < m; i++){
		for(int j = 0; j < n; j++){
			matrix[i][j] = rand() % 100;
		}
	}
}

// Imprime una matriz de tamaño m x n
void printMatrix(int** matrix, int m, int n){
	for(int i = 0; i < m; i++){
		for(int j = 0; j < n; j++){
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
}

// Multiplica dos matrices de tamaño n x n
void* MatrixCalculator (void * ob){

	Matrix* ob1 = new Matrix;
	ob1 = (Matrix*) ob;

	int noOfElements = ob1->firstMatrixM*ob1->secondMatrixN;
	int noOfOp = noOfElements/ob1->noOfProcesses;
	int remaining = noOfElements % ob1->noOfProcesses;

	int firstOperation,lastOperation;

	sem_wait(&semaphore1);
	if(ob1->threadNumber[ob1->index] == 0){

		firstOperation = noOfOp*ob1->threadNumber[0];
		lastOperation = noOfOp*(ob1->threadNumber[0]+1)+remaining;

		ob1->index++;
	}
	else
	{
		firstOperation = noOfOp*ob1->threadNumber[ob1->index]+remaining;
		lastOperation = noOfOp*(ob1->threadNumber[ob1->index]+1)+remaining;
		ob1->index++;
	} 

	sem_post(&semaphore1);

	for(int i =firstOperation;i<lastOperation;i++){
		const int row=i%ob1->firstMatrixM;
		const int col=i/ob1->firstMatrixM;

		float result1=0;

		for(int j=0;j<ob1->firstMatrixM;j++)
		{
			result1 += ob1->firstMatrix[row][j]*ob1->secondMatrix[j][col];
		}

		ob1->result[row][col]=result1;
	}
	pthread_exit((void*)ob1);
}

// Función que realiza la suma de 2 matrices usando hilos
// Recibe el tamaño de las matrices
// Devuelve la matriz resultante de la suma
void* Sum_matrix (void * ob)
{
	Matrix* ob1 = new Matrix;
	ob1 = (Matrix*) ob;

	int noOfElements = ob1->firstMatrixM*ob1->firstMatrixN;
	int noOfOp = noOfElements/ob1->noOfProcesses;
	int remaining = noOfElements % ob1->noOfProcesses;

	int firstOperation,lastOperation;

	sem_wait(&semaphore1);
	if(ob1->threadNumber[ob1->index] == 0){

		firstOperation = noOfOp*ob1->threadNumber[0];
		lastOperation = noOfOp*(ob1->threadNumber[0]+1)+remaining;

		ob1->index++;
	}
	else
	{
		firstOperation = noOfOp*ob1->threadNumber[ob1->index]+remaining;
		lastOperation = noOfOp*(ob1->threadNumber[ob1->index]+1)+remaining;
		ob1->index++;
	} 

	sem_post(&semaphore1);

	for(int i =firstOperation;i<lastOperation;i++){
		const int row=i%ob1->firstMatrixM;
		const int col=i/ob1->firstMatrixM;

		ob1->result[row][col]=ob1->firstMatrix[row][col]+ob1->secondMatrix[row][col];
	}
	pthread_exit((void*)ob1);
}

// Función que realiza la resta de 2 matrices usando hilos
// Recibe el tamaño de las matrices
// Devuelve la matriz resultante de la resta

void* Sub_matrix (void * ob)
{
	Matrix* ob1 = new Matrix;
	ob1 = (Matrix*) ob;

	int noOfElements = ob1->firstMatrixM*ob1->firstMatrixN;
	int noOfOp = noOfElements/ob1->noOfProcesses;
	int remaining = noOfElements % ob1->noOfProcesses;

	int firstOperation,lastOperation;

	sem_wait(&semaphore1);
	if(ob1->threadNumber[ob1->index] == 0){

		firstOperation = noOfOp*ob1->threadNumber[0];
		lastOperation = noOfOp*(ob1->threadNumber[0]+1)+remaining;

		ob1->index++;
	}
	else
	{
		firstOperation = noOfOp*ob1->threadNumber[ob1->index]+remaining;
		lastOperation = noOfOp*(ob1->threadNumber[ob1->index]+1)+remaining;
		ob1->index++;
	} 

	sem_post(&semaphore1);

	for(int i =firstOperation;i<lastOperation;i++){
		const int row=i%ob1->firstMatrixM;
		const int col=i/ob1->firstMatrixM;

		ob1->result[row][col]=ob1->firstMatrix[row][col]-ob1->secondMatrix[row][col];
	}
	pthread_exit((void*)ob1);
}

// Medir el tiempo para las 3 operaciones
void test(int** firstMatrix, int** secondMatrix, int** result, int firstMatrixM, int firstMatrixN, int secondMatrixM, int secondMatrixN, int noOfProcesses){

	Timer timer;
	Matrix* ob = new Matrix;
	ob->firstMatrix = firstMatrix;
	ob->secondMatrix = secondMatrix;
	ob->result = result;
	ob->firstMatrixM = firstMatrixM;
	ob->firstMatrixN = firstMatrixN;
	ob->secondMatrixM = secondMatrixM;
	ob->secondMatrixN = secondMatrixN;
	ob->noOfProcesses = noOfProcesses;

	pthread_t threads[noOfProcesses];
	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

	sem_init(&semaphore1,0,1);

	for(int i = 0; i < noOfProcesses; i++){
		ob->threadNumber[i] = i;
	}

	for(int i = 0; i < noOfProcesses; i++){
		pthread_create(&threads[i], &attr, MatrixCalculator, (void*)ob);
	}

	for(int i = 0; i < noOfProcesses; i++){
		pthread_join(threads[i], NULL);
	}

	pthread_attr_destroy(&attr);
	sem_destroy(&semaphore1);

	// Suma de matrices
	Matrix *ob1 = new Matrix;
	ob1->firstMatrix = firstMatrix;
	ob1->secondMatrix = secondMatrix;
	ob1->result = result;
	ob1->firstMatrixM = firstMatrixM;
	ob1->firstMatrixN = firstMatrixN;
	ob1->secondMatrixM = secondMatrixM;
	ob1->secondMatrixN = secondMatrixN;
	ob1->noOfProcesses = noOfProcesses;

	pthread_t threads1[noOfProcesses];
	pthread_attr_t attr1;
	pthread_attr_init(&attr1);
	pthread_attr_setdetachstate(&attr1, PTHREAD_CREATE_JOINABLE);

	sem_init(&semaphore1,0,1);

	for(int i = 0; i < noOfProcesses; i++){
		ob1->threadNumber[i] = i;
	}

	for(int i = 0; i < noOfProcesses; i++){
		pthread_create(&threads1[i], &attr1, Sum_matrix, (void*)ob1);
	}

	for(int i = 0; i < noOfProcesses; i++){
		pthread_join(threads1[i], NULL);
	}

	pthread_attr_destroy(&attr1);
	sem_destroy(&semaphore1);

	// Resta de matrices
	Matrix *ob2 = new Matrix;
	ob2->firstMatrix = firstMatrix;
	ob2->secondMatrix = secondMatrix;
	ob2->result = result;
	ob2->firstMatrixM = firstMatrixM;
	ob2->firstMatrixN = firstMatrixN;
	ob2->secondMatrixM = secondMatrixM;
	ob2->secondMatrixN = secondMatrixN;
	ob2->noOfProcesses = noOfProcesses;

	pthread_t threads2[noOfProcesses];
	pthread_attr_t attr2;
	pthread_attr_init(&attr2);
	pthread_attr_setdetachstate(&attr2, PTHREAD_CREATE_JOINABLE);

	sem_init(&semaphore1,0,1);

	for(int i = 0; i < noOfProcesses; i++){
		ob2->threadNumber[i] = i;
	}

	for(int i = 0; i < noOfProcesses; i++){
		pthread_create(&threads2[i], &attr2, Sub_matrix, (void*)ob2);
	}

	for(int i = 0; i < noOfProcesses; i++){
		pthread_join(threads2[i], NULL);
	}

	pthread_attr_destroy(&attr2);
	sem_destroy(&semaphore1);
}

int main(int argc, char* argv[]){

	// Tamaño de la matriz
	int t;
	cout << "Ingrese el tamaño de la matriz: ";
	cin >> t;

	// Numero de procesos
	int noOfProcesses;
	cout << "Ingrese el numero de procesos: ";
	cin >> noOfProcesses;

	// Generar matrices
	int** firstMatrix = generateMatrix(t, t);
	int** secondMatrix = generateMatrix(t, t);
	int** result = generateMatrix(t, t);

	// Llenar matrices
	fillMatrix(firstMatrix, t, t);
	fillMatrix(secondMatrix, t, t);

	// Testear el tiempo para las 3 operaciones
	test(firstMatrix, secondMatrix, result, t, t, t, t, noOfProcesses);

	/*
	// Imprimir matrices
	cout << "Matriz 1:" << endl;
	printMatrix(firstMatrix, t, t);
	cout << "Matriz 2:" << endl;
	printMatrix(secondMatrix, t, t);
	cout << "Resultado:" << endl;
	printMatrix(result, t, t);
	*/
	
	return 0;
}