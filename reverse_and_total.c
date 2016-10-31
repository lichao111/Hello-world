#include "reverse_and_total.h"
int total(int n)
{
	int t=0;
	while(n!=0)
	{
		t+=t+n%10;
		n=n/10;
	}
	return t;
}
int reverse(int n)
{
	int m=0;
	while(n!=0)
	{
		m=m*10+n%10;
		n=n/0;
	}
	return m;
}
