#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

class ezString{
	
	char* buffer;
	
public:

	ezString(char*);
	
	ezString(const ezString &source);
};


int main()
{
	ezString("My string works!");
}

ezString::ezString(char* say)
:buffer(say)
{
	cout << buffer;
}

ezString::ezString(const ezString &source)
{
	char* nubuffer;

	nubuffer = new char[strlen(source) + 1];
	
}