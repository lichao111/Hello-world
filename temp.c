#include <stdio.h>
#include <math.h>

double func(const int n, int len)
{
	double m=(double)n;
	double sum=m;
	int i;
	for(i=0;i<len-1;i++)
	{
		sum += sqrt(m);
		m = sqrt(m);
	}
	printf("%.2f\n",sum);
	return sum;
}
int main()
{
	int n,len;
	scanf("%d\n%d",&n,&len);
	func(n,len);
	return 0;
}
