#include <stdio.h>
int main()
{
	int n =567;
	printf("%d%d%d",n%10,(n/10)%10,(n/100)%10);
	printf("\n");
	int m =48579;
	while(m!=0)
	{printf("%d",m%10);
	m=m/10;
	}printf("\n");
	//int l=98374;
	int i ;
	scanf("%d",n);
	for(i=n;i!=0;i=i/10)
		printf("%d",i%10);
	printf("\n");	
	return 0;
}


