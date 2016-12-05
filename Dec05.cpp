#include <iterator>
#include <iostream>
#include <cstring>
using namespace std;
int main(){
	char a[10]="IamChaoLi";
	cout<<sizeof(a)<<endl;
	char* o=begin(a);
	cout<<*o<<endl;
	cout<<strlen(a)<<endl;
	cout<<a<<endl;
	cout<<"size of int"<<sizeof(long int)<<endl;
	int n=0;
	int* p=&n;
	cout<<"size of int "<<sizeof(int)<<endl;
	char b[1];
	strcpy(b,a);
	cout<<b<<endl;
	return 0;
}
