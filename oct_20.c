#include <iostream>
using namespace std;

struct Date
{
	int yr;
	int mo;
	int day;
};
istream &operator>>(istream &ins, Date &dt);
ostream &operator<<(ostream &out,Date &dt);
int main()
{
/*	Date dt1,dt2;
	cout<<"pleast input one data:";
	cin>>dt1;
	cout<<"inut another date:";
	cin>>dt2;
	cout<<dt1<<endl;
	cout<<dt2<<endl;
	int a;
	cin>>a;
	cout<<"the intger is:"<<a<<endl;
*/
	int a=3;
	int b=a;
	b=4;
	cout<<a<<endl;
	cout<<b<<endl;
	return 0;
}

istream &operator>>(istream &ins,Date &dt)
{
	ins>>dt.yr>>dt.mo>>dt.day;
	return ins;
}
ostream &operator <<(ostream &outs,Date &dt)
{
	outs<<dt.yr<<'/'<<dt.mo<<'/'<<dt.day;
	return outs;
}
