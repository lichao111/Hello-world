#include <stdio.h>
#include <math.h>


int main()
{
	int a[3][5]={{5,10,2,3,4},{1,2,3,4,5},{101,102,103,104,105}};
	int i=0,j;
	for(;i<3;i++)
	{	for(j=0;j<5;j++)
			printf("%d\t",a[i][j]);
		printf("\n");
	}
	for(i=0;i<5;i++)
	{
		for(j=0;j<3;j++)
			printf("%d\t",*(a[j]+i));
		printf("\n");
	}
	int *p=a[0];
	printf("%p,%p\n",p,p+1);
	printf("%p\n",a);
	int *c[]={p,p+1,p+2};
	int **q=c;
	printf("%p\n",c[0]);
	printf("%p\n",q);
	printf("%p\n",*q);
	printf("%.1f\n",sqrt(2));
	printf("%6s\n","hell0");
	return 0;
}
