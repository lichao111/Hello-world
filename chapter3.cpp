#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;	

template <class T>
int len_arry(T& arry)
{
	return (sizeof(arry)/sizeof(arry[0]));
}

int total(int *n);
int main()
{
	/*char a[]={'a','b','c','d','e','f','g'};
	int b[]={1,2,3,4,5,6};
	cout<<strlen(a)<<endl<<len_arry(b)<<endl<<"len of a:"<<len_arry(a)<<endl;
	int Max=b[0], Min=b[0];
	for (int j =0; j<=len_arry(b);j++)
	{
		if (Max<=b[j])
		{Max=b[j];}
		if (Min>=b[j])
		{Min=b[j];}
	}
	cout<<"Max:"<<Max<<"Min:"<<Min<<endl;
	int len=len_arry(b);
	for (int j = 0;j<len/2;j++)
	{
		int t;
		t=b[len-1-j];
		b[len-j-1]=b[j];
		b[j]=t;
	}
	for (int j=0;j<len;j++)
	{
		cout<<b[j]<<endl;
	}
	char name='C';
	cout<<sizeof(name)<<endl<<sizeof(b)<<endl<<sizeof(a)<<endl;
	cout<<"-----------------------------------"<<endl;
	int k=9;
	int * p ;
	p=&k;
	cout<<p <<endl<<&p<<endl<<*p<<endl;
	int o =4376387;
	cout<<total(&o)<<endl;
	int hah=1;
	int h=hah;
	cout<<&hah<<endl<<&h<<endl;
	int *l= &hah;
	cout<<l<<endl;
	return 0;
	int a[10]={0,1,2,3,4,5,6,7,8,9};
	cout<<a<<endl;
	for( int j=0; j<=9;j++)
	{
		printf("a+%d:\n",j);
		cout<<*(a+j)<<endl;}
	int *p =  a;
	cout<<p<<endl<<p[0]<<"\t"<<p[1]<<endl;
	cout<<sizeof(int)<<endl<<sizeof(double)<<endl<<sizeof(float)<<endl<<sizeof(char)<<endl;
	int * p = (int*) malloc (5*sizeof(int));
	if (p=NULL)
	{
		cout<<"allocation failure! now exit!!"<<endl;
		exit(1);
	}
	cout<<&p<<endl;
	free(p);
	cout<<&p<<endl<<sizeof(p)<<endl;*/
	/*void * vp =malloc(9);
	int * ip;
	float * fp;
	if (vp = NULL)
	{
		printf("allocation failture!!");
		exit(1);
	}
	ip = (int * ) vp;
	*ip =89;
	*ip %= 5;
	printf("%d", *ip);
	fp=(float*)vp;
	*fp = 3.14159F;
	*fp /= 2;
	printf("%f\n",*fp);
	free(vp);*/
	int a=1;
	float b=2;
	double c =3;
	printf("%-4d\n",a);
	printf("%-4f\n",b);
	printf("%f\n",c);

	
	
	return 0;
}

int total(int *p)

{
	int total =0;
	while(*p != 0)
	{
		total += *p %10;
		*p /= 10;
	}
	return total;
}


























