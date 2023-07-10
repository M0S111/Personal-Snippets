#include <iostream>

using namespace std;

class Enemy
{
  public:
	virtual void attack() = 0;

	virtual ~Enemy()
	{
		cout << "\nEnemy gone!" << endl;
	}
};

class Ninja final : public Enemy
{
  public:
	void attack()
	{
		cout << "Ninja attacks!" << endl;
	}

	~Ninja()
	{
		cout << "\nNinja gone." << endl;
	}
};

class Monster final : public Enemy
{
  public:
	void attack()
	{
		cout << "Monster attacks!" << endl;
	}
};

int main()
{
	const int SIZE = 9;

	try
	{
		if (SIZE > 10)
		{
			throw 0;
		}
	}

	catch (int err)
	{
		cout << "Error Code: " << err << endl;
		cout << "Excessively large value." << endl;
		exit(err);
	}

	Enemy *EnAr[SIZE];

	EnAr[0] = new Monster;
	EnAr[1] = new Ninja;
	//EnAr[2] = new Enemy; //won't work since class is abstract with virtual functions

	EnAr[0]->attack();
	EnAr[1]->attack();
	//EnAr[2]->attack();

	delete EnAr[0];
	delete EnAr[1];
	//delete EnAr[2];
}