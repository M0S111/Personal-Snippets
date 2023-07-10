#include <iostream>

using namespace std;

template <typename T1 = int,typename T2 = double>

class Temp
{
	T1 val1;
	T2 val2;
	double valfin;


public:

	Temp(T1 a, T2 b): val1(a),val2(b)
	{
		valfin = a+b;
	}
	
	const double& SeeRes()
	{
		return valfin;
	}
};

template <typename O1>

const O1& Say(O1 thing)
{
	return thing;
}

int main()
{
	Temp <> Furst(44,67.8);
	
	Temp <int,int> Secundo(73,88);
	
	cout << Furst.SeeRes() << endl;
	cout << Secundo.SeeRes() << endl;
	
	long long Num = 389294782984728012;
	double N2 = 667.8;
	
	cout << Say(Num) << endl;
	cout << Say(N2) << endl;
}