#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

class Offspring{

    string name;
    string sex;
    string hairColor;
    string skinColor;
    
public:
    
    Offspring(string n = "Peter",string s = "M",string hC = "Brunette",string sC = "Pale")
    :name(n),sex(s),hairColor(hC),skinColor(sC)
{
    cout << "\nConstructed your desired offspring with these features:";
    cout << "\n" << name << "\n" << sex << "\n" << hairColor << "\n" << skinColor << endl;
}

    ~Offspring();


};

int main()
{
    Offspring Uno;
}


Offspring::~Offspring()
{
    cout << "\nOffspring killed sucessfully." << endl;
}

