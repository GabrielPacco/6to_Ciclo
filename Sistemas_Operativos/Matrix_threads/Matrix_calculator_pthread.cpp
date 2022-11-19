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


int main(int argc,char* argv[]){

	Timer timer;
	Matrix ob;
	int flag=readFile(argv[1],ob.firstMatrix,ob.firstMatrixM,ob.firstMatrixN);
	int flag1=readFile(argv[2],ob.secondMatrix,ob.secondMatrixM,ob.secondMatrixN);

	if(flag == -1 || flag1 ==-1){cout << "No se puede abrir el archivo! " <<endl;return 0;}


	if(ob.firstMatrixN != ob.secondMatrixM){
		cout<<"El orden de la matriz no es apropiado para la multiplicación\n";
		return 0;
	}


	sem_init(&semaphore1, 1, 1);
	
	ob.result = new int*[ob.firstMatrixM];
	for(int i=0;i<ob.firstMatrixM;i++)
	{
		ob.result[i] = new int [ob.secondMatrixN];
	}

	ob.noOfProcesses=get_nprocs();
	int noOfElements1 = ob.firstMatrixM*ob.secondMatrixN;

	if(ob.noOfProcesses > noOfElements1)
	{
		ob.noOfProcesses=noOfElements1;
	}

	pthread_t tid[ob.noOfProcesses];
	ob.index=0;
	for(int i=0;i<ob.noOfProcesses;i++){
		ob.threadNumber[i]=i;	
		pthread_create (&tid[i],NULL,&MatrixCalculator,(void*) &ob);
	}

	Matrix * ob2;
	for(int i=0;i<ob2->noOfProcesses;i++){
		pthread_join(tid[i],(void**)&ob2);
	}

	for(int i =0;i<ob2->firstMatrixM;i++){
		for(int j=0;j<ob2->secondMatrixN;j++){
			cout << ob2->result[i][j] << " ";
		}
		cout<<endl;
	}

	return 0;
}


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

int readFile(char* fileName,int** &arr,int& m,int& n){

	ifstream MatrixFile(fileName);

	if(MatrixFile.fail()){
		cout << " Error 23234x : File Corrupt or cannot find file " << endl;
		return -1;
	}

	MatrixFile >> m;
	MatrixFile >> n;

	arr = new int* [m];

	for(int i=0;i<m;i++){
		arr[i] = new int [n];
	}

	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
		MatrixFile >> arr[i][j];
		}
	}

	MatrixFile.close();

	return 0;
}
