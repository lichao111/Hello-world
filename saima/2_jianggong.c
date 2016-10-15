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
		if(func1(i)==m)
			n++;
	if (n!=0)
		return n;
	else
		return -1;
}

int func1(x)
{
int countx =0;
while(x)
{
countx ++;
x = x&(x-1);
}
return countx;
} 

int main()
{
	int l,r,m;
	scanf("%d\n%d\n%d",&l,&r,&m);
	printf("%d\n",func(l,r,m));
	return 0;
}
