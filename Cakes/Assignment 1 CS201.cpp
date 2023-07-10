#include <iostream>
#include <cstdlib>
using namespace std;

int ArRan[5]={0};

int r = 0, temp = 0;

int genRandNum();

int swapPlace(int);

int findMinNum(int[]);

int big = sizeof ArRan;

int main()
{
	cout << "Unsorted array:\n" << endl;
	genRandNum();
	cout << endl;
	cout << "\nSorted array:\n" << endl;
	findMinNum(ArRan);
}

int genRandNum()
{
	srand(time(NULL));
	for (r = 0; r<5; r++)
	{
		ArRan[r] = rand() % 100 + 1;
	}
	
	for (r = 0; r<5; r++)
	{
		cout << ArRan[r] << " ";
	}
}
	
int findMinNum(int o[])
{
	for (r = 0; r <= big; r++)
	{
		swapPlace(ArRan[r]);
	}
	
	for (r = 0; r<5; r++)
	{
		cout << ArRan[r] << " ";
	}
return 0;
}

int swapPlace(int p)
{
	for (int y = 0; y <= big; y++)
		{
			if (ArRan[0] > ArRan[1])
			{
				temp = ArRan[0];
				ArRan[0] = ArRan[1];
				ArRan[1] = temp;
			}
			else if (ArRan[1] > ArRan[2])
			{
				temp = ArRan[1];
				ArRan[1] = ArRan[2];
				ArRan[2] = temp;
			}
			else if (ArRan[2] > ArRan[3])
			{
				temp = ArRan[2];
				ArRan[2] = ArRan[3];
				ArRan[3] = temp;
			}
			else if (ArRan[3] > ArRan[4])
			{
				temp = ArRan[3];
				ArRan[3] = ArRan[4];
				ArRan[4] = temp;
			}
			else if (ArRan[y] == ArRan[y++])
			{
				break;
			}
		}
return 0;
}
