#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int Maxarray(int A[],int n);
void sort(int a[]);
int main()
{
	//----------1----------------
/*	printf("how long of this array?\n");
	int n;
	scanf("%d",&n);
	int A[n];
	printf("please input the value of the arrary\n");
	for (int i =0; i<n; i++)
	{
		printf("A[%d]:\n",i);
		scanf("%d",&A[i]);
	}
	int M;
	M = Maxarray(A,n);
	cout<<"the max number is :"<<M<<endl;

	int A[]={9,4,5,6,7,2,3,4,5};
	sort(A);
	for (int j=0; j<9; ++j)
	{
		printf("A[%d]:%d\n",j,A[j]);
	}
	int *p,x,a[5]={1,2,3,4,5};p=a;
	cout<<a[2]<<endl<<*(p+2)<<endl<<*(a+1)<<endl;
	int b[5]={1,2};
	float g[5];int *s=a;*/
	/*int a[]={15,12,-9,28,5,3},*p=a;
	p=a+3;
	long int e=0x7fff75ac74c0;
	long int r=0x7fff75ac74cc;
	printf("%ld\t%ld\n",e,r);
	cout<<a<<"---"<<p<<"---"<<p-a<<endl;
	char a1[]="China";
	cout<<a1[0]<<endl<<&a1<<endl;
	int a=4;
	int *p = &a;
	cout<<p<<endl<<*p<<endl<<*p<<endl;
	char a = 'a';
	char b[] = "b";
	cout<<a<<endl<<sizeof(a)<<endl;
	cout<<b<<endl<<sizeof(b)<<endl;
	char c[]="I am Li";
	cout<<c<<endl;
	const char * p1="China";
	cout<<*(p1+3)<<endl;
	puts("china");
	char a[8]="china";
	puts(a);
	char b[5];
	gets(b);
	puts(b);
	char a[10];
	strcpy(a, "work");
	printf("%ld\n",strlen(a));
	printf("%s\n",strcpy(a,"study"));
	printf("%s\n",strcat(a,"hard"));
	printf("%d\n",strcmp(a,"studyhard"));
	char d[]="I am";*/
	char a[]="chaoLi";
	char b[]="";
	long unsigned int c = strlen(a);
	printf("%ld\n",c);
	printf("%s\n",strcpy(b,a));
	printf("%s\n",b);
	return 0;
}

int Maxarray(int A[],int n)
{
	int M=A[0];
	for(int j=0;j<n;j++)
	{
		if (M<=A[j])
			M = A[j];
	}
	return M;
}

/*void sort(const int a[],const int n)
{
	int i , j ;
	for (i=0; i<n;i++)
		for (j=i; j<n; j++)
		{	
			if(a[i]>a[j])
			{
				int temp;
				temp=a[j];
				a[j]=a[i];
				a[i]=temp;
			}
		}
	return 0;
}
*/
