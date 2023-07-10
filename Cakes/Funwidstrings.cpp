#include <iostream>
#include <cstdlib>
#include <string>
#include <ctype.h>
using namespace std;

int dafuc = 22;

char damn;

int main()
{
	damn = dafuc;
	cout << isalnum(damn);
}