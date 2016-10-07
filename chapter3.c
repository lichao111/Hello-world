#include <stdio.h>
#include <math.h>


//int reverse(int);
//int total (int);
//int jiechengtotal(int);
double pit();
int translate(int );
int main()
{
	/*printf("please input the number which you want to get its reverse:");
	int n;
	scanf("%d",&n);
	printf("%d\nthe total of the %d:%d\n",reverse(n),reverse(n),total(n));
	printf("how many number you want to compare:");
	int k;
	scanf("%d",&k);
	printf("%d", biggertotal(k));*/
	//int n;
	//scanf("%d",&n);
	//printf("%d\n",jiechengtotal(n));
	//printf("pi:%f\n",pit());
	//printf("please input the number which you want to check whether its a zhishu:");
	//int n;	scanf("%d",&n);
	//printf("%d\n",zhishu(n));
	printf("%d\n",translate(15));
	return 0;
}
/*
int reverse(int n)
{
	int m=0;
	while (n!=0)
	{
		m=m*10+ n%10;
		n /= 10;
	}
	return m;
}

int total(int n)
{
	int m=0;
	while(n!=0)
	{
		m += n%10;
		n /= 10;
	}
	return m;
}

int jiechengtotal(int n)
{
	int i,j,m=0;
	for (i=1;i<=n;i++)
	{
		int k=1;
		for(j=1; j<=i; j++)
		{
			k *= j ;
		}
		m += k;
	}
	return m;
}*/

double pit()
{
	int n=1;
	double pi=0;
	while(1)
	{
		pi +=(double) pow(-1,n-1)*((double)1/(2*n-1));
		n++;
		if((double) 1/(2*n-1)<=1e-10)
			break;
	}
	return pi*4;
}
int zhishu(int n)
{
	int i, j= sqrt(n);
	for(i=2;i<=j;i++)
	{
		if (n%i==0)
			return 0;
	}
	return 1;
}

int translate(int n )
{
	printf("translate to ?\n");
	int k,m=0,l=1;
	scanf("%d",&k);
	while (n!=0)
	{
		m += l*(n%k);
		l *= 10;
		n /=k;
	}
	return m;
}

