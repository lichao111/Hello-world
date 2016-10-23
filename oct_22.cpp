#include <iostream>

using namespace  std;

class CAT
{
	public:
		CAT();
		CAT(CAT &cat);
		~CAT();
		int Getage()const{return *itsAge;}
		int GetWeight() const {return *itsWeight;}
		void SetAge(int age) {*itsAge = age;}
	private:
		int* itsAge;
		int* itsWeight;
};

CAT::CAT()
{
 	itsAge = new int;
	itsWeight = new int;
	*itsAge = 5;
	*itsWeight == 9;
}

int main()
{
	int* a;
	a = new int;
	*a=9;
	cout<<a<<endl<<*a<<endl;
	int c=10;
	int d=c;
	cout<<"&c:"<<&c<<endl<<"&d:"<<&d<<endl;
	int *p= new int;
	*p=9;
	cout<<p<<endl<<*p<<endl;
	delete p;
	cout<<p<<endl<<*p<<endl;
	string k ="Whoareyou?";
	cout<<"k:"<<k<<endl;
	cout<<"the length of k:"<<k.length()<<endl;

	string o("iamphantom");
	cout<<o<<endl;
	
	
	return 0;
}
