// C++ program to demonstrate memset
#include <cstring>
#include <iostream>
using namespace std;

int C[143], DP[20086];
// Driver Code
int main()
{
	memset(DP, 127, sizeof(DP));
	int n=3;
	int p = 14;
	int C[3] = { 5, 10, 20 };

	DP [0] = 0;
	for (int i=0; i<n; ++i) { // for each coin
            int c = C[i];  // coin
            for (int j=p; j>=0; --j) { // for each amount of change
				//cout << "DP[j+c] = " << DP[j+c] << endl;
                DP[j+c] = min(DP[j+c], DP[j]+1); // update DP
                //cout << "Min = " << min(DP[j+c], DP[j]+1) << endl;
				//cout << "DP[j] = " << DP[j] << endl;
                //cout << "DP[j] + 1 = " << DP[j]+1 << endl;
            }
        }

	for (int i = 0; i < 21; i++)
		cout << "Valor DP " << i << " " << DP[i] << "\n";
	int j;  // amount of change
        for (j=p; DP[j]>100; ++j);  // find minimum amount of change
        cout << j << ' ' << DP[j] << '\n'; // print minimum amount of change and minimum number of coins
	return 0;
}
