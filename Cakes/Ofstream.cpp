#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

string data = "\nSo I'll keep at it till I claw my way out."; //Data is string or char[]


int main()
{
	ofstream Fuyhl; //This is the ofstream object
	
	Fuyhl.open("Learning sumore.txt", ios::app); //Open 	function is given 2 params, address & what to do 		with it
		
	Fuyhl << data; //Data is being "output" (written) to 	ofstream object
	
	cout << "\n";
	
	Fuyhl.close();
}