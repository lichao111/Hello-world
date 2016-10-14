#include <stdio.h>
#include <math.h>
int num2bin(int n)
{
	int bin=0;
	int i=0;
	while(n !=0)
	{
		bin += n%2*(pow(10,i++));
		n /= 2;
	}
	return bin;
}
int num(int a)
{
	int n=0;
	while(a!=0)
	{
		if(a%10==1)
			n++;
		a /=10;
	}
	return n;
}

int func(int l, int r,int m)
{
	int i;
	int n=0;
	for(i=l;i<=r;i++)
		if(num(i)==m)
			n++;
	if (n!=0)
		return n;
	else
		return -1;
}

int main()
{
	int l,r,m;
	scanf("%d\n%d\n%d",&l,&r,&m);
	l=num2bin(l);
	r=num2bin(r);
	printf("%d\n",func(l,r,m));
	return 0;
}
