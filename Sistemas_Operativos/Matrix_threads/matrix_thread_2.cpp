#include <iostream>
#include <fstream>
#include <pthread.h>
#include <sys/sysinfo.h>
#include <semaphore>
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

int readFile(char* fileName,int** &arr,int& m,int& n);
void* MatrixCalculator (void * ob);

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

// Leer la matriz del archivo de texto
int readFile(char* fileName,int** &arr,int& m,int& n){
    ifstream file;
    file.open(fileName);
    if(!file.is_open()){return -1;}
    file >> m >> n;
    arr = new int*[m];
    for(int i=0;i<m;i++){
        arr[i] = new int[n];
    }
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            file >> arr[i][j];
        }
    }
    file.close();
    return 0;
}

// Multiplicar las matrices en paralelo
void* MatrixCalculator (void * ob){
    Matrix* obj = (Matrix*) ob;
    int index = obj->index;
    int firstMatrixM = obj->firstMatrixM;
    int firstMatrixN = obj->firstMatrixN;
    int secondMatrixM = obj->secondMatrixM;
    int secondMatrixN = obj->secondMatrixN;
    int** firstMatrix = obj->firstMatrix;
    int** secondMatrix = obj->secondMatrix;
    int** result = obj->result;
    int noOfProcesses = obj->noOfProcesses;
    int* threadNumber = obj->threadNumber;
    int i,j,k;
    for(i=0;i<firstMatrixM;i++){
        for(j=0;j<secondMatrixN;j++){
            for(k=0;k<firstMatrixN;k++){
                result[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
            }
        }
    }
    sem_post(&semaphore1);
    pthread_exit(NULL);
}

int main(int argc,char* argv[]){
    Timer timer;
    Matrix ob;
    int flag=readFile(argv[1],ob.firstMatrix,ob.firstMatrixM,ob.firstMatrixN);
    int flag1=readFile(argv[2],ob.secondMatrix,ob.secondMatrixM,ob.secondMatrixN);

    if(flag == -1 || flag1 ==-1){cout << "No se puede abrir el archivo! " <<endl;return 0;}

    if(ob.firstMatrixN != ob.secondMatrixM){
        cout<<"El orden de la matriz no es apropiado para la multiplicación de matrices";
        return 0;
    }

    ob.result = new int*[ob.firstMatrixM];
    for(int i=0;i<ob.firstMatrixM;i++){
        ob.result[i] = new int[ob.secondMatrixN];
    }

    int noOfThreads = get_nprocs();
    pthread_t threads[noOfThreads];
    sem_init(&semaphore1,0,0);
    int index = 0;

    for(int i=0;i<noOfThreads;i++){
        ob.index = index;
        ob.noOfProcesses = noOfThreads;
        ob.threadNumber[i] = i;
        pthread_create(&threads[i],NULL,MatrixCalculator,(void*)&ob);
        index++;
    }

    for(int i=0;i<noOfThreads;i++){
        sem_wait(&semaphore1);
    }

    ofstream file;
    file.open("result.txt");
    for(int i=0;i<ob.firstMatrixM;i++){
        for(int j=0;j<ob.secondMatrixN;j++){
            file << ob.result[i][j] << " ";
        }
        file << endl;
    }

    file.close();
    return 0;
}