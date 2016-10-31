#include <stdio.h>
#include "reverse_and_total.h"
#define PI 3.1415926
#define max(a,b) a>=b? a:b
#define DEBUG
int main()
{
	#ifdef DEBUG
	printf("this is for debug!!\n");
	#endif
	printf("%f\n",PI);
	int s;
	s=max(4,5);
	printf("%d\n",s);

	int x=52;
	x=total(x);
	printf("%d\n",x);
	x=reverse(x);
	printf("%d\n",x);
	return 0;
}

