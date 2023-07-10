#include <cstdlib>
#include <iostream>
#include <ctime>
#include <string>

using namespace std;

const int r = 4, c = 3;

int total = 0, row = 0, col = 0;

string prompt = "n", numz = "";

int chin[r][c] = {0};

void CeeLo(int);

int main()
{
	do
	{
		cout << "\nDo you feel lucky, punk?! ";
		cin >> prompt;
		
		srand(time(0));
		
		if (prompt == "y")
		{
			for (row = 0; row < r; row++)
			{
				for (col = 0; col < c; col++)
				{
					chin[row][col] = rand() % 6 + 1;
				}
			}
			
		}
		else
		{
			goto over;
		}

	} while (prompt == "n");

	cout << endl;

	cout << "\nYour rolls were:";

	cout << endl;

	for (row = 1; row <= r; row++)
	{
		cout << "\nRoll " << row << ": ";

		for (col = 1; col <= c; col++)
		{
			cout << chin[row][col] << " ";
			total += chin[row][col];
		}
		
		cout << " (Total for this roll: " << total << 		")\n";
		total = 0;
	}

	//CeeLo(chin);
	
	over:

		return 0;
}

void CeeLo(int ar)
{
	if (ar == 123)
	{
		cout << endl;
		cout << "\nAutomatic Loss";
	}
}
