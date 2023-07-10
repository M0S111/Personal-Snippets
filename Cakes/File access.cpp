#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

char data;

int main()
{
	
	ifstream Fuyhl; // This is the ifstream object 		declaration
	
	Fuyhl.open("Learning sumore.txt"); // Created object 	is being opened by giving address to open function
	
	if (!Fuyhl) // Error check
	{
		cout << "This file is missing." <<  endl; 
		exit(1); 
	}
	else
	{
		cout << "\nSuccessfully accessed file.\n" << 			endl;
	}

	while(Fuyhl.get(data)) //Loop sticks file 			content into data 1 char at a time, then prints it
	{
		cout << data;
	}
	
	cout << "\n";
	
	Fuyhl.close();
}