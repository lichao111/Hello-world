#include <stdio.h>
#include <string.h>
/*#include <iostream>
using namespace std;
int c;
int *func(int *,int *);	//zhizhen hanshu
int func2(int);
int main()
{
	int i=0;	// an integer
	int a[3]={1,2,3};//整形数组
	int b[3]={4,5,6};
	int c[3]={7,8,9};
	int *p[3];	//指针数组
	p[1]=a;p[2]=b;p[3]=c;
	cout<<p[1]<<','<<p[2]<<','<<p[3]<<endl;
	printf("%p",p[1]);
	int (*q)[3];	//数组指针
	q=&a;
	cout<<q<<','<<*q<<','<<a<<','<<&a<<','<<*a<<endl;
	int (*function)(int);	//函数指针
	function =func2;
	cout<<funct`ion<<','<<func2<<endl;
	return 0;
}
int *func(int *a, int *b)
{
	 c=(*a+*b);
	return &c;
}

int func2(int a)
{
	return a;
}*/
unsigned num(const char *a,const char *b);
int main()
{
	char a[]="Iamlichaoyouamlichaowhoislichao";
	char b[]="adh";
	printf("%d\n",num(a,b));
	return 0;
}
unsigned num(const char*a, const char *b)
{
	unsigned n;
	if(strstr(a,b)==NULL)
		return 0;
	else
	{	
		char *temp=strstr(a,b);
		while(strstr(temp,b)!=NULL)
		{
			printf("%s\n",strstr(temp,b));
			n++;
			if(strlen(temp)>strlen(b))
				temp=strstr(temp+strlen(b),b);
			else
				break;
				printf("%s\n",temp);	
		}
	}
	return n;
}
		


