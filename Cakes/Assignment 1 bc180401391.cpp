#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

class GUI{
public:
	GUI()
		{
		cout << "\nGUI Feature Constructor called";
		};
};

class CUI{
public:
	CUI()
		{
		cout << "\nCUI Feature Constructor called";
		};
};

class UserInput{
public:
	UserInput()
		{
		cout << "\nUser Input Feature Constructor called";
		};
};

class AllInput{
public:
	AllInput()
		{
		cout << "\nAll Input Feature Constructor called";
		};
};

class GameScene: public GUI,CUI,UserInput,AllInput
{	
public:
	GameScene()
		{
		cout << endl;
		cout << "\nGame Scene Constructor called" << endl;
		};
};

class TitleScene{
public:
	TitleScene(){
		cout << "\nTitle Scene Constructor called";
		};
};

class StartScene{
public:
	StartScene(){
		cout << "\nStart Scene Constructor called";
		};
};

class EndScene{
public:
	EndScene(){
		cout << "\nEnd Scene Constructor called";
		};
};

class TotalScene: public GameScene,TitleScene,StartScene,EndScene
{
public:
	TotalScene(){
		cout << endl;
		cout << "\nScene Constructor called";
		};
};


int main()
{
	TotalScene Lv1;
}