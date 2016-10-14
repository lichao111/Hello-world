#include <stdio.h>
int func(int n)
{
	int i=0;	// n -2i   
	int j;
	int s=0;
	if(n<=2)
	{
		return n;
	}
	for(j=2;s<n;j++)
	{
		s+=j;
		i++;
	}
	
	return (n-2*i+2);
}

int main()
{
	int n;
	scanf("%d",&n);
	printf("%d\n",func(n));
	return 0;
}

