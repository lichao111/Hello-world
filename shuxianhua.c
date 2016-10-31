#include <stdio.h>
int check(const int n)
{
	int sum=0;
	int m=n;
	while(m!=0)
	{
		int k=m%10;
		sum += (k*k*k);
		m /= 10;
	}
	if (sum == n)
		return 1;
	else 
		return 0;
}
int main()
{
	int n,m,num=0;
	scanf("%d\n%d",&n,&m);
	int i;
	for(i=n;i<=m;i++)
		if(check(i))
			{	
				printf("%d ",i);
				num++;
			}
	if(num==0)
		printf("no\n");
	return 0;
}
