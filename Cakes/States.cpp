#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;


int Shitty = 0;

int* shtPtr = &Shitty;

//int States[3] = {10, 20, 31};

int main()
{
	cout << " Dear Shami bhaijaan, state your age. ";
	cin >> Shitty;
	
	//int s = States[Shitty];
	
	switch (*shtPtr)
	{
		case 10: cout << endl << "\nThis guy's an asshole.";
		break;
		
		case 20: cout << endl << "\nStill an asshole.";
		break;
		
		case 31: cout << endl << "\nA 2 bit bitch with pretensions.";
		break;	
		
		default: cout << endl << "\nThere's no helping this clown.";
	}
}
