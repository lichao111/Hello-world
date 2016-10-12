#include <stdio.h>
#include <stdlib.h>
#define arrarylen(a) sizeof(a)/sizeof(a[0])
void arrary(int a[],int size)
{
	int i=0;
	for(;i<size;i++)
		printf("%d\t",a[i]);
	printf("\n");
}
void display(int *a,int size)
{
	int i=0;
	for(i;i<size;i++)
		printf("%d\n",*(a+i));
}
	
int func(int a[],int size)	//O(n^2)
{
  
	int i,j;
	for(i=0;i<size;i++)	//O(size)
	{
		for(j=0;j<size;j++)	//O(size)
			if(a[i]==a[j]&& i!=j)
				break;
		if (j==size)
			return a[i];
	}
}
int main(int argc, char * argv[])
{
	int a[16]={1,1,1,2,2,2,3,4,5,4,4,5,5,3,3,9};
	printf("%ld\n",arrarylen(a));
	printf("%d\n",func(a,arrarylen(a)));
	printf("%d",9&8);
	return 0;
}
